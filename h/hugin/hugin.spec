# force to use GDK_BACKEND=x11 while wxWidgets wxGLCanvas
# WxGTK Wayland support
%def_disable gdk_x11
# Python scripting interface disabled by default since 2018.0.0
%def_enable hsi
# lapack support disabled by default
%def_disable lapack
%def_enable epoxy

Name: hugin
Version: 2023.0.0
Release: alt1.1

Summary: hugin - Goal: an easy to use cross-platform GUI for Panorama Tools.
Group: Graphics
License: GPLv2+
Url: https://hugin.sourceforge.net/

#tarball: https://downloads.sourceforge.net/%name/%name-%version.tar.bz2
Source: %name-%version.tar
Patch1: Add-translations-in-desktop-files.patch
Patch2: Fix-build-without-distutils.patch
Patch3: Fix-deprecated-boost-filesystem-usage.patch

%define boost_ver 1.54
%define pano_ver 2.9.21
%define wx_ver 3.0.0
%define enblend_ver 3.2

Requires: libpano13 >= %pano_ver
Requires: enblend >= %enblend_ver
Requires: autopano-sift-C perl-Image-ExifTool make

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ gcc-fortran libgomp-devel
BuildRequires: libpano13-devel >= %pano_ver libwxGTK3.2-devel >= %wx_ver
BuildRequires: boost-devel >= %boost_ver boost-thread-devel boost-devel boost-thread-devel
BuildRequires: boost-datetime-devel boost-regex-devel boost-filesystem-devel boost-iostreams-devel
BuildRequires: boost-system-devel boost-signals-devel
BuildRequires: libXi-devel libXmu-devel libglew-devel
BuildRequires: libjpeg-devel libpng-devel libtiff-devel libexiv2-devel
BuildRequires: liblensfun-devel liblcms2-devel libvigra-devel
BuildRequires: zlib-devel libpango-devel openexr-devel libtclap-devel
BuildRequires: libfftw3-devel libsqlite3-devel
BuildRequires: libflann-devel
%if_enabled hsi
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel swig
%add_python3_path %_datadir/%name/data/plugins*
%endif
%{?_enable_lapack:BuildRequires: liblapack-devel}
%{?_enable_epoxy:BuildRequires: libepoxy-devel}
BuildRequires: desktop-file-utils libappstream-glib-devel perl-podlators

%description
With hugin you can assemble a mosaic of photographs into a complete immersive
panorama, stitch any series of overlapping pictures and much more.

%prep
%setup
%patch1 -p2
%patch2 -p1
%patch3 -p1

%build
%add_optflags %(getconf LFS_CFLAGS)
# reenable RPTHs because libraries in private subdirectory
%cmake -DINSTALL_XRC_DIR="/usr/share/hugin/xrc" \
	-DCMAKE_SKIP_RPATH:BOOL=OFF \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
	%{?_enable_gdk_x11:-DUSE_GDKBACKEND_X11:BOOL=ON} \
	%{?_enable_hsi:-DBUILD_HSI:BOOL=ON} \
	%{?_enable_lapack:-DENABLE_LAPACK:BOOL=ON} \
	%{?_enable_epoxy:-DBUILD_WITH_EPOXY:BOOL=ON} \
	-DPYTHON_EXECUTABLE=%__python3
%cmake_build

%install
%cmake_install
%find_lang --output=%name.lang %name nona_gui
/bin/install -p -m644 -D src/hugin1/hugin/xrc/data/hugin.png %buildroot%_datadir/pixmaps/%name.png
/bin/install -p -m644 -D src/hugin1/hugin/xrc/data/hugin.png %buildroot%_niconsdir/%name.png

for file in hugin PTBatcherGUI calibrate_lens_gui pto_gen; do
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Photography \
	%buildroot%_desktopdir/$file.desktop
done

