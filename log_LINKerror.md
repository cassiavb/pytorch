
```

(integration8) C:\Users\localaccount\Documents\Integration\new_repo\pytorch>
(integration8) C:\Users\localaccount\Documents\Integration\new_repo\pytorch>compile_Win32bits.bat
**********************************************************************
** Visual Studio 2019 Developer Command Prompt v16.8.5
** Copyright (c) 2020 Microsoft Corporation
**********************************************************************
[vcvarsall.bat] Environment initialized for: 'x86'
Building wheel torch-1.10.0a0+git1562b44
-- Building version 1.10.0a0+git1562b44
cmake -GNinja -DBUILD_CAFFE2=OFF -DBUILD_CAFFE2_OPS=OFF -DBUILD_PYTHON=True -DBUILD_TEST=True -DCMAKE_BUILD_TYPE=Release -DCMAKE_GENERATOR=Ninja -DCMAKE_INCLUDE_PATH=C:\Users\localaccount\Documents\Integration\MKL\include -DCMAKE_INSTALL_PREFIX=C:\Users\localaccount\Documents\Integration\new_repo\pytorch\torch -DCMAKE_MAKE=Ninja -DCMAKE_PREFIX_PATH=C:\Users\localaccount\anaconda3\envs\integration8\Lib\site-packages -DNUMPY_INCLUDE_DIR=C:\Users\localaccount\anaconda3\envs\integration8\lib\site-packages\numpy\core\include -DPYTHON_EXECUTABLE=C:\Users\localaccount\anaconda3\envs\integration8\python.exe -DPYTHON_INCLUDE_DIR=C:\Users\localaccount\anaconda3\envs\integration8\Include -DPYTHON_LIBRARY=C:\Users\localaccount\anaconda3\envs\integration8/libs/python38.lib -DTORCH_BUILD_VERSION=1.10.0a0+git1562b44 -DUSE_CUDA=0 -DUSE_FBGEMM=0 -DUSE_KINETO=0 -DUSE_NUMPY=True C:\Users\localaccount\Documents\Integration\new_repo\pytorch
-- The CXX compiler identification is MSVC 19.28.29337.0
-- The C compiler identification is MSVC 19.28.29337.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/VC/Tools/MSVC/14.28.29333/bin/Hostx86/x86/cl.exe - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/VC/Tools/MSVC/14.28.29333/bin/Hostx86/x86/cl.exe - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Not forcing any particular BLAS to be found
CMake Warning at CMakeLists.txt:345 (message):
  TensorPipe cannot be used on Windows.  Set it to OFF


-- Performing Test COMPILER_WORKS
-- Performing Test COMPILER_WORKS - Success
-- Performing Test SUPPORT_GLIBCXX_USE_C99
-- Performing Test SUPPORT_GLIBCXX_USE_C99 - Success
-- Performing Test CAFFE2_EXCEPTION_PTR_SUPPORTED
-- Performing Test CAFFE2_EXCEPTION_PTR_SUPPORTED - Success
-- std::exception_ptr is supported.
-- Performing Test CAFFE2_NEED_TO_TURN_OFF_DEPRECATION_WARNING
-- Performing Test CAFFE2_NEED_TO_TURN_OFF_DEPRECATION_WARNING - Failed
-- Performing Test C_HAS_AVX_1
-- Performing Test C_HAS_AVX_1 - Success
-- Performing Test C_HAS_AVX2_1
-- Performing Test C_HAS_AVX2_1 - Failed
-- Performing Test C_HAS_AVX2_2
-- Performing Test C_HAS_AVX2_2 - Failed
-- Performing Test C_HAS_AVX2_3
-- Performing Test C_HAS_AVX2_3 - Failed
-- Performing Test C_HAS_AVX512_1
-- Performing Test C_HAS_AVX512_1 - Success
-- Performing Test CXX_HAS_AVX_1
-- Performing Test CXX_HAS_AVX_1 - Success
-- Performing Test CXX_HAS_AVX2_1
-- Performing Test CXX_HAS_AVX2_1 - Failed
-- Performing Test CXX_HAS_AVX2_2
-- Performing Test CXX_HAS_AVX2_2 - Failed
-- Performing Test CXX_HAS_AVX2_3
-- Performing Test CXX_HAS_AVX2_3 - Failed
-- Performing Test CXX_HAS_AVX512_1
-- Performing Test CXX_HAS_AVX512_1 - Success
-- Performing Test CAFFE2_COMPILER_SUPPORTS_AVX512_EXTENSIONS
-- Performing Test CAFFE2_COMPILER_SUPPORTS_AVX512_EXTENSIONS - Success
-- Current compiler supports avx512f extension. Will build fbgemm.
-- Performing Test COMPILER_SUPPORTS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_SUPPORTS_HIDDEN_VISIBILITY - Failed
-- Performing Test COMPILER_SUPPORTS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_SUPPORTS_HIDDEN_INLINE_VISIBILITY - Failed
-- Building using own protobuf under third_party per request.
-- Use custom protobuf build.
--
-- 3.13.0.0
-- Looking for pthread.h
-- Looking for pthread.h - not found
-- Found Threads: TRUE
-- Caffe2 protobuf include directory: $<BUILD_INTERFACE:C:/Users/localaccount/Documents/Integration/new_repo/pytorch/third_party/protobuf/src>$<INSTALL_INTERFACE:include>
-- Trying to find preferred BLAS backend of choice: MKL
-- MKL_THREADING = OMP
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of void*
-- Check size of void* - done
-- MKL_THREADING = OMP
CMake Warning at cmake/Dependencies.cmake:177 (message):
  MKL could not be found.  Defaulting to Eigen
Call Stack (most recent call first):
  CMakeLists.txt:656 (include)


CMake Warning at cmake/Dependencies.cmake:205 (message):
  Preferred BLAS (MKL) cannot be found, now searching for a general BLAS
  library
Call Stack (most recent call first):
  CMakeLists.txt:656 (include)


-- MKL_THREADING = OMP
-- Checking for [mkl_intel - mkl_intel_thread - mkl_core - libiomp5md]
--   Library mkl_intel: not found
-- Checking for [mkl_intel - mkl_intel_thread - mkl_core]
--   Library mkl_intel: not found
-- Checking for [mkl_intel - mkl_sequential - mkl_core]
--   Library mkl_intel: not found
-- Checking for [mkl_intel - mkl_core - libiomp5md - pthread]
--   Library mkl_intel: not found
-- Checking for [mkl_intel - mkl_core - pthread]
--   Library mkl_intel: not found
-- Checking for [mkl - guide - pthread - m]
--   Library mkl: not found
-- MKL library not found
-- Checking for [blis]
--   Library blis: BLAS_blis_LIBRARY-NOTFOUND
-- Checking for [Accelerate]
--   Library Accelerate: BLAS_Accelerate_LIBRARY-NOTFOUND
-- Checking for [vecLib]
--   Library vecLib: BLAS_vecLib_LIBRARY-NOTFOUND
-- Checking for [openblas]
--   Library openblas: BLAS_openblas_LIBRARY-NOTFOUND
-- Checking for [openblas - pthread - m]
--   Library openblas: BLAS_openblas_LIBRARY-NOTFOUND
-- Checking for [openblas - pthread - m - gomp]
--   Library openblas: BLAS_openblas_LIBRARY-NOTFOUND
-- Checking for [libopenblas]
--   Library libopenblas: BLAS_libopenblas_LIBRARY-NOTFOUND
-- Checking for [goto2 - gfortran]
--   Library goto2: BLAS_goto2_LIBRARY-NOTFOUND
-- Checking for [goto2 - gfortran - pthread]
--   Library goto2: BLAS_goto2_LIBRARY-NOTFOUND
-- Checking for [acml - gfortran]
--   Library acml: BLAS_acml_LIBRARY-NOTFOUND
-- Checking for [blis]
--   Library blis: BLAS_blis_LIBRARY-NOTFOUND
-- Could NOT find Atlas (missing: Atlas_CBLAS_INCLUDE_DIR Atlas_CLAPACK_INCLUDE_DIR Atlas_CBLAS_LIBRARY Atlas_BLAS_LIBRARY Atlas_LAPACK_LIBRARY)
-- Checking for [ptf77blas - atlas - gfortran]
--   Library ptf77blas: BLAS_ptf77blas_LIBRARY-NOTFOUND
-- Checking for [blas]
--   Library blas: BLAS_blas_LIBRARY-NOTFOUND
-- Cannot find a library with BLAS API. Not using BLAS.
-- Using pocketfft in directory: C:/Users/localaccount/Documents/Integration/new_repo/pytorch/third_party/pocketfft
-- The ASM compiler identification is MSVC
-- Found assembler: C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/VC/Tools/MSVC/14.28.29333/bin/Hostx86/x86/cl.exe
-- Found Python: C:/Users/localaccount/anaconda3/envs/integration8/python.exe (found version "3.8.11") found components: Interpreter
-- Found Git: C:/Users/localaccount/anaconda3/envs/integration8/Library/bin/git.exe (found version "2.23.0.windows.1")
-- git version: v1.5.5 normalized to 1.5.5
-- Version: 1.5.5
-- Performing Test HAVE_STD_REGEX
-- Performing Test HAVE_STD_REGEX
-- Performing Test HAVE_STD_REGEX -- success
-- Performing Test HAVE_GNU_POSIX_REGEX
-- Performing Test HAVE_GNU_POSIX_REGEX
-- Performing Test HAVE_GNU_POSIX_REGEX -- failed to compile
-- Performing Test HAVE_POSIX_REGEX
-- Performing Test HAVE_POSIX_REGEX
-- Performing Test HAVE_POSIX_REGEX -- failed to compile
-- Performing Test HAVE_STEADY_CLOCK
-- Performing Test HAVE_STEADY_CLOCK
-- Performing Test HAVE_STEADY_CLOCK -- success
CMake Warning at cmake/Dependencies.cmake:784 (message):
  Turning USE_FAKELOWP off as it depends on USE_FBGEMM.
Call Stack (most recent call first):
  CMakeLists.txt:656 (include)


-- Using third party subdirectory Eigen.
-- Found PythonInterp: C:/Users/localaccount/anaconda3/envs/integration8/python.exe (found suitable version "3.8.11", minimum required is "3.0")
-- Found PythonLibs: C:/Users/localaccount/anaconda3/envs/integration8/libs/python38.lib (found suitable version "3.8.11", minimum required is "3.0")
-- Using third_party/pybind11.
-- pybind11 include dirs: C:/Users/localaccount/Documents/Integration/new_repo/pytorch/cmake/../third_party/pybind11/include
-- Could NOT find MPI_C (missing: MPI_C_LIB_NAMES MPI_C_HEADER_DIR MPI_C_WORKS)
-- Could NOT find MPI_CXX (missing: MPI_CXX_LIB_NAMES MPI_CXX_HEADER_DIR MPI_CXX_WORKS)
-- Could NOT find MPI (missing: MPI_C_FOUND MPI_CXX_FOUND)
    Reason given by package: MPI component 'Fortran' was requested, but language Fortran is not enabled.

CMake Warning at cmake/Dependencies.cmake:1086 (message):
  Not compiling with MPI.  Suppress this warning with -DUSE_MPI=OFF
Call Stack (most recent call first):
  CMakeLists.txt:656 (include)


-- MKL_THREADING = OMP
-- MKL_THREADING = OMP
CMake Warning (dev) at C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/Common7/IDE/CommonExtensions/Microsoft/CMake/CMake/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake:273 (message):
  The package name passed to `find_package_handle_standard_args` (OpenMP_C)
  does not match the name of the calling package (OpenMP).  This can lead to
  problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/Modules/FindOpenMP.cmake:576 (find_package_handle_standard_args)
  cmake/Dependencies.cmake:1141 (find_package)
  CMakeLists.txt:656 (include)
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/Common7/IDE/CommonExtensions/Microsoft/CMake/CMake/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake:273 (message):
  The package name passed to `find_package_handle_standard_args` (OpenMP_CXX)
  does not match the name of the calling package (OpenMP).  This can lead to
  problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/Modules/FindOpenMP.cmake:576 (find_package_handle_standard_args)
  cmake/Dependencies.cmake:1141 (find_package)
  CMakeLists.txt:656 (include)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Adding OpenMP CXX_FLAGS: -openmp:experimental -IC:/Users/localaccount/Documents/Integration/MKL/include
-- No OpenMP library needs to be linked against
CMake Warning at cmake/Dependencies.cmake:1353 (message):
  Gloo can only be used on 64-bit systems.
Call Stack (most recent call first):
  CMakeLists.txt:656 (include)


CMake Warning at cmake/Dependencies.cmake:1458 (message):
  Metal is only used in ios builds.
Call Stack (most recent call first):
  CMakeLists.txt:656 (include)


-- Found PythonInterp: C:/Users/localaccount/anaconda3/envs/integration8/python.exe (found version "3.8.11")
-- Found PythonLibs: C:/Users/localaccount/anaconda3/envs/integration8/libs/python38.lib (found version "3.8.11")
Generated: C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx/onnx_onnx_torch-ml.proto
Generated: C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx/onnx-operators_onnx_torch-ml.proto
Generated: C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx/onnx-data_onnx_torch.proto
--
-- ******** Summary ********
--   CMake version             : 3.18.20081302-MSVC_2
--   CMake command             : C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/Common7/IDE/CommonExtensions/Microsoft/CMake/CMake/bin/cmake.exe
--   System                    : Windows
--   C++ compiler              : C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/VC/Tools/MSVC/14.28.29333/bin/Hostx86/x86/cl.exe
--   C++ compiler version      : 19.28.29337.0
--   CXX flags                 : /DWIN32 /D_WINDOWS /GR /EHsc /w /bigobj -DUSE_PTHREADPOOL -openmp:experimental -IC:/Users/localaccount/Documents/Integration/MKL/include /EHsc /wd26812
--   Build type                : Release
--   Compile definitions       : WIN32_LEAN_AND_MEAN;ONNX_ML=1;ONNXIFI_ENABLE_EXT=1
--   CMAKE_PREFIX_PATH         : C:\Users\localaccount\anaconda3\envs\integration8\Lib\site-packages
--   CMAKE_INSTALL_PREFIX      : C:/Users/localaccount/Documents/Integration/new_repo/pytorch/torch
--   CMAKE_MODULE_PATH         : C:/Users/localaccount/Documents/Integration/new_repo/pytorch/cmake/Modules
--
--   ONNX version              : 1.8.204
--   ONNX NAMESPACE            : onnx_torch
--   ONNX_USE_LITE_PROTO       : OFF
--   USE_PROTOBUF_SHARED_LIBS  : OFF
--   ONNX_DISABLE_EXCEPTIONS   : OFF
--   ONNX_WERROR               : OFF
--   ONNX_BUILD_TESTS          : OFF
--   ONNX_BUILD_BENCHMARKS     : OFF
--   ONNXIFI_DUMMY_BACKEND     : OFF
--   ONNXIFI_ENABLE_EXT        : OFF
--
--   Protobuf compiler         :
--   Protobuf includes         :
--   Protobuf libraries        :
--   BUILD_ONNX_PYTHON         : OFF
--
-- ******** Summary ********
--   CMake version         : 3.18.20081302-MSVC_2
--   CMake command         : C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/Common7/IDE/CommonExtensions/Microsoft/CMake/CMake/bin/cmake.exe
--   System                : Windows
--   C++ compiler          : C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/VC/Tools/MSVC/14.28.29333/bin/Hostx86/x86/cl.exe
--   C++ compiler version  : 19.28.29337.0
--   CXX flags             : /DWIN32 /D_WINDOWS /GR /EHsc /w /bigobj -DUSE_PTHREADPOOL -openmp:experimental -IC:/Users/localaccount/Documents/Integration/MKL/include
--   Build type            : Release
--   Compile definitions   : WIN32_LEAN_AND_MEAN;ONNX_ML=1;ONNXIFI_ENABLE_EXT=1
--   CMAKE_PREFIX_PATH     : C:\Users\localaccount\anaconda3\envs\integration8\Lib\site-packages
--   CMAKE_INSTALL_PREFIX  : C:/Users/localaccount/Documents/Integration/new_repo/pytorch/torch
--   CMAKE_MODULE_PATH     : C:/Users/localaccount/Documents/Integration/new_repo/pytorch/cmake/Modules
--
--   ONNX version          : 1.4.1
--   ONNX NAMESPACE        : onnx_torch
--   ONNX_BUILD_TESTS      : OFF
--   ONNX_BUILD_BENCHMARKS : OFF
--   ONNX_USE_LITE_PROTO   : OFF
--   ONNXIFI_DUMMY_BACKEND : OFF
--
--   Protobuf compiler     :
--   Protobuf includes     :
--   Protobuf libraries    :
--   BUILD_ONNX_PYTHON     : OFF
-- Could not find CUDA with FP16 support, compiling without torch.CudaHalfTensor
-- Adding -DNDEBUG to compile flags
CMake Warning at cmake/Dependencies.cmake:1679 (message):
  Not compiling with MAGMA.  Suppress this warning with -DUSE_MAGMA=OFF.
Call Stack (most recent call first):
  CMakeLists.txt:656 (include)


-- Could not find hardware support for NEON on this machine.
-- No OMAP3 processor on this machine.
-- No OMAP4 processor on this machine.
-- Looking for cpuid.h
-- Looking for cpuid.h - not found
-- Performing Test NO_GCC_EBX_FPIC_BUG
-- Performing Test NO_GCC_EBX_FPIC_BUG - Failed
-- AVX compiler support found
-- MKL_THREADING = OMP
-- Checking for [mkl_intel - mkl_intel_thread - mkl_core - libiomp5md]
--   Library mkl_intel: not found
-- Checking for [mkl_intel - mkl_intel_thread - mkl_core]
--   Library mkl_intel: not found
-- Checking for [mkl_intel - mkl_sequential - mkl_core]
--   Library mkl_intel: not found
-- Checking for [mkl_intel - mkl_core - libiomp5md - pthread]
--   Library mkl_intel: not found
-- Checking for [mkl_intel - mkl_core - pthread]
--   Library mkl_intel: not found
-- Checking for [mkl - guide - pthread - m]
--   Library mkl: not found
-- MKL library not found
-- Checking for [blis]
--   Library blis: BLAS_blis_LIBRARY-NOTFOUND
-- Checking for [Accelerate]
--   Library Accelerate: BLAS_Accelerate_LIBRARY-NOTFOUND
-- Checking for [vecLib]
--   Library vecLib: BLAS_vecLib_LIBRARY-NOTFOUND
-- Checking for [openblas]
--   Library openblas: BLAS_openblas_LIBRARY-NOTFOUND
-- Checking for [openblas - pthread - m]
--   Library openblas: BLAS_openblas_LIBRARY-NOTFOUND
-- Checking for [openblas - pthread - m - gomp]
--   Library openblas: BLAS_openblas_LIBRARY-NOTFOUND
-- Checking for [libopenblas]
--   Library libopenblas: BLAS_libopenblas_LIBRARY-NOTFOUND
-- Checking for [goto2 - gfortran]
--   Library goto2: BLAS_goto2_LIBRARY-NOTFOUND
-- Checking for [goto2 - gfortran - pthread]
--   Library goto2: BLAS_goto2_LIBRARY-NOTFOUND
-- Checking for [acml - gfortran]
--   Library acml: BLAS_acml_LIBRARY-NOTFOUND
-- Checking for [blis]
--   Library blis: BLAS_blis_LIBRARY-NOTFOUND
-- Could NOT find Atlas (missing: Atlas_CBLAS_INCLUDE_DIR Atlas_CLAPACK_INCLUDE_DIR Atlas_CBLAS_LIBRARY Atlas_BLAS_LIBRARY Atlas_LAPACK_LIBRARY)
-- Checking for [ptf77blas - atlas - gfortran]
--   Library ptf77blas: BLAS_ptf77blas_LIBRARY-NOTFOUND
-- Checking for [blas]
--   Library blas: BLAS_blas_LIBRARY-NOTFOUND
-- Cannot find a library with BLAS API. Not using BLAS.
-- LAPACK requires BLAS
-- Cannot find a library with LAPACK API. Not using LAPACK.
disabling CUDA because NOT USE_CUDA is set
-- USE_CUDNN is set to 0. Compiling without cuDNN support
disabling ROCM because NOT USE_ROCM is set
-- MIOpen not found. Compiling without MIOpen support
CMake Warning at cmake/Dependencies.cmake:1797 (message):
  x64 operating system is required for MKLDNN.  Not compiling with MKLDNN.
  Turn this warning off by USE_MKLDNN=OFF.
Call Stack (most recent call first):
  CMakeLists.txt:656 (include)


disabling MKLDNN because USE_MKLDNN is not set
-- Performing Test C_HAS_THREAD
-- Performing Test C_HAS_THREAD - Success
-- Version: 7.0.3
-- Build type: Release
-- CXX_STANDARD: 14
-- Performing Test has_std_14_flag
-- Performing Test has_std_14_flag - Failed
-- Performing Test has_std_1y_flag
-- Performing Test has_std_1y_flag - Failed
-- Performing Test SUPPORTS_USER_DEFINED_LITERALS
-- Performing Test SUPPORTS_USER_DEFINED_LITERALS - Success
-- Performing Test FMT_HAS_VARIANT
-- Performing Test FMT_HAS_VARIANT - Success
-- Required features: cxx_variadic_templates
-- Looking for _strtod_l
-- Looking for _strtod_l - found
-- Looking for backtrace
-- Looking for backtrace - not found
-- Could NOT find Backtrace (missing: Backtrace_LIBRARY Backtrace_INCLUDE_DIR)
-- don't use NUMA
-- Using ATen parallel backend: OMP
disabling CUDA because USE_CUDA is set false
AT_INSTALL_INCLUDE_DIR include/ATen/core
core header install: C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/aten/src/ATen/core/TensorBody.h
CMake Warning (dev) at torch/CMakeLists.txt:407:
  Syntax Warning in cmake code at column 107

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at torch/CMakeLists.txt:407:
  Syntax Warning in cmake code at column 115

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/Common7/IDE/CommonExtensions/Microsoft/CMake/CMake/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake:273 (message):
  The package name passed to `find_package_handle_standard_args` (OpenMP_C)
  does not match the name of the calling package (OpenMP).  This can lead to
  problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/Modules/FindOpenMP.cmake:576 (find_package_handle_standard_args)
  caffe2/CMakeLists.txt:1204 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/Common7/IDE/CommonExtensions/Microsoft/CMake/CMake/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake:273 (message):
  The package name passed to `find_package_handle_standard_args` (OpenMP_CXX)
  does not match the name of the calling package (OpenMP).  This can lead to
  problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/Modules/FindOpenMP.cmake:576 (find_package_handle_standard_args)
  caffe2/CMakeLists.txt:1204 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- pytorch is compiling with OpenMP.
OpenMP CXX_FLAGS: -openmp:experimental -IC:/Users/localaccount/Documents/Integration/MKL/include.
OpenMP libraries: .
-- Caffe2 is compiling with OpenMP.
OpenMP CXX_FLAGS: -openmp:experimental -IC:/Users/localaccount/Documents/Integration/MKL/include.
OpenMP libraries: .
-- Using Lib/site-packages as python relative installation path
CMake Warning at CMakeLists.txt:988 (message):
  Generated cmake files are only fully tested if one builds with system glog,
  gflags, and protobuf.  Other settings may generate files that are not well
  tested.


--
-- ******** Summary ********
-- General:
--   CMake version         : 3.18.20081302-MSVC_2
--   CMake command         : C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/Common7/IDE/CommonExtensions/Microsoft/CMake/CMake/bin/cmake.exe
--   System                : Windows
--   C++ compiler          : C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/VC/Tools/MSVC/14.28.29333/bin/Hostx86/x86/cl.exe
--   C++ compiler id       : MSVC
--   C++ compiler version  : 19.28.29337.0
--   Using ccache if found : OFF
--   CXX flags             : /DWIN32 /D_WINDOWS /GR /EHsc /w /bigobj -DUSE_PTHREADPOOL -openmp:experimental -IC:/Users/localaccount/Documents/Integration/MKL/include -DNDEBUG -DUSE_XNNPACK -DSYMBOLICATE_MOBILE_DEBUG_HANDLE -DEDGE_PROFILER_USE_KINETO
--   Build type            : Release
--   Compile definitions   : WIN32_LEAN_AND_MEAN;ONNX_ML=1;ONNXIFI_ENABLE_EXT=1;ONNX_NAMESPACE=onnx_torch;_CRT_SECURE_NO_DEPRECATE=1;USE_EXTERNAL_MZCRC;MINIZ_DISABLE_ZIP_READER_CRC32_CHECKS
--   CMAKE_PREFIX_PATH     : C:\Users\localaccount\anaconda3\envs\integration8\Lib\site-packages
--   CMAKE_INSTALL_PREFIX  : C:/Users/localaccount/Documents/Integration/new_repo/pytorch/torch
--   USE_GOLD_LINKER       : OFF
--
--   TORCH_VERSION         : 1.10.0
--   CAFFE2_VERSION        : 1.10.0
--   BUILD_CAFFE2          : OFF
--   BUILD_CAFFE2_OPS      : OFF
--   BUILD_CAFFE2_MOBILE   : OFF
--   BUILD_STATIC_RUNTIME_BENCHMARK: OFF
--   BUILD_TENSOREXPR_BENCHMARK: OFF
--   BUILD_NVFUSER_BENCHMARK: OFF
--   BUILD_BINARY          : OFF
--   BUILD_CUSTOM_PROTOBUF : ON
--     Link local protobuf : ON
--   BUILD_DOCS            : OFF
--   BUILD_PYTHON          : True
--     Python version      : 3.8.11
--     Python executable   : C:/Users/localaccount/anaconda3/envs/integration8/python.exe
--     Pythonlibs version  : 3.8.11
--     Python library      : C:/Users/localaccount/anaconda3/envs/integration8/libs/python38.lib
--     Python includes     : C:/Users/localaccount/anaconda3/envs/integration8/include
--     Python site-packages: Lib/site-packages
--   BUILD_SHARED_LIBS     : ON
--   CAFFE2_USE_MSVC_STATIC_RUNTIME     : OFF
--   BUILD_TEST            : True
--   BUILD_JNI             : OFF
--   BUILD_MOBILE_AUTOGRAD : OFF
--   BUILD_LITE_INTERPRETER: OFF
--   INTERN_BUILD_MOBILE   :
--   USE_BLAS              : 0
--   USE_LAPACK            : 0
--   USE_ASAN              : OFF
--   USE_CPP_CODE_COVERAGE : OFF
--   USE_CUDA              : 0
--   USE_ROCM              : OFF
--   USE_EIGEN_FOR_BLAS    : ON
--   USE_FBGEMM            : OFF
--     USE_FAKELOWP          : OFF
--   USE_KINETO            : 0
--   USE_FFMPEG            : OFF
--   USE_GFLAGS            : OFF
--   USE_GLOG              : OFF
--   USE_LEVELDB           : OFF
--   USE_LITE_PROTO        : OFF
--   USE_LMDB              : OFF
--   USE_METAL             : OFF
--   USE_PYTORCH_METAL     : OFF
--   USE_PYTORCH_METAL_EXPORT     : OFF
--   USE_FFTW              : OFF
--   USE_MKL               : OFF
--   USE_MKLDNN            : OFF
--   USE_NCCL              : OFF
--   USE_NNPACK            : OFF
--   USE_NUMPY             : ON
--   USE_OBSERVERS         : ON
--   USE_OPENCL            : OFF
--   USE_OPENCV            : OFF
--   USE_OPENMP            : ON
--   USE_TBB               : OFF
--   USE_VULKAN            : OFF
--   USE_PROF              : OFF
--   USE_QNNPACK           : OFF
--   USE_PYTORCH_QNNPACK   : OFF
--   USE_REDIS             : OFF
--   USE_ROCKSDB           : OFF
--   USE_ZMQ               : OFF
--   USE_DISTRIBUTED       : ON
--     USE_MPI               : OFF
--     USE_GLOO              : OFF
--     USE_GLOO_WITH_OPENSSL : OFF
--     USE_TENSORPIPE        : OFF
--   USE_DEPLOY           : OFF
--   USE_BREAKPAD         : ON
--   Public Dependencies  : Threads::Threads
--   Private Dependencies : pthreadpool;cpuinfo;XNNPACK;fp16;foxi_loader;fmt::fmt-header-only
--   USE_COREML_DELEGATE     : OFF
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    CMAKE_MAKE


-- Build files have been written to: C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build
cmake --build . --target install --config Release
[57/3791] Building RC object third_party\protobuf\cmake\CMakeFiles\libprotoc.dir\version.rc.res
Microsoft (R) Windows (R) Resource Compiler Version 10.0.10011.16384
Copyright (C) Microsoft Corporation.  All rights reserved.

[242/3791] Building RC object third_party\protobuf\cmake\CMakeFiles\libprotobuf-lite.dir\version.rc.res
Microsoft (R) Windows (R) Resource Compiler Version 10.0.10011.16384
Copyright (C) Microsoft Corporation.  All rights reserved.

[248/3791] Building RC object third_party\protobuf\cmake\CMakeFiles\protoc.dir\version.rc.res
Microsoft (R) Windows (R) Resource Compiler Version 10.0.10011.16384
Copyright (C) Microsoft Corporation.  All rights reserved.

[486/3791] Building RC object third_party\protobuf\cmake\CMakeFiles\libprotobuf.dir\version.rc.res
Microsoft (R) Windows (R) Resource Compiler Version 10.0.10011.16384
Copyright (C) Microsoft Corporation.  All rights reserved.

[525/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\average-pooling-nhwc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[527/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\argmax-pooling-nhwc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[528/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\constant-pad-nd.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[531/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\depth-to-space-nhwc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[533/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\channel-shuffle-nc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[534/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\binary-elementwise-nd.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[535/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\deconvolution-nhwc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[537/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\convolution-nhwc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[539/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\depth-to-space-nchw2nhwc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[540/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\max-pooling-nhwc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[541/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\fully-connected-nc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[542/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\prelu-nc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[543/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\convolution-nchw.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[544/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\leaky-relu-nc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[545/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\unpooling-nhwc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[546/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\global-average-pooling-ncw.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[547/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\global-average-pooling-nwc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[548/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\softmax-nc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[549/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\unary-elementwise-nc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[550/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\resize-bilinear-nchw.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[551/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\sigmoid-nc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[552/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\argmax-pooling-2d.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[553/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\bankers-rounding.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[554/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operators\resize-bilinear-nhwc.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[555/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\average-pooling-2d.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[556/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\ceiling.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[557/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\abs.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[558/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\clamp.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[559/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\add2.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[561/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\convolution-2d.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[562/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\deconvolution-2d.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[563/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\divide.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[564/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\depthwise-convolution-2d.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[565/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\depth-to-space.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[566/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\hardswish.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[567/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\fully-connected.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[568/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\floor.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[569/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\global-average-pooling-2d.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[570/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\leaky-relu.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[571/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\maximum2.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[572/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\elu.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[573/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\multiply2.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[574/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\minimum2.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[575/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\negate.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[576/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\max-pooling-2d.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[577/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\softmax.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[578/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\square-root.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[579/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\squared-difference.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[580/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\prelu.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[581/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\sigmoid.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[582/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\datatype-strings.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[583/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\square.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[584/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\static-reshape.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[585/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\subtract.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[586/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\unpooling-2d.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[587/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\static-resize-bilinear-2d.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[588/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph\static-constant-pad.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[589/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\memory-planner.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[590/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph-strings.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[591/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\allocator.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[592/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operator-strings.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[593/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\operator-delete.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[600/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\subgraph.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[601/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\tensor.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[604/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\init.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[617/3791] Building C object confu-deps\XNNPACK\CMakeFiles\XNNPACK.dir\src\runtime.c.obj
cl : Command line warning D9025 : overriding '/O2' with '/O1'
[2416/3791] Running gen_proto.py on onnx/onnx.in.proto
Processing C:\Users\localaccount\Documents\Integration\new_repo\pytorch\third_party\onnx\onnx\onnx.in.proto
Writing C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx\onnx_onnx_torch-ml.proto
Writing C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx\onnx_onnx_torch-ml.proto3
Writing C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx\onnx-ml.pb.h
generating C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx\onnx_pb.py
[2458/3791] Building CXX object third_party\googletest\googlemock\CMakeFiles\gmock_main.dir\src\gmock_main.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
[2460/3791] Building CXX object third_party\googletest\googlemock\CMakeFiles\gmock_main.dir\src\gmock-all.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
[2461/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark_main.dir\benchmark_main.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2462/3791] Building CXX object third_party\googletest\googlemock\CMakeFiles\gmock.dir\src\gmock-all.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
[2463/3791] Building CXX object third_party\googletest\googletest\CMakeFiles\gtest_main.dir\src\gtest_main.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
[2464/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\benchmark_runner.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2465/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\benchmark.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2466/3791] Building CXX object third_party\googletest\googlemock\CMakeFiles\gmock_main.dir\__\googletest\src\gtest-all.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
[2467/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\benchmark_register.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2469/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\benchmark_name.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2470/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\benchmark_api_internal.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2471/3791] Building CXX object third_party\googletest\googlemock\CMakeFiles\gmock.dir\__\googletest\src\gtest-all.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
[2472/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\counter.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2474/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\console_reporter.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2475/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\complexity.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2476/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\colorprint.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2477/3791] Building CXX object third_party\googletest\googletest\CMakeFiles\gtest.dir\src\gtest-all.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
[2478/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\csv_reporter.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2479/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\commandlineflags.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2482/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\sleep.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2483/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\perf_counters.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2484/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\reporter.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2485/3791] Running gen_proto.py on onnx/onnx-operators.in.proto
Processing C:\Users\localaccount\Documents\Integration\new_repo\pytorch\third_party\onnx\onnx\onnx-operators.in.proto
Writing C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx\onnx-operators_onnx_torch-ml.proto
Writing C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx\onnx-operators_onnx_torch-ml.proto3
Writing C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx\onnx-operators-ml.pb.h
generating C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx\onnx_operators_pb.py
[2486/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\statistics.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2487/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\timers.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2488/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\string_util.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2490/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\json_reporter.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2491/3791] Running gen_proto.py on onnx/onnx-data.in.proto
Processing C:\Users\localaccount\Documents\Integration\new_repo\pytorch\third_party\onnx\onnx\onnx-data.in.proto
Writing C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx\onnx-data_onnx_torch.proto
Writing C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx\onnx-data_onnx_torch.proto3
Writing C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx\onnx-data.pb.h
generating C:/Users/localaccount/Documents/Integration/new_repo/pytorch/build/third_party/onnx/onnx\onnx_data_pb.py
[2492/3791] Building CXX object third_party\benchmark\src\CMakeFiles\benchmark.dir\sysinfo.cc.obj
cl : Command line warning D9025 : overriding '/w' with '/W4'
cl : Command line warning D9025 : overriding '/W4' with '/w'
[2578/3791] Linking CXX shared library bin\c10.dll
   Creating library lib\c10.lib and object lib\c10.exp
[2587/3791] Linking CXX executable bin\c10_flags_test.exe
   Creating library lib\c10_flags_test.lib and object lib\c10_flags_test.exp
[2610/3791] Linking CXX executable bin\c10_registry_test.exe
   Creating library lib\c10_registry_test.lib and object lib\c10_registry_test.exp
[2613/3791] Building CXX object c10\test\CMakeFiles\c10_Metaprogramming_test.dir\util\Metaprogramming_test.cpp.obj
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.28.29333\include\tuple(163): warning C4244: 'initializing': conversion from '_Ty' to '_Ty', possible loss of data
        with
        [
            _Ty=double
        ]
        and
        [
            _Ty=float
        ]
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.28.29333\include\tuple(245): note: see reference to function template instantiation 'std::_Tuple_val<_This>::_Tuple_val<_Ty>(_Other &&)' being compiled
        with
        [
            _This=float,
            _Ty=double,
            _Other=double
        ]
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.28.29333\include\tuple(245): note: see reference to function template instantiation 'std::_Tuple_val<_This>::_Tuple_val<_Ty>(_Other &&)' being compiled
        with
        [
            _This=float,
            _Ty=double,
            _Other=double
        ]
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.28.29333\include\tuple(245): note: see reference to function template instantiation 'std::tuple<float>::tuple<std::_Exact_args_t,_Ty,,0>(_Tag,_This2 &&)' being compiled
        with
        [
            _Ty=double,
            _Tag=std::_Exact_args_t,
            _This2=double
        ]
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.28.29333\include\tuple(245): note: see reference to function template instantiation 'std::tuple<float>::tuple<std::_Exact_args_t,_Ty,,0>(_Tag,_This2 &&)' being compiled
        with
        [
            _Ty=double,
            _Tag=std::_Exact_args_t,
            _This2=double
        ]
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.28.29333\include\tuple(326): note: see reference to function template instantiation 'std::tuple<std::string,float>::tuple<std::_Exact_args_t,const char(&)[2],_Ty,0>(_Tag,_This2,_Ty &&)' being compiled
        with
        [
            _Ty=double,
            _Tag=std::_Exact_args_t,
            _This2=const char (&)[2]
        ]
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.28.29333\include\tuple(326): note: see reference to function template instantiation 'std::tuple<std::string,float>::tuple<std::_Exact_args_t,const char(&)[2],_Ty,0>(_Tag,_This2,_Ty &&)' being compiled
        with
        [
            _Ty=double,
            _Tag=std::_Exact_args_t,
            _This2=const char (&)[2]
        ]
..\c10\test\util\Metaprogramming_test.cpp(566): note: see reference to function template instantiation 'std::tuple<std::string,float>::tuple<const char(&)[2],double,0>(_This2,double &&) noexcept(false)' being compiled
        with
        [
            _This2=const char (&)[2]
        ]
..\c10\test\util\Metaprogramming_test.cpp(563): note: see reference to function template instantiation 'std::tuple<std::string,float>::tuple<const char(&)[2],double,0>(_This2,double &&) noexcept(false)' being compiled
        with
        [
            _This2=const char (&)[2]
        ]
[2640/3791] Linking CXX executable bin\c10_typeid_test.exe
   Creating library lib\c10_typeid_test.lib and object lib\c10_typeid_test.exp
[3041/3791] Building CXX object caffe2\CMakeFiles\torch_cpu.dir\utils\threadpool\ThreadPool.cc.obj
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.28.29333\include\xstddef(251): warning C4018: '>=': signed/unsigned mismatch
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.28.29333\include\xstddef(250): note: while compiling class template member function 'bool std::greater_equal<void>::operator ()<const T1&,const T2&>(_Ty1,_Ty2) noexcept(<expr>) const'
        with
        [
            T1=unsigned int,
            T2=int,
            _Ty1=const unsigned int &,
            _Ty2=const int &
        ]
C:\Users\localaccount\Documents\Integration\new_repo\pytorch\caffe2\utils\threadpool\WorkersPool.h(336): note: see reference to function template instantiation 'void c10::enforce_detail::enforceThatImpl<std::greater_equal<void>,unsigned int,int,>(Pred,const T1 &,const T2 &,const char *,int,const char *,const void *)' being compiled
        with
        [
            Pred=std::greater_equal<void>,
            T1=unsigned int,
            T2=int
        ]
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.28.29333\include\xstddef(253): warning C4018: '>=': signed/unsigned mismatch
..\c10/util/Logging.h(209): note: see reference to function template instantiation 'bool std::greater_equal<void>::operator ()<const T1&,const T2&>(_Ty1,_Ty2) noexcept const' being compiled
        with
        [
            T1=unsigned int,
            T2=int,
            _Ty1=const unsigned int &,
            _Ty2=const int &
        ]
C:\Users\localaccount\Documents\Integration\new_repo\pytorch\caffe2\utils\threadpool\WorkersPool.h(336): note: see reference to function template instantiation 'void c10::enforce_detail::enforceThatImpl<std::greater_equal<void>,unsigned int,int,>(Pred,const T1 &,const T2 &,const char *,int,const char *,const void *)' being compiled
        with
        [
            Pred=std::greater_equal<void>,
            T1=unsigned int,
            T2=int
        ]
[3688/3791] Linking CXX shared library bin\torch_cpu.dll
LINK : the 32-bit linker (C:\PROGRA~2\MICROS~2\2019\BUILDT~1\VC\Tools\MSVC\1428~1.293\bin\Hostx86\x86\link.exe) ran out of heap space and is going to restart linking with a 64-bit linker
LINK : restarting link with 64-bit linker `C:\PROGRA~2\MICROS~2\2019\BUILDT~1\VC\Tools\MSVC\1428~1.293\bin\Hostx64\x86\link.exe'
   Creating library lib\torch_cpu.lib and object lib\torch_cpu.exp
