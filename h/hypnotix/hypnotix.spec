Name: hypnotix
Version: 3.4
Release: alt1
Summary: An M3U IPTV Player
License: GPL-2.0-or-later
Group: Video
Url: https://github.com/linuxmint/hypnotix
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
# https://github.com/linuxmint/hypnotix/issues/254
# Patch0: mpv-remove-deprecated-detach-destroy.patch
# https://github.com/linuxmint/hypnotix/issues/84
Patch1: 0001-fix-python3-shebang.patch
Patch2: 0002-Fix-hypnotix-GUI-error.patch

BuildRequires: glib2-devel python3-dev
Requires: libmpv2
Requires: python3-module-cinemagoer
Requires: python3-module-pygobject3
Requires: python3-module-pycairo
Requires: python3-module-setproctitle
Requires: python3-module-xapp
Requires: libxapps-gir
BuildArch: noarch

%description
Hypnotix is an IPTV streaming application with support for live TV, movies and series.

%prep
%setup
%autopatch -p2

%build
%make_build

%install
mkdir -p %buildroot/usr
cp -r usr %buildroot

%find_lang %name

%files
%doc README.md
%_bindir/%name
%_prefix/lib/%name/
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/org.x.%name.gschema.xml
%_datadir/%name/*
%_datadir/locale/*/LC_MESSAGES/*.mo
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Tue Jun 20 2023 Artyom Bystrov <arbars@altlinux.org> 3.4-alt1
- New version

* Tue Jan 31 2023 Artyom Bystrov <arbars@altlinux.org> 3.2-alt1
- update to new version (ALT#43208)

* Fri Dec 09 2022 L.A. Kostis <lakostis@altlinux.ru> 3.1-alt2.1
- NMU:
  + update libmpv req.
  + mpv: remove deprecated detach_destroy call.

* Sat Dec 03 2022 Artyom Bystrov <arbars@altlinux.org> 3.1-alt2
- back localizations in package

* Sat Dec 03 2022 Artyom Bystrov <arbars@altlinux.org> 3.1-alt1
- update to new version

* Fri Nov 25 2022 Artyom Bystrov <arbars@altlinux.org> 1.4-alt1
- initial build for ALT Sisyphus
