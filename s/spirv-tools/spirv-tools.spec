%define sover 0
%define git %nil
%define build_type RelWithDebInfo
%define _cmake %cmake -GNinja -DCMAKE_BUILD_TYPE:STRING="%build_type" -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON

Name: spirv-tools
Version: 2021.1
Release: alt1
Epoch: 1

Summary: API and commands for processing SPIR-V modules
Group: Development/C++
License: Apache-2.0

Url: https://www.khronos.org/registry/spir-v/
Packager: L.A. Kostis <lakostis@altlinux.org>

Source: https://github.com/KhronosGroup/SPIRV-Tools/archive/v%version/SPIRV-Tools-%version.tar.gz
Patch0: %name-soname-alt.patch
Patch1: %name-alt-cmake-path.patch

BuildRequires(pre): cmake ninja-build
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: spirv-headers >= 1.5.4-alt1.gbcf5521

%description
The package includes an assembler, binary module parser,
disassembler, and validator for SPIR-V.

%package -n lib%name%sover
Summary: SPIR-V tool component library
Group: System/Libraries

%description -n lib%name%sover
The SPIR-V Tool library contains all of the implementation details
driving the SPIR-V assembler, binary module parser, disassembler and
validator, and is used in the standalone tools whilst also enabling
integration into other code bases directly.

%package -n lib%name-devel
Summary: Development headers for the SPIR-V tool library
Group: Development/C++
Requires: lib%name%sover = %EVR

%description -n lib%name-devel
The SPIR-V Tool library contains all of the implementation details
driving the SPIR-V assembler, binary module parser, disassembler and
validator, and is used in the standalone tools whilst also enabling
integration into other code bases directly.

%prep
%setup -n SPIRV-Tools-%version
%patch0 -p2
%patch1 -p2

# will check protobuf support later
# for fuzzler
%build
%_cmake \
  -DSPIRV_BUILD_COMPRESSION=OFF \
  -DSPIRV_BUILD_FUZZER=OFF \
  -DSPIRV_TOOLS_BUILD_STATIC=OFF \
  -DSPIRV-Headers_SOURCE_DIR=%_prefix \
%ifarch %e2k
  -DSPIRV_WERROR=OFF \
%endif
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DBUILD_SHARED_LIBS=ON

ninja \
  -vvv \
  -j %__nprocs \
  -C %_cmake__builddir

%install
pushd %_cmake__builddir
cmake -DCMAKE_INSTALL_PREFIX=%buildroot%prefix -DSHARE_INSTALL_PREFIX=%buildroot%_datadir ../
popd
ninja -C %_cmake__builddir install

%files
%doc CHANGES LICENSE README.md
%_bindir/spirv-*

%files -n lib%name%sover
%_libdir/libSPIRV-Tools.so.*
%_libdir/libSPIRV-Tools-*.so.*

%files -n lib%name-devel
%_libdir/libSPIRV-Tools.so
%_libdir/libSPIRV-Tools-*.so
%_pkgconfigdir/SPIRV-Tools.pc
%_pkgconfigdir/SPIRV-Tools-shared.pc
%_includedir/%name
%_datadir/cmake/SPIRV-Tools*

%changelog
* Mon Jun 14 2021 L.A. Kostis <lakostis@altlinux.ru> 1:2021.1-alt1
- Updated to v2021.1.
- .spec: update cmake macros.

* Mon Feb 15 2021 L.A. Kostis <lakostis@altlinux.ru> 1:2020.6-alt1
- Updated to v2020.6.
- Update -alt patches.
- Disable static build explicitly.
- Simplify build flags.

* Sun Feb 14 2021 Nazarov Denis <nenderus@altlinux.org> 1:2020.4-alt2
- Rollback to 2020.4-alt1 (ALT #39672)

* Fri Feb 05 2021 Nazarov Denis <nenderus@altlinux.org> 2020.6-alt1
- Updated to v2020.6.

* Tue Sep 08 2020 L.A. Kostis <lakostis@altlinux.ru> 2020.4-alt1
- Updated to v2020.4.

* Thu Jun 04 2020 L.A. Kostis <lakostis@altlinux.ru> 2020.3-alt1
- Updated to v2020.3.
- Added cmake files.
- Change packager.

* Sat Apr 11 2020 Michael Shigorin <mike@altlinux.org> 2019.4-alt2
- E2K: disable -Werror (hex_float.h:766 triggers ftbfs with -Werror=conversion)

* Thu Aug 29 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.4-alt1
- Updated to 2019.4.
- Update all -alt patches.

* Thu May 02 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.3-alt2.g26c1b88
- fix debuginfo build (disable compression).
- use ninja build.

* Thu May 02 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.3-alt1.g26c1b88
- Updated to v2019.3-dev g26c1b88.
- Build with python3.
- Enable compression support.
- Update -soname patch.

* Fri Mar 09 2018 Nazarov Denis <nenderus@altlinux.org> 2018.2-alt1%%ubt
- Version 2018.2

* Tue Apr 18 2017 Nazarov Denis <nenderus@altlinux.org> 2016.6-alt0.M80P.1
- Build for branch p8

* Sat Apr 15 2017 Nazarov Denis <nenderus@altlinux.org> 2016.6-alt1
- Initial build for ALT Linux