[3689/3791] Linking CXX shared library bin\torch.dll
   Creating library lib\torch.lib and object lib\torch.exp
[3690/3791] Linking CXX executable bin\KernelFunction_test.exe
   Creating library lib\KernelFunction_test.lib and object lib\KernelFunction_test.exp
[3691/3791] Linking CXX executable bin\extension_backend_test.exe
   Creating library lib\extension_backend_test.lib and object lib\extension_backend_test.exp
[3694/3791] Linking CXX executable bin\math_kernel_test.exe
   Creating library lib\math_kernel_test.lib and object lib\math_kernel_test.exp
[3695/3791] Linking CXX executable bin\pow_test.exe
   Creating library lib\pow_test.lib and object lib\pow_test.exp
[3697/3791] Linking CXX executable bin\tensor_iterator_test.exe
   Creating library lib\tensor_iterator_test.lib and object lib\tensor_iterator_test.exp
[3698/3791] Linking CXX executable bin\verify_api_visibility.exe
   Creating library lib\verify_api_visibility.lib and object lib\verify_api_visibility.exp
[3700/3791] Linking CXX executable bin\mobile_memory_cleanup.exe
   Creating library lib\mobile_memory_cleanup.lib and object lib\mobile_memory_cleanup.exp
[3701/3791] Linking CXX executable bin\kernel_function_test.exe
   Creating library lib\kernel_function_test.lib and object lib\kernel_function_test.exp
