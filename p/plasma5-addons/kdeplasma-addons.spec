%define rname kdeplasma-addons

%ifarch %not_qt5_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

%define plasmacomicprovidercore_sover 0
%define libplasmacomicprovidercore libplasmacomicprovidercore%plasmacomicprovidercore_sover
%define plasmaweatherprivate_sover 0
%define libplasmaweatherprivate libplasmaweatherprivate%plasmaweatherprivate_sover
%define plasmapotdprovidercore_sover 0
%define libplasmapotdprovidercore libplasmapotdprovidercore%plasmapotdprovidercore_sover

Name: plasma5-addons
Version: 5.27.9
Release: alt2
Epoch: 1
%K5init

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 Plasma addons
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: %name-common = %version-%release
# plasma.quickshare
Requires: kf5-purpose
# plasma.diskquota
Requires: quota
#
Provides: kf5-kdeplasma-addons = %EVR
Obsoletes: kf5-kdeplasma-addons < %EVR

Source: %rname-%version.tar
Patch2: alt-sover.patch
Patch3: alt-weather-usability.patch
Patch4: alt-color-picker.patch
Patch5: alt-fixed-comic-widget-crash.patch
Patch6: alt-def-dict.patch

# Automatically added by buildreq on Mon Mar 30 2015 (-bi)
# optimized out: cmake cmake-modules elfutils glib2-devel kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcloog-isl4 libdbusmenu-qt52 libgio-devel libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms libxcbutil-keysyms-devel libxkbfile-devel pkg-config python-base qt5-base-devel ruby ruby-stdlibs scim-libs xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kparts-devel kf5-krunner-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel libibus-devel python-module-google qt5-declarative-devel qt5-x11extras-devel rpm-build-ruby scim-devel
BuildRequires(pre): rpm-build-kf5 rpm-macros-qt5-webengine
BuildRequires: extra-cmake-modules gcc-c++ qt5-declarative-devel qt5-x11extras-devel qt5-script-devel
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%endif
BuildRequires: libxcbutil-image-devel libxcb-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel
BuildRequires: kf5-kdesignerplugin-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel kf5-kpackage-devel kf5-kparts-devel kf5-krunner-devel kf5-kservice-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-framework-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel kf5-kross-devel kf5-knewstuff-devel kf5-kactivities-devel
BuildRequires: kf5-kdeclarative-devel kf5-kholidays-devel kf5-networkmanager-qt-devel
BuildRequires: plasma5-workspace-devel plasma5-libksysguard-devel

%description
Plasma addons.

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kf5-filesystem
Provides: kf5-kdeplasma-addons-common = %EVR
Obsoletes: kf5-kdeplasma-addons-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Provides: kf5-kdeplasma-addons-devel = %EVR
Obsoletes: kf5-kdeplasma-addons-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libplasmacomicprovidercore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libplasmacomicprovidercore
KF5 library

%package -n %libplasmaweatherprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libplasmaweatherprivate
KF5 library

%package -n %libplasmapotdprovidercore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libplasmapotdprovidercore
KF5 library

%prep
%setup -n %rname-%version
%patch2 -p1
#%patch3 -p1
#%patch4 -p2
%patch5 -p2
%patch6 -p1

