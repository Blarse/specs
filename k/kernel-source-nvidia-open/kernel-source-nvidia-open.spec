# -*- rpm-spec -*-
%define module_name	nvidia-open
%define module_version  535.86.05

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: alt1
Provides: kernel-source-%module_name-%module_version
Summary: NVIDIA Linux open GPU kernel module source
License: MIT/GPLv2
Group: Development/Kernel
Url: https://github.com/NVIDIA/open-gpu-kernel-modules
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%version.tar

BuildPreReq: kernel-build-tools
BuildArch: noarch

%description
NVIDIA Linux open GPU kernel module source.

%prep
%setup -c -q

%install
mkdir -p %kernel_srcdir
tar jcf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Wed Jul 19 2023 L.A. Kostis <lakostis@altlinux.ru> 535.86.05-alt1
- 535.86.05.

* Sat Jul 01 2023 L.A. Kostis <lakostis@altlinux.ru> 535.54.03-alt1
- 535.54.03.

* Wed May 31 2023 L.A. Kostis <lakostis@altlinux.ru> 535.43.02-alt1
- 535.43.02.

* Thu Mar 23 2023 L.A. Kostis <lakostis@altlinux.ru> 530.41.03-alt1
- 530.41.03.

* Thu Mar 02 2023 L.A. Kostis <lakostis@altlinux.ru> 530.30.02-alt1
- 530.30.02.

* Fri Feb 10 2023 L.A. Kostis <lakostis@altlinux.ru> 525.89.02-alt1
- 525.89.02.

* Sun Jan 22 2023 L.A. Kostis <lakostis@altlinux.ru> 525.85.05-alt1
- 525.85.05.

* Fri Jan 06 2023 L.A. Kostis <lakostis@altlinux.ru> 525.78.01-alt1
- 525.78.01.

* Fri Dec 23 2022 L.A. Kostis <lakostis@altlinux.ru> 525.60.13-alt1
- 525.60.13.

* Thu Dec 01 2022 L.A. Kostis <lakostis@altlinux.ru> 525.60.11-alt1
- 525.60.11.

* Fri Nov 11 2022 L.A. Kostis <lakostis@altlinux.ru> 525.53-alt1
- 525.53.

* Tue Nov 01 2022 L.A. Kostis <lakostis@altlinux.ru> 520.56.06-alt1
- Initial build for ALTLinux.

