%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 1.0
%define beta %nil
%define api_ver 1+

%def_disable bootstrap
%def_disable check

Name: glycin-loaders
Version: %ver_major.0
Release: alt1%beta

Summary: Glycin loaders for several formats
License: MPL-2.0 OR LGPL-2.1-or-later
Group: Graphics
Url: https://gitlab.gnome.org/Incubator/loupe

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/glycin.git
Source: %name-%version%beta.tar
%endif
%{?_enable_snapshot:Source1: %name-%version-cargo.tar}

%define gtk_ver 4.12
%define cairo_ver 1.17
%define heif_ver 1.14.2

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson git rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(cairo) >= %cairo_ver
BuildRequires: pkgconfig(libheif) >= %heif_ver
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libjxl)
BuildRequires: pkgconfig(libseccomp)

BuildRequires: clang-devel

%description
Glycin image library allows to decode images into gdk::Texture
(https://gtk-rs.org/gtk4-rs/stable/latest/docs/gdk4/struct.Texture.html)
and to extract image metadata.

This package provides modular image loaders for Glycin.

%prep
%setup -n %name-%version%beta %{?_enable_snapshot:%{?_disable_bootstrap:-a1}}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libexecdir/%name/%api_ver/glycin-heif
%_libexecdir/%name/%api_ver/glycin-jxl
%_libexecdir/%name/%api_ver/glycin-svg
%_libexecdir/%name/%api_ver/glycin-image-rs
%_datadir/%name/%api_ver/conf.d/glycin-heif.conf
%_datadir/%name/%api_ver/conf.d/glycin-jxl.conf
%_datadir/%name/%api_ver/conf.d/glycin-svg.conf
%_datadir/%name/%api_ver/conf.d/glycin-image-rs.conf
%doc README*


%changelog
* Sun Mar 17 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Tue Nov 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- 0.1.2

* Thu Sep 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- 0.1.0

* Sun Jul 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt0.1.alpha
- first build for Sisyphus


