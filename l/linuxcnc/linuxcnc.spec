# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_without docs
%set_verify_elf_method unresolved=relaxed
Name: linuxcnc
Version: 2.9.0
Release: alt0.4.20210826

Summary: LinuxCNC controls CNC machines
Summary(ru_RU.UTF-8): Программа управления ЧПУ станков
License: GPLv2+ and LGPLv2
Group: Engineering
Url: https://github.com/LinuxCNC/linuxcnc

ExclusiveArch: aarch64 alpha %arm ia64 %ix86 x86_64 %e2k

Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
Patch1: fix-dir-path.patch
Patch6: qtvcp_import_fix.patch
Patch7: not_require_dpkg.patch
Patch8: linuxcnc-alt-python3.patch
Patch9: linuxcnc-alt-tirpc.patch
Buildrequires(pre): rpm-build-tcl rpm-build-python3
Buildrequires: rpm-build-gir
Buildrequires: python3-devel
BuildRequires: gcc-c++ pkgconfig(glib-2.0)
BuildRequires: libgtk+3-gir-devel
BuildRequires: python3-module-pygobject3
BuildRequires: libGL-devel libGLU-devel
BuildRequires: libXaw-devel libXinerama-devel libXmu-devel libXt-devel xorg-cf-files
BuildRequires: pkgconfig(libmodbus)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libudev)
BuildRequires: libncurses-devel libreadline-devel
BuildRequires: libtirpc-devel
BuildRequires: kmod
BuildRequires: man-db
BuildRequires: python3-modules-tkinter
#python3-modules-unittest
BuildRequires: python3-module-yapps2
BuildRequires: boost-devel-headers
BuildRequires: boost-python3-devel
BuildRequires: tcl-devel tk-devel tcl-img tclx bwidget
#BuildRequires: tcl-blt-devel
BuildRequires: intltool
#BuildRequires: pkgconfig(libgnomeprintui-2.2)
%if_with docs
BuildRequires: asciidoc-a2x ghostscript-common ghostscript-utils source-highlight graphviz groff-ps
%endif
BuildRequires: desktop-file-utils ImageMagick-tools

Obsoletes: %name-data =< %EVR
Requires: lib%name = %EVR
# for qtvcp
Requires: python3-module-PyQt5-devel

Requires: tclx tcl-blt
%py3_requires Xlib
%py3_requires PyQt5.Qsci

# Fix me!!!
%add_python3_req_skip __main__ gi.repository.GdkPixbuf gst gtk gtk.glade Cairo
%add_python3_req_skip emccanon interpreter

%filter_from_requires s/^.*rip-environment//

%add_python3_path %_datadir/qtvcp
%add_python3_path %_datadir/%name/ncfiles

%description
LinuxCNC is software that runs on Linux, on most standard PCs, that can
interpret G-code and run a CNC machine. It was originally developed on a
milling machine, but support was added for lathes and many other types of
machine. It can be used with mills, lathes, plasma cutters, routers, robots,
and so on. 

%description -l ru_RU.UTF-8
LinuxCNC это программа, которая работает на ОС Linux на большинстве стандартных
ПК, которые могут интерпретировать G-код и запустить станок с ЧПУ. Изначально он
был разработан для фрезерного станка, но поддержка была добавлена и для токарных
станков и многих других типов машин. Он может быть использован с токарными
станками, станками плазменной резки, роботами и так далее.

%package -n liblinuxcnc-devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description -n liblinuxcnc-devel
Development files for %name

%package -n lib%name
Summary: Library for %name
Group: Engineering

%description -n lib%name
Library for %name

%package doc
Summary: Documementation for %name
Buildarch: noarch
Group: Documentation

%description doc
Documementation for %name

%package doc-fr
Summary: French documementation for %name
Buildarch: noarch
Group: Documentation
Requires: %name-doc = %version

%description doc-fr
French documementation for %name

%package doc-es
Summary: Spanish documementation for %name
Buildarch: noarch
Group: Documentation
Requires: %name-doc = %version

%description doc-es
Spanish documementation for %name

%prep
%setup
%autopatch -p1

