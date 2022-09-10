Name: anilibria-winmaclinux
Version: 1.1.12
Release: alt1

Summary: AniLibria online video player for desktop platforms
Summary(ru_RU.UTF-8): Онлайн-видеоплеер AniLibria для настольных платформ
License: GPL-3.0-only
Group: Video
Url: http://anilibriadesktop.reformal.ru

ExcludeArch: %not_qt5_qtwebengine_arches

Requires: qt5-graphicaleffects
Requires: libqt5-multimedia
Requires: qt5-quickcontrols2
Requires: qt5-quickcontrols
Requires: libqt5-svg

# Source-url: https://github.com/anilibria/anilibria-winmaclinux/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Patch: %name-1.1.9-alt-config.patch

BuildRequires: qt5-base-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-webview-devel
BuildRequires: qt5-webengine-devel
BuildRequires: qt5-graphicaleffects
BuildRequires: qt5-svg-devel
BuildRequires: qt5-websockets-devel
BuildRequires: qt5-declarative-devel
BuildRequires: gstreamer1.0-devel

BuildRequires(pre): rpm-macros-qt5 
BuildRequires(pre): rpm-macros-qt5-webengine

%description
Linux\Windows\Mac client for online viewing of cartoons and animated films
from a group of well-known fandabers AniLibria.

%description -l ru_RU.UTF-8
Linux\Windows\Mac клиент для онлайн просмотра мультфильмов и анимационных
фильмов от группы известных фандаберов AniLibria.

%prep
%setup
%autopatch -p1

%build
pushd src
%qmake_qt5
%make_build
popd

%install
pushd src
INSTALL_ROOT=%buildroot %makeinstall_std
popd

%files
%doc README.md cinemahall.md remoteprotocol.md
%_bindir/AniLibria
%_desktopdir/anilibria.desktop
%_iconsdir/hicolor/*/apps/anilibria.png

%changelog
* Sat Sep 10 2022 Evgeny Chuck <koi@altlinux.org> 1.1.12-alt1
- new version (1.1.12) with rpmgs script

* Fri Aug 19 2022 Evgeny Chuck <koi@altlinux.org> 1.1.11-alt1
- new version (1.1.11) with rpmgs script
- Changed the description of the "Summary" tag to be more accurate

* Mon Aug 15 2022 Evgeny Chuck <koi@altlinux.org> 1.1.10-alt3
- Added dependencies that fix errors when running the QML interface

* Mon Aug 01 2022 Evgeny Chuck <koi@altlinux.org> 1.1.10-alt2
- Added dependency libqt5-multimedia to fix media playback

* Mon Jul 25 2022 Evgeny Chuck <koi@altlinux.org> 1.1.10-alt1
- new version (1.1.10) with rpmgs script

* Sat Jun 18 2022 Evgeny Chuck <koi@altlinux.org> 1.1.9-alt1
- initial build for ALT Linux Sisyphus
