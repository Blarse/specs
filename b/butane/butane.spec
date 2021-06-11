
%global import_path github.com/coreos/butane

Name: butane
Version: 0.12.1
Release: alt1

Summary: Butane translates human readable Butane YAML Configs into machine readable Ignition JSON Configs
License: Apache-2.0
Group: System/Configuration/Boot and Init

URL: https://github.com/coreos/butane/blob/main/docs/getting-started.md
Source: %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Butane translates human-readable Butane Configs into machine-readable Ignition
configs for provisioning operating systems that use Ignition.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GO111MODULE=on
export GOFLAGS=-mod=vendor
export CGO_ENABLED=0
export version=v%version
export LDFLAGS="-X %import_path/internal/version.Raw=$version"

%golang_prepare
pushd $BUILDDIR/src/%import_path
%gobuild -o ./bin/butane internal/main.go
popd

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

pushd $BUILDDIR/src/%import_path
install -p -D -m 0755 ./bin/butane %buildroot%_bindir/butane
popd
ln -s butane %buildroot%_bindir/fcct


%files
%doc README.md NEWS docs
%_bindir/*

%changelog
* Fri Jun 11 2021 Alexey Shabalin <shaba@altlinux.org> 0.12.1-alt1
- 0.12.1

* Fri Jun 11 2021 Alexey Kostarev <kaf@altlinux.org> 0.12.0-alt1
- v0.12.0

