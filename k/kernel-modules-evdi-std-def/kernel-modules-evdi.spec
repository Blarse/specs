%define module_name	evdi
%define module_version	1.9.1
%define module_release	alt2

%define flavour		std-def
%define karch %ix86 x86_64 aarch64 ppc64le armh
BuildRequires(pre): kernel-headers-modules-std-def
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: DisplayLink kernel module
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
URL: https://github.com/DisplayLink/evdi
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %EVR

PreReq: coreutils
PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %ix86 x86_64

%description
Extensible Virtual Display Interface

The Extensible Virtual Display Interface (EVDI) is a Linux kernel module that
enables management of multiple screens, allowing user-space programs to take
control over what happens with the image. It is essentially a virtual display
you can add, remove and receive screen updates for, in an application that uses
the libevdi library.

%prep
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour M=`pwd` modules

%install
install -d %buildroot%module_dir
install evdi.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Nov 22 2021 L.A. Kostis <lakostis@altlinux.org> 1.9.1-alt2
- Add ExclusiveArch.

* Mon Nov 22 2021 L.A. Kostis <lakostis@altlinux.org> 1.9.1-alt1
- Initial build for Sisyphus.
