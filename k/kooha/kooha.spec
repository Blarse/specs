Name: kooha
Version: 2.2.4
Release: alt1
Epoch: 1

Summary: Simple screen recorder with a minimal interface

License: GPL-3.0+
Group: Video
Url: https://github.com/SeaDve/Kooha

Source0: %url/archive/%version/Kooha-%version.tar.gz
Source1: vendor.tar

BuildPreReq: rpm-macros-meson rpm-build-rust
BuildRequires: /proc
BuildRequires: meson glib2-devel libgio-devel libgtk4-devel libadwaita-devel gstreamer1.0-devel gst-plugins1.0-devel libpulseaudio-devel /usr/bin/appstream-util

%description
%summary.

%prep
%setup -n Kooha-%version -a1
%autopatch -p1

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc COPYING README.md
%_bindir/%name
%_desktopdir/io.github.seadve.Kooha.desktop
%_datadir/glib-2.0/schemas/io.github.seadve.Kooha.gschema.xml
%_iconsdir/hicolor/scalable/apps/io.github.seadve.Kooha.svg
%_iconsdir/hicolor/symbolic/apps/io.github.seadve.Kooha-symbolic.svg
%dir %_datadir/%name/
%_datadir/%name/resources.gresource
%_datadir/metainfo/io.github.seadve.Kooha.metainfo.xml
%_datadir/locale/zh_Hans/LC_MESSAGES/%name.mo
%_datadir/locale/zh_Hant/LC_MESSAGES/%name.mo

%changelog
* Mon Sep 25 2023 Leontiy Volodin <lvol@altlinux.org> 1:2.2.4-alt1
- New version 2.2.4.

* Tue Dec 27 2022 Leontiy Volodin <lvol@altlinux.org> 1:2.2.3-alt1
- New version 2.2.3.

* Thu Dec 15 2022 Leontiy Volodin <lvol@altlinux.org> 1:2.1.1-alt1.1.git3a27e73
- Revert version 2.1.1.

* Fri Dec 09 2022 Leontiy Volodin <lvol@altlinux.org> 2.2.2-alt1
- Initial build for ALT Sisyphus.
