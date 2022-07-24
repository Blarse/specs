%define _unpackaged_files_terminate_build 1

%global import_path github.com/yggdrasil-network/yggdrasil-go

Name: yggdrasil
Version: 0.4.4
Release: alt1

Summary: End-to-end encrypted IPv6 networking
License: LGPLv3
Group: Security/Networking
Url: https://yggdrasil-network.github.io

Source: %name-%version.tar
Patch0: go_mod_vendor.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
Yggdrasil is an overlay network implementation of a new routing scheme for mesh
networks. It is designed to be a future-proof decentralised alternative to the
structured routing protocols commonly used today on the Internet and other
networks.

The current implementation of Yggdrasil is a lightweight userspace software
router which is easy to configure and supported on a wide range of platforms.
It provides end-to-end encrypted IPv6 routing between all network participants.
Peerings between nodes can be configured using TCP/TLS connections over local
area networks, point-to-point links or the Internet. Even though the Yggdrasil
Network provides IPv6 routing between nodes, peering connections can be set up
over either IPv4 or IPv6.

%prep
%setup
%patch0 -p1

%build
export GO111MODULE=off
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

cp -r LICENSE README.md CHANGELOG.md contrib/systemd/* %_builddir/
%golang_prepare

cd .build/src/%import_path

# remove genkeys util
rm -rf cmd/genkeys

export PKGSRC="%import_path/src/version"
export PKGNAME="%name"
export PKGVER="%version-%release"
export LDFLAGS="-X $PKGSRC.buildName=$PKGNAME -X $PKGSRC.buildVersion=$PKGVER"
%golang_build cmd/*


%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

pushd %_builddir
    sed -i yggdrasil-default-config.service -e 's/\/usr\/bin\/chmod/\/bin\/chmod/g'
    install -pD yggdrasil.service %buildroot%_unitdir/yggdrasil.service
    install -pD yggdrasil-default-config.service %buildroot%_unitdir/yggdrasil-default-config.service
popd

%files
%doc LICENSE README.md CHANGELOG.md
%attr(0755,root,root) %_bindir/*
%attr(0644,root,root) %_unitdir/*

%pre
/usr/sbin/groupadd -r -f yggdrasil

%changelog
* Sun Jul 24 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4.4-alt1
- update to 0.4.4

* Tue Jun 07 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4.3-alt2
- change instructions for golang building
- add buildName and buildVersion to the output of `yggdrasil -version'

* Mon May 30 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4.3-alt1
- initial build for Sisyphus
