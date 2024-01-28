%define ver_major 6.0
%define _libexecdir %_prefix/libexec

Name: cinnamon-screensaver
Version: %ver_major.3
Release: alt1

Summary: Cinnamon Screensaver
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/cinnamon-screensaver

Provides: screen-saver-engine
Provides: screen-saver-frontend
Provides: cinnamon-screensaver-module

# Source-url: https://github.com/linuxmint/cinnamon-screensaver/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Source1: %name.pam
Patch: %name-%version-%release.patch

BuildPreReq: meson
BuildRequires: python3-dev
BuildRequires: libgio-devel
BuildRequires: libgtk+3-devel
BuildRequires: libgtk+3-gir-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libpam0-devel
BuildRequires: libXinerama-devel
BuildRequires: xdotool-devel
BuildRequires: libXrandr-devel
Requires: %name-translations
Requires: typelib(CDesktopEnums)

%add_python3_self_prov_path %buildroot%_datadir/%name

%description
cinnamon-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the Cinnamon desktop.

%package -n lib%name
Summary: Shared libraries needed to run %name
Group: System/Libraries

%description -n lib%name
This package contains shared libraries needed to run %name and its
components.

%package -n lib%name-devel
Summary: Libraries and include files for developing %name components
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides the necessary development libraries and include
files to allow you to develop %name components.

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release
Requires: libxapps-gir

%description -n lib%name-gir
GObject introspection data for the %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS=-DUSE_SETRES
%meson
%meson_build

%install
%meson_install

rm -f %buildroot/%_sysconfdir/pam.d/%name
install -pm640 %SOURCE1 %buildroot/%_sysconfdir/pam.d/%name

%filter_from_requires /python3[(]dbusdepot[)]/d
%filter_from_requires /python3[(]util[)]/d
%filter_from_requires /python3[(]widgets[)]/d
%filter_from_requires /python3[(]pamhelper[)]/d
%filter_from_requires /python3[(]pamhelper[)]/d
%filter_from_requires /python3[(]gi.repository.CDesktopEnums[)]/d