# disable krunners by default
for d in runners/*/*.json ; do
    sed -i '/EnabledByDefault/s|true|false|' $d
done

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    #

%install
%K5install
%K5install_move data kwin kdevappwizard kdevfiletemplates locale knsrcfiles
%K5install_move icon all
%find_lang %name --all-name
# ensure arch-dependence
touch touch-%_arch

%files common -f %name.lang
%doc touch-%_arch LICENSES/*
%_K5icon/*/*/*/*.*
%_datadir/qlogging-categories5/*.*categories

%files
%_K5data/knsrcfiles/*.knsrc
%_K5plug/kf5/krunner/kcms/*.so
%_K5plug/plasma/applets/*.so
%_K5plug/kpackage/packagestructure/*.so
%_K5plug/plasmacalendarplugins/*
%_K5plug/potd/
%_K5plug/kf5/krunner/*.so
%_K5qml/org/kde/plasma/private/*/
%_K5qml/org/kde/plasmacalendar/*/
%_K5qml/org/kde/plasma/wallpapers/potd/
%_kf5_data/plasma/*
%_K5data/kwin/*
%_K5srvtyp/*
%_datadir/metainfo/*.xml

%files devel
%_K5inc/plasma/potdprovider/
%_K5link/lib*.so
%_libdir/cmake/PlasmaPotdProvider/
%_K5data/kdev*/templates/*.tar.*

#%files -n %libplasmacomicprovidercore
#%_K5lib/libplasmacomicprovidercore.so.*
#%_K5lib/libplasmacomicprovidercore.so.%plasmacomicprovidercore_sover
%files -n %libplasmapotdprovidercore
%_K5lib/libplasmapotdprovidercore.so.*
%_K5lib/libplasmapotdprovidercore.so.%plasmapotdprovidercore_sover

%changelog
* Thu Nov 02 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.9-alt2
- dont force alternate placement

* Thu Oct 26 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.9-alt1
- new version

* Tue Sep 12 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.8-alt1
- new version

* Wed Sep 06 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.7-alt2
- set dict widget defaults

* Tue Aug 01 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.7-alt1
- new version

* Wed Jul 05 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.6-alt1
- new version

* Wed May 10 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.5-alt1
- new version

* Thu Apr 06 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.4-alt1
- new version

* Thu Mar 16 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.3-alt1
- new version

* Tue Feb 28 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.2-alt1
- new version

* Thu Jan 12 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.26.5-alt2
- fix build requires

* Mon Jan 09 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.26.5-alt1
- new version

* Tue Nov 29 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.4-alt1
- new version

* Thu Nov 10 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.3-alt2
- fix build requires

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.3-alt1
- new version

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.2-alt1
- new version

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.5-alt1
- new version

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.4-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.6-alt1
- new version

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.5-alt1
- new version

* Wed Mar 30 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.4-alt1
- new version

* Mon Jan 31 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.23.5-alt3
- build without qtwebengine on e2k

* Wed Jan 26 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.23.5-alt2
- build without qtwebengine on ppc64le

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.23.5-alt1
- new version

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.4-alt1
- new version

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.3-alt1
- new version

* Mon Nov 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.2-alt1
- new version

* Wed Sep 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.5-alt1
- new version

* Tue Jul 27 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.4-alt1
- new version

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.3-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.2-alt1
- new version

* Thu May 13 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.5-alt1
- new version

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.4-alt1
- new version

* Fri Mar 19 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.3-alt1
- new version

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.20.5-alt1
- new version

* Wed Dec 02 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.20.4-alt1
- new version

* Wed Oct 28 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.20.2-alt1
- new version

* Thu Sep 17 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.19.5-alt1
- new version

* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.19.4-alt1
- new version

* Tue Jul 07 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.19.3-alt1
- new version

* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.5-alt1
- new version

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.4-alt1
- new version

* Wed Apr 01 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.3-alt2
- turn off some krunner plugins by default

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.3-alt1
- new version

* Fri Feb 28 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.18.1-alt2
- Applied upstream patch removing extra configure button for comic and weather widgets.

* Wed Feb 19 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.1-alt1
- new version

* Thu Feb 13 2020 Oleg Solovyov <mcpain@altlinux.org> 1:5.17.5-alt2
- fix konsoleprofiles runner

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.17.5-alt1
- new version

* Fri Dec 27 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.4-alt2
- fix requires

* Thu Dec 05 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.4-alt1
- new version

* Wed Nov 13 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.3-alt1
- new version

* Fri Nov 01 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.2-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.1-alt1
- new version

* Thu Oct 17 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.0-alt1
- new version

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.5-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.4-alt1
- new version

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.3-alt1
- new version

* Tue Jul 02 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.2-alt2
- rediff alt-weather-usability.patch

* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.2-alt1
- new version

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.1-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.5-alt2
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.5-alt1
- new version

* Wed Apr 24 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.4-alt1
- new version

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.12.8-alt1
- new version

* Wed Nov 21 2018 Pavel Moseev <mars@altlinux.org> 1:5.12.7-alt3
- add two patches to fix comic widget crash

* Fri Oct 12 2018 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.7-alt2
- dictionary runner: allow dictionary to search the same word many times

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.7-alt1
- new version

* Fri Sep 07 2018 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.6-alt6
- fix colorpicker widget layout

* Wed Aug 08 2018 Ivan Razzhivin <underwit@altlinux.org> 1:5.12.6-alt5
- improve weather widget usability 
- fix fifteenpuzzle widget error

* Wed Aug 01 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.6-alt4
- fix dictionary translation

* Thu Jul 12 2018 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.6-alt3
- fix dictionary search

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.6-alt2
- fix version

* Tue Jul 03 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2
- update russian translation

* Wed Jun 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Mon Feb 19 2018 Maxim Voronov <mvoronov@altlinux.org> 5.12.0-alt2
- renamed kf5-kdeplasma-addons -> plasma5-addons

* Wed Feb 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Wed Jan 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1
- new version

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1
- new version

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1
- new version

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1
- new version

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

* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

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

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Fri Nov 20 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt4
- build with scim

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

* Wed May 13 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt2
- fix conflict with KDE4

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
