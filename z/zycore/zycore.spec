%define sover 1.5

Name: zycore
Version: 1.5.0
Release: alt1

Summary: Zyan Core Library for C
License: MIT
Group: System/Libraries

Url: https://github.com/zyantific/%name-c
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/zyantific/zycore-c/archive/refs/tags/v%version/%name-c-%version.tar.gz
Source: %name-c-%version.tar

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: graphviz

%description
Internal library providing platform independent types, macros and a fallback for environments without LibC.

%package -n lib%name%sover
Summary: Zyan Core Library for C
Group: System/Libraries

%description -n lib%name%sover
Internal library providing platform independent types, macros and a fallback for environments without LibC.

%package -n lib%name-devel
Summary: Header files for lib%name
Group: Development/C

%description -n lib%name-devel
Header files for lib%name

%prep
%setup -n %name-c-%version

%build
%cmake -DZYCORE_BUILD_SHARED_LIB:BOOL=TRUE
%cmake_build

%install
%cmake_install

%files -n lib%name%sover
%doc LICENSE README.md
%_libdir/libZycore.so.*

%files -n lib%name-devel
%_libdir/cmake/%name
%_libdir/libZycore.so
%_includedir/Zycore
%_defaultdocdir/Zycore
%_man3dir/*

%changelog
* Tue Feb 13 2024 Nazarov Denis <nenderus@altlinux.org> 1.5.0-alt1
- New version 1.5.0.

* Mon Oct 30 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.4.1-alt2
- NMU: fixed FTBFS on LoongArch

* Mon May 29 2023 Nazarov Denis <nenderus@altlinux.org> 1.4.1-alt1
- Initial build for ALT Linux
