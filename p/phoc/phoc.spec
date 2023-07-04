%def_enable snapshot
%define _libexecsir %_prefix/libexec
%define ver_major 0.29
%define beta %nil
%define rdn_name sm.puri.Phoc

%define dev_uid 500

%def_enable embed_wlroots
%{?_enable_embed_wlroots:%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}}
%def_disable check

Name: phoc
Version: %ver_major.0
Release: alt1%beta

Summary: Display compositor designed for mobile devices
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/World/Phosh/phoc

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Vcs: https://gitlab.gnome.org/World/Phosh/phoc.git
Source: %name-%version%beta.tar
%endif

%define gnome_desktop_ver 43

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0) >= 2.50.0
BuildRequires: pkgconfig(glib-2.0) >= 2.50.0
BuildRequires: pkgconfig(gnome-desktop-3.0) >= %gnome_desktop_ver
BuildRequires: pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols) >= 1.15
BuildRequires: pkgconfig(json-glib-1.0)

%{?_disable_embed_wlroots:BuildRequires: pkgconfig(wlroots) >= 0.15}
%{?_enable_embed_wlroots:BuildRequires: libgbm-devel libseat1-devel
BuildRequires: pkgconfig(xcb-renderutil) pkgconfig(xcb-icccm)
#BuildRequires: pkgconfig(xcb-errors)
BuildRequires: xorg-xwayland-devel libglvnd-devel libvulkan-devel}
%{?_enable_check:BuildRequires: xvfb-run mutter-gnome}

%description
Phoc is a wlroots based mobile devices compositor. Phoc is pronounced
like the English word fog.

%prep
%setup -n %name-%version%beta

%build
%meson %{?_disable_embed-wlroots:-Dembed-wlroots=disabled} \
    %{?_enable_embed_wlroots:--default-library=static} \
    -Ddev-uid=%dev_uid
%nil
%meson_build

%install
%meson_install

%{?_enable_embed_wlroots:
rm -r %buildroot%_includedir/wlr
rm %buildroot%_libdir/libwlroots.a
rm %buildroot%_pkgconfigdir/wlroots.pc}

%check
xvfb-run %__meson_test

%files
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/sm.puri.phoc.gschema.xml
%_iconsdir/hicolor/symbolic/apps/%rdn_name.svg
%doc README.md NEWS

%changelog
* Tue Jul 04 2023 Yuri N. Sedunov <aris@altlinux.org> 0.29.0-alt1
- 0.29.0

* Wed May 31 2023 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1
- updated to v0.28.0-1-gf707185

* Mon May 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.27.0-alt1
- 0.27.0

* Fri Mar 31 2023 Yuri N. Sedunov <aris@altlinux.org> 0.26.0-alt1
- 0.26.0

* Sun Mar 12 2023 Yuri N. Sedunov <aris@altlinux.org> 0.25.2-alt1
- 0.25.2

* Wed Mar 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.25.0-alt1
- 0.25.0

* Thu Feb 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.24.0-alt1
- 0.24.0

* Mon Jan 16 2023 Yuri N. Sedunov <aris@altlinux.org> 0.23.0-alt1
- 0.23.0

* Sat Sep 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.21.1-alt1
- v0.21.1-1-gc25d237

* Sun Jul 31 2022 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt0.5%beta
- first build for Sisyphus (v0.21.0_beta1-21-ge367874)


