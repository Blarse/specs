%def_disable snapshot
%define _libexecdir %prefix/libexec
%define ver_major 0.29
%define beta %nil
%define api_ver 0
%define rdn_name sm.puri.Phosh
%define dev_uid 1000

%def_enable gtk_doc
%def_enable man

# not installed
%def_disable tools
%def_disable check

Name: phosh
Version: %ver_major.0
Release: alt1.2%beta

Summary: A pure Wayland shell for mobile devices
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/World/Phosh/phosh

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Vcs: https://gitlab.gnome.org/World/Phosh/phosh.git
Source: %name-%version%beta.tar
%endif
Source1: %name.pam
Source2: sm.puri.OSK0.desktop
Patch1: %name-0.28.0-alt-tcb-check.patch
# https://bugzilla.altlinux.org/46930
Patch2: %name-0.29.0-alt-service.patch

Requires: phoc >= 0.28
Requires: gnome-shell-data
Requires: mutter-gnome
Requires: gnome-session
Requires: iio-sensor-proxy
Requires: fonts-ttf-google-lato

Requires: squeekboard

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson
BuildRequires: desktop-file-utils
BuildRequires: pam-devel
BuildRequires: libcallaudio-devel
BuildRequires: libfeedback-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gcr-3) >= 3.7.5
BuildRequires: pkgconfig(gio-2.0) >= 2.72
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.58
BuildRequires: pkgconfig(glib-2.0) >= 2.70.0
BuildRequires: pkgconfig(gnome-desktop-3.0) >= 3.26
BuildRequires: pkgconfig(gsettings-desktop-schemas) >= 42
BuildRequires: pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.22
BuildRequires: pkgconfig(gtk+-wayland-3.0) >= 3.22
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(libfeedback-0.0)
BuildRequires: pkgconfig(libhandy-1) >= 1.1.90
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libnm) >= 1.14
BuildRequires: pkgconfig(libpulse) >= 2.0
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(polkit-agent-1) >= 0.105
BuildRequires: pkgconfig(upower-glib) >= 0.99.1
BuildRequires: pkgconfig(wayland-client) >= 1.14
BuildRequires: pkgconfig(wayland-protocols) >= 1.12
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libecal-2.0)
BuildRequires: pkgconfig(evince-document-3.0)
%{?_enable_gtk_doc:BuildRequires: gi-docgen libhandy1-gir-devel}
%{?_enable_man:BuildRequires: /usr/bin/rst2man}
%{?_enable_check:BuildRequires: xvfb-run dbus at-spi2-core}

%description
Phosh is a simple shell for Wayland compositors speaking the layer-surface
protocol. It currently supports

* a lockscreen
* brightness control and nighlight
* the gcr system-prompter interface
* acting as a polkit auth agent
* enough of org.gnome.Mutter.DisplayConfig to make gnome-settings-daemon happy
* a homebutton that toggles a simple favorites menu
* status icons for battery, wwan and wifi

%package devel
Summary: Development files for Phosh
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides files needed to develop Phosh plugins.

%prep
%setup -n %name-%version%beta
%patch1 -p2
%patch2 -p1 -b .alt
sed -i 's|\(User=\)1000|\1%dev_uid|' data/%name.service

%build
%meson \
    -Dsystemd=true \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{?_enable_man:-Dman=true} \
    %{?_enable_tools:-Dtools=true} \
    -Dphoc_tests=disabled
%nil
%meson_build

%install
%meson_install
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/pam.d/%name
install -Dpm 0644 data/phosh.service %buildroot%_unitdir/phosh.service

install -d %buildroot%_datadir/applications
desktop-file-install --dir %buildroot%_datadir/applications %SOURCE2

%find_lang %name

%check
xvfb-run %__meson_test

