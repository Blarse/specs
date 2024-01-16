%define module_name rtl8812au
%define module_version 5.6.4.2
%define module_release alt2

%define flavour	std-def
%define karch %ix86 x86_64
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define _moduledir /lib/modules/%kversion-%flavour-%krelease

Name: kernel-modules-%module_name-%flavour
Group: System/Kernel and hardware
Summary: Module for Realtek RTL8812ce
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
Epoch: 1
Url: https://github.com/tomaspinho/rtl8821ce.git
License: GPLv2

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
ExclusiveArch: %ix86 x86_64

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

%description
These packages contain Realtek RTL8812au module.

%prep
rm -rf kernel-source-%module_name-%module_version
tar xvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build \
    ARCH=%base_arch \
    CROSS_COMPILE= \
    KSRC=%_usrsrc/linux-%kversion-%flavour \
    modules \
    USER_EXTRA_CFLAGS="-Wno-error=date-time -Wno-error=incompatible-pointer-types" \
    V=1

%install
install -D -m 644 88XXau.ko %buildroot%_moduledir/net/wireless/realtek/rtlwifi/%module_name.ko

%files
%dir %_moduledir/net
%dir %_moduledir/net/wireless
%dir %_moduledir/net/wireless/realtek
%dir %_moduledir/net/wireless/realtek/rtlwifi
%_moduledir/net/wireless/realtek/rtlwifi/*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %epoch:%version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
