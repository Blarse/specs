%define _unpackaged_files_terminate_build 1

%global import_path github.com/neilalexander/yggmail

Name: yggmail
Version: 0.0.0
Release: alt1.git3becf52

Summary: End-to-end encrypted email for the mesh networking age
License: MPL-2.0
Group: Networking/Mail
Url: https://github.com/neilalexander/yggmail
Vcs: https://github.com/neilalexander/yggmail

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar

Requires: yggdrasil

BuildRequires(pre): rpm-build-golang

%description
It's email, but not as you know it.

Yggmail is a single-binary all-in-one mail transfer agent which sends
and receives email natively over the Yggdrasil Network.

* Yggmail runs just about anywhere you like - your inbox is stored
  right on your own machine;
* Implements IMAP and SMTP protocols for sending and receiving mail,
  so you can use your favourite client (hopefully);
* Mails are exchanged between Yggmail users using built-in Yggdrasil
  connectivity;
* All mail exchange traffic between any two Yggmail nodes is always
  end-to-end encrypted without exception;
* Yggdrasil and Yggmail nodes on the same network are discovered
  automatically using multicast or you can configure a static
  Yggdrasil peer.

Email addresses are based on your public key.

%prep
%setup -a1

%build
export GO111MODULE=off
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Thu Aug 03 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.0-alt1.git3becf52
- Built for ALT Sisyphus.

