%define _unpackaged_files_terminate_build 1
%define appname id.waydro.Container

Name: waydroid
Version: 1.4.1
Release: alt1

Summary: Container-based approach to boot a full Android system on a regular GNU/Linux system
License: GPLv3+
Group: Emulators

Url: https://waydro.id/

# https://github.com/waydroid/waydroid/archive/refs/tags/<version>.tar.gz
Source: %name-%version.tar

BuildRequires: rpm-build-python3 python3-module-gbinder-python

BuildArch: noarch

# not strictly required but nice to have
Requires: python3-module-pyclip
# as waydroid uses lxc for containers
Requires: lxc

%add_python3_path %_libexecdir/%name
%add_python3_req_skip tools.interfaces

%description
Waydroid uses Linux namespaces (user, pid, uts, net, mount, ipc) to run a full
Android system in a container and provide Android applications on any
GNU/Linux-based platform.

The Android system inside the container has direct access to any needed
hardware.

%prep
%setup

%build

%install
make install DESTDIR=%buildroot USE_NFTABLES=1
rm -rf %buildroot%_libexecdir/systemd && mkdir -p %buildroot%_unitdir
install -m644 systemd/%name-container.service %buildroot%_unitdir/
mkdir -p %buildroot%_sysconfdir && touch %buildroot%_sysconfdir/gbinder.conf

%files
%ghost %attr(644,root,root) %config(missingok) %verify(not md5 mtime size) %_sysconfdir/gbinder.conf
%_unitdir/*.service
%_bindir/%name
%_libexecdir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/512x512/apps/%{name}.png
%_datadir/dbus-1/system-services/%{appname}.service
%_datadir/dbus-1/system.d/%{appname}.conf
%_datadir/metainfo/id.waydro.%{name}.metainfo.xml
%_datadir/polkit-1/actions/%{appname}.policy

%changelog
* Mon Apr 24 2023 L.A. Kostis <lakostis@altlinux.ru> 1.4.1-alt1
- 1.4.1.

* Thu Mar 30 2023 L.A. Kostis <lakostis@altlinux.ru> 1.4.0-alt1
- Initial build for ALTLinux.
