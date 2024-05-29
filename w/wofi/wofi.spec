Name: wofi
Version: 1.4.1
Release: alt1

Summary: launcher/menu program for wlroots based wayland compositors such as sway
License: GPLv3
Group: Graphical desktop/Other

Url: https://hg.sr.ht/~scoopta/wofi

# Source-url: https://hg.sr.ht/~scoopta/wofi/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: meson
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(wayland-client)
BuildRequires(pre): rpm-macros-meson

%description
%summary

%package devel
Group: Development/C
Summary: Development package for %name

%description devel
%summary devel

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%_bindir/%name
%_man1dir/*
%_man5dir/*
%_man7dir/*

%files devel
%_includedir/wofi-1/*.h
%_pkgconfigdir/wofi.pc
%_man3dir/*

%changelog
* Wed May 29 2024 Roman Alifanov <ximper@altlinux.org> 1.4.1-alt1
- new version (1.4.1) with rpmgs script
- move to tarball

* Sun Nov 06 2022 Roman Alifanov <ximper@altlinux.org> 1.3-alt3
- Added comment on use of hg-git

* Tue Nov 01 2022 Roman Alifanov <ximper@altlinux.org> 1.3-alt2
- fixed Group: for -devel subpackage (thx grenka@)

* Sun Oct 16 2022 Roman Alifanov <ximper@altlinux.org> 1.3-alt1
- initial build for sisyphus
