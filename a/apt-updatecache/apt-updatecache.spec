Name:    apt-updatecache
Version: 1.1
Release: alt1

Summary: Service for update APT cache on boot and every 4 hours
License: GPL-3.0+ 
Group:   System/Configuration/Packaging
URL:     http://altlinux.org/apt-updatecache

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
Service for update APT cache on boot and every 4 hours.

%prep
%setup

%install
install -pD -m644 %name.service %buildroot%systemd_unitdir/%name.service
install -pD -m644 %name.timer %buildroot%systemd_unitdir/%name.timer

%preun
%preun_service %name

%post
%post_service %name

%files
%config(noreplace) %systemd_unitdir/*

%changelog
* Thu Jul 08 2021 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Add [Install] section in service file.

* Thu Jul 08 2021 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
