%ifndef _unitdir_user
%define _unitdir_user %prefix/lib/systemd/user
%endif

%define rname kwin

%define kwin_sover 5
%define libkwin libkwin%kwin_sover
%define kcmkwincommon_sover 5
%define libkcmkwincommon libkcmkwincommon%kcmkwincommon_sover
%define kwineffects_sover 14
%define libkwineffects libkwineffects%kwineffects_sover
%define kwinglutils_sover 14
%define libkwinglutils libkwinglutils%kwinglutils_sover
%define kwinxrenderutils_sover 14
%define libkwinxrenderutils libkwinxrenderutils%kwinxrenderutils_sover

Name: plasma5-%rname
Version: 5.27.10
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 Window Manager
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kf5-kwin = %EVR
Obsoletes: kf5-kwin < %EVR

Requires: hwdatabase
Requires: /usr/bin/Xwayland kf5-kirigami plasma5-kscreenlocker
Requires: qml(QtMultimedia) qml(QtQuick.VirtualKeyboard) qt5-quickcontrols qt5-quickcontrols2
Requires: qml(org.kde.kquickcontrols) qml(org.kde.plasma.components) qml(org.kde.plasma.core)
Requires(post): /sbin/setcap

Source: %rname-%version.tar
#
Patch1: alt-def-window-buttons.patch
Patch2: alt-def-nocompositing.patch
Patch3: alt-def-qcompositing.patch
Patch4: alt-hwdatabase.patch
Patch5: alt-def-xkb.patch
Patch6: alt-def-layout-switch.patch

# Automatically added by buildreq on Thu Mar 05 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils glibc-devel-static kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcloog-isl4 libgpg-error libjson-c libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libudev-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libxcb-devel libxcbutil-icccm libxcbutil-image libxcbutil-keysyms libxcbutil-keysyms-devel libxkbfile-devel pkg-config python-base qt5-base-devel qt5-declarative-devel qt5-tools-devel ruby ruby-stdlibs wayland-devel xml-common xml-utils xorg-kbproto-devel xorg-xextproto-devel xorg-xf86miscproto-devel xorg-xf86vidmodeproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdecoration-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel libepoxy-devel libinput-devel libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel libxcbutil-icccm-devel libxcbutil-image-devel libxkbcommon-devel python-module-google qt5-multimedia-devel qt5-script-devel qt5-tools-devel-static qt5-x11extras-devel rpm-build-gir rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: rpm-build-python3
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel-static qt5-declarative-devel
BuildRequires: libqaccessibilityclient-qt5-devel
BuildRequires: libcap-utils libcap-devel zlib-devel
BuildRequires: libxcbutil-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-cursor-devel libxcbutil-keysyms-devel
BuildRequires: libxkbcommon-devel libxkbcommon-x11-devel libgbm-devel libdrm-devel libEGL-devel libxcvt-devel
BuildRequires: fontconfig-devel libfreetype-devel liblcms2-devel
BuildRequires: libepoxy-devel libinput-devel libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel
BuildRequires: pipewire-libs-devel
BuildRequires: qt5-wayland-devel kde5-plasma-wayland-protocols wayland-protocols
BuildRequires: qt5-multimedia-devel qt5-script-devel qt5-tools-devel-static qt5-x11extras-devel qt5-sensors-devel
BuildRequires: kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdeclarative-devel plasma5-kdecoration-devel kf5-kdelibs4support
BuildRequires: kf5-kdoctools kf5-kdoctools-devel
BuildRequires: kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kpackage-devel
BuildRequires: kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel kf5-kidletime-devel
BuildRequires: kf5-kirigami-devel kf5-krunner-devel
BuildRequires: plasma5-kscreenlocker-devel plasma5-breeze-devel

%description
KDE Window Manager

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: kf5-kwin-common = %EVR
Obsoletes: kf5-kwin-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Provides: kf5-kwin-devel = %EVR
Obsoletes: kf5-kwin-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkwin
Group: System/Libraries
Summary: KF5 library
Requires: %name-common
%description -n %libkwin
KF5 library

%package -n %libkcmkwincommon
Group: System/Libraries
Summary: KF5 library
Requires: %name-common
%description -n %libkcmkwincommon
KF5 library

