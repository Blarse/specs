Name: qt5ct
Version: 1.7
Release: alt3

Summary: Qt5 Configuration Tool
Summary(ru_RU.UTF-8): Инструмент для настройки оформления приложений Qt5

License: BSD-2-Clause-NetBSD
Group: System/Configuration/Other
Url: https://sourceforge.net/projects/qt5ct

# Source-url: https://sourceforge.net/projects/qt5ct/files/qt5ct-%version.tar.bz2/download
Source: %name/%name-%version.tar

Patch1: %name-1.5-alt-desktop.patch

BuildRequires(pre): rpm-macros-qt5
BuildRequires: qt5-base-devel-static
BuildRequires: qt5-tools-devel

%package -n lib%name-devel
Summary: Development library for %name
Summary(ru_RU.UTF-8): Библиотека разработки для %name
Group: Development/C++
Requires: %name = %version-%release

%description
This applications allows users to configure Qt5 settings (theme,
font, icons, etc.) under DE/WM without Qt integration.

%description -l ru_RU.UTF-8
Это приложение позволяет пользователям настраивать параметры Qt5 (тема,
шрифт, значки и т. д.) в DE / WM без интеграции с Qt.

%description -n lib%name-devel
Development library %name.

%description -n lib%name-devel -l ru_RU.UTF-8
Библиотека разработки %name.

%prep
%setup
%autopatch -p2

echo "export QT_QPA_PLATFORMTHEME='%name'" > %name.sh
echo "setenv QT_QPA_PLATFORMTHEME '%name'" > %name.csh

%build
%qmake_qt5 CONFIG+=debug
%make_build

%install
INSTALL_ROOT=%buildroot %makeinstall_std

install -Dm 0755 %name.sh %buildroot%_sysconfdir/profile.d/%name.sh
install -Dm 0755 %name.csh %buildroot%_sysconfdir/profile.d/%name.csh

%files
%doc AUTHORS ChangeLog COPYING README
%config %_sysconfdir/profile.d/%name.*sh
%_bindir/%name
%_datadir/%name
%dir %_libdir/qt5/plugins/platformthemes/
%_libdir/qt5/plugins/platformthemes/lib%name.so
%_libdir/qt5/plugins/styles/libqt5ct-style.so
%_libdir/lib%name-common.so.*
%_desktopdir/%name.desktop

%files -n lib%name-devel
%_libdir/lib%name-common.so

%changelog
* Thu Sep 07 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.7-alt3
- NMU: trimmed build requirements, build on all architectures

* Fri Mar 03 2023 Evgeny Chuck <koi@altlinux.org> 1.7-alt2
- Fixed packaging in accordance with the Shared Library Policy

* Wed Mar 01 2023 Evgeny Chuck <koi@altlinux.org> 1.7-alt1
- new version (1.7) with rpmgs script
- added debug package

* Tue Feb 28 2023 Evgeny Chuck <koi@altlinux.org> 1.6-alt1
- new version (1.6) with rpmgs script

* Sun Sep 04 2022 Evgeny Chuck <koi@altlinux.org> 1.5-alt3
- Fixed a bug in the description of the desktop file

* Sun Feb 13 2022 Evgeny Chuck <koi@altlinux.org> 1.5-alt2
- fix License tag (BSD -> BSD-2-Clause-NetBSD)
- cleanup spec

* Sun Dec 05 2021 Evgeny Chuck <koi@altlinux.org> 1.5-alt1
- new version (1.5) with rpmgs script
- Update spec for version 1.5:
  + added package description in Russian
  + minor fixes in spec

* Wed Aug 19 2020 Ivan A. Melnikov <iv@altlinux.org> 1.1-alt1
- New version

* Fri Feb 01 2019 Ivan A. Melnikov <iv@altlinux.org> 0.37-alt1
- New version
- Make /etc/profile.d/qt5ct* executable (closes: #35769)

* Thu Oct 19 2017 Sergey V Turchin <zerg@altlinux.org> 0.30-alt1.1
- NMU: build with Qt 5.9

* Tue Jan 31 2017 Hihin Ruslan <ruslandh@altlinux.ru> 0.30-alt1
- New Version

* Sat Jun 04 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.24-alt1
- initial build for ALT Linux Sisyphus
