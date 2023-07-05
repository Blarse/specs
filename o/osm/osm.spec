Name: osm
Version: 1.2.3
Release: alt1

Summary: Open Sound Meter
License: GPLv3
Group: Sound
Url: https://opensoundmeter.com/

Requires: qml(QtQuick.Controls) = 1.4
Requires: qml(QtQuick.Controls) = 2.0
Requires: qml(QtGraphicalEffects)

Source: %name-%version-%release.tar

ExclusiveArch: aarch64 x86_64

BuildRequires: gcc-c++
BuildRequires: ImageMagick-tools
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickControls2)

%description
Sound measurement application for tuning audio systems in real-time.

%prep
%setup
sed -i 's,@APP_GIT_VERSION@,v%version,' OpenSoundMeter.pro

%build
%qmake_qt5 -o Makefile OpenSoundMeter.pro
%make_build

%install
install -pm0755 -D OpenSoundMeter %buildroot%_bindir/OpenSoundMeter
ln -s OpenSoundMeter %buildroot%_bindir/osm
sed -i '/^Icon/ s,white,osm,' OpenSoundMeter.desktop
install -pm0644 -D OpenSoundMeter.desktop %buildroot%_desktopdir/OpenSoundMeter.desktop
for sz in 16x16 32x32 48x48; do
    d=%buildroot%_iconsdir/hicolor/$sz/apps; mkdir -p $d
    convert icons/white.png -resize $sz $d/osm.png
done

%files
%doc LICENSE README*
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*.png

%changelog
* Tue Jun 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.3-alt1
- 1.2.3 released