%package -n %libkwineffects
Group: System/Libraries
Summary: KF5 library
Requires: %name-common >= %EVR
%description -n %libkwineffects
KF5 library

%package -n %libkwinglutils
Group: System/Libraries
Summary: KF5 library
Requires: %name-common >= %EVR
%description -n %libkwinglutils
KF5 library

%package -n %libkwinxrenderutils
Group: System/Libraries
Summary: KF5 library
Requires: %name-common >= %EVR
%description -n %libkwinxrenderutils
KF5 library

%prep
%setup -n %rname-%version
%patch1 -p1
#%patch2 -p1 -b .nocompositing
#%patch3 -p1 -b .qcompositing
%patch4 -p1 -b .hwinfo
#%patch5 -p1 -b .xkb
%patch6 -p1

for f in src/kcms/compositing/kwincompositing.json ; do
    sed -i '/X-DocPath/d' $f
done

%build
%K5build \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    -DDATA_INSTALL_DIR=%_K5data \
    #

%install
%K5install
%K5install_move data kconf_update knsrcfiles krunner
%find_lang %name --with-kde --all-name

%post
/sbin/setcap CAP_SYS_NICE=+ep %_K5bin/kwin_wayland ||:

%files common -f %name.lang
%doc LICENSES/*
%_K5icon/*/*/apps/*.*

%files
%_datadir/qlogging-categories5/*.*categories
%_K5bin/kwin*
%_K5exec/*kwin*
%_K5plug/kpackage/packagestructure/kwin_*.so
%_K5plug/kwin/
%_K5plug/plasma/kcms/systemsettings/*kwin*.so
%_K5plug/plasma/kcms/systemsettings/*virtua*.so
%_K5plug/plasma/kcms/systemsettings_qwidgets/*kwin*.so
%_K5plug/org.kde.kdecoration2/
%_K5xdgapp/*kwin*.desktop
%_K5xdgapp/*virtua*.desktop
%_K5cf_bin/kwin*
%_K5conf_up/kwin*
%_K5qml/org/kde/kwin*/
%_K5cfg/*.kcfg
%_K5data/kpackage/kcms/kcm_*/
%_K5data/kwin/
%_K5data/knsrcfiles/*.knsrc
%_K5data/krunner/dbusplugins/*.desktop
#%_K5srv/kwin/
%_K5srvtyp/*.desktop
%_K5notif/*.notifyrc
%_unitdir_user/*.service

%files devel
%_K5inc/kwin*.h
%_K5link/lib*.so
%_K5lib/cmake/KWin*/
%_K5dbus_iface/*.xml

%files -n %libkwineffects
%_K5lib/libkwineffects.so.%kwineffects_sover
%_K5lib/libkwineffects.so.*
%files -n %libkwinglutils
%_K5lib/libkwingl*utils.so.%kwinglutils_sover
%_K5lib/libkwingl*utils.so.*
%files -n %libkwin
%_K5lib/libkwin.so.%kwin_sover
%_K5lib/libkwin.so.*
#%files -n %libkwinxrenderutils
#%_K5lib/libkwinxrenderutils.so.%kwinxrenderutils_sover
#%_K5lib/libkwinxrenderutils.so.*
%files -n %libkcmkwincommon
%_K5lib/libkcmkwincommon.so.%kcmkwincommon_sover
%_K5lib/libkcmkwincommon.so.*


%changelog
* Thu Dec 07 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.10-alt1
- new version

* Thu Nov 02 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.9-alt2
- dont force alternate placement

* Thu Oct 26 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.9-alt1
- new version

* Tue Sep 12 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.8-alt1
- new version

* Tue Aug 01 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.7-alt1
- new version

* Wed Jul 05 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.6-alt1
- new version

* Wed May 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.5-alt1
- new version

* Wed Apr 12 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.4-alt3
- update to 5.27.4.1

* Thu Apr 06 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.4-alt2
- fix default keyboard layout switch mode

* Thu Apr 06 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.4-alt1
- new version

* Thu Mar 16 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.3-alt1
- new version

* Tue Feb 28 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.2-alt1
- new version

* Mon Jan 30 2023 Sergey V Turchin <zerg@altlinux.org> 5.26.5-alt2
- build with pipewire to enable screencasting on wayland

* Mon Jan 09 2023 Sergey V Turchin <zerg@altlinux.org> 5.26.5-alt1
- new version

* Tue Nov 29 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.4-alt1
- new version

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.3-alt1
- new version

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.2-alt2
- add fix against kdebug#461032 (closes: 44246)

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.2-alt1
- new version

* Mon Oct 03 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt2
- remove help button from compositing settings module

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt1
- new version

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.4-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.6-alt1
- new version

* Tue Jun 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.5-alt4
- remove unneeded docs entry

* Thu Jun 02 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.5-alt3
- remove unneeded docs entry

* Fri May 13 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.5-alt2
- load default xkb settings from /etc/X11/xinit/Xkbmap

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.5-alt1
- new version

* Wed Mar 30 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.4-alt1
- new version

* Mon Mar 28 2022 Oleg Solovyov <mcpain@altlinux.org> 5.23.5-alt2
- Backport self-hiding GHNS buttons

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.5-alt1
- new version

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt1
- new version

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3-alt1
- new version

* Mon Nov 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.2-alt1
- new version

* Tue Sep 28 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt2
- fix to build with libglvnd-1.3.4

* Wed Sep 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt1
- new version

* Tue Jul 27 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.4-alt1
- new version

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.3-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.2-alt1
- new version

* Thu May 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.5-alt1
- new version

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.4-alt1
- new version

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.3-alt2
- merge p9 changelog

* Mon Apr 05 2021 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt2
- add upstream fix get all EGL extension defines

* Fri Mar 19 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.3-alt1
- new version

* Tue Feb 02 2021 Sergey V Turchin <zerg@altlinux.org> 5.20.5-alt2
- fix to xrender renderer defaults

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.20.5-alt1
- new version

* Wed Dec 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.4-alt1
- new version

* Wed Oct 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.2-alt1
- new version

* Fri Sep 25 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.5-alt2
- fix default window title buttons

* Thu Sep 17 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.5-alt1
- new version

* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.4-alt1
- new version

* Tue Jul 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.3-alt1
- new version

* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt1
- new version

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.4-alt1
- new version

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt1
- new version

* Wed Feb 19 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt1
- new version

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.17.5-alt1
- new version

* Thu Dec 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.4-alt1
- new version

* Mon Dec 02 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.3-alt2
- update build requires

* Wed Nov 13 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.3-alt1
- new version

* Fri Nov 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.2-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.1-alt1
- new version

* Thu Oct 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Tue Oct 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.5-alt2
- update requires

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.5-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.4-alt1
- new version

* Tue Jul 23 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.3-alt3
- use XRender compositing by default

* Fri Jul 12 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.3-alt2
- fix requires

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.3-alt1
- new version

* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.2-alt1
- new version

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.1-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt2
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt1
- new version

* Wed Apr 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Thu Apr 04 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt2
- add upstream fix to force glXSwapBuffers to block with NVIDIA driver

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Tue Aug 14 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt2
- rebuild with new Qt

* Wed Jun 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt2
- rebuild with new libwayland-egl

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Mon Feb 19 2018 Maxim Voronov <mvoronov@altlinux.org> 5.12.0-alt2
- renamed kf5-kwin -> plasma5-kwin

* Tue Feb 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Tue Feb 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1.1
- rebuild with new Qt

* Wed Jan 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1
- new version

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1
- new version

* Wed Oct 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt2
- rebuild with new Qt

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1
- new version

* Thu Aug 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt2
- enable compositing by default

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1
- new version

* Mon Jul 03 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt2.1
- rebuild

* Mon Jun 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt2
- update from 5.9 branch

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1
- new version

* Mon Apr 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.1-alt1
- new version

* Thu Jan 12 2017 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt2
- rebuild with new Qt

* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt0.M80P.1
- build for M80P

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt1
- new version

* Mon Aug 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.3-alt1
- new version

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Wed Jul 06 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt1
- new version

* Wed Jun 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.5-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt1
- new version

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version

* Wed Mar 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt1
- new version

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- new version

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt2
- setup default window buttons

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Sat Aug 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Wed Apr 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt2
- fix package on arm
- disable compositing by default

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
