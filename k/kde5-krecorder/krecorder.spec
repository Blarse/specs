%define rname krecorder

Name: kde5-%rname
Version: 22.04
Release: alt1
%K5init no_appdata

Group: Graphical desktop/KDE
Summary: Audio recording
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Aug 18 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libqt5-svg libqt5-widgets libqt5-xml libsasl2-3 libssl-devel libstdc++-devel python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 sh4 tzdata
#BuildRequires: appstream extra-cmake-modules kf5-kconfig-devel kf5-ki18n-devel kf5-kirigami-devel python3-dev qt5-multimedia-devel qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: qt5-multimedia-devel qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel
BuildRequires: kf5-kconfig-devel kf5-ki18n-devel kf5-kirigami-devel kf5-kcoreaddons-devel

%description
A convergent audio recording application for Plasma.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5recorder
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkf5recorder
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/krecorder
%_K5xdgapp/*krecorder*.desktop
%_K5icon/hicolor/*/apps/*krecorder*.*

#%files devel
#%_K5inc/krecorder_version.h
#%_K5inc/krecorder/
#%_K5link/lib*.so
#%_K5lib/cmake/krecorder
#%_K5archdata/mkspecs/modules/qt_krecorder.pri

#%files -n libkf5recorder
#%_K5lib/libkrecorder.so.*

%changelog
* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 22.04-alt1
- new version

* Mon Feb 14 2022 Sergey V Turchin <zerg@altlinux.org> 22.02-alt1
- new version

* Fri Dec 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.12-alt1
- new version

* Wed Sep 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08-alt1
- new version

* Wed Aug 18 2021 Sergey V Turchin <zerg@altlinux.org> 21.07-alt1
- initial build