sed -i 's|lib/tcltk/linuxcnc|%_lib/tcl/linuxcnc|' lib/python/rs274/options.py
sed -i 's|INCLUDES := .|INCLUDES := . /usr/include/tirpc|' src/Makefile
sed -i 's|LDFLAGS := |LDFLAGS := -ltirpc |' src/Makefile

#fix make install
sed 's/ -o root//g' -i src/Makefile

# explicitly set python-3
find . -type f -name *.py | xargs sed -i \
	-e '1s:^#!/usr/bin/env python$:#!/usr/bin/python%__python3_version:' \
	-e '1s:^#!/usr/bin/python$:#!/usr/bin/python%__python3_version:' \
	-e '1s:^#!/usr/bin/python2$:#!/usr/bin/python%__python3_version:' \
	%nil

%ifarch %e2k
# unsupported as of lcc 1.25.17
sed -i 's,-fno-fast-math,,' src/Makefile*
%endif

%build
pushd src
%autoreconf
%configure \
    --enable-non-distributable=yes \
    --with-realtime=uspace \
    --disable-gtk2 \
    %if_with docs
    --enable-build-documentation=pdf
    %endif

%make_build
popd

%install
pushd src
%makeinstall_std
popd

install -d -m755 %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc.desktop %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc-latency.desktop %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc-pncconf.desktop %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc-stepconf.desktop %buildroot%_desktopdir

#fix desktop Name
pushd %buildroot%_desktopdir
sed 's/Name=/Name=LinuxCNC /g' -i linuxcnc-pncconf.desktop \
    linuxcnc-stepconf.desktop linuxcnc-latency.desktop
popd

