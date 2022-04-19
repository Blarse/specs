Name: epdfinfo
Version: 0.91
Release: alt1

Summary: Emacs PDF helper
License: GPLv3
Group: Text tools
Url: https://github.com/vedang/pdf-tools

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(poppler)
BuildRequires: pkgconfig(poppler-glib)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(zlib)

%description
%summary

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/epdfinfo

%changelog
* Tue Apr 19 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.91-alt1
- initial
