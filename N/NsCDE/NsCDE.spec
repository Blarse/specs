Name:		NsCDE
Version:	2.1
Release:	alt1
Summary:	Not so Common Desktop Environment
Group: Graphical desktop/Other
Packager: Ilya Mashkin <oddity@altlinux.ru>

License:	GPLv3
URL:		https://github.com/NsCDE
Source0:	https://github.com/NsCDE/NsCDE/releases/download/2.1/NsCDE-2.1.tar.gz


BuildRequires:  gcc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	make
BuildRequires:	gettext libX11-devel libXt-devel libXext-devel libXpm-devel
BuildRequires: ImageMagick
BuildRequires: oksh pdksh mksh
BuildRequires: python3-module-psutil rpm-build-python3 rpm-build-perl
BuildRequires: python3-module-yaml python3-module-PyQt5-devel python-module-pygtk-devel
BuildRequires:  glibc-devel

Requires:	xterm sed fvwm cpp xsettingsd stalonetray dunst xclip xdotool
Requires: python3-module-yaml dex
#Requires: python3-qt5 libqt5-qtstyleplugins-platformtheme-gtk2
Requires:	%{_bindir}/convert
Requires:	%{_bindir}/import
Requires:	%{_bindir}/xrdb
Requires:	%{_bindir}/xset
Requires:	%{_bindir}/xprop
Requires:	%{_bindir}/xdpyinfo
Requires:	%{_bindir}/xrandr
Requires:	xdg-utils gettext

%add_python3_req_skip SpritesGtk2

%add_findprov_skiplist %{_libdir}/NsCDE/python/SpritesGtk2.py
#add_findprov_skiplist %{_datadir}/NsCDE/backdrops/Afternoon.pm
#add_findprov_skiplist %{_datadir}/NsCDE/backdrops/Ankh.pm
%add_findreq_skiplist %{_datadir}/NsCDE/backdrops/*.pm
%add_findreq_skiplist %{_datadir}/NsCDE/defaults/backer/*.pm
%add_findreq_skiplist %{_datadir}/NsCDE/icons/NsCDE/*.pm
%add_findreq_skiplist %{_libdir}/NsCDE/python/SpritesGtk2.py

%description
NsCDE is a retro but powerful UNIX desktop environment which resembles
CDE look (and partially feel) but with a more powerful and flexible
framework beneath-the-surface, more suited for 21st century unix-like
and Linux systems and user requirements than original CDE.

NsCDE can be considered as a heavyweight FVWM theme on steroids, but
combined with a couple other free software components and custom FVWM
applications and a lot of configuration, NsCDE can be considered a
lightweight hybrid desktop environment.


%prep
%setup -q -n %name-%version


%build
autoreconf -ivf
%configure --prefix=/usr --sysconfdir=/etc
%make_build


%install
%makeinstall_std

%find_lang NsCDE --all-name

%files -f NsCDE.lang
#files
%{_bindir}/*
%{_libexecdir}/%{name}/
%{_libdir}/%{name}/
%{_datadir}/applications/*
%{_datadir}/desktop-directories/*
%{_datadir}/xsessions/nscde.desktop
%{_datadir}/icons/*
%{_datadir}/doc/nscde/
#{_datadir}/locale/*
%{_datadir}/%{name}/
%{_sysconfdir}/xdg/menus/nscde-applications.menu


%changelog
* Wed Apr 13 2022 Ilya Mashkin <oddity@altlinux.ru> 2.1-alt1
- Build for Sisiphus

* Tue Mar 22 2022 Hegel3DReloaded <nscde@protonmail.com> - 2.1-4
- New colormgr.local / colormgr.addons scheme
- Introduce key binding sets
- Backup old gtk and qt configs during bootstrap
- Optionally specify alternative root setter for fvwm3 non-global monitors
- Inject new NSCDE_VERSION on restart after upgrade
- Various fixes
- Qt5 Kvantum engine support
- Update docs

* Thu Jan 6 2022 Hegel3DReloaded <nscde@protonmail.com> - 2.0-6
- Fix system Subpanels.actions S10 help backspaces
- Fix move first item to the end double copy on the subpanels

* Wed Jan 5 2022 Hegel3DReloaded <nscde@protonmail.com> - 2.0-5
- Fix generate_subpanels backslash and quoting

* Tue Dec 21 2021 Hegel3DReloaded <nscde@protonmail.com> - 2.0-4
- Release NsCDE 2.0
- Fix Qt5 qt5ct.conf new fonts handling
- Update fontsets for higher resolutions
- Add more handy key bindings into style managers
- Documentation now has descriptions of XDG subsystems in NsCDE
- Support for more terminal emulators in colormgr.local and fontmgr.local
- Illustrated documentation
- Smart XDG paths from configure.ac
- Front Panel and Subpanels smart contextual Help
- Correct screen calculation for GWM under FVWM3 with multiple monitors
- Misc minor fixes

* Fri Dec 3 2021 Hegel3DReloaded <nscde@protonmail.com> - 2.0-3
- Introduce Front Panel Icon Manager
- Update docs and locales
- Misc minor fixes
- Move Front Panel icons feature
- Rename Subpanel Items feature
- Input checking

* Tue Nov 9 2021 Hegel3DReloaded <nscde@protonmail.com> - 2.0
- First RPM package, working example

