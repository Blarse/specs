#%%set_verify_elf_method relaxed

Name: deepin-manual
Version: 5.7.0.75
Release: alt3
Summary: Help files for DDE
License: GPL-3.0+ and (BSD-3-Clause and Qt.Commercial) and ISC
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-manual
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake qt5-base-devel qt5-tools-devel qt5-webchannel-devel dtk5-widget-devel qt5-x11extras-devel qt5-webengine-devel libgmock-devel
Requires: %name-data

%description
%summary.

%package data
Summary: Data files for %name
Group: Graphical desktop/Other
BuildArch: noarch

%description data
Data files for %name.

%prep
%setup
subst 's|lrelease|lrelease-qt5|' translate_generation.sh

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DAPP_VERSION=%version \
    -DVERSION=%version \
    -DLIB_INSTALL_DIR=%_libdir \
#
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/dman
%_bindir/dmanHelper
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/com.deepin.Manual.Open.service
%_datadir/dbus-1/services/com.deepin.Manual.Search.service
%_iconsdir/hicolor/scalable/apps/%name.svg

%files data
%_datadir/%name/

%changelog
* Thu Jul 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.0.75-alt3
- Fixed build with libgmock.so.1.11.0.

* Wed Jun 23 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.0.75-alt2
- Added deepin-manual-data in requires.

* Wed Jun 16 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.0.75-alt1
- New version (5.7.0.75) with rpmgs script.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 5.7.0.7-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu Sep 10 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.0.7-alt1
- Initial build for ALT Sisyphus.
