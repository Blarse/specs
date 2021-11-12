# SPDX-License-Identifier: GPL-2.0-only

Name: kernel-source-hinic
Version: 2.3.2.17
Release: alt2
Summary: Huawei(R) Intelligent Network Interface Card Driver
License: GPL-2.0-only
Group: Development/Kernel
Url: https://openeuler.org/en/
Vcs: https://github.com/openeuler-mirror/kernel.git
# Vcs: https://gitee.com/openeuler/kernel.git

Source0: %name-%version.tar
BuildArch: noarch
ExclusiveArch: x86_64 aarch64
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-un-def
BuildRequires: kernel-headers-modules-std-def

%description
%summary

%prep
%setup

%install
install -pDm0644 %_sourcedir/%name-%version.tar %kernel_srcdir/%name-%version.tar

%check
make -C /lib/modules/*-un-def-*/build  M=$PWD/drivers/net/ethernet/huawei/hinic -j
make -C /lib/modules/*-std-def-*/build M=$PWD/drivers/net/ethernet/huawei/hinic -j

%files
%kernel_src/%name-%version.tar

%changelog
* Fri Nov 12 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.3.2.17-alt2
- Compile for 5.15 kernel.

* Wed Mar 03 2021 Vitaly Chikunov <vt@altlinux.org> 2.3.2.17-alt1
- First import of 2.3.2.17 from openEuler kernel-4.19.
