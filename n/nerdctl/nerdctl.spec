%global import_path github.com/containerd/nerdctl
Name:     nerdctl
Version:  0.17.1
Release:  alt1

Summary:  contaiNERD CTL - Docker-compatible CLI for containerd
License:  Apache-2.0
Group:    System/Configuration/Other
Url:      https://github.com/containerd/nerdctl

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

Patch1:   wrap-selinuxenabled-to-wariable-to-skip-requires.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Requires: containerd cni-plugins iptables

%description
Docker-compatible CLI for containerd, with support for Compose, Rootless,
eStargz, OCIcrypt, IPFS.

To run rootless need package %name-rootless.

%package rootless
Summary: Use nerdctl rootless
Group: System/Configuration/Other
Requires: rootlesskit nerdctl

%description rootless
%summary

%prep
%setup
%patch1 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
export LDFLAGS="${LDFLAGS:-} -X github.com/containerd/nerdctl/pkg/version.Version=%version"
%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -m 0755 extras/rootless/containerd-rootless-setuptool.sh \
    %buildroot%_bindir/containerd-rootless-setuptool.sh
install -m 0755 extras/rootless/containerd-rootless.sh %buildroot%_bindir/containerd-rootless.sh


mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%name
mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files rootless
%exclude %_bindir/%name
%_bindir/*

%files
%_bindir/%name
%doc *.md
%doc docs
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Mon Mar 14 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.17.1-alt1
- new version 0.17.1

* Tue Mar 01 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Tue Feb 01 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.16.1-alt1
- Initial build for Sisyphus
