# spec file for package ripasso
#

# Not usable yet - 20210706
%def_without  gtk
# Not even buildable yet - 202010706
%def_without  qml

Name: ripasso
Version: 0.5.0
Release: alt1

Summary: a simple password manager written in Rust
Summary(ru_RU.UTF-8): простой парольный менеджер, написанный на Rust

License: %gpl3only
Group: Text tools
Url: https://github.com/cortex/ripasso

Packager: Nikolay A. Fetisov <naf@altlinux.org>


Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source1: vendor.tar
Source2: config.toml

Source10: ripasso.sh

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Sat Jul 03 2021
# optimized out: at-spi2-atk ca-trust fontconfig glib2-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgpg-error-devel libharfbuzz-devel libpango-devel libsasl2-3 libwayland-client libwayland-cursor libwayland-egl libxcb-devel llvm11.0-libs pkg-config python-modules python2-base python3 python3-base python3-module-paste ruby ruby-stdlibs rust sh4 zlib-devel
BuildRequires: libgpgme-devel libssl-devel libxcb-devel zlib-devel

BuildRequires: rust-cargo
BuildRequires: /proc


%description
Ripasso is a simple password manager written in Rust.

The root crate ripasso is a library for accessing and
decrypting passwords stored in pass format (GPG-encrypted files),
with a file-watcher event emitter.

Multiple UI's in different stages of development are available
in subcrates.

%description -l ru_RU.UTF-8
Ripasso - простой менеджер паролей, написанный на Rust.



%prep
%setup
%patch0 -p1

# Rust packages, update them before new build!
tar xf %SOURCE1
install -Dm664 -- %SOURCE2 .cargo/config


%build
export CARGO_HOME=`pwd`/cargo
cargo build --release --offline

for d in cursive %{?_with_gtk:gkt} %{?_with_qml:qml}; do
   pushd $d
     cargo build --release --offline
   popd
done

%install
# Binary files:
mkdir -p -- %buildroot%_bindir
for d in cursive %{?_with_gtk:gkt} %{?_with_qml:qml}; do
   cp -a -- target/release/ripasso-$d %buildroot%_bindir/
done

# Wrapper script
install -m 0755 -- %SOURCE10  %buildroot%_bindir/ripasso

# Man pages:
mkdir -p -- %buildroot%_mandir/man1/

cp -a -- target/man-page/cursive/ripasso-cursive.1 %buildroot%_mandir/man1/

# Translations:
mkdir -p -- %buildroot%_datadir/%name
cp -a -- target/translations/*  %buildroot%_datadir/%name/

%files
%doc LICENCE README.md

%_bindir/%{name}*
%_man1dir/%{name}*
%_datadir/%name


%changelog
* Wed Jul 07 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.5.0-alt1
- Initial build for ALT Linux Sisyphus
