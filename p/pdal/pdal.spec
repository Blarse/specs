%define _unpackaged_files_terminate_build 1

Name:    pdal
Version: 2.5.6
Release: alt2

Summary: PDAL is Point Data Abstraction Library. GDAL for point cloud data.
License: BSD-3-Clause
Group:   Other
Url:     https://github.com/PDAL/PDAL

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: PDAL-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: bash-completion
BuildRequires: hdf-devel
BuildRequires: libcurl-devel
BuildRequires: libgdal-devel
BuildRequires: libgeotiff-devel
BuildRequires: libssl-devel
BuildRequires: libunwind-devel
BuildRequires: libxml2-devel
BuildRequires: libzstd-devel
BuildRequires: python3-devel

%description
%summary

%package -n lib%name
Summary: Library of %name
Group: System/Libraries

%description -n lib%name
%summary

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%{name}-devel
%summary

%prep
%setup -n PDAL-%version

%build
%cmake -GNinja -Wno-dev \
       -DPDAL_LIB_INSTALL_DIR=%_libdir
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files
%doc AUTHORS.txt LICENSE.txt README.md
%_bindir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/pdal-config
%_includedir/*
%_libdir/*.so
%_libdir/*.so
%_libdir/cmake/PDAL
%_libdir/pkgconfig/%name.pc

%changelog
* Sun Aug 20 2023 Andrey Cherepanov <cas@altlinux.org> 2.5.6-alt2
- Added libcurl-devel.

* Sat Aug 19 2023 Andrey Cherepanov <cas@altlinux.org> 2.5.6-alt1
- New version.

* Sun Jun 25 2023 Andrey Cherepanov <cas@altlinux.org> 2.5.5-alt1
- Initial build for Sisyphus.
