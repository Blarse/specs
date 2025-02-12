%define _name girara
%define _soname 4
%define _unpackaged_files_terminate_build 1

# Tests disabled for now: they cause hasher-priv to freeze
%define _disable_check 1

%if %{expand:%%{!?_without_check:%%{!?_disable_check:1}}0}
%define tests enabled
%else
%define tests disabled
%endif

Name: lib%_name
Version: 0.4.4
Release: alt1

Summary: GTK-based minimalistic user interface library
License: Zlib
Group: System/Libraries
URL: https://pwmt.org/projects/girara
Vcs: https://github.com/pwmt/girara.git
Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): meson

BuildRequires: libgtk+3-devel >= 3.4 libpango-devel
BuildRequires: intltool
%{?!_without_check:%{?!_disable_check:BuildRequires: libcheck-devel xvfb-run}}

%description
girara is a library that implements a user interface that focuses on
simplicity and minimalism.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: libgtk+3-devel

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p1

%build
%meson \
	-Djson=disabled \
	-Dtests=%tests

%meson_build -v

%install
%meson_install
%find_lang %name-gtk3-%_soname

%check
%meson_test

%files -f %name-gtk3-%_soname.lang
%doc AUTHORS README.md LICENSE
%_libdir/*.so.%_soname
%_libdir/*.so.%_soname.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
* Mon May 13 2024 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt1
- Dropped libnotify dependence.
- Updated Vcs tag.
- Updated to 0.4.4.

* Sun Jan 14 2024 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1
- Disabled tests.
- Updated to 0.4.2.

* Wed Dec 13 2023 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- Enabled tests.
- Updated to 0.4.1.

* Wed Mar 22 2023 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- Updated to 0.4.0.

* Tue Jan 17 2023 Mikhail Efremov <sem@altlinux.org> 0.3.9-alt1
- Updated to 0.3.9.

* Tue Nov 29 2022 Mikhail Efremov <sem@altlinux.org> 0.3.8-alt1
- Updated to 0.3.8.

* Tue Feb 15 2022 Mikhail Efremov <sem@altlinux.org> 0.3.7-alt1
- Updated to 0.3.7.

* Thu Dec 16 2021 Mikhail Efremov <sem@altlinux.org> 0.3.6-alt2
- Fixed meson options.

* Thu Jul 15 2021 Mikhail Efremov <sem@altlinux.org> 0.3.6-alt1
- Updated to 0.3.6.

* Mon Aug 03 2020 Mikhail Efremov <sem@altlinux.org> 0.3.5-alt1
- Updated to 0.3.5.

* Thu Jan 09 2020 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt1
- Used Vcs tag.
- Fixed license.
- Updated to 0.3.4.

* Mon Sep 16 2019 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt1
- Updated to 0.3.3.

* Mon Dec 24 2018 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Updated to 0.3.2.

* Fri Sep 21 2018 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Fri May 25 2018 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Updated to 0.3.0.

* Wed Apr 18 2018 Mikhail Efremov <sem@altlinux.org> 0.2.9-alt1
- Updated to 0.2.9.

* Mon Jan 15 2018 Mikhail Efremov <sem@altlinux.org> 0.2.8-alt1
- Updated to 0.2.8.

* Tue Jan 24 2017 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1
- Updated to 0.2.7.

* Wed Apr 27 2016 Mikhail Efremov <sem@altlinux.org> 0.2.6-alt1
- Updated to 0.2.6.

* Mon Dec 21 2015 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1
- Updated to 0.2.5.

* Fri Apr 17 2015 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1
- Updated to 0.2.4.

* Fri Oct 17 2014 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- Updated to 0.2.3.

* Thu Jul 03 2014 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Enable libnotify support.
- Updated to 0.2.2.

* Fri Feb 21 2014 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Build with GTK+3.
- Updated to 0.2.0.

* Tue Nov 19 2013 Mikhail Efremov <sem@altlinux.org> 0.1.9-alt1
- Updated to 0.1.9.

* Thu Nov 14 2013 Mikhail Efremov <sem@altlinux.org> 0.1.8-alt1
- Updated to 0.1.8.

* Fri Aug 16 2013 Mikhail Efremov <sem@altlinux.org> 0.1.7-alt1
- Updated to 0.1.7.

* Mon May 13 2013 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1
- Package LICENSE.
- Updated to 0.1.6.

* Tue Feb 12 2013 Mikhail Efremov <sem@altlinux.org> 0.1.5-alt1
- Updated to 0.1.5.

* Wed Jan 09 2013 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1
- Updated to 0.1.4.

* Wed Jun 13 2012 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1
- Updated to 0.1.3.

* Thu Mar 29 2012 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Updated to 0.1.2.

* Thu Mar 15 2012 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Initial build.

