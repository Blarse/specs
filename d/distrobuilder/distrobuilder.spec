%global import_path github.com/lxc/distrobuilder
Name:     distrobuilder
Version:  2.1
Release:  alt3

Summary:  System container image builder for LXC and LXD
License:  Apache-2.0
Group:    Other
Url:      https://github.com/lxc/distrobuilder

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

Patch1: unset-tmpdir-in-alt-ci-example.patch
Patch2: distrobuilder-2.1-gentoo-glibc-2.36-fix.patch
Patch3500: alt-x-sys-loongarch64.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Requires: squashfs-tools

%description
%summary

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3500 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build distrobuilder

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md doc

%changelog
* Wed May 08 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.1-alt3
- NMU: fixed FTBFS on LoongArch

* Fri Aug 25 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.1-alt2
- Fix rebuild

* Mon Nov 14 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.1-alt1
- new version 2.1

* Wed Jul 14 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.2-alt120.21dde21.2
- Add require to squashfs-tools
- Fix alt package manager to clean properly

* Fri Jul 09 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.2-alt120.21dde21.1
- update

* Sun Jun 02 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.0.0.0.1-alt0.428.06a6a8e.1
- Initial build for Sisyphus
