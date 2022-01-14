# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: git-delta
Version: 0.11.3
Release: alt1
Summary: A syntax-highlighting pager for git, diff, and grep output
Group: Development/Other
License: MIT
Url: https://github.com/dandavison/delta
Source: %name-%version.tar

BuildRequires: /proc
BuildRequires: rust-cargo
%{?!_without_check:%{?!_disable_check:BuildRequires: git-core}}

%description
Code evolves, and we all spend time studying diffs. Delta aims to make
this both efficient and enjoyable: it allows you to make extensive
changes to the layout and styling of diffs, as well as allowing you to
stay arbitrarily close to the default git/diff output.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Cdebuginfo=1"]
EOF

%build
cargo build %_smp_mflags --offline --release

%install
cargo install %_smp_mflags --offline --no-track --path .
install -Dpm0644 etc/completion/completion.bash \
		%buildroot%_datadir/bash-completion/completions/delta
install -Dpm0644 etc/completion/completion.zsh \
		%buildroot%_datadir/zsh/site-functions/_delta

%check
target/release/delta --version
cargo test %_smp_mflags --release --no-fail-fast

%files
%doc LICENSE README.md
%_bindir/delta
%_datadir/bash-completion/completions/delta
%_datadir/zsh/site-functions/_delta

%changelog
* Fri Jan 14 2022 Vitaly Chikunov <vt@altlinux.org> 0.11.3-alt1
- Imported 0.11.3-28-ge9bec95a (2022-01-14).
