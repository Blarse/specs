%define rname kgpg

Name: kde5-%rname
Version: 23.08.5
Release: alt2
%K5init

Group: File tools
Summary: Graphical frontend to GPG
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-gpg-bin.patch
Patch2: alt-revoke-fix-segfault.patch
Patch3: alt-remove-details-button.patch
Patch4: alt-gpg-home-args.patch
Patch5: alt-gpg-verify.patch

# Automatically added by buildreq on Wed Mar 29 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ glibc-devel-static gtk-update-icon-cache kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgpg-error-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-script libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 xml-common xml-utils
#BuildRequires: boost-devel-headers extra-cmake-modules kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-kcontacts-devel kf5-karchive-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemmodels-devel kf5-knotifications-devel kf5-ktextwidgets-devel kf5-kwindowsystem-devel libgpgme-devel python-module-google python3-dev ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: boost-devel libgpgme-devel
BuildRequires: kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-kcontacts-devel
BuildRequires: kf5-karchive-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel
BuildRequires: kf5-kiconthemes-devel kf5-kio-devel kf5-kitemmodels-devel kf5-knotifications-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kwindowsystem-devel

%description
Graphical GPG frontend.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%K5build

%install
%K5install
%K5install_move data kgpg kio
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/kgpg
%_K5xdgapp/org.kde.kgpg.desktop
%_K5data/kgpg/
%_K5data/kio/servicemenus/*kgpg*.desktop
%_K5start/org.kde.kgpg.desktop
%_K5cfg/kgpg.kcfg
%_K5xmlgui/kgpg/
%_K5icon/*/*/apps/kgpg.*
%_K5icon/*/*/actions/*key*.*
%_K5icon/*/*/status/*key*.*
%_datadir/qlogging-categories5/*.*categories
%_datadir/metainfo/*.xml

%changelog
* Tue Jun 25 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 23.08.5-alt2
- fix verify option in command line (closes: 41057)

* Fri Feb 16 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.5-alt1
- new version

* Mon Dec 11 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt1
- new version

* Fri Nov 10 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt1
- new version

* Fri Oct 13 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt1
- new version

* Thu Oct 05 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.1-alt1
- new version

* Fri Jul 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt1
- new version

* Fri Jun 09 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.2-alt1
- new version

* Thu Jun 01 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.1-alt1
- new version

* Mon Mar 06 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.3-alt1
- new version

* Mon Feb 06 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Wed Jan 11 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Fri Dec 09 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt2
- fixes the display of the trust indicator(thanks sirius@alt) (closed: 44348)

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Thu Sep 15 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Fri May 13 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Fri Mar 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Mon Jan 17 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Thu Sep 23 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt2
- fix expert mode when create keypair

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Mon Aug 23 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Thu Jul 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Thu Jun 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.2-alt1
- new version

* Wed May 19 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Mon Apr 26 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt2
- fix to use gpg2 at first start

* Thu Mar 11 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Thu Jan 14 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt1
- new version

* Fri Dec 18 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Wed Oct 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Fri Sep 18 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Fri Aug 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Mon Mar 23 2020 Oleg Solovyov <mcpain@altlinux.org> 19.12.3-alt2
- remove unneeded "Details >>" button in signature check dialog
- fix crash when revoking keys after deletion

* Thu Mar 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Wed Mar 04 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt2
- fix default gpg program

* Fri Feb 14 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Tue Jan 21 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Fri Nov 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Fri Oct 25 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Tue Aug 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Mon May 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Tue Feb 19 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Fri Oct 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt3
- update russian translation

* Fri Jul 27 2018 Pavel Akopov <pak@altlinux.org> 18.04.3-alt2%ubt
- Fix translated labels text cropping in kgpgfirstassistant.

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Tue May 22 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Mon Nov 13 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- initial build