%files
%_bindir/%name
%_bindir/cinnamon-unlock-desktop
%attr(2711,root,chkpwd) %_libexecdir/%name-pam-helper
%attr(640,root,chkpwd) %config(noreplace) %_sysconfdir/pam.d/*
%_libexecdir/cs-backup-locker
%_bindir/%name-command
%_datadir/%name
%_datadir/dbus-1/services/*.service
%_datadir/applications/*.desktop
%_datadir/icons/hicolor/scalable/*/*.svg
%_datadir/icons/hicolor/scalable/*/*.svg
%doc AUTHORS NEWS README.md

%files -n lib%name
%_libdir/libcscreensaver.so.*

%files -n lib%name-devel
%_libdir/*.so
%_pkgconfigdir/*

%files -n lib%name-gir
%_libdir/girepository-1.0/*

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*

%changelog
* Mon Jan 29 2024 Anton Midyukov <antohami@altlinux.org> 6.0.3-alt1
- 6.0.3

* Fri Dec 29 2023 Anton Midyukov <antohami@altlinux.org> 6.0.2-alt1
- 6.0.2

* Thu Dec 21 2023 Anton Midyukov <antohami@altlinux.org> 6.0.1-alt1
- 6.0.1

* Fri Dec 01 2023 Anton Midyukov <antohami@altlinux.org> 6.0.0-alt1
- 6.0.0

* Mon Jul 10 2023 Vladimir Didenko <cow@altlinux.org> 5.8.1-alt1.gitd5ad373
- 5.8.1-1-gd5ad373

* Tue Jun 13 2023 Vladimir Didenko <cow@altlinux.org> 5.8.0-alt1.git84cf44a
- 5.8.0-1-g84cf44a

* Fri Feb 10 2023 Stanislav Levin <slev@altlinux.org> 5.6.3-alt2
- Filtered Python's self-provides (related #45231).

* Tue Jan 10 2023 Vladimir Didenko <cow@altlinux.org> 5.6.3-alt1
- 5.6.3

* Wed Dec 14 2022 Vladimir Didenko <cow@altlinux.org> 5.6.2-alt1
- 5.6.2-1-gb032c8d

* Fri Dec 2 2022 Vladimir Didenko <cow@altlinux.org> 5.6.1-alt1
- 5.6.1

* Fri Nov 18 2022 Vladimir Didenko <cow@altlinux.org> 5.6.0-alt1
- 5.6.0

* Fri Aug 26 2022 Vladimir Didenko <cow@altlinux.org> 5.4.4-alt1
- 5.4.4

* Tue Aug 2 2022 Vladimir Didenko <cow@altlinux.org> 5.4.2-alt1
- 5.4.2

* Thu Jul 21 2022 Vladimir Didenko <cow@altlinux.org> 5.4.1-alt1
- 5.4.1-3-g8d658e7

* Fri Jun 10 2022 Vladimir Didenko <cow@altlinux.org> 5.4.0-alt1
- 5.4.0

* Thu Mar 10 2022 Vladimir Didenko <cow@altlinux.org> 5.2.1-alt1
- 5.2.1

* Mon Nov 29 2021 Vladimir Didenko <cow@altlinux.org> 5.2.0-alt1
- 5.2.0

* Tue Nov 9 2021 Vladimir Didenko <cow@altlinux.org> 5.0.7-alt1
- 5.0.7

* Mon Jun 28 2021 Vladimir Didenko <cow@altlinux.org> 5.0.6-alt1
- 5.0.6

* Wed Jun 16 2021 Vladimir Didenko <cow@altlinux.org> 5.0.5-alt1
- 5.0.5

* Tue Jun 1 2021 Vladimir Didenko <cow@altlinux.org> 5.0.1-alt1
- 5.0.1

* Mon May 31 2021 Vladimir Didenko <cow@altlinux.org> 5.0.0-alt1
- 5.0.0

* Fri Dec 11 2020 Vladimir Didenko <cow@altlinux.org> 4.8.1-alt1
- 4.8.1

* Fri Nov 27 2020 Vladimir Didenko <cow@altlinux.org> 4.8.0-alt1
- 4.8.0

* Fri May 15 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt2
- add USE_SETRES flag (screensaver doesn't work properly without it)

* Thu May 14 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt1
- 4.6.0

* Wed Dec 11 2019 Vladimir Didenko <cow@altlinux.org> 4.4.1-alt1
- 4.4.1

* Wed Nov 20 2019 Vladimir Didenko <cow@altlinux.org> 4.4.0-alt1
- 4.4.0

* Tue Jun 25 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt1
- 4.2.0

* Tue Jun 25 2019 Vladimir Didenko <cow@altlinux.org> 4.0.3-alt1
- 4.0.3

* Tue Dec 25 2018 Vladimir Didenko <cow@altlinux.org> 4.0.3-alt1
- 4.0.3

* Tue Nov 20 2018 Vladimir Didenko <cow@altlinux.org> 4.0.1-alt1
- 4.0.1

* Fri Jun 15 2018 Vladimir Didenko <cow@altlinux.org> 3.8.2-alt2
- add translation package to dependency

* Wed Jun 13 2018 Vladimir Didenko <cow@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon May 7 2018 Vladimir Didenko <cow@altlinux.org> 3.8.1-alt1
- 3.8.1

* Thu May 3 2018 Vladimir Didenko <cow@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Nov 22 2017 Vladimir Didenko <cow@altlinux.org> 3.6.1-alt1
- 3.6.1

* Fri Oct 27 2017 Vladimir Didenko <cow@altlinux.org> 3.6.0-alt1
- 3.6.0

* Thu Aug 24 2017 Vladimir Didenko <cow@altlinux.org> 3.4.2-alt1
- 3.4.2

* Thu Jun 29 2017 Vladimir Didenko <cow@altlinux.org> 3.4.1-alt1
- 3.4.1

* Fri May 5 2017 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Jan 31 2017 Vladimir Didenko <cow@altlinux.org> 3.2.13-alt1
- 3.2.13-31-gd5d40bd

* Fri Dec 23 2016 Vladimir Didenko <cow@altlinux.org> 3.2.12-alt1
- 3.2.12

* Fri Dec 14 2016 Vladimir Didenko <cow@altlinux.org> 3.2.9-alt2
- Better patch for pam-helper location

* Tue Dec 13 2016 Vladimir Didenko <cow@altlinux.org> 3.2.9-alt1
- 3.2.9

* Mon Dec 12 2016 Vladimir Didenko <cow@altlinux.org> 3.2.8-alt1
- 3.2.8

* Fri Nov 25 2016 Vladimir Didenko <cow@altlinux.org> 3.2.6-alt1
- 3.2.6

* Fri Nov 18 2016 Vladimir Didenko <cow@altlinux.org> 3.2.3-alt1
- 3.2.3-2-gac3d612

* Thu Nov 17 2016 Vladimir Didenko <cow@altlinux.org> 3.2.2-alt1
- 3.2.2-9-g53b3ef5

* Sun Nov 13 2016 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1
- 3.2.0-5-g0dd6f89

* Wed Jun 1 2016 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Apr 25 2016 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- 3.0.0

* Mon Oct 19 2015 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- 2.8.0

* Tue Jun 2 2015 Vladimir Didenko <cow@altlinux.org> 2.6.3-alt1
- 2.6.3

* Sat May 23 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt2
- git20150523

* Tue May 19 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri May 8 2015 Vladimir Didenko <cow@altlinux.org> 2.5.0-alt1
- git20150506

* Mon Mar 30 2015 Vladimir Didenko <cow@altlinux.org> 2.4.2-alt1
- 2.4.2

* Fri Oct 31 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Oct 14 2014 Vladimir Didenko <cow@altlinux.org> 2.3.0-alt1
- git20140923

* Tue Jul 22 2014 Vladimir Didenko <cow@altlinux.org> 2.2.4-alt1
- 2.2.4

* Mon May 12 2014 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt1
- 2.2.3

* Mon May 5 2014 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- 2.2.2

* Wed Apr 30 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt2
- 2.2.0-1-g68b6a34

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- 2.2.0

* Mon Apr 7 2014 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt2
- git20140327

* Tue Oct 29 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3

* Mon Oct 21 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1.1
- fix build

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- 2.0.0

* Fri Sep 27 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt3.1
- fixed build

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt3
- rebuild for GNOME-3.10

* Thu Aug 29 2013 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt2
- git20130829

* Mon May 6 2013 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- 1.8.0

* Fri Feb 22 2013 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt1
- Initial build for Alt Linux
