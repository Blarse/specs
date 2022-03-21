%define _unpackaged_files_terminate_build 1

Name: spotify-tui
Version: 0.25.0
Release: alt1

Summary: Spotify for the terminal written in Rust
License: MIT
Group: Sound
Url: https://github.com/Rigellute/spotify-tui

Source0: %name-%version.tar
Source1: crates.tar
Patch0: %name-%version-alt.patch

BuildRequires: /proc
BuildRequires: python3
BuildRequires: libssl-devel
BuildRequires: libxcb-devel
BuildRequires: rust-cargo

%description
A Spotify client for the terminal written in Rust.

%prep
%setup -a1
%patch -p1

%build
export CARGO_HOME=${PWD}/.cargo
cargo build --release

%install
export CARGO_HOME=${PWD}/.cargo
cargo install --force --root %buildroot/%_usr --path ./ --no-track

%check
export CARGO_HOME=${PWD}/.cargo
cargo test --release

%files
%_bindir/spt

%changelog
* Sun Dec 12 2021 Ivan Alekseev <qwetwe@altlinux.org> 0.25.0-alt1
- Initial build
