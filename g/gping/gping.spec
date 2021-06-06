Name: gping
Version: 1.2.1
Release: alt1
Summary: Ping, but with a graph
License: MIT
Group: Networking/Other
Url: https://github.com/orf/gping
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildRequires: rust-cargo
BuildRequires: /proc

%description
%summary.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --offline --release

%install
mkdir -p %buildroot%_bindir
install -m 0755 target/release/%name %buildroot%_bindir

%files
%_bindir/%name
%doc readme.md LICENSE

%changelog
* Sun Jun 06 2021 Alexander Makeenkov <amakeenk@altlinux.org> 1.2.1-alt1
 - Initial build for ALT

