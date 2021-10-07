# Compiling Pytorch in Windows 32bits

## Requirements

- Install Visual Studio 16.8.5 Build Tools (as advised here https://github.com/pytorch/pytorch#install-pytorch)

   - Link to download older VS versions: https://docs.microsoft.com/en-us/visualstudio/releases/2019/history#release-dates-and-build-numbers
   - Just double-click on the donwloaded installer, default options are fine but make sure to install the C++ cmake tools (select C++ tools)

- Install Anaconda for Windows (downloaded from website)

- Install Git (via conda, see below)

- Install MKL, run this in Powershell:  
curl https://s3.amazonaws.com/ossci-windows/mkl_2020.2.254.7z --output mkl_2020.2.254.7z   
Then install 7-zip and uncompress files. Then in compile_Win32bits.bat (see below) set these to point to the location of that:
```
set "CMAKE_INCLUDE_PATH=C:\Users\localaccount\Documents\Integration\MKL\include"
set "LIB=C:\Users\localaccount\Documents\Integration\MKL\lib;%LIB%"
```

## Setup environment

Create a conda environment Python 3.8 using the Anaconda Navigator interface, I called this environment integration8

Open an Anaconda prompt (search/open from Windows Start menu) and:
```
conda activate integration8
conda install ninja
conda install pyyaml
conda install -c anaconda git
conda install -c conda-forge libuv=1.39
pip install typing_extensions
pip install numpy mkl intel-openmp mkl_fft
```

and clone pytorch:
```
cd Documents/Integration/
git clone --recursive https://github.com/cassiavb/pytorch.git
cd pytorch
```

## Compile

Following the instructions from here:  
https://github.com/pytorch/pytorch/issues/38322  
https://github.com/pytorch/pytorch#install-pytorch  

I created a .bat script to compile Pytorch in Windows 32bits.

In that Anaconda (integration) environment run that batch script:  
```
./compile_Win32bits.bat
```

Note: to clear up any cmake issues or weird behaviours in compilation delete the file build/CMakeCache.txt that is created after cmake is run.

## Compilation errors

I get the following errors when running that script:
```
[2778/3791] Building CXX object caffe2\CMakeFiles\torch_cpu.dir\__\aten\src\ATen\native\DispatchStub.cpp.obj
FAILED: caffe2/CMakeFiles/torch_cpu.dir/__/aten/src/ATen/native/DispatchStub.cpp.obj
C:\PROGRA~2\MICROS~2\2019\BUILDT~1\VC\Tools\MSVC\1428~1.293\bin\Hostx86\x86\cl.exe  /nologo /TP -DADD_BREAKPAD_SIGNAL_HANDLER -DCPUINFO_SUPPORTED_PLATFORM=1 -DFMT_HEADER_ONLY=1 -DMINIZ_DISABLE_ZIP_READER_CRC32_CHECKS -DONNXIFI_ENABLE_EXT=1 -DONNX_ML=1 -DONNX_NAMESPACE=onnx_torch -DUSE_DISTRIBUTED -DUSE_EXTERNAL_MZCRC -DWIN32_LEAN_AND_MEAN -D_CRT_SECURE_NO_DEPRECATE=1 -Dtorch_cpu_EXPORTS -Iaten\src -I..\aten\src -I. -I..\ -I..\cmake\..\third_party\benchmark\include -I..\third_party\onnx -Ithird_party\onnx -I..\third_party\foxi -Ithird_party\foxi -I..\torch\csrc\api -I..\torch\csrc\api\include -I..\caffe2\aten\src\TH -Icaffe2\aten\src\TH -Icaffe2\aten\src -I..\caffe2\..\third_party -I..\caffe2\..\third_party\breakpad\src -Icaffe2\..\aten\src -Icaffe2\..\aten\src\ATen -I..\torch\csrc -I..\third_party\miniz-2.0.8 -I..\torch\csrc\distributed -I..\aten\src\TH -I..\aten\..\third_party\catch\single_include -I..\aten\src\ATen\.. -Icaffe2\aten\src\ATen -I..\c10\.. -I..\third_party\pthreadpool\include -I..\third_party\cpuinfo\include -I..\third_party\FP16\include -I..\third_party\fmt\include -I..\cmake\..\third_party\googletest\googlemock\include -I..\cmake\..\third_party\googletest\googletest\include -I..\third_party\protobuf\src -I..\third_party\XNNPACK\include -I..\cmake\..\third_party\eigen -IC:\Users\localaccount\anaconda3\envs\integration8\include -IC:\Users\localaccount\anaconda3\envs\integration8\lib\site-packages\numpy\core\include -I..\cmake\..\third_party\pybind11\include -I..\caffe2 /DWIN32 /D_WINDOWS /GR /EHsc /w /bigobj -DUSE_PTHREADPOOL -openmp:experimental -IC:/Users/localaccount/Documents/Integration/MKL/include -DNDEBUG -DUSE_XNNPACK -DSYMBOLICATE_MOBILE_DEBUG_HANDLE -DEDGE_PROFILER_USE_KINETO -DHAVE_AVX512_CPU_DEFINITION /MD /O2 /Ob2 /DNDEBUG /w /bigobj -DNDEBUG -DUSE_GCC_GET_CPUID -DUSE_AVX -DTH_HAVE_THREAD /EHsc /DNOMINMAX /wd4267 /wd4251 /wd4522 /wd4838 /wd4305 /wd4244 /wd4190 /wd4101 /wd4996 /wd4275 /bigobj -O2 -openmp:experimental -IC:/Users/localaccount/Documents/Integration/MKL/include -DCAFFE2_BUILD_MAIN_LIB -DONNX_BUILD_MAIN_LIB -std:c++14 /showIncludes /Focaffe2\CMakeFiles\torch_cpu.dir\__\aten\src\ATen\native\DispatchStub.cpp.obj /Fdcaffe2\CMakeFiles\torch_cpu.dir\ /FS -c ..\aten\src\ATen\native\DispatchStub.cpp
..\aten\src\ATen\native\DispatchStub.cpp(126): error C2065: 'AVX2': undeclared identifier
..\aten\src\ATen\native\DispatchStub.cpp(127): error C2065: 'AVX2': undeclared identifier
[2783/3791] Building CXX object caffe2\CMakeFiles\torch_cpu.dir\__\aten\src\ATen\native\DilatedMaxPool3d.cpp.obj
ninja: build stopped: subcommand failed.
```

These lines (125,126) run because pytorch 'found' AVX512 but did not find AVX2. 

The AVX's tests happen in pytorch\cmake\Modules\FindAVX.cmake  

Even though the machine I use has AVX2 it does not pass the AVX2 test because of the intrinsic:  
\_mm256_extract_epi64  
that is used for testing AVX2 (that intrinsic requires 64bits).   
This was added to the test to force the detection to fail in 32bits systems (otherwise other issues happen later on).

This explains the issue:  
https://github.com/pytorch/pytorch/issues/17901  
that was mentioned more recently here:  
https://github.com/pytorch/pytorch/issues/40988  

According to this: https://github.com/pytorch/pytorch/issues/35678  
"Stuff that goes through DispatchStub.cpp can be controlled by runtime by ATEN_CPU_CAPABILITY environment variable.  For example, set ATEN_CPU_CAPABILITY=default to avoid the AVX and AVX2 code paths."
but setting ATEN_CPU_CAPABILITY=default or to AVX it still gives me the 'AVX2': undeclared identifier error in DispatchStub.cpp 

I modified DispatchStub.cpp lines 125,126 declaring AVX2 as void (or to not use AVX2 flag when AVX512 exists) but in either case I get the following link error later on:  

```
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
```

The same link error happens if I try to 'trick' it to not passing the AVX512 test by modifying FindAVX.

Full logs here:  
- AVX2 undeclared errors [log_AVX2error.md](log_AVX2error.md)  
- link errors (when 'bypassing' AVX2 error) [log_LINKerror.md](log_LINKerror.md))  

