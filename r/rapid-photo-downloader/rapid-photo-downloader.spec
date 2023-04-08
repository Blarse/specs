Name: rapid-photo-downloader
Version: 0.9.34
Release: alt1.1

%define xdg_name net.damonlynch.rapid_photo_downloader

Summary: Download photos and videos from cameras, memory cards and Portable Storage Devices
License: GPLv3+
Group: Graphics

Url: http://www.damonlynch.net/rapid/
Source: http://launchpad.net/rapid/pyqt/%version/+download/%name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-gir rpm-build-python3
BuildRequires: intltool perl-podlators
BuildRequires: python3-devel python3-module-setuptools

%if "%(rpmvercmp '%{get_version python3}' '3.6.0')" <= "0"
Requires: python3-module-typing >= 3.6.4
%endif

Requires: python3-module-PyQt5 >= 5.15.6 libqt5-svg
Requires: python3-module-zmq >= 16.0.2
Requires: python3-module-easygui >= 0.98.1
Requires: python3-module-pymediainfo >= 2.2.0
Requires: python3-module-pyprind
Requires: python3-module-colorlog
Requires: gphoto2 exiv2 perl-Image-ExifTool >= 10.87
Requires: gst-plugins-good1.0 gst-libav
# since 0.9.27
Requires: showinfilemanager >= 1.1.2
Requires: libimobiledevice ifuse fuse

%add_typelib_req_skiplist typelib(Unity)

%description
Rapid Photo Downloader imports photos and videos from cameras, phones,
memory cards and other devices at high speed. It can be configured to
rename photos and videos with meaningful filenames you specify. It can
also back up photos and videos as they are downloaded. It downloads from
and backs up to multiple devices simultaneously.

%prep
%setup
sed -i "s|'share\/solid\/actions'|'share/apps/solid/actions'|
        s|\(>=3.6\)\.\*|\1|" setup.py

%build
%python3_build

%install
%python3_install
# install translations
mkdir -p %buildroot%_datadir/locale
cp -r build/mo/* %buildroot%_datadir/locale
%find_lang %name

%files -f %name.lang
%_bindir/%name
%python3_sitelibdir/*
%_desktopdir/%xdg_name.desktop
%_datadir/metainfo/%xdg_name.metainfo.xml
%_man1dir/%name.1.*
%_datadir/solid/actions/%xdg_name.desktop
%doc README* RELEASE_NOTES* CHANGES*

%changelog
* Sat Apr 08 2023 Yuri N. Sedunov <aris@altlinux.org> 0.9.34-alt1.1
- fixed build with newer setuptools

* Sat Nov 12 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.34-alt1
- 0.9.34

* Sat Mar 12 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.33-alt1
- 0.9.33

* Tue Dec 28 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.28-alt1
- 0.9.28

* Tue Dec 14 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.27-alt1
- 0.9.27

* Fri Dec 25 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.26-alt1
- 0.9.26

* Mon Dec 21 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.25-alt1
- 0.9.25

* Sun May 10 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.24-alt1
- 0.9.24

* Mon Apr 20 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.23-alt1
- 0.9.23

* Sun Apr 12 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.22-alt1
- 0.9.22

* Mon Mar 23 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.20-alt1
- 0.9.20

* Thu Mar 19 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.19-alt1
- 0.9.19

* Thu Jan 23 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.18-alt1
- 0.9.18

* Wed Aug 21 2019 Yuri N. Sedunov <aris@altlinux.org> 0.9.17-alt1
- 0.9.17

* Mon Aug 12 2019 Yuri N. Sedunov <aris@altlinux.org> 0.9.16-alt1
- 0.9.16

* Sun Jul 14 2019 Yuri N. Sedunov <aris@altlinux.org> 0.9.15-alt1
- 0.9.15

* Sat Apr 06 2019 Yuri N. Sedunov <aris@altlinux.org> 0.9.14-alt1
- 0.9.14

* Sat Nov 24 2018 Yuri N. Sedunov <aris@altlinux.org> 0.9.13-alt1
- 0.9.13

* Tue Oct 09 2018 Yuri N. Sedunov <aris@altlinux.org> 0.9.12-alt1
- 0.9.12

* Wed Sep 19 2018 Yuri N. Sedunov <aris@altlinux.org> 0.9.11-alt1
- 0.9.11

* Mon Mar 26 2018 Yuri N. Sedunov <aris@altlinux.org> 0.9.9-alt1
- 0.9.9

* Tue Feb 27 2018 Yuri N. Sedunov <aris@altlinux.org> 0.9.8-alt1
- 0.9.8

* Thu Oct 30 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.10-alt1
- 0.4.10

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 0.4.1-alt1
- Initial build.
