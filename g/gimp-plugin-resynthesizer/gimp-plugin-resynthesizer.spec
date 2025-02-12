%define _name resynthesizer

%define gimpplugindir %(gimptool-2.0 --gimpplugindir)
%define gimpdatadir %(gimptool-2.0 --gimpdatadir)

Name: gimp-plugin-%_name
Version: 2.0.3
Release: alt4

Summary: Gimp plug-in for manipulating textures
License: GPLv3+
Group: Graphics
Url: https://github.com/bootchk/resynthesizer

#Original author's version was at http://logarithmic.net/pfh/resynthesizer
Vcs: https://github.com/bootchk/resynthesizer.git
Source: %_name-%version.tar

Requires: gimp

BuildRequires(pre): rpm-build-python python2-base
BuildRequires: intltool libgimp-devel python2-base

%description
Resynthesizer is a Gimp plug-in that when given a sample of a texture can
synthesize more of that texture. It can also be used to create tiling patterns,
to remove an object from am image by inventing a plausable background, or to
apply a theme to an image (for example to make an image look as though it were
painted).

%prep
%setup -n %_name-%version
# http://gcc.gnu.org/onlinedocs/gcc/Variable-Length.html
# http://stackoverflow.com/questions/26256533/iso-c-forbids-forward-parameter-declaration
sed -i '/ThreadedProgressRecord/{:a;n;s/mutexProgress;/mutexProgress/;ba}' lib/progress.h
sed -i 's|\(#!/usr/bin/\)env \(python\)|\1\22|' PluginScripts/*

%build
%autoreconf
%configure PYTHON=python2
%make_build

%install
%makeinstall_std
%find_lang %_name

%files -f %_name.lang
%gimpplugindir/plug-ins/*
%_datadir/%_name
%doc README.md NEWS

%changelog
* Sat Mar 30 2024 Michael Shigorin <mike@altlinux.org> 2.0.3-alt4
- E2K: fix build with non-gcc (ilyakurdyukov@)

* Wed Aug 03 2022 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt3
- updated to v2.0.3-24-gecfc4e7

* Sat Mar 28 2020 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt2
- replaced python by python2

* Fri Jan 19 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Sun Jan 07 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Wed May 17 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Thu Nov 21 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0-alt1
- 2.0

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Tue Apr 26 2011 Victor Forsiuk <force@altlinux.org> 1.0-alt1
- 1.0 (new upstream).

* Tue Oct 07 2008 Victor Forsyuk <force@altlinux.org> 0.16-alt2
- Install all by hand due to broken gimp-2.6's gimptool.

* Fri Mar 28 2008 Victor Forsyuk <force@altlinux.org> 0.16-alt1
- 0.16

* Mon Sep 17 2007 Victor Forsyuk <force@altlinux.org> 0.15-alt1
- Initial build.
