Provides: cmake(Fcitx5Core)
Provides: cmake(Fcitx5Utils)

%define _libexecdir %_prefix/libexec
Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-alternatives rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/Xvfb /usr/bin/desktop-file-install /usr/bin/doxygen /usr/bin/gettext /usr/bin/wayland-scanner libxcbutil-devel pkgconfig(dbus-1) pkgconfig(enchant-2) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(libevent_core)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name fcitx5
%define autorelease 0

%global _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/fcitx5.conf
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

Name:           fcitx5
Version:        5.0.19
Release:        alt2_%autorelease
Summary:        Next generation of fcitx
License:        LGPLv2+
URL:            https://github.com/fcitx/fcitx5
Source:         https://download.fcitx-im.org/fcitx5/fcitx5/fcitx5-%{version}_dict.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/fcitx5/fcitx5-%{version}_dict.tar.xz.sig
# Checked by chatting, this key is used to verify fcitx* tarballs
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9
Source3:        fcitx5-xinput
Source4:        fcitx5.sh

BuildRequires:  ctest cmake
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  gnupg2
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  rpm-macros-systemd
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cldr-emoji-annotation)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-imdkit)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  /usr/bin/appstream-util
Requires:       dbus
Requires:       %{name}-data = %{version}-%{release}
Requires:       setup

#Recommends:       (fcitx5-gtk if (gtk2 or gtk3 or gtk4))
#Recommends:       (fcitx5-qt if (qt5-qtbase or qt6-qtbase))
#Recommends:       (fcitx5-qt-module if (qt5-qtbase or qt6-qtbase))
##bootstrap##Requires:       fcitx5-configtool
Source44: import.info

%description
Fcitx 5 is a generic input method framework released under LGPL-2.1+.

%package data
Group: Graphical desktop/Other
Summary:        Data files of Fcitx5
BuildArch:      noarch
# require with isa will lead to problem on koji build
Requires:       %{name} = %{version}-%{release}
Requires:       icon-theme-hicolor
Requires:       dbus

%description data
The %{name}-data package provides shared data for Fcitx5.

%package devel
Group: Graphical desktop/Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files necessary for
developing programs using Fcitx5 libraries.

%package autostart
Group: Graphical desktop/Other
Summary:        This package will make fcitx5 start with your GUI session
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description autostart
This package will setup autostart and environment needed for fcitx5 to work properly.

%prep
%setup -q

sed -i '1s,env bash,env bash4,' data/fcitx5-diagnose.sh

%build
%{fedora_v2_cmake} -GNinja
%fedora_v2_cmake_build 

%install
%fedora_v2_cmake_install
install -pm 644 -D %{S:3} %{buildroot}%{_xinputconf}
install -pm 644 -D %{S:4} %{buildroot}%{_sysconfdir}/profile.d/fcitx5.sh
install -d                %{buildroot}%{_datadir}/%{name}/inputmethod
install -d                %{buildroot}%{_datadir}/%{name}/table
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-configtool.desktop
 
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/org.fcitx.Fcitx5.desktop
  
# convert symlinked icons to copied icons, this will help co-existing with
# fcitx4
for iconfile in $(find %{buildroot}%{_datadir}/icons -type l)
do
  origicon=$(readlink -f ${iconfile})
  rm -f ${iconfile}
  cp ${origicon} ${iconfile}
done 
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xinputrc_fcitx5<<EOF
%{_sysconfdir}/X11/xinit/xinputrc	%{_xinputconf}	56
EOF

%check
#fedora_v2_ctest

%files -f %{name}.lang
%_altdir/xinputrc_fcitx5
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%config %{_xinputconf}
%{_bindir}/%{name}
%{_bindir}/%{name}-configtool
%{_bindir}/%{name}-remote
%{_bindir}/%{name}-diagnose
%{_libdir}/%{name}/
%{_libdir}/libFcitx5*.so.*.*
%{_libdir}/libFcitx5Config.so.6
%{_libdir}/libFcitx5Core.so.7
%{_libdir}/libFcitx5Utils.so.2
%{_libexecdir}/fcitx5-wayland-launcher

%files devel
%{_includedir}/Fcitx5/
%{_libdir}/cmake/Fcitx5*
%{_libdir}/libFcitx5*.so
%{_libdir}/pkgconfig/Fcitx5*.pc


%files data
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.fcitx.Fcitx5.service
%{_datadir}/applications/org.fcitx.Fcitx5.desktop
%{_metainfodir}/org.fcitx.Fcitx5.metainfo.xml
%{_datadir}/applications/%{name}-configtool.desktop
%{_datadir}/icons/hicolor/*/apps/*

%files autostart
%config %{_sysconfdir}/xdg/autostart/org.fcitx.Fcitx5.desktop
%config %{_sysconfdir}/profile.d/fcitx5.sh

%changelog
* Tue Sep 20 2022 Igor Vlasenko <viy@altlinux.org> 5.0.19-alt2_0
- bootstrap; added cmake provides

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.19-alt1_0
- bootstrap build w/o configtool

