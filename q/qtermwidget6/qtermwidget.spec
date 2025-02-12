# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 2

Name: qtermwidget6
Version: 2.0.1
Release: alt1

Summary: unicode-enabled, embeddable QT6 terminal widget
License: GPL-2.0-or-later
Group: Terminals

Url: https://github.com/lxqt/qtermwidget
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: qt6-base-devel qt6-tools-devel
BuildRequires: lxqt2-build-tools

%description
QTermWidget is an opensource project based on KDE Konsole
application. The main goal of this project is to provide
unicode-enabled, embeddable Qt6 widget for using as a built-in
console (or terminal emulation widget).

Of course I'm aware about embedding abilities of original
Konsole, but once I had Qt without KDE, and it was a serious
problem.

0.4.0+ is a friendly fork, the original project is still available
at http://qtermwidget.sourceforge.net/

%package data
Summary: unicode-enabled, embeddable Qt6 terminal widget shared data
Group: Terminals
BuildArch: noarch

%description data
QTermWidget is an opensource project based on KDE Konsole
application. The main goal of this project is to provide
unicode-enabled, embeddable Qt6 widget for using as a built-in
console (or terminal emulation widget).

This package contains the shared data.

%package -n lib%name
Summary: unicode-enabled, embeddable Qt6 terminal widget library
Group: System/Libraries
Requires: %name-data

%description -n lib%name
This package contains the shared library for %name.

%package -n lib%name-devel
Summary: unicode-enabled, embeddable Qt6 terminal widget library
Group: Development/KDE and QT
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains the development headers for %name library.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files data
%_datadir/%name/

%files -n lib%name
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%sover.*

%files -n lib%name-devel
%doc AUTHORS LICENSE README*
%_includedir/%name/
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%_libdir/cmake/%name/

%changelog
* Wed Jul 10 2024 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt1
- New version 2.0.1

* Wed Jun 12 2024 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- New version 2.0.0
- rename qtermwidget -> qtermwidget6

* Sun Nov 05 2023 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- New version 1.4.0.

* Sat Apr 15 2023 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

* Sat Nov 05 2022 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sun Apr 17 2022 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Fri Nov 05 2021 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Fri Apr 16 2021 Anton Midyukov <antohami@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Thu Nov 05 2020 Anton Midyukov <antohami@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Mon Jan 28 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Sat Aug 25 2018 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1.1
- Rebuilt with qt 5.11s

* Tue May 22 2018 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1
- 0.9.0

* Tue Oct 24 2017 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- added conflicts with qtermwidget-qt5 package

* Tue Oct 24 2017 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0 built against Qt5

* Tue Oct 04 2016 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- 0.7.0

* Fri Nov 14 2014 Michael Shigorin <mike@altlinux.org> 0.6.0-alt1
- 0.6.0 (see also #30468)
- updated Url:

* Wed Mar 07 2012 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- initial build (loosely based on qterminal.spec and upstream one)

