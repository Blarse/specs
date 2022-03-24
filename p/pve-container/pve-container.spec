%define _unpackaged_files_terminate_build 1
%set_perl_req_method relaxed

Name: pve-container
Summary: Proxmox VE Container management tool
Version: 4.1.4
Release: alt1
License: AGPL-3.0+
Group: System/Servers
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/pve-container.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

Requires(pre,postun): shadow-submap
Requires: pve-lxc dtach pve-lxc-syscalld xz

BuildRequires: pve-common pve-guest-common pve-qemu-server pve-storage pve-firewall pve-cluster libpve-cluster-perl pve-doc-generator xmlto pve-lxc
BuildRequires: perl(Crypt/Eksblowfish/Bcrypt.pm) perl(UUID.pm)

%description
%summary.
Tool to manage Linux Containers on Proxmox VE.

%prep
%setup

%install
%makeinstall_std -C src
mkdir -p %buildroot%_sysctldir
mv %buildroot/usr/lib/sysctl.d/10-pve-ct-inotify-limits.conf %buildroot%_sysctldir/10-pve-ct-inotify-limits.conf
%post
%_sbindir/usermod --add-subgids 100000-165535 root ||:
%_sbindir/usermod --add-subuids 100000-165535 root ||:

%files
%_sysctldir/10-pve-ct-inotify-limits.conf
%_datadir/bash-completion/completions/*
%_datadir/zsh/vendor-completions/*
%_unitdir/*
%_sbindir/*
%_datadir/lxc
%perl_vendor_privlib/PVE/LXC
%perl_vendor_privlib/PVE/*.pm
%perl_vendor_privlib/PVE/API2/LXC
%perl_vendor_privlib/PVE/API2/*.pm
%perl_vendor_privlib/PVE/CLI/*.pm
%perl_vendor_privlib/PVE/VZDump/*.pm
%_man1dir/*
%_man5dir/*

%changelog
* Thu Mar 10 2022 Alexey Shabalin <shaba@altlinux.org> 4.1.4-alt1
- 4.1-4
- build as separate package

