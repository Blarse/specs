%define llvm_ver 16.0
%define soname 1

# LTO causes segfaults (
%define optflags_lto %nil

Name: rocr-runtime
Version: 5.5.1
Release: alt0.2
License: MIT
Summary: HSA Runtime API and runtime for ROCm
Url: https://github.com/RadeonOpenCompute/ROCR-Runtime
Group: System/Libraries

Source: %name-%version.tar
Patch0: rocr-image-bitcode-path.patch
# https://bugs.gentoo.org/716948
Patch1: rocr-runtime-4.3.0_no-aqlprofiler.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ libelf-devel libdrm-devel hsakmt-rocm-devel rocm-device-libs xxd
BuildRequires: clang%{llvm_ver}-devel llvm%{llvm_ver}-devel mlir%{llvm_ver}-tools lld%{llvm_ver}

# exclude armh
# doesn't compile on ix86
ExclusiveArch: x86_64 aarch64 ppc64le

%description
AMD's implementation of the core HSA Runtime API's.

%package -n libhsa-runtime%{soname}
Summary: HSA Runtime API and runtime for ROCm
Provides: libhsa-runtime64 = %EVR, hsa-rocr = %EVR
Group: System/Libraries

%description -n libhsa-runtime%{soname}
AMD's implementation of the core HSA Runtime API's.

%package -n hsa-rocr-devel
Summary: HSA Runtime API and runtime for ROCm development
Group: Development/C++

%description -n hsa-rocr-devel
HSA Runtime API and runtime for ROCm development headers and library.

%prep
%setup
%patch0 -p1
%patch1 -p0

%build
export ALTWRAP_LLVM_VERSION=%{llvm_ver}
pushd src
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS=ON \
	-DINCLUDE_PATH_COMPATIBILITY=OFF \
	-DCMAKE_INSTALL_LIBDIR=%_lib
%cmake_build

%install
pushd src
%cmake_install

%files -n libhsa-runtime%{soname}
%doc src/LICENSE.md src/README.md
%_libdir/libhsa-runtime64.so.%{soname}*

%files -n hsa-rocr-devel
%_includedir/hsa
%_libdir/libhsa-runtime64.so
%_libdir/cmake/hsa-runtime64

%changelog
* Thu Jun 15 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.2
- Disable 32-bit completely.

* Sun May 28 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.1
- rocm-5.5.1.
- llvm15->llvm16.

* Wed Jan 04 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.2
- Restrict build to 64-bit.

* Mon Jan 02 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.1
- First build for ALTLinux.
