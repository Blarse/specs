Name:    netplan
Version: 0.106
Release: alt2

Summary: Backend-agnostic network configuration in YAML
License: GPL-3.0
Group:   System/Configuration/Networking
URL:     https://github.com/CanonicalLtd/netplan

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  %_bindir/pandoc

Requires:       iproute2

%add_python3_path %_datadir/%name

Source:  %name-%version.tar

%description
%summary

%prep
%setup -n %name-%version

%build
%make_build

%install
%makeinstall_std DOCDIR=%_docdir/%name-%version LIBDIR=%_libdir
mkdir -p %buildroot%_sysconfdir/%name

%files
%_sbindir/%name
%_gen_dir/%name
/lib/%name
%_libdir/libnetplan.so.0.0
%_datadir/bash-completion/completions/%name
%_datadir/%name
%_datadir/dbus-1/system-services/io.netplan.Netplan.service
%_datadir/dbus-1/system.d/io.netplan.Netplan.conf
%dir %_sysconfdir/%name
%doc *.md
%_man5dir/%{name}*
%_man8dir/%{name}*

%changelog
* Tue Jul 02 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.106-alt2
- Fix rebuild using %%_gen_dir

* Mon Apr 24 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.106-alt1
- New version 0.106.

* Thu Jan 13 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.103-alt2
- Fix rebuild

* Mon Nov 08 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.103-alt1
- new version 0.103

* Thu Jan 14 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.101-alt1
- new version 0.101

* Thu Mar 19 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.98-alt1
- new version 0.98
- (ALT#37740) fix path to wpa_supplicant

* Thu Aug 15 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.97-alt2
- Remove Requires to systemd and systemd-networkd, it could use NetworkManager

* Fri Jul 26 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.97-alt1
- Initial build for Sisyphus