[3702/3791] Linking CXX executable bin\memory_overlapping_test.exe
   Creating library lib\memory_overlapping_test.lib and object lib\memory_overlapping_test.exp
[3703/3791] Linking CXX executable bin\kernel_lambda_legacy_test.exe
   Creating library lib\kernel_lambda_legacy_test.lib and object lib\kernel_lambda_legacy_test.exp
[3704/3791] Linking CXX executable bin\TensorImpl_test.exe
FAILED: bin/TensorImpl_test.exe
cmd.exe /C "cd . && "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin\cmake.exe" -E vs_link_exe --intdir=caffe2\CMakeFiles\TensorImpl_test.dir --rc=C:\PROGRA~2\WI3CF2~1\10\bin\100183~1.0\x86\rc.exe --mt=C:\PROGRA~2\WI3CF2~1\10\bin\100183~1.0\x86\mt.exe --manifests  -- C:\PROGRA~2\MICROS~2\2019\BUILDT~1\VC\Tools\MSVC\1428~1.293\bin\Hostx86\x86\link.exe /nologo caffe2\CMakeFiles\TensorImpl_test.dir\__\aten\src\ATen\core\TensorImpl_test.cpp.obj  /out:bin\TensorImpl_test.exe /implib:lib\TensorImpl_test.lib /pdb:bin\TensorImpl_test.pdb /version:0.0 /machine:X86 /ignore:4049 /ignore:4217 /ignore:4099 /INCREMENTAL:NO /subsystem:console  lib\gtest_main.lib  lib\torch.lib  lib\torch_cpu.lib  lib\libprotobuf.lib  lib\c10.lib  lib\gtest.lib  kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib && cd ."
LINK: command "C:\PROGRA~2\MICROS~2\2019\BUILDT~1\VC\Tools\MSVC\1428~1.293\bin\Hostx86\x86\link.exe /nologo caffe2\CMakeFiles\TensorImpl_test.dir\__\aten\src\ATen\core\TensorImpl_test.cpp.obj /out:bin\TensorImpl_test.exe /implib:lib\TensorImpl_test.lib /pdb:bin\TensorImpl_test.pdb /version:0.0 /machine:X86 /ignore:4049 /ignore:4217 /ignore:4099 /INCREMENTAL:NO /subsystem:console lib\gtest_main.lib lib\torch.lib lib\torch_cpu.lib lib\libprotobuf.lib lib\c10.lib lib\gtest.lib kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib /MANIFEST /MANIFESTFILE:bin\TensorImpl_test.exe.manifest" failed (exit code 1120) with the following output:
   Creating library lib\TensorImpl_test.lib and object lib\TensorImpl_test.exp