%files -f %name.lang
%doc AUTHORS README
%_bindir/*
%_desktopdir/*.desktop
%_datadir/%name/
%_datadir/pixmaps/*
%_datadir/mime/packages/hugin.xml
%_libdir/%name/
%{?_enable_hsi:%python3_sitelibdir/*}
%_iconsdir/hicolor/48x48/mimetypes/application-x-ptoptimizer-script.png
%_iconsdir/hicolor/*x*/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg
%_man1dir/*
%_datadir/metainfo/PTBatcherGUI.appdata.xml
%_datadir/metainfo/calibrate_lens_gui.appdata.xml
%_datadir/metainfo/%name.appdata.xml

%changelog
* Wed Jun 12 2024 Ivan A. Melnikov <iv@altlinux.org> 2023.0.0-alt1.1
- NMU fix FTBFS
  + add change from upstream to fix build with Boost 1.85.0
  + partially backport change from upstream to fix build
    without distutils

* Sun Nov 12 2023 Yuri N. Sedunov <aris@altlinux.org> 2023.0.0-alt1
- 2023.0.0

* Tue Nov 07 2023 Yuri N. Sedunov <aris@altlinux.org> 2022.0.0-alt3
- rebuilt against libexiv2.so.28

* Wed Jun 07 2023 Yuri N. Sedunov <aris@altlinux.org> 2022.0.0-alt2
- build with libepoxy instead of GLEW for OpenGL pointer management (ALT #45876)

* Tue Dec 20 2022 Yuri N. Sedunov <aris@altlinux.org> 2022.0.0-alt1
- 2022.0.0
- built with wxGTK-3.2

* Fri Dec 31 2021 Yuri N. Sedunov <aris@altlinux.org> 2021.0.0-alt1
- 2021.0.0

* Sun Dec 13 2020 Yuri N. Sedunov <aris@altlinux.org> 2020.0.0-alt1
- 2020.0.0

* Mon Dec 30 2019 Yuri N. Sedunov <aris@altlinux.org> 2019.2.0-alt1
- 2019.2.0

* Sun Aug 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2019.0.0-alt1
- 2019.0.0
- built against libexiv2-0.27
- built HSI with python3

* Mon Oct 29 2018 Pavel Moseev <mars@altlinux.org> 2018.0.0-alt4
- Updated translations in the form of individual patches

* Mon Oct 29 2018 Pavel Moseev <mars@altlinux.org> 2018.0.0-alt3
- Updated translations

* Mon Jul 02 2018 Yuri N. Sedunov <aris@altlinux.org> 2018.0.0-alt2
- fixed buildreqs

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2018.0.0-alt1.1
- NMU: rebuilt with boost-1.67.0

* Sun Feb 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2018.0.0-alt1
- 2018.0.0

* Wed Sep 13 2017 Yuri N. Sedunov <aris@altlinux.org> 2017.0.0-alt2
- rebuilt with boost-1.65

* Thu Aug 10 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2017.0.0-alt1.1
- Rebuilt for changed libwxGTK3.0 ABI

* Sat Jul 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2017.0.0-alt1
- 2017.0.0

* Wed Feb 01 2017 Yuri N. Sedunov <aris@altlinux.org> 2016.2.0-alt2
- rebuilt with boost-1.63

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 2016.2.0-alt1
- 2016.2.0

* Mon Apr 18 2016 Yuri N. Sedunov <aris@altlinux.org> 2016.0.0-alt1
- 2016.0.0

* Sat Aug 08 2015 Yuri N. Sedunov <aris@altlinux.org> 2015.0.0-alt1
- 2015.0.0 release

* Sat Aug 01 2015 Yuri N. Sedunov <aris@altlinux.org> 2015.0.0-alt0.2
- 2015.0.0 rc3

* Mon Jul 13 2015 Yuri N. Sedunov <aris@altlinux.org> 2015.0.0-alt0.1
- 2015.0.0 rc2
- removed obsolete patches
- updated buildreqs
- spec cleanup

* Wed Jun 17 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2013.0.0-alt3.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Dec 10 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2013.0.0-alt3
- rebuild with libexiv2

* Mon Oct 28 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2013.0.0-alt2
- 2013.0.0 release

* Wed Sep 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2013.0.0-alt1.rc2
- 2013.0.0 rc2

* Fri Mar 22 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2012.0.0-alt2.4
- build fixed

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.0.0-alt2.3
- Rebuilt with Boost 1.53.0

* Mon Jan 28 2013 Yuri N. Sedunov <aris@altlinux.org> 2012.0.0-alt2.2
- rebuilt against libexiv2.so.12

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.0.0-alt2.1
- Rebuilt with Boost 1.52.0

* Tue Nov 06 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2012.0.0-alt2
- 2012.0.0

* Fri Sep 21 2012 Repocop Q. A. Robot <repocop@altlinux.org> 2012.0.0-alt1rc1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for hugin

* Fri Aug 31 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2012.0.0-alt1rc1
- 2012.0.0.rc1

* Wed Dec 21 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2011.4.0-alt1
- 2011.4.0

* Tue Dec 06 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2011.2.0-alt1.1
- rebuild with boost 1.48

* Wed Nov 02 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2011.2.0-alt1
- 2011.2.0

* Fri Sep 23 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2011.0.0-alt2
- requires: make added

* Wed Jun 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2011.0.0-alt1
- 2011.0.0

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2010.4.0-alt1.2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for hugin

* Sat Mar 26 2011 Ivan A. Melnikov <iv@altlinux.org> 2010.4.0-alt1.2
- rebuild with boost 1.46.1
- updated boost and xorg build-requires

* Wed Feb 09 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2010.4.0-alt1.1
- build fixed

* Thu Jan 13 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2010.4.0-alt1
- 2010.4.0

* Wed Dec 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2010.2.0-alt1.1
- rebuild with boost 1.45
- icon in desktop file fixed

* Tue Oct 12 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2010.2.0-alt1
- new upstream version
- (closes: #23822)

* Tue Jun 08 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2010.0.0-alt1.1
- Rebult with 0.20-alt1

* Wed Jun 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2010.0.0-alt1
- new upstream version

* Mon Jan 11 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2009.4.0-alt2
- Rebuit with exiv2-0.19

* Fri Dec 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2009.4.0-alt1
- new upstream version

* Mon Nov 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2009.2.0-alt1.1
- rebuild with libpano13

* Thu Oct 15 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2009.2.0-alt1
- new upstream version

* Tue Aug 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.0-alt2.2
- rebuild with wxGTK-2:2.8.10-alt2 (see 20451)

* Thu Jul 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.0-alt2.1
- rebuild with exiv2-0.18.2 

* Wed Jul 22 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.0-alt2
- 0.8.0 release (identical with rc5)
- requirement to exiftool added ( closes: #20843 )

* Fri Jul 10 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.0-alt1.rc5
- rc5
- some unpackaged files added

* Tue Jun 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.0-alt1.rc3
- new version 
- wxGTK instead wxGTK2u

* Wed Jun 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt7
- build fixed 

* Thu Feb 26 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt6
- translated desktop file of batch stitcher 

* Fri Oct 10 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt5
- new version 

* Tue May 20 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt4.beta4
- added %_datadir/hugin/xrc to package

* Thu Apr 10 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt3.beta4
- fixed build 

* Tue Apr 08 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt2.1.beta4
- no real changes, fix conflict with tvb@ package 

* Tue Apr 08 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt2.beta4
- fixed build with new gettext-tools 

* Thu Jun 28 2007 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.0-alt1.beta4
- Fix build with new version of boost
- Add desktop file

* Wed Feb 14 2007 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.0-alt0.beta4
- New version

* Mon Sep 25 2006 Sergei Epiphanov <serpiph@altlinux.ru> 0.6.1-alt1
- New version
- Cleanup patches

* Fri May 19 2006 Sergei Epiphanov <serpiph@altlinux.ru> 0.6-alt0.0.cvs20060517
- Updating to CVS version
- Checking patches
- Checking dependencies

* Wed May 17 2006 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt11
- Fixing code for gcc4.1
- Adding unpackaged files

* Tue Mar 07 2006 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt10
- Cleanup spec

* Sat Feb 11 2006 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt9
- Removing stale require panorama-tools

* Wed Dec 28 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt8
- Correction of default settings for Linux

* Fri Dec 16 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt7
- First stable release of hugin at 11-12-2005

* Sat Dec 03 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt6.cvs20051203
- Updated to CVS version
- Compiled with wxGTK2u
- Added missed requires.

* Fri Sep 23 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt5.rc2
- Fixing build errors

* Fri Sep 23 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt4.rc2
- New RC.
- Some spec corrections.

* Fri Sep 09 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt3.rc1
- Adding menu entry for program

* Mon Sep 05 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt2.rc1
- Fixing for ALT Linux

* Tue Jul 26 2005 Sergei Epiphanov <serpiph@nikiet.ru> 0.5_rc1-alt1
-initial build
