%define name adriconf
%define build_type RelWithDebInfo
%define _cmake %cmake -DCMAKE_BUILD_TYPE=%build_type -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON
%define version 2.7.1
%define release alt1

Summary: Advanced Mesa DRI Configurator
Name: %name
Version: %version
Release: %release
License: GPL-3
Group: System/Configuration/Hardware
Url: https://gitlab.freedesktop.org/mesa/adriconf/
Packager: L.A. Kostis <lakostis@altlinux.org>

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): cmake

BuildRequires: cmake gcc-c++ libdrm-devel
BuildRequires: libgbm-devel libgtkmm4-devel libpci-devel libpugixml-devel libGL-devel libEGL-devel libatkmm2.36-devel

%description
adriconf (Advanced DRI CONFigurator) is a GUI tool used to configure open
source graphics drivers. It works by setting options and writing them to the
standard drirc file used by the Mesa drivers.

%prep
%setup -q
%patch -p1

%build
%_cmake \
 -DCMAKE_INSTALL_LIBDIR=%_libdir \
 -DENABLE_UNIT_TESTS=NO
%cmake_build
%cmakeinstall_std
%find_lang %{name}

mkdir -p %buildroot{%_datadir/metainfo,%_desktopdir,%_iconsdir}
install -m644 flatpak/org.freedesktop.%name.png %buildroot%{_iconsdir}/
install -m644 flatpak/org.freedesktop.%name.desktop %buildroot%{_desktopdir}/
install -m644 flatpak/org.freedesktop.%name.metainfo.xml %buildroot%{_datadir}/metainfo/

%files -f %{name}.lang
%doc LICENSE AUTHORS VERSION *.md
%_bindir/%name
%_datadir/metainfo/org.freedesktop.%name.metainfo.xml
%_desktopdir/*.desktop
%_iconsdir/*.png

%changelog
* Wed Sep 06 2023 L.A. Kostis <lakostis@altlinux.ru> 2.7.1-alt1
- 2.7.1.

* Sun Jun 25 2023 L.A. Kostis <lakostis@altlinux.ru> 2.7.0-alt2
- Apply fix to compile with gcc-13.

* Sun Apr 16 2023 L.A. Kostis <lakostis@altlinux.ru> 2.7.0-alt1
- 2.7.0.

* Thu Mar 23 2023 L.A. Kostis <lakostis@altlinux.ru> 2.6.0-alt1
- 2.6.0.
- BR: migrate to gtkmm4 + add libatkmm2.36.

* Sun Dec 25 2022 L.A. Kostis <lakostis@altlinux.ru> 2.5.1-alt1
- 2.5.1.
- Update BR.

* Mon May 23 2022 L.A. Kostis <lakostis@altlinux.ru> 2.5.0-alt1
- 2.5.0.

* Wed May 26 2021 L.A. Kostis <lakostis@altlinux.ru> 2.4.1-alt1
- Initial build for ALTLinux.