I noticed the following warnings in log_LINKerror before the link errors:
```
LINK : the 32-bit linker ran out of heap space and is going to restart linking with a 64-bit linker
```

I checked for updates to the VS BuildTools (I read somewhere that the issue was fixed in recent versions) and after updating it I dont get this anymore, but the same link errors are still there:  
[log_LINKerror_update.md](log_LINKerror_update.md))  

The issue I created in pytorch repo (https://github.com/pytorch/pytorch/issues/65615) was closed with the following comment:

"As documented in https://pytorch.org/docs/stable/notes/windows.html , PyTorch does not support 32 bit runtimes anymore. Although we would a non-invasive patch that fixes
the compilation problem."

## Using a 32bits conda environment

```
(base) C:\Users\localaccount>set CONDA_FORCE_32BIT=1
(base) C:\Users\localaccount>conda create -n integration32_8 python=3.8
(base) C:\Users\localaccount>conda activate integration32_8

(integration32_8) conda install ninja
(integration32_8) conda install pyyaml
(integration32_8) conda install -c anaconda git
(integration32_8) conda install -c conda-forge libuv=1.39
(integration32_8) pip install typing_extensions
(integration32_8) pip install numpy mkl intel-openmp mkl_fft

(integration32_8) C:\Users\localaccount\Documents\Integration\new_repo\pytorch>compile_Win32bits.bat
**********************************************************************
** Visual Studio 2019 Developer Command Prompt v16.11.4
** Copyright (c) 2021 Microsoft Corporation
**********************************************************************
[vcvarsall.bat] Environment initialized for: 'x86'
32-bit Windows Python runtime is not supported. Please switch to 64-bit Python.
32-bit Windows Python runtime is not supported. Please switch to 64-bit Python.
(integration32_8) C:\Users\localaccount\Documents\Integration\new_repo\pytorch>
```