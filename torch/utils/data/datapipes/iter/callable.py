import copy
import warnings
from torch.utils.data import IterDataPipe, _utils, functional_datapipe, DataChunk
from typing import Callable, Dict, Iterator, Optional, Sized, Tuple, TypeVar

try:
    import dill

    # XXX: By default, dill writes the Pickler dispatch table to inject its
    # own logic there. This globally affects the behavior of the standard library
    # pickler for any user who transitively depends on this module!
    # Undo this extension to avoid altering the behavior of the pickler globally.
    dill.extend(use_dill=False)
    DILL_AVAILABLE = True
except ImportError:
    DILL_AVAILABLE = False

T_co = TypeVar("T_co", covariant=True)


@functional_datapipe("map")
class MapperIterDataPipe(IterDataPipe[T_co]):
    r""":class:`MapperIterDataPipe`.

    Iterable DataPipe to run a function over each item from the source DataPipe.
    The function can be any regular python function or partial object. Lambda
    function is not recommended as it is not supported by pickle.

    Args:
        datapipe: Source Iterable DataPipe
        fn: Function called over each item
        input_col: Index or indices of data which `fn` is applied.
            - None as default to apply `fn` to the data directly.
            - Integer(s) is used for list/tuple.
            - Key(s) is used for dict.
        output_col: Index or indices of data where result of `fn` is placed.
            - None as default to replace the index that `input_col` specified;
              For multiple indices of `input_col`, the left-most one is used.
            - Integer is used for list/tuple. -1 represents to appending result at the end.
            - Key is used for dict. New key is acceptable.
            - Multiple integers or keys is used to expand the result of `fn` to be placed
              at the corresponding location. `TypeError` would be raised when the size of
              `output_col` is different from the size of result.
        fn_args: Positional arguments for `fn`
        fn_kwargs: Keyword arguments for `fn`
        nesting_level: Determines which level the fn gets applied to, by default it applies to the top level (= 0).
            This also accepts -1 as input to apply the function to the lowest nesting level. It currently doesn't support
            argument < -1.
    """
    datapipe: IterDataPipe
    fn: Callable

    def __init__(
        self,
        datapipe: IterDataPipe,
        fn: Callable,
        input_col=None,
        output_col=None,
        *,
        fn_args: Optional[Tuple] = None,
        fn_kwargs: Optional[Dict] = None,
        nesting_level: int = 0,
    ) -> None:
        super().__init__()
        self.datapipe = datapipe
        # Partial object has no attribute '__name__', but can be pickled
        if hasattr(fn, "__name__") and fn.__name__ == "<lambda>" and not DILL_AVAILABLE:
            warnings.warn(
                "Lambda function is not supported for pickle, please use "
                "regular python function or functools.partial instead."
            )
        self.fn = fn  # type: ignore[assignment]
        self.input_col = input_col
        self.output_col = output_col
        self.args = () if fn_args is None else fn_args
        self.kwargs = {} if fn_kwargs is None else fn_kwargs
        if nesting_level < -1:
            raise ValueError("nesting_level must be -1 or >= 0")
        self.nesting_level = nesting_level

    def _apply_fn(self, data):
        if self.input_col is None:
            res = self.fn(data, *self.args, **self.kwargs)
        elif isinstance(self.input_col, (list, tuple)):
            args = tuple(data[col] for col in self.input_col)
            res = self.fn(*args, *self.args, **self.kwargs)
        else:
            res = self.fn(data[self.input_col], *self.args, **self.kwargs)

        if self.input_col is None and self.output_col is None:
            return res

        if isinstance(data, tuple):
            t_flag = True
            data = list(data)
        else:
            t_flag = False
            # Deepcopy data to prevent the original date modified. E.g. list, dict
            data = copy.deepcopy(data)

        if self.output_col is None:
            if isinstance(self.input_col, (list, tuple)):
                data[self.input_col[0]] = res
            else:
                data[self.input_col] = res
        elif isinstance(self.output_col, (list, tuple)):
            if not isinstance(res, Sized) or len(res) != len(self.output_col):
                raise TypeError(
                    "Result of callable function ({}) doesn't match the size of `output_col` ({})".format(
                        res, len(self.output_col)
                    )
                )
            for idx, r in zip(self.output_col, res):  # type: ignore[call-overload]
                if idx == -1:
                    data.append(r)
                else:
                    data[idx] = r
        else:
            if self.output_col == -1:
                data.append(res)
            else:
                data[self.output_col] = res

        return tuple(data) if t_flag else data

    def _apply(self, data, nesting_level):
        if nesting_level == 0:
            return self._apply_fn(data)
        elif nesting_level > 0:
            if isinstance(data, DataChunk):
                return type(data)(
                    [self._apply(i, nesting_level - 1) for i in data.raw_iterator()]
                )
            elif isinstance(data, list):
                return [self._apply(i, nesting_level - 1) for i in data]
            else:
                raise IndexError(
                    f"nesting_level {self.nesting_level} out of range (exceeds data pipe depth)"
                )
        else:
            if isinstance(data, DataChunk):
                return type(data)(
                    [self._apply(i, nesting_level) for i in data.raw_iterator()]
                )
            elif isinstance(data, list):
                return [self._apply(i, nesting_level) for i in data]
            else:
                return self._apply_fn(data)

    def __iter__(self) -> Iterator[T_co]:
        for data in self.datapipe:
            yield self._apply(data, self.nesting_level)

    def __len__(self) -> int:
        if isinstance(self.datapipe, Sized):
            return len(self.datapipe)
        raise TypeError(
            "{} instance doesn't have valid length".format(type(self).__name__)
        )

    def __getstate__(self):
        if DILL_AVAILABLE:
            dill_function = dill.dumps(self.fn)
        else:
            dill_function = self.fn
        state = (
            self.datapipe,
            dill_function,
            self.input_col,
            self.output_col,
            self.args,
            self.kwargs,
            self.nesting_level,
        )
        return state

    def __setstate__(self, state):
        (
            self.datapipe,
            dill_function,
            self.input_col,
            self.output_col,
            self.args,
            self.kwargs,
            self.nesting_level,
        ) = state
        if DILL_AVAILABLE:
            self.fn = dill.loads(dill_function)  # type: ignore[assignment]
        else:
            self.fn = dill_function  # type: ignore[assignment]