TensorImpl_test.cpp.obj : error LNK2019: unresolved external symbol "__declspec(dllimport) public: __thiscall caffe2::Tensor::Tensor(struct c10::Device)" (__imp_??0Tensor@caffe2@@QAE@UDevice@c10@@@Z) referenced in function "private: virtual void __thiscall TensorImplTest_Caffe2Constructor_Test::TestBody(void)" (?TestBody@TensorImplTest_Caffe2Constructor_Test@@EAEXXZ)
TensorImpl_test.cpp.obj : error LNK2019: unresolved external symbol "__declspec(dllimport) public: class c10::ArrayRef<__int64> __thiscall caffe2::Tensor::strides(void)const " (__imp_?strides@Tensor@caffe2@@QBE?AV?$ArrayRef@_J@c10@@XZ) referenced in function "private: virtual void __thiscall TensorImplTest_Caffe2Constructor_Test::TestBody(void)" (?TestBody@TensorImplTest_Caffe2Constructor_Test@@EAEXXZ)
TensorImpl_test.cpp.obj : error LNK2019: unresolved external symbol "__declspec(dllimport) public: __thiscall caffe2::Tensor::~Tensor(void)" (__imp_??1Tensor@caffe2@@QAE@XZ) referenced in function "private: virtual void __thiscall TensorImplTest_Caffe2Constructor_Test::TestBody(void)" (?TestBody@TensorImplTest_Caffe2Constructor_Test@@EAEXXZ)
bin\TensorImpl_test.exe : fatal error LNK1120: 3 unresolved externals
[3705/3791] Linking CXX executable bin\cpu_profiling_allocator_test.exe
   Creating library lib\cpu_profiling_allocator_test.lib and object lib\cpu_profiling_allocator_test.exp
[3707/3791] Linking CXX executable bin\cpu_generator_test.exe
   Creating library lib\cpu_generator_test.lib and object lib\cpu_generator_test.exp
[3709/3791] Building CXX object caffe2\torch\CMakeFiles\torch_python.dir\csrc\jit\python\script_init.cpp.obj
ninja: build stopped: subcommand failed.
(integration8) C:\Users\localaccount\Documents\Integration\new_repo\pytorch>
(integration8) C:\Users\localaccount\Documents\Integration\new_repo\pytorch>

```
