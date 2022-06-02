%define _unpackaged_files_terminate_build 1
%def_with gtk3

Name: 	 solvespace
Version: 3.1
Release: alt1
Epoch:   1

Summary: SolveSpace parametric 2d/3d CAD
License: GPLv3
Group: 	 Graphics
Url: 	 http://solvespace.com/
#VCS:    https://github.com/solvespace/solvespace

Packager: Andrey Cherepanov <cas@altlinux.org>
Source0:  %name-%version.tar
Source1:  libdxfrw.tar
Source2:  mimalloc.tar
Patch1:   use-explicit-git-hash.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: fontconfig-devel
BuildRequires: eigen3
BuildRequires: libGL-devel
BuildRequires: libGLEW-devel
BuildRequires: libGLU-devel
%if_with gtk3
BuildRequires: libgtkmm3-devel
%else
BuildRequires: libgtkmm2-devel
%endif
BuildRequires: libpangomm-devel
BuildRequires: libjson-c-devel
BuildRequires: libpng-devel
BuildRequires: libharfbuzz-devel
BuildRequires: libdrm-devel
BuildRequires: libpcre-devel
BuildRequires: libpixman-devel
BuildRequires: libexpat-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXdamage-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libspnav-devel
BuildRequires: zlib-devel

%description
SolveSpace is a parametric 2d/3d CAD program. Applications include:
* modeling 3d parts - draw with extrudes, revolves, and Boolean
  (union / difference) operations;
* modeling 2d parts - draw the part as a single section, and export DXF,
  PDF, SVG; use 3d assembly to verify fit;
* 3d-printed parts - export the STL or other triangle mesh expected by
  most 3d printers;
* preparing CAM data - export 2d vector art for a waterjet machine or
  laser cutter; or generate STEP or STL, for import into third-party
  CAM software for machining;
* mechanism design - use the constraint solver to simulate planar or
  spatial linkages, with pin, ball, or slide joints;
* plane and solid geometry - replace hand-solved trigonometry and
  spreadsheets with a live dimensioned drawing.

%package -n libslvs
Summary: SolveSpace geometric kernel
Group: System/Libraries

%description -n libslvs
SolveSpace is a parametric 2d/3d CAD. libslvs contains the geometric
kernel of SolveSpace, built as a library.

%package -n libslvs-devel
Summary: SolveSpace geometric kernel (development files)
Group: Development/C
Requires: libslvs

%description -n libslvs-devel
SolveSpace is a parametric 2d/3d CAD. libslvs contains the geometric
kernel of SolveSpace, built as a library.

This package includes development files for libslvs.

%prep
%setup -q
tar xf %SOURCE1
tar xf %SOURCE2
%patch1 -p1

%build
%cmake \
    -GNinja \
    -Wno-dev \
    -DCMAKE_BUILD_TYPE=Release
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
%find_lang %name

%files -f %name.lang
%doc COPYING.txt README.md wishlist.txt
%_bindir/%name
%_bindir/%name-cli
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/*/apps/%name.svg
%_iconsdir/hicolor/*/mimetypes/application-x-solvespace.png
%_iconsdir/hicolor/scalable/mimetypes/application-x-solvespace.svg
%_desktopdir/%name.desktop
%_datadir/%name
%_datadir/mime/packages/solvespace-slvs.xml
%_datadir/metainfo/*.metainfo.xml

%files -n libslvs
%_libdir/libslvs.so.*

%files -n libslvs-devel
%_libdir/libslvs.so
%_includedir/slvs.h

%changelog
* Thu Jun 02 2022 Andrey Cherepanov <cas@altlinux.org> 1:3.1-alt1
- New version.

* Sun Apr 18 2021 Andrey Cherepanov <cas@altlinux.org> 1:3.0-alt1
- New version.
- Build with GTK 3.

* Fri Apr 07 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.3-alt1.qa1
- Fixed build with glibc >= 2.25.

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1:2.3-alt1
- New version

* Wed Oct 05 2016 Andrey Cherepanov <cas@altlinux.org> 1:2.1-alt2
- Use explicit commit hash

* Tue Jul 12 2016 Andrey Cherepanov <cas@altlinux.org> 1:2.1-alt1
- New version

* Tue Feb 16 2016 Andrey Cherepanov <cas@altlinux.org> 20160214-alt1
- Inital build in Sisyphus