#fix desktop categories
desktop-file-install --dir %buildroot%_desktopdir \
        --remove-key=Version \
        --remove-category=X-CNC \
        --add-category=Development \
        --add-category=Engineering \
        %buildroot%_desktopdir/*.desktop

### == desktop file documentation
cat>%buildroot%_desktopdir/%name-documentation.desktop<<END
[Desktop Entry]
Name=LinuxCNC Documentation
Name[ru_RU]= LinuxCNC Документация 
Exec=%_bindir/xdg-open %_docdir/%name
Icon=linuxcncicon
Terminal=false
Type=Application
Categories=Development;Engineering;
END

#install rules
mkdir -p %buildroot%_udevrulesdir
cp debian/extras/lib/udev/rules.d/* %buildroot%_udevrulesdir

# convert and install icon files
for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps
    convert linuxcncicon.png -resize $x'x'$x \
            %buildroot%_iconsdir/hicolor/$x'x'$x/apps/linuxcncicon.png
done

#fix uncompressed manual pages
pushd %buildroot%_mandir
xz `find -name *.?`
popd

# remove unpackaged static libraries
rm %buildroot%_libdir/*.a

%find_lang %name gmoccapy --output=%name.lang

%files -f %name.lang
%_bindir/*
%_libexecdir/%name
%_tcllibdir/%name
%python3_sitelibdir/*
%_sysconfdir/%name
%_initdir/realtime
%_udevrulesdir/*.rules
%_desktopdir/*.desktop
# Fix me!!! Exclude not working with python3 application:
%exclude %_desktopdir/linuxcnc-pncconf.desktop
%exclude %_desktopdir/linuxcnc-stepconf.desktop
%_sysconfdir/X11/app-defaults/*
%_datadir/axis
%_datadir/%name
%_datadir/glade3
%_datadir/gmoccapy
%_datadir/gscreen
%_datadir/gtksourceview-2.0/*
%_datadir/qtvcp/*
%_liconsdir/*
%_niconsdir/*
%_miconsdir/*
%_mandir/man?/*
%_docdir/%name
%if_with docs
%exclude %_docdir/%name/*.pdf
%endif

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name
%_libdir/*.so

%if_with docs
%files doc
%_docdir/%name/*.pdf
%exclude %_docdir/%name/*_??.pdf

%files doc-fr
%_docdir/%name/*_fr.pdf

%files doc-es
%_docdir/%name/*_es.pdf
%endif

%changelog
* Thu Aug 26 2021 Anton Midyukov <antohami@altlinux.org> 2.9.0-alt0.4.20210826
- new snapshot
- remove unpackaged static libraries (fix build with LTO flag)
- cleanup spec

* Sun Aug 01 2021 Anton Midyukov <antohami@altlinux.org> 2.9.0-alt0.3.20210801
- new snapshot

* Wed Jul 28 2021 Michael Shigorin <mike@altlinux.org> 2.9.0-alt0.2
- E2K: fix build

* Mon Jul 26 2021 Anton Midyukov <antohami@altlinux.org> 2.9.0-alt0.1
- New snapshot
- switch to python3 (Closes: 40376)
- exclude pncconf, stepconf (not support python3)

* Fri Jun 25 2021 Anton Midyukov <antohami@altlinux.org> 2.8.2-alt1
- new version 2.8.2

* Wed Apr 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.1-alt3
- Rebuilt with boost-1.76.0.

* Thu Mar 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.1-alt2
- Fixed build with gcc-10 and rebuilt with new boost libraries.

* Sun Dec 06 2020 Anton Midyukov <antohami@altlinux.org> 2.8.1-alt1
- New version 2.8.1

* Thu Sep 17 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.15-alt3
- Fixed build on armh and rebuilt with new boost.

* Thu Mar 12 2020 Anton Midyukov <antohami@altlinux.org> 2.7.15-alt2
- Fixed tcl dir again

* Fri Mar 06 2020 Anton Midyukov <antohami@altlinux.org> 2.7.15-alt1
- New version 2.7.15

* Thu Mar 5 2020 Anton Midyukov <antohami@altlinux.org> 2.7.14-alt5
- Fixed tcl dir
- Enabled hierarchical dependency search for python2
- Update buildrequires
- Added missing requires

* Mon Dec 16 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.14-alt4
- Rebuilt with boost-1.71.0.

* Tue Oct 01 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.7.14-alt3
- Added ExclusiveArch tag to limit architectures to aarch64, alpha, %%arm,
  ia64, %%ix86, and x86_64.
- Removed noarch from %%name-data subpackage.

* Sat May 25 2019 Anton Midyukov <antohami@altlinux.org> 2.7.14-alt2
- Add io.h for aarch64 (dummy) instead of without-sys-io.h-for-no-x86.patch
- Build with libtirpc

* Tue Jul 03 2018 Anton Midyukov <antohami@altlinux.org> 2.7.14-alt1
- new version 2.7.14

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.13-alt1.1
- NMU: rebuilt with boost-1.67.0

* Sun May 13 2018 Anton Midyukov <antohami@altlinux.org> 2.7.13-alt1
- new version 2.7.13

* Tue Mar 06 2018 Anton Midyukov <antohami@altlinux.org> 2.7.12-alt2
- replace requres python-module-gst -> python-module-gst1.0
- disable build docs

* Tue Jan 30 2018 Anton Midyukov <antohami@altlinux.org> 2.7.12-alt1
- new version 2.7.12
- Fix pathdir

* Wed Aug 30 2017 Anton Midyukov <antohami@altlinux.org> 2.7.11-alt1
- New version 2.7.11
- Added missing requires 

* Sun Jul 30 2017 Anton Midyukov <antohami@altlinux.org> 2.7.10-alt2
- Fix desktop categories.

* Tue Jul 25 2017 Anton Midyukov <antohami@altlinux.org> 2.7.10-alt1
- new version 2.7.10

* Sun Jun 11 2017 Anton Midyukov <antohami@altlinux.org> 2.7.9-alt1
- New version 2.7.9
- Remove fix_build_for_i586.patch

* Fri Mar 24 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.7.8-alt1.qa1
- Rebuilt against Tcl/Tk 8.6

* Sat Feb 04 2017 Anton Midyukov <antohami@altlinux.org> 2.7.8-alt1
- New version 2.7.8
- Fix build with libmodbus3.1.4
- Fix build for i586
- Remove subpackage python-module-linuxcnc and tcl-linuxcnc

* Fri Jul 22 2016 Anton Midyukov <antohami@altlinux.org> 2.7.5-alt1
- New version 2.7.5
- Fix repocop warning.

* Thu May 12 2016 Anton Midyukov <antohami@altlinux.org> 2.7.4-alt1.20160506.1
- Initial build for Alt Linux Sisyphus.
