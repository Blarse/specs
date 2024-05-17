%define git %nil
%define rname dxcompiler

%ifarch %ix86
%define optflags_lto %nil
%endif

Name: DirectXShaderCompiler
Version: 1.8.2403
Release: alt0.3
Summary: DirectX Shader Compiler
Group: Development/C++
License: Apache-2.0 with LLVM-exception

URL: https://github.com/microsoft/DirectXShaderCompiler
Packager: L.A. Kostis <lakostis@altlinux.org>

Source0: %name-%version.tar
# see https://github.com/microsoft/DirectXShaderCompiler/issues/5079#issuecomment-1480210642
Source1: DirectX-Headers.tar
Patch0: alt-spirv-tools-shared.patch
Patch2000: alt-e2k.patch
Patch3500: alt-loongarch64.patch

ExclusiveArch: %ix86 x86_64 aarch64 %e2k loongarch64

Provides: lib%{rname}-devel = %EVR, lib%{rname} = %EVR
# upstream commit 6d3574a34b7180d75df3a893fe12447c6231a450 removed sonames
Obsoletes: lib%{rname}3

BuildRequires(pre): cmake
BuildRequires: gcc-c++ ninja-build spirv-headers libspirv-tools-devel python3-devel git-core
BuildRequires: directx-headers

%description
The DirectX Shader Compiler project includes a compiler and related tools used
to compile High-Level Shader Language (HLSL) programs into DirectX Intermediate
Language (DXIL) representation. Applications that make use of DirectX for
graphics, games, and computation can use it to generate shader programs.

%prep
%setup -n %name-%version -a1
%patch0 -p1

%ifarch %e2k
%patch2000 -p1
%endif
%patch3500 -p1
cp -aLt autoconf -- /usr/share/automake/config.{guess,sub}

%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_C_COMPILER=gcc \
  -DCMAKE_CXX_COMPILER=c++ \
  -DSPIRV-Headers_SOURCE_DIR=%_prefix \
  -DSPIRV_BUILD_TESTS=OFF \
  -C ./cmake/caches/PredefinedParams.cmake
%cmake_build

%install
mkdir -p %buildroot{%_libdir,%_bindir}
cp -ar %_cmake__builddir/lib/lib%{rname}.so* %buildroot%_libdir/
cp -ar %_cmake__builddir/bin/dxc* %buildroot%_bindir/

%files
%_bindir/*
%_libdir/lib%{rname}.so

%changelog
* Fri May 17 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.8.2403-alt0.3
- Fixed build for Elbrus

* Mon May 06 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.8.2403-alt0.2
- NMU: build for LoongArch.

* Thu Mar 14 2024 L.A. Kostis <lakostis@altlinux.ru> 1.8.2403-alt0.1
- Updated to v1.8.2403.

* Wed Feb 07 2024 L.A. Kostis <lakostis@altlinux.ru> 1.7.2308-alt0.1
- Updated to v1.7.2308.

* Fri Jun 30 2023 L.A. Kostis <lakostis@altlinux.ru> 1.7.2212.1-alt0.4
- Added a fix to compile with gcc-13.

* Sun Mar 26 2023 Michael Shigorin <mike@altlinux.org> 1.7.2212.1-alt0.3
- E2K: update/adjust build scripts.

* Tue Mar 21 2023 L.A. Kostis <lakostis@altlinux.ru> 1.7.2212.1-alt0.2
- Use special rev of dx headers to compile.
- Don't pack library separately due upstream changes and soname removal.

* Mon Mar 20 2023 L.A. Kostis <lakostis@altlinux.ru> 1.7.2212.1-alt0.1
- Updated to v1.7.2212.1.
- BR: add directx-headers.

* Thu Jan 26 2023 L.A. Kostis <lakostis@altlinux.ru> 1.7.2207-alt0.4.geaf2d73
- Set cmake release target.

* Thu Jan 26 2023 L.A. Kostis <lakostis@altlinux.ru> 1.7.2207-alt0.3.geaf2d73
- Updated to 1.7.2207 GIT eaf2d736d5d1b2a262964fd23f9e407d944ab543.

* Wed Nov 23 2022 L.A. Kostis <lakostis@altlinux.ru> 1.7.2207-alt0.2.ge3f3223
- Disable LTO on ix86.

* Mon Oct 17 2022 L.A. Kostis <lakostis@altlinux.ru> 1.7.2207-alt0.1.ge3f3223
- Updated to 1.7.2207 GIT e3f322389dadc5d5370bc8e17d3494a7909b6238.

* Sat Oct 15 2022 L.A. Kostis <lakostis@altlinux.ru> 1.6.2112-alt0.1.g6f204c7
- initial build for ALTLinux.
- Compile only library and dxc tool (as required by AMDVLK driver).