%files -f %name.lang
%config(noreplace) %_sysconfdir/pam.d/%name
%_bindir/%name-session
%attr(2711, root, chkpwd) %_libexecdir/%name
%_libexecdir/%name-calendar-server
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%dir %_libdir/%name/plugins/prefs
%_libdir/%name/plugins/lib%name-plugin-calendar.so
%_libdir/%name/plugins/calendar.plugin
%_libdir/%name/plugins/lib%name-plugin-ticket-box.so
%_libdir/%name/plugins/ticket-box.plugin
%_libdir/%name/plugins/lib%name-plugin-upcoming-events.so
%_libdir/%name/plugins/upcoming-events.plugin
%_libdir/%name/plugins/emergency-info.plugin
%_libdir/%name/plugins/lib%name-plugin-emergency-info.so
%_libdir/%name/plugins/prefs/lib%name-plugin-prefs-ticket-box.so
%_libdir/%name/plugins/prefs/lib%name-plugin-prefs-emergency-info.so

%_desktopdir/%rdn_name.desktop
%_desktopdir/sm.puri.OSK0.desktop
%_datadir/glib-2.0/schemas/sm.puri.phosh.gschema.xml
%_datadir/glib-2.0/schemas/sm.puri.phosh.enums.xml
%_datadir/glib-2.0/schemas/sm.puri.phosh.plugins.ticket-box.gschema.xml
%_datadir/glib-2.0/schemas/00_%rdn_name.gschema.override
%_datadir/dbus-1/services/%rdn_name.CalendarServer.service
%_datadir/gnome-session/sessions/%name.session
%_datadir/wayland-sessions/%name.desktop
%_datadir/%name/
%_unitdir/phosh.service
%_userunitdir/gnome-session@%name.target.d/session.conf
%_userunitdir/%rdn_name.service
%_userunitdir/%rdn_name.target
%_datadir/xdg-desktop-portal/portals/%name.portal
%_iconsdir/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%{?_enable_man:%_man1dir/%name.1*
%_man1dir/%name-session.1*}
%doc NEWS README.md

%files devel
%_includedir/%name/
%_pkgconfigdir/%name-plugins.pc
%{?_enable_gtk_doc:%doc %_datadir/doc/%name-%api_ver}

%changelog
* Fri Jul 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.29.0-alt1.2
- data/phosh.service: removed "Environment=LANG=C.UTF-8",
  switched TTYPath/UtmpIdentifier from tty7 to tty1 (ALT#46930)

* Thu Jul 13 2023 Yuri N. Sedunov <aris@altlinux.org> 0.29.0-alt1.1
- required gnome-shell-data & mutter-gnome (ALT#46896)

* Thu Jul 06 2023 Yuri N. Sedunov <aris@altlinux.org> 0.29.0-alt1
- 0.29.0

* Mon Jun 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1.1
- cas@: fixed lock screen authentication (ALT #46389)

* Thu Jun 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1
- 0.28.0

* Tue May 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.27.0-alt1
- 0.27.0
- restored default UID from 500 to 1000
- enabled gtk-doc and man builds

* Mon Apr 03 2023 Yuri N. Sedunov <aris@altlinux.org> 0.26.0-alt1
- 0.26.0

* Sun Mar 12 2023 Yuri N. Sedunov <aris@altlinux.org> 0.25.2-alt1
- 0.25.2

* Thu Mar 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.25.1-alt1
- 0.25.1

* Wed Mar 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.25.0-alt1
- 0.25.0

* Thu Feb 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.24.0-alt1
- 0.24.0

* Wed Dec 28 2022 Yuri N. Sedunov <aris@altlinux.org> 0.23.0-alt1
- 0.23.0
- new -devel subpackage

* Wed Dec 7 2022 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- v0.22.0-13-g3c3ce51a

* Thu Sep 29 2022 Yuri N. Sedunov <aris@altlinux.org> 0.21.1-alt1
- 0.21.1

* Sat Sep 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt1
- 0.21.0

* Sat Jul 30 2022 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt0.5.beta3
- first build for Sisyphus

