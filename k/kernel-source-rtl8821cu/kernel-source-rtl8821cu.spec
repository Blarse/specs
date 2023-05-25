%define module_name rtl8821cu
%define git_rev e49409f

Name: kernel-source-%module_name
Version: 5.12.0.4
Release: alt1.git%git_rev

Summary: Realtek RTL8811CU/RTL8821CU USB wifi adapter driver
Group: Development/Kernel
License: GPL-2.0
URL: https://github.com/morrownr/8821cu-20210916

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kernel

%description
%{summary}.

%prep
%setup -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Thu May 25 2023 Andrey Cherepanov <cas@altlinux.org> 5.12.0.4-alt1.gite49409f
- New version from https://github.com/morrownr/8821cu-20210916.

* Fri Apr 22 2022 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt6.git8c2226a
- Fixed build for kernel 5.17.

* Mon Mar 21 2022 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt5.gitef3ff12
- Fix source tag for kernel 5.15 support.

* Fri Jan 28 2022 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt4.gitef3ff12
- Upstream support of kernel 5.15.

* Mon May 24 2021 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt3.gitf1bc7e8
- Upstream support of kernel 5.12.

* Tue Jan 12 2021 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt2.gitdeff094
- Upstream support of kernel 5.10.

* Fri Oct 30 2020 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt1.git45a8b43
- Initial build for Sisyphus.
