# Debuginfo packages are disabled to prevent rpmbuild from generating an empty
# debuginfo package for the empty main package.
%global debug_package %nil

Name: cereal
Version: 1.3.2
Release: alt1

Summary: A header-only C++11 serialization library
License: BSD
Group: Development/C++

Url: http://uscilab.github.io/cereal/
# Source-url:  https://github.com/USCiLab/cereal/archive/v%version.tar.gz#/%name-%version.tar.gz
Source: %name-%version.tar
# https://github.com/USCiLab/cereal/pull/736
Patch: d7b68df.patch

BuildRequires: gcc-c++
BuildRequires: boost-program_options-devel
BuildRequires: cmake >= 3.0
BuildRequires: ctest rpm-macros-cmake

%description
cereal is a header-only C++11 serialization library. cereal takes arbitrary
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast,
light-weight, and easy to extend - it has no external dependencies and can be
easily bundled with other code or used standalone.

%package devel
Summary: Development headers and libraries for %name
Group: Development/C++

%description devel
cereal is a header-only C++11 serialization library. cereal takes arbitrary
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast,
light-weight, and easy to extend - it has no external dependencies and can be
easily bundled with other code or used standalone.

This package contains development headers and libraries for the cereal library

%prep
%setup
#patch -p1
%ifarch %e2k
# works around an internal error in EDG frontend (mcst#6699)
sed -i "/String& decomposition = String.*;/{s/;/{};/;s/=/);Result(bool x):Result(x,/}" \
    unittests/doctest.h
%endif

%build
%cmake -DSKIP_PORTABILITY_TEST=ON -DWITH_WERROR=OFF
%cmake_build

%install
%cmake_install

%check
%make_build -C %_cmake__builddir test

%files devel
%doc README.md
%_includedir/%name
#_datadir/cmake/%name
%_libdir/cmake/%name/*

%changelog
* Sat Apr 20 2024 Ilya Mashkin <oddity@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Wed Apr 27 2022 Michael Shigorin <mike@altlinux.org> 1.3.0-alt1.1
- E2K: EDG ICE workaround by ilyakurdyukov@ (mcst#6699)

* Fri Apr 22 2022 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- new version (1.3.0) with rpmgs script
