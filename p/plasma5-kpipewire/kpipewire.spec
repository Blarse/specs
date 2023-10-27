%ifndef _unitdir_user
%define _unitdir_user %prefix/lib/systemd/user
%endif

%define sover 5
%define libkpipewire libkpipewire%sover
%define libkpipewirerecord libkpipewirerecord%sover
%define libkpipewiredmabuf libkpipewiredmabuf%sover


%define rname kpipewire
Name: plasma5-%rname
Version: 5.27.9
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: Set of convenient classes to use PipeWire
Url: http://www.kde.org
License: LGPL-2.0-only AND LGPL-3.0-only

Source: %rname-%version.tar
Patch1: alt-format-buffer.patch

# Automatically added by buildreq on Mon Oct 31 2022 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libavcodec-devel libavutil-devel libcairo-gobject libctf-nobfd0 libgdk-pixbuf libglvnd-devel libgpg-error libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-waylandclient librabbitmq-c4 libsasl2-3 libssl-devel libstdc++-devel libwayland-client-devel libwayland-server libx265-199 perl pipewire-libs pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 rpm-build-qml rpm-macros-python sh4 tzdata wayland-devel
#BuildRequires: appstream clang-tools extra-cmake-modules kde5-plasma-wayland-protocols kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kwayland-devel libavformat-devel libdrm-devel libepoxy-devel libgbm-devel libswscale-devel lua5.3 pipewire-libs-devel python-modules-compiler python3-module-setuptools python3-module-zope qt5-imageformats qt5-svg-devel qt5-wayland-devel qt5-webengine-devel rpm-build-kf5 rpm-build-lua tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-wayland-devel rpm-build-qml
BuildRequires: extra-cmake-modules
BuildRequires: libavformat-devel libdrm-devel libepoxy-devel libgbm-devel libswscale-devel
BuildRequires: pipewire-libs-devel
BuildRequires: kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kwayland-devel
BuildRequires: kde5-plasma-wayland-protocols

%description
Offers a set of convenient classes to use PipeWire (https://pipewire.org/) in Qt projects.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: pipewire-libs-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkpipewirerecord
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpipewirerecord
%name library

%package -n %libkpipewire
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpipewire
%name library

%package -n %libkpipewiredmabuf
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpipewiredmabuf
%name library

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    -DBUILD_TESTING:BOOL=ON \
    #

%install
%K5install
%K5install_move data locale
%find_lang %name --all-name
%K5find_qtlang %name --append --all-name

%files
%_K5qml/org/kde/pipewire/

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories5/*.*categories

%files devel
%_K5inc/KPipeWire/
%_K5link/lib*.so
%_K5lib/cmake/KPipeWire/
#%_K5archdata/mkspecs/modules/qt_KPipeWire.pri
#%_pkgconfigdir/*.pc

%files -n %libkpipewire
%_K5lib/libKPipeWire.so.%sover
%_K5lib/libKPipeWire.so.*
%files -n %libkpipewirerecord
%_K5lib/libKPipeWireRecord.so.%sover
%_K5lib/libKPipeWireRecord.so.*
%files -n %libkpipewiredmabuf
%_K5lib/libKPipeWireDmaBuf.so.%sover
%_K5lib/libKPipeWireDmaBuf.so.*

%changelog
* Thu Oct 26 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.9-alt1
- new version

* Tue Sep 12 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.8-alt1
- new version

* Tue Aug 01 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.7-alt1
- new version

* Wed Jul 05 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.6-alt1
- new version

* Fri Jun 02 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.5-alt3
- update requires

* Thu May 25 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.5-alt2
- increase buffer for pipewire format negotiation

* Wed May 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.5-alt1
- new version

* Thu Apr 06 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.4-alt1
- new version

* Thu Mar 16 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.3-alt1
- new version

* Tue Feb 28 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.2-alt1
- new version

* Mon Jan 09 2023 Sergey V Turchin <zerg@altlinux.org> 5.26.5-alt1
- new version

* Tue Nov 29 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.4-alt1
- new version

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.3-alt1
- new version

* Mon Oct 31 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.2-alt1
- initial build
