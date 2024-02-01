%def_disable snapshot
%define _name Fretboard
%define ver_major 5.3
%define xdg_name dev.bragefuglseth.%_name

%def_disable bootstrap

Name: fretboard
Version: %ver_major
Release: alt1

Summary: Look up guitar chords
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/bragefuglseth/fretboard

%if_disabled snapshot
Source: %url/releases/download/v%version/%name-%version.tar.xz
%else
Vcs: https://github.com/bragefuglseth/fretboard.git
Source: %name-%version.tar
%endif
# tarball provides vendored sources
%{?_enable_snapshot:Source1: %name-%version-cargo.tar}

%define gtk_ver 4.10
%define adwaita_ver 1.4

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver typelib(Adw) = 1

%description
Fretboard lets you find guitar chords by typing their names or plotting
them on an interactive guitar neck. When you have identified a chord,
you can experiment with changing it, see more ways to play it, or
bookmark it to save it for later. No matter if you are a beginner or an
advanced guitarist, you can use Fretboard to practice, learn, and master
your favorite songs!

%prep
%setup -n %name-%version %{?_disable_bootstrap:%{?_enable_snapshot:-a1}}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/appdata/%xdg_name.metainfo.xml
%doc README*

%changelog
* Thu Feb 01 2024 Yuri N. Sedunov <aris@altlinux.org> 5.3-alt1
- first build for Sisyphus



