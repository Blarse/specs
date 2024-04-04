%define rname kimageannotator

%define sover 0
%define libkimageannotator libkimageannotator%sover

Name: kde5-%rname
Version: 0.7.1
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: Library and a tool for annotating images
Url: https://github.com/ksnip/kImageAnnotator
License: LGPL-3.0

Source: %rname-%version.tar
Patch1: alt-void-return.patch

# Automatically added by buildreq on Fri Feb 05 2021 (-bi)
# optimized out: cmake-modules elfutils fontconfig-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXmu-devel libXrender-devel libXt-devel libctf-nobfd0 libfreetype-devel libglvnd-devel libqt5-core libqt5-gui libqt5-svg libqt5-widgets libsasl2-3 libssl-devel libstdc++-devel libxcb-devel libxkbcommon-devel pkg-config python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel qt5-tools rpm-build-python3 sh4 xorg-proto-devel xorg-xf86miscproto-devel
#BuildRequires: cmake kde5-kcolorpicker-devel libXScrnSaver-devel libXaw-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxcbutil-devel libxcbutil-icccm-devel libxkbcommon-x11-devel libxkbfile-devel python3-dev python3-module-mpl_toolkits qt5-svg-devel qt5-tools-devel qt5-translations qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake
BuildRequires: qt5-svg-devel qt5-tools-devel qt5-translations qt5-wayland-devel
BuildRequires: kde5-kcolorpicker-devel

%description
%summary

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
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkimageannotator
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkimageannotator
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1


%build
%K5build \
    -DBUILD_WITH_QT6=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF \
    #

%install
%K5install
mkdir %buildroot/%_libdir/cmake/kImageAnnotator/
for f in %buildroot/%_libdir/cmake/kImageAnnotator-Qt?/* ; do
    ln -sr $f %buildroot/%_libdir/cmake/kImageAnnotator/
done
for f in %buildroot/%_libdir/cmake/kImageAnnotator/* ; do
    echo "$f" | grep -q '\-Qt[[:digit:]]' \
	&& ln -sr $f `echo "$f" | sed 's|\-Qt[[:digit:]]||'` \
	||:
done
%find_lang %name --all-name --with-qt

%files common -f %name.lang
%doc LICENSE* CHANGELOG.md README.md

%files devel
%_includedir//kImageAnnotator-Qt?/
%_libdir/cmake//kImageAnnotator/
%_libdir/cmake//kImageAnnotator-Qt?/
%_K5link/lib*.so

%files -n %libkimageannotator
%_K5lib/libkImageAnnotator.so.%sover
%_K5lib/libkImageAnnotator.so.*

%changelog
* Thu Apr 04 2024 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt1
- new version

* Tue Apr 25 2023 Sergey V Turchin <zerg@altlinux.org> 0.6.1-alt1
- new version

* Mon Aug 01 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 0.6.0-alt1
- NMU:
      + new version
      + remove BR unneded

* Wed Nov 24 2021 Sergey V Turchin <zerg@altlinux.org> 0.5.3-alt1
- new version

* Tue Oct 05 2021 Sergey V Turchin <zerg@altlinux.org> 0.5.2-alt1
- new version

* Wed May 12 2021 Sergey V Turchin <zerg@altlinux.org> 0.4.2-alt1
- new version

* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- initial build
