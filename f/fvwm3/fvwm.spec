Name: fvwm3
Version: 1.0.5
Release: alt2

Summary: F(?) Virtual Window Manager, the successor to fvwm2
License: GPLv2+
Group: Graphical desktop/FVWM based
Url: http://www.fvwm.org/

# https://github.com/fvwmorg/fvwm3
Source: %name-%version.tar

BuildRequires: asciidoctor /usr/bin/pod2man
BuildRequires: libbson-devel libevent-devel libfribidi-devel
BuildRequires: libXcursor-devel libXpm-devel libXrandr-devel libXt-devel libXft-devel
BuildRequires: libpng-devel librsvg-devel libcairo-devel libreadline-devel
BuildRequires: perl-Tk rpm-build-python3

%description
fvwm3 window manager, the successor to fvwm2.

Fvwm is a virtual window manager for the X windows system. It was
originally a feeble fork of TWM by Robert Nation in 1993 (fvwm history),
and has evolved into the fantastic, fabulous, famous, flexible, and so
on, window manager we have today.

Fvwm is ICCCM-compliant and highly configurable. Starting from a minimal
configuration, Fvwm can be configured with both internal tools and third
party software to customize most aspects of a desktop.

Currently, your existing fvwm2 config will work with fvwm3, but over time
this will change.

%package scripts
Summary: F(?) Virtual Window Manager, the successor to fvwm2, additional scripts
Group: Graphical desktop/FVWM based
BuildArch: noarch
Requires: %name = %version
%description scripts
This package contains the FvwmPerl module, fvwm Perl library and other
scripts for fvwm3 window manager, the successor to fvwm2.


%prep
%setup -q

%build
%autoreconf
%configure --enable-mandoc
%make

%install
%makeinstall_std
(
  cd %buildroot/%_mandir/man1/;  for i in fvwm[^3]*; do mv $i fvwm3${i#fvwm}; done
  cd %buildroot/%_mandir/man1/;  for i in Fvwm[^3]*; do mv $i Fvwm3${i#Fvwm}; done
  cd %buildroot/%_bindir/;       for i in fvwm[^3]*; do mv $i fvwm3${i#fvwm}; done
  cd %buildroot/%_bindir/;       for i in Fvwm[^3]*; do mv $i Fvwm3${i#Fvwm}; done
)


# install additional docs
install -p -D -m644 COPYING NEWS *.md -t $RPM_BUILD_ROOT%_docdir/%name-%version/

%define _perl_lib_path %perl_vendor_privlib:%_datadir/fvwm3/perllib

%find_lang --output=%name.lang fvwm FvwmScript

%files -f %name.lang
%_bindir/fvwm3
%_bindir/fvwm3-config
%_bindir/fvwm3-root

%dir %_libexecdir/fvwm3/
%dir %_libexecdir/fvwm3/%version/
%_libexecdir/fvwm3/%version/*
%exclude %_libexecdir/fvwm3/%version/FvwmPerl

%dir %_datadir/fvwm3/
%_datadir/fvwm3/*
%exclude %_datadir/fvwm3/perllib/
%exclude %_datadir/fvwm3/fvwm-script-ComExample.pl

%_mandir/man?/*
%exclude %_mandir/man1/fvwm3-convert-2.6.1*
%exclude %_mandir/man1/fvwm3-menu-desktop.1*
%exclude %_mandir/man1/fvwm3-menu-directory.1*
%exclude %_mandir/man1/fvwm3-menu-xlock.1*
%exclude %_mandir/man1/fvwm3-perllib.1*
%exclude %_mandir/man1/Fvwm3Perl.1*
%_docdir/%name-%version

%files scripts
%_bindir/Fvwm3Command
%_bindir/fvwm3-convert-2.6
%_bindir/fvwm3-menu-desktop
%_bindir/fvwm3-menu-directory
%_bindir/fvwm3-menu-xlock
%_bindir/fvwm3-perllib

%_libexecdir/fvwm3/%version/FvwmPerl

%_datadir/fvwm3/perllib/
%_datadir/fvwm3/fvwm-script-ComExample.pl
%_mandir/man1/fvwm3-convert-2.6.1*
%_mandir/man1/fvwm3-menu-desktop.1*
%_mandir/man1/fvwm3-menu-directory.1*
%_mandir/man1/fvwm3-menu-xlock.1*
%_mandir/man1/fvwm3-perllib.1*
%_mandir/man1/Fvwm3Perl.1*

%changelog
* Wed Oct 19 2022 Vladislav Zavjalov <slazav@altlinux.org> 1.0.5-alt2
- rename scripts and perl libraries to avoid collisions with old fvwm

* Wed Oct 19 2022 Vladislav Zavjalov <slazav@altlinux.org> 1.0.5-alt1
- 1.0.5

* Mon Sep 20 2021 Vladislav Zavjalov <slazav@altlinux.org> 1.0.4-alt1
- 1.0.4

* Tue Dec 22 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.0.2-alt2
- Rename perl modules to avoid duplicated provides

* Mon Dec 21 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.0.2-alt1
- 1.0.2, first build for Altlinux
