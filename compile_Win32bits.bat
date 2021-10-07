
@echo off
setlocal enabledelayedexpansion

:: Changed - 32bits
:: for /f "usebackq tokens=*" %%i in (`"%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe" -version [15^,16^) -products * -latest -property installationPath`) do ( 
::)

:: This calls the 32bits MSVC environment -- the above lines dont work for me
:: I tried placing this before and after setting environment, doesnt make a differece
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" x86

set "CMAKE_INCLUDE_PATH=C:\Users\localaccount\Documents\Integration\MKL\include"
set "LIB=C:\Users\localaccount\Documents\Integration\MKL\lib;%LIB%"

set CMAKE=cmake
set CMAKE_GENERATOR=Ninja
set CMAKE_MAKE=Ninja
set DISTUTILS_USE_SDK=1
set USE_CUDA=0

:: I tried with and without these flags, doesnt make a difference
set BUILD_CAFFE2_OPS=OFF
set BUILD_CAFFE2=OFF
set INTERN_BUILD_ATEN_OPS=OFF
set USE_FBGEMM=0
set ATEN_AVX512_256=FALSE
set USE_KINETO=0
set ATEN_CPU_CAPABILITY=default
:: set ATEN_THREADING=OMP also gives AVX2 undeclared error

:: To clean up the compilation
python setup.py clean

:: Remove --cmake if you dont want cmake to run again
python setup.py install --cmake

