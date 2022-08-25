Name: installer-feature-webterminal-setup
Version: 0.1.2
Release: alt1

Summary: Setup WEB-Terminal after install
License: GPL-2.0-or-later
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Source: %name-%version.tar

%description
Setup WEB-Terminal after system installation.

%prep
%setup

%build

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Thu Aug 25 2022 Sergey V Turchin <zerg@altlinux.org> 0.1.2-alt1
- update kiosk profile

* Thu Aug 25 2022 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt1
- fix paths

* Thu Aug 25 2022 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
