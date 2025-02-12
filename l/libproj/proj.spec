%def_disable static

Name: libproj
Version: 9.4.0
Release: alt1

Summary: PROJ.4 - cartographic projections library
Group: Sciences/Geosciences
License: MIT
Url: https://proj4.org/
Source: proj-%version.tar.gz

BuildPreReq: rpm-macros-cmake
BuildRequires: cmake libgtest-devel libtiff-devel libcurl-devel
BuildRequires: gcc-c++ libstdc++-devel libsqlite3-devel sqlite3

%description
This package contains the PROJ.4 cartographic projections library.

%package -n proj
Summary: PROJ.4 programs
Group: Sciences/Geosciences
Requires: %name = %version-%release
%description -n proj
This package contains PROJ.4 programs.

%package devel
Summary: PROJ.4 development files
Group: Sciences/Geosciences
Requires: %name = %version-%release
Requires: libcurl-devel
Obsoletes: proj-devel
Provides:  proj-devel
%description devel
This package contains PROJ.4 development files.

%if_enabled static
%package devel-static
Group: Sciences/Geosciences
Summary: PROJ.4 static library
Requires: %name-devel = %version-%release
%description devel-static
This package contains PROJ.4 static library.
%endif #enabled static

%package nad
Summary: Empty package. US and Canadian datum shift grids moved to libproj
Group: Sciences/Geosciences
BuildArch: noarch
%description nad
Empty package. US and Canadian datum shift grids moved to libproj

%prep
%setup

%build
%cmake_insource -DUSE_EXTERNAL_GTEST=TRUE
%cmake_build

%install
%cmake_install

%files
%doc NEWS AUTHORS COPYING README ChangeLog
%_libdir/*.so.*
%_datadir/proj/*
%dir %_datadir/proj

%files -n proj
%doc NEWS AUTHORS COPYING
%_bindir/*
%_mandir/man1/*.1*

%files devel
%_includedir/*.h
%_includedir/proj/*.hpp
%dir %_includedir/proj
%_libdir/*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/proj/*.cmake
%dir %_libdir/cmake/proj
%_libdir/cmake/proj4/*.cmake
%dir %_libdir/cmake/proj4

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files nad

%changelog
* Tue Apr 30 2024 Vladislav Zavjalov <slazav@altlinux.org> 9.4.0-alt1
- 9.4.0

* Mon Dec 18 2023 Vladislav Zavjalov <slazav@altlinux.org> 9.3.1-alt1
- 9.3.1

* Mon Sep 25 2023 Vladislav Zavjalov <slazav@altlinux.org> 9.3.0-alt1
- 9.3.0

* Sat Jul 15 2023 Vladislav Zavjalov <slazav@altlinux.org> 9.2.1-alt1
- 9.2.1

* Thu Nov 03 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 9.1.0-alt1.1
- fixed build for Elbrus

* Wed Oct 19 2022 Vladislav Zavjalov <slazav@altlinux.org> 9.1.0-alt1
- 9.1.0

* Mon Sep 20 2021 Vladislav Zavjalov <slazav@altlinux.org> 6.3.1-alt2
- fix build with LTO by disabling static library

* Thu Mar 19 2020 Vladislav Zavjalov <slazav@altlinux.org> 6.3.1-alt1
- 6.3.1

* Thu Oct 03 2019 Vladislav Zavjalov <slazav@altlinux.org> 6.2.0-alt1
- move all datafiles from libproj-nad subpackage to libproj
- 6.2.0

* Fri Feb 15 2019 Vladislav Zavjalov <slazav@altlinux.org> 5.2.0-alt1
- 5.2.0

* Wed Apr 18 2012 Vladislav Zavjalov <slazav@altlinux.org> 4.8.0-alt1
- 4.8.0

* Tue Dec 20 2011 Vladislav Zavjalov <slazav@altlinux.org> 4.7.0-alt6
- spec: do autoreconf to avoid RPATH with standard paths

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7.0-alt5.1
- Rebuilt for debuginfo

* Thu Oct 21 2010 Vladislav Zavjalov <slazav@altlinux.org> 4.7.0-alt5
- rebuild for soname set-versions

* Mon May 24 2010 Vladislav Zavjalov <slazav@altlinux.org> 4.7.0-alt4
- spec: libproj-{devel,nad} provides proj-{devel,nad} (closes #23527)

* Sat May 22 2010 Vladislav Zavjalov <slazav@altlinux.org> 4.7.0-alt3
- cleanup spec: fix some repocop warnings, closes #11468
  * move libraries into libproj-* subpackages
  * move static library to devel-static subpackage
  * make libproj-nad package to be noarch
  * replace make -> make_build in the build section
  * remove BuildRequires: libqt4-core
  * change Group to Sciences/Geosciences

* Wed Apr 07 2010 Vladislav Zavjalov <slazav@altlinux.org> 4.7.0-alt2
- merge with git.alt:/srpms/p/proj.git to include repocop changes

* Tue Apr 06 2010 Vladislav Zavjalov <slazav@altlinux.org> 4.7.0-alt1
- new version
- cleanup spec (rider@)
- reset LC_NUMERIC in pj_init() (bga@)

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 4.5.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for proj
  * postun_ldconfig for proj
  * postclean-05-filetriggers for spec file

* Wed Jan 17 2007 Dmitri Kuzishchin <dim@altlinux.ru> 4.5.0-alt1
- Initial package.
