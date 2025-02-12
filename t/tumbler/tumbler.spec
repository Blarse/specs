%def_enable ffmpeg
%def_disable gstreamer
%def_enable gepub

Name: tumbler
Version: 4.19.1
Release: alt1

Summary: A thumbnail D-Bus service
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/XFce

Url: https://docs.xfce.org/xfce/tumbler/start
Packager: Xfce Team <xfce@packages.altlinux.org>

Requires: lib%name = %version-%release

Vcs: https://gitlab.xfce.org/xfce/tumbler.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4util-devel >= 4.17.1
BuildRequires: libfreetype-devel libgio-devel libgtk+2-devel libjpeg-devel libpng-devel
BuildRequires: libpoppler-glib-devel libgsf-devel libcurl-devel
%{?!_with_bootstrap:BuildRequires: libopenraw-gnome-devel}
%{?_enable_ffmpeg:BuildRequires: libffmpegthumbnailer-devel}
%{?_enable_gstreamer:BuildRequires: libgdk-pixbuf-devel gstreamer1.0-devel gst-plugins1.0-devel}
%{?_enable_gepub:BuildRequires: libgepub-devel libgdk-pixbuf-devel}
# NOTE: gtk-doc is required by build system even if docs are disabled.
BuildRequires: gtk-doc

%define _unpackaged_files_terminate_build 1

%description
Tumbler is a D-Bus service for applications to request
thumbnails for various URI schemes and MIME types.
It is an implementation of the thumbnail management D-Bus
specification

%package -n lib%name
Summary: A D-bus thumbnailing framweork
Group: System/Libraries
License: LGPLv2+

%description -n lib%name
Tumbler is a D-Bus service for applications to request
thumbnails for various URI schemes and MIME types

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
License: LGPLv2+
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files and headers for %name

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--libexecdir=%_prefix/libexec \
	%{?_disable_ffmpeg:--disable-ffmpeg-thumbnailer} \
	%{?_disable_gstreamer:--disable-gstreamer-thumbnailer} \
	%{?_disable_gepub:--disable-gepub-thumbnailer} \
	--disable-static \
	--disable-gtk-doc

%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS
%_sysconfdir/xdg/%name
%_prefix/libexec/%name-1
%_libdir/%name-1
%_datadir/dbus-1/services/*.service
%_user_unitdir/*.service
%_iconsdir/hicolor/*/apps/*

%exclude %_libdir/%name-1/plugins/*.la
%exclude %_libdir/%name-1/plugins/cache/*.la

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name-1
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu May 30 2024 Mikhail Efremov <sem@altlinux.org> 4.19.1-alt1
- Exlicitly disabled gtk-doc
- Use _user_unitdir macro
- Updated to 4.19.1.

* Thu Nov 30 2023 Mikhail Efremov <sem@altlinux.org> 4.18.2-alt1
- Updated to 4.18.2.

* Tue Apr 18 2023 Mikhail Efremov <sem@altlinux.org> 4.18.1-alt2
- Don't use _user_unitdir macro.

* Mon Apr 17 2023 Mikhail Efremov <sem@altlinux.org> 4.18.1-alt1
- Updated to 4.18.1.

* Thu Dec 15 2022 Mikhail Efremov <sem@altlinux.org> 4.18.0-alt1
- Updated to 4.18.0.

* Tue Nov 01 2022 Mikhail Efremov <sem@altlinux.org> 4.17.3-alt1
- Updated to 4.17.3.

* Fri Sep 02 2022 Mikhail Efremov <sem@altlinux.org> 4.17.2-alt2
- Fixed build gepub plugin with libgepub-7.

* Mon Jun 20 2022 Mikhail Efremov <sem@altlinux.org> 4.17.2-alt1
- Updated to 4.17.2.

* Tue Jun 14 2022 Mikhail Efremov <sem@altlinux.org> 4.17.1-alt1
- Updated to 4.17.1.

* Mon Jan 10 2022 Mikhail Efremov <sem@altlinux.org> 4.17.0-alt1
- tumblerd.service: Fixed path.
- Updated to 4.17.0.

* Wed Dec 23 2020 Mikhail Efremov <sem@altlinux.org> 4.16.0-alt1
- Updated to 4.16.0.

* Mon Nov 16 2020 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Updated Url tag.
- Enabled gepub plugin.
- Updated to 0.3.1.

* Thu Sep 03 2020 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Updated to 0.3.0.

* Wed Aug 12 2020 Mikhail Efremov <sem@altlinux.org> 0.2.9-alt1
- Added Vcs tag.
- Updated to 0.2.9.

* Mon Dec 23 2019 Mikhail Efremov <sem@altlinux.org> 0.2.8-alt1
- Don't use rpm-build-licenses.
- Updated to 0.2.8.

* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1
- Updated to 0.2.7.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 0.2.6-alt1
- Updated to 0.2.6.

* Sun Jun 30 2019 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1
- Updated to 0.2.5.

* Mon May 20 2019 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1
- Updated to 0.2.4.

* Thu Sep 13 2018 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- Updated to 0.2.3.

* Sun Sep 09 2018 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Updated to 0.2.2.

* Mon Apr 02 2018 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Updated to 0.2.1.

* Mon Jul 31 2017 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Drop obsoleted patch.
- Updated to 0.2.0.

* Thu Jul 27 2017 Michael Shigorin <mike@altlinux.org> 0.1.90-alt1.1
- BOOTSTRAP: avoid libopenraw for hefty BRs (boost).

* Tue May 16 2017 Mikhail Efremov <sem@altlinux.org> 0.1.90-alt1
- Updated to 0.1.90.

* Thu Jan 19 2017 Mikhail Efremov <sem@altlinux.org> 0.1.31-alt2
- Fix build with libopenraw-0.1.0.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 0.1.31-alt1
- Updated to 0.1.31.

* Mon Feb 24 2014 Mikhail Efremov <sem@altlinux.org> 0.1.30-alt1
- Fix Xfce name (XFCE -> Xfce).
- Updated to 0.1.30.

* Mon May 06 2013 Mikhail Efremov <sem@altlinux.org> 0.1.29-alt1
- Updated translations from upstream git.
- Updated to 0.1.29.

* Thu Jan 24 2013 Mikhail Efremov <sem@altlinux.org> 0.1.27-alt2
- libtumbler-devel: Added strict dependency on libtumbler
    (closes: #28456).
- Updated from upstream git (translations and minor build fixes).

* Sun Jan 13 2013 Mikhail Efremov <sem@altlinux.org> 0.1.27-alt1
- Updated to 0.1.27.
- Don't package tumbler-xdg-cache.la.

* Tue Dec 11 2012 Mikhail Efremov <sem@altlinux.org> 0.1.26-alt1
- Fix URL.
- FIx License.
- Build ODF and RAW thumbnailer plugins.
- Use %%xfce4reconf.
- Updated to 0.1.26 (closes: #28211).

* Wed Mar 09 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.1.21-alt1
- 0.1.21
- fixed path to tumblerd in dbus service files (closes: #25206)

* Mon Nov 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Thu Nov 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Tue Jan 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.1-alt1
- initial release

