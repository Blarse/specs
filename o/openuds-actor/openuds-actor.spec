%add_python3_lib_path %_datadir/UDSActor
%allow_python3_import_path %_datadir/UDSActor
%define oname udsactor

Name: openuds-actor
Version: 3.6.0
Release: alt4
Summary: Actor for Universal Desktop Services (UDS) Broker
License: BSD-3-Clause
Group: Networking/Remote access
URL: https://github.com/dkmstr/openuds

Source0: %name-%version.tar
Source1: %oname.init
Source2: %oname.service
Source3: %oname.logrotate
Source4: %oname.cfg

BuildArch: noarch
BuildRequires(pre): rpm-build-xdg rpm-build-python3
Requires: realmd

%description
This package provides the required components
to allow this machine to work on an environment managed by UDS Broker.

%prep
%setup

sed -i 's|#!/usr/bin/env python3|#!/usr/bin/python3|' \
    $(find . -name '*.py')

%install
pushd linux
%make DESTDIR=%buildroot install-udsactor
popd

install -p -D -m 755 %SOURCE1 %buildroot%_initdir/%oname
install -p -D -m 644 %SOURCE2 %buildroot%_unitdir/%oname.service
install -p -D -m 644 %SOURCE3 %buildroot%_logrotatedir/%oname
install -p -D -m 600 %SOURCE4 %buildroot%_sysconfdir/%oname/%oname.cfg

%post
%post_service %oname

%preun
%preun_service %oname

%files
%dir %attr(0700, root, root) %_sysconfdir/%oname
%config(noreplace) %attr(0600, root, root) %_sysconfdir/%oname/*
%config(noreplace) %_logrotatedir/%oname
%_unitdir/%oname.service
%_initdir/%oname
%_xdgconfigdir/autostart/UDSActorTool.desktop
%_bindir/UDSActorTool-startup
%_bindir/%oname
%_bindir/udsvapp
%_bindir/UDSActorTool
%_sbindir/UDSActorConfig
%_sbindir/UDSActorConfig-pkexec
%_sbindir/UDSActorRegister
%_datadir/UDSActor
%exclude %_datadir/UDSActor/%oname/windows
%_desktopdir/UDS_Actor_Configuration.desktop
%_datadir/autostart/UDSActorTool.desktop
%_datadir/polkit-1/actions/org.openuds.pkexec.UDSActorConfig.policy

%changelog
* Mon Jul 01 2024 Alexander Burmatov <thatman@altlinux.org> 3.6.0-alt4
- Adding a script to register an actor on a server without a GUI (using the CLI).

* Fri Jun 30 2023 Alexander Burmatov <thatman@altlinux.org> 3.6.0-alt3
- Revert 4.0 changes.

* Thu Jun 29 2023 Alexander Burmatov <thatman@altlinux.org> 3.6.0-alt2
- Rollback 4.0 changes.

* Thu May 25 2023 Alexander Burmatov <thatman@altlinux.org> 3.6.0-alt1
- v3.6 snapshot 2c61de63781fa8072c5cfb8d8602ec6605969ea6

* Mon Aug 22 2022 Alexey Shabalin <shaba@altlinux.org> 3.5.0-alt1
- v3.5 snapshot 83394f0d34daf18722923be8d57b35627b330121

* Sat Aug 21 2021 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt2
- v3.0 snapshot 51b0cec5365698dffdb9a3a468d52bbba4656ba4

* Thu Nov 05 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- 3.0.0 Release

* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt0.1.git.d7e30d14
- Initial build for ALT

