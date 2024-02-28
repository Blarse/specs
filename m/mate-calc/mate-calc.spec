Name: mate-calc
Version: 1.28.0
Release: alt1
Epoch: 1
Summary: MATE Desktop calculator
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common libgtk+3-devel libxml2-devel libmpfr-devel libmpc-devel yelp-tools

%description
mate-calc is a powerful graphical calculator with financial, logical and scientific modes.
It uses a multiple precision package to do its arithmetic to give a high degree of accuracy.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING README.md
%_bindir/*
%_datadir/metainfo/%name.appdata.xml
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/org.mate.calc.gschema.xml
%_man1dir/*.1*

%changelog
* Wed Feb 28 2024 Valery Inozemtsev <shrek@altlinux.ru> 1:1.28.0-alt1
- 1.28.0

* Tue Apr 11 2023 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt3
- fixed round keys (closes: #44349)

* Tue Apr 11 2023 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt2
- updated translation

* Tue Aug 10 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt1
- 1.26.0

* Thu Aug 20 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.1-alt1
- 1.24.1

* Wed Feb 26 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.0-alt1
- 1.24.0

* Wed Oct 16 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Mon May 13 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Thu Mar 07 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Tue Feb 12 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.3-alt1
- 1.20.3

* Tue Mar 20 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
