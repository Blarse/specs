Name: libetonyek
Version: 0.1.10
Release: alt2

Summary: A library for import of Apple Keynote presentations
License: MPL-2.0
Group: System/Libraries

# https://gerrit.libreoffice.org/#/admin/projects/libetonyek
Url: http://www.freedesktop.org/wiki/Software/libetonyek/
Source: %name-%version.tar.xz
Patch: libetonyek-0.1.9-ALT-C++11.patch

# Automatically added by buildreq on Mon Sep 21 2015
# optimized out: boost-devel-headers gnu-config libstdc++-devel pkg-config xz
BuildRequires: doxygen gcc-c++ libglm-devel librevenge-devel libxml2-devel mdds-devel zlib-devel
BuildRequires: liblangtag-devel mdds-devel
BuildRequires: cppunit-devel

%description
libetonyek is library providing ability to interpret and import Apple
Keynote presentations into various applications. Only version 5 is
supported at the moment, although versions 2-4 should work.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation of %name API
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform Apple Keynote presentations into other formats
Group: Development/C++

%description tools
Tools to transform Apple Keynote presentations into other formats.
Currently supported: XHTML, raw, text.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--disable-silent-rules \
	--disable-static \
	--disable-werror \
	--with-mdds=2.1
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

%install
%makeinstall_std
rm -f %buildroot/%_libdir/*.la
# we install API docs directly from build
rm -rf %buildroot/%_docdir/%name

%check
export LD_LIBRARY_PATH=%buildroot/%_libdir${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make check

%files
%doc AUTHORS COPYING FEATURES NEWS README
%_libdir/*.so.*

%files devel
%doc ChangeLog
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc COPYING
%doc docs/doxygen/html

%files tools
%_bindir/*

%changelog
* Mon Apr 15 2024 Michael Shigorin <mike@altlinux.org> 0.1.10-alt2
- E2K: drop the old kudge (reverts 0.1.6-alt4 change)
- Minor spec cleanup

* Fri Oct 13 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 0.1.10-alt1
- Updated to upstream 0.1.10
- Skipped patch 0001-glm-force-dmat3-initialization-needed-from-v0.9.9.0.patch
- Used mdds-2.1

* Thu Feb 03 2022 Andrey Cherepanov <cas@altlinux.org> 0.1.9-alt3
- FTBFS: fix build with mdds-2.0.

* Sat Jun 13 2020 Fr. Br. George <george@altlinux.ru> 0.1.9-alt2
- Fix build

* Tue Apr 28 2020 Andrey Cherepanov <cas@altlinux.org> 0.1.9-alt1.1
- Fix build with mdds-1.5.
- glm: force dmat3 initialization.

* Mon Feb 11 2019 Fr. Br. George <george@altlinux.ru> 0.1.9-alt1
- Autobuild version bump to 0.1.9

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 0.1.7-alt1
- Autobuild version bump to 0.1.7

* Fri Sep 08 2017 Michael Shigorin <mike@altlinux.org> 0.1.6-alt4
- E2K: work around FTBFS against boost 1.65 with lcc 1.21.20

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt3
- Fix build

* Mon Jul 25 2016 Fr. Br. George <george@altlinux.ru> 0.1.6-alt2
- Fix build

* Wed Apr 13 2016 Fr. Br. George <george@altlinux.ru> 0.1.6-alt1
- Autobuild version bump to 0.1.6

* Wed Sep 16 2015 Fr. Br. George <george@altlinux.ru> 0.1.3-alt1
- Autobuild version bump to 0.1.3

* Wed Jun 11 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- 0.1.1

* Tue May 13 2014 Fr. Br. George <george@altlinux.ru> 0.0.4-alt1
- Autobuild version bump to 0.0.4
- Drop patch

* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 0.0.3-alt1
- Initial build from FC

* Fri Dec 06 2013 David Tardon <dtardon@redhat.com> - 0.0.3-1
- new release

* Wed Dec 04 2013 David Tardon <dtardon@redhat.com> - 0.0.2-1
- new release

* Mon Nov 04 2013 David Tardon <dtardon@redhat.com> - 0.0.1-1
- new release

* Wed Oct 30 2013 David Tardon <dtardon@redhat.com> 0.0.0-1
- initial import
