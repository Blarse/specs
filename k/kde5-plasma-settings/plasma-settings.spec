%define rname plasma-settings

Name: kde5-%rname
Version: 21.08
Release: alt1
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: Settings application for Plasma Mobile
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: qml(org.kde.kcm)

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Aug 18 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-common kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-common kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-common kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libcrypt-devel libctf-nobfd0 libgio-devel libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-svg libqt5-test libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libxcbutil-keysyms pkg-config python-modules python2-base python3 python3-base python3-module-paste qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 rpm-build-qml rpm-macros-python sh4 tzdata
#BuildRequires: appstream extra-cmake-modules kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kio-devel kf5-kpackage-devel kf5-plasma-framework-devel libkf5kcmutils python-modules-compiler python3-dev qt5-svg-devel qt5-translations qt5-wayland-devel qt5-webengine-devel tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kio-devel
BuildRequires: kf5-kpackage-devel kf5-plasma-framework-devel
BuildRequires: pkgconfig(gobject-2.0) pkgconfig(gio-2.0)

%description
Settings application for Plasma Mobile.

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

%package -n libkf5plasma-settings
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkf5plasma-settings
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kpackage
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/plasma-settings
%_K5plug/kcms/*.so
%_K5xdgapp/*plasmasettings*.desktop
%_K5data/kpackage/kcms/*/
%_K5data/kpackage/genericqml/org.kde.plasma.settings/
%_K5srv/*.desktop

#%files devel
#%_K5inc/plasma-settings_version.h
#%_K5inc/plasma-settings/
#%_K5link/lib*.so
#%_K5lib/cmake/plasma-settings
#%_K5archdata/mkspecs/modules/qt_plasma-settings.pri

#%files -n libkf5plasma-settings
#%_K5lib/libplasma-settings.so.*

%changelog
* Wed Sep 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08-alt1
- new version

* Wed Aug 18 2021 Sergey V Turchin <zerg@altlinux.org> 21.07-alt1
- initial build
