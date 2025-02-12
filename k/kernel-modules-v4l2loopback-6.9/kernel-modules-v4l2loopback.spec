%define git %nil
%define module_name	v4l2loopback
%define module_version	0.13.2
%define module_release	alt1

%define flavour		6.9
%define karch %ix86 x86_64 aarch64 ppc64le armh
BuildRequires(pre): kernel-headers-modules-6.9
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: v4l2-loopback device
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
URL: https://github.com/umlaeute/v4l2loopback
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %EVR

PreReq: coreutils
PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
v4l2loopback kernel module.

This module allows you to create "virtual video devices". Normal (v4l2)
applications will read these devices as if they were ordinary video devices,
but the video will not be read from e.g. a capture card but instead it is
generated by another application. This allows you for instance to apply some
nifty video effects on your Skype video... It also allows some more serious
things (e.g. I've been using it to add streaming capabilities to an application
by the means of hooking GStreamer into the loopback devices).

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour M=`pwd` modules

%install
install -d %buildroot%module_dir
install v4l2loopback.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Wed Jun 5 2024 L.A. Kostis <lakostis@altlinux.org> 0.13.2-alt1
- 0.13.2.

* Thu Aug 3 2023 L.A. Kostis <lakostis@altlinux.org> 0.12.7-alt2.g9ba7e29
- GIT 9ba7e29.

* Wed Nov 2 2022 L.A. Kostis <lakostis@altlinux.org> 0.12.7-alt1.g5e9dd41
- GIT 5e9dd41.

* Fri Nov 26 2021 L.A. Kostis <lakostis@altlinux.org> 0.12.5-alt2
- Added -centos kernel arches.

* Sat Dec 5 2020 L.A. Kostis <lakostis@altlinux.org> 0.12.5-alt1
- Initial build for Sisyphus.