@functional_datapipe("collate")
class CollatorIterDataPipe(MapperIterDataPipe):
    r""":class:`CollatorIterDataPipe`.

    Iterable DataPipe to collate samples from datapipe to Tensor(s) by `util_.collate.default_collate`,
    or customized Data Structure by collate_fn.

    Args:
        datapipe: Iterable DataPipe being collated
        collate_fn: Customized collate function to collect and combine data or a batch of data.
            Default function collates to Tensor(s) based on data type.
        fn_args: Positional arguments for `collate_fn`
        fn_kwargs: Keyword arguments for `collate_fn`

    Example: Convert integer data to float Tensor
        >>> class MyIterDataPipe(torch.utils.data.IterDataPipe):
        ...     def __init__(self, start, end):
        ...         super(MyIterDataPipe).__init__()
        ...         assert end > start, "this example code only works with end >= start"
        ...         self.start = start
        ...         self.end = end
        ...
        ...     def __iter__(self):
        ...         return iter(range(self.start, self.end))
        ...
        ...     def __len__(self):
        ...         return self.end - self.start
        ...
        >>> ds = MyIterDataPipe(start=3, end=7)
        >>> print(list(ds))
        [3, 4, 5, 6]

        >>> def collate_fn(batch):
        ...     return torch.tensor(batch, dtype=torch.float)
        ...
        >>> collated_ds = CollateIterDataPipe(ds, collate_fn=collate_fn)
        >>> print(list(collated_ds))
        [tensor(3.), tensor(4.), tensor(5.), tensor(6.)]
    """

    def __init__(
        self,
        datapipe: IterDataPipe,
        collate_fn: Callable = _utils.collate.default_collate,
        fn_args: Optional[Tuple] = None,
        fn_kwargs: Optional[Dict] = None,
    ) -> None:
        super().__init__(datapipe, fn=collate_fn, fn_args=fn_args, fn_kwargs=fn_kwargs)
