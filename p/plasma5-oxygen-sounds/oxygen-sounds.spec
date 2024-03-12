%define rname oxygen-sounds

Name: plasma5-oxygen-sounds
Version: 5.27.11
Release: alt1
Epoch: 1
%K5init

Group: Graphical desktop/KDE
Summary: Oxygen sounds
Url: http://www.kde.org
License: GPL-2.0-or-later

BuildArch: noarch

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5

# Automatically added by buildreq on Tue Aug 30 2022 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libgpg-error libqt5-core libsasl2-3 libssl-devel libstdc++-devel python-modules python2-base python3 python3-base python3-dev python3-module-paste rpm-build-file rpm-build-python3 sh4 tzdata
BuildRequires: extra-cmake-modules qt5-base-devel

%description
%name provides encrypted vaults.

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


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data sounds

%files
%doc LICENSES/*
%_K5snd/*

%changelog
* Thu Mar 07 2024 Sergey V Turchin <zerg@altlinux.org> 1:5.27.11-alt1
- new version

* Thu Dec 07 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.10-alt1
- new version

* Thu Nov 02 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.9-alt2
- dont force alternate placement

* Thu Oct 26 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.9-alt1
- new version

* Tue Sep 12 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.8-alt1
- new version

* Tue Aug 01 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.7-alt1
- new version

* Wed Jul 05 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.6-alt1
- new version

* Wed May 10 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.5-alt1
- new version

* Thu Apr 06 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.4-alt1
- new version

* Thu Mar 16 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.3-alt1
- new version

* Tue Feb 28 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.27.2-alt1
- new version

* Mon Jan 09 2023 Sergey V Turchin <zerg@altlinux.org> 1:5.26.5-alt1
- new version

* Tue Nov 29 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.4-alt1
- new version

* Thu Nov 10 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.3-alt2
- fix internal version

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.3-alt1
- new version

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.2-alt1
- new version

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.5-alt1
- new version

* Tue Aug 30 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.4-alt1
- initial build
