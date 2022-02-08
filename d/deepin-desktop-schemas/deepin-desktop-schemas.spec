Name: deepin-desktop-schemas
Version: 5.10.2
Release: alt1
Summary: GSettings deepin desktop-wide schemas
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-desktop-schemas
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-desktop-schemas-5.9.16-default-value-for-timeout-lockscreen.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-golang
BuildRequires: python3
BuildRequires: glib2
BuildRequires: libgio
# BuildRequires: golang-deepin-go-lib-devel
# Requires: deepin-sound-theme
Requires: gnome-backgrounds
Requires: icon-theme-deepin
Requires: gtk-theme-deepin
Requires(post): dconf gsettings-desktop-schemas
Requires(postun): dconf gsettings-desktop-schemas

%description
%summary.

%prep
%setup
%patch -p1

sed -i 's|pkg.deepin.io/lib/|github.com/linuxdeepin/go-lib/|' \
    $(find ./ -type f -name '*.go')
sed -i 's|adwaita-lock.jpg|adwaita-night.jpg|' \
    schemas/wrap/com.deepin.wrap.gnome.desktop.screensaver.gschema.xml
# sed -i 's|python|python3|' Makefile tools/overrides.py
sed -i 's|uos-browser|chromium-browser|' \
    overrides/common/*/*.override \
    schemas/com.deepin.dde.dock.gschema.xml

%build
export GOPATH="%go_path:$(pwd)/vendor"
export SYSTYPE=Desktop
%make_build ARCH=%_arch

%install
%makeinstall_std
cp -a \
    %buildroot%_datadir/deepin-desktop-schemas/server-override \
    %buildroot%_datadir/glib-2.0/schemas/91_deepin_product.gschema.override

# force change the value of the "Lock screen after" variable
mkdir -p %buildroot%_sysconfdir/dconf/profile

cat > %buildroot%_sysconfdir/dconf/profile/user <<EOF
user-db:user
system-db:local
EOF

mkdir -p %buildroot%_sysconfdir/dconf/db/local.d

cat > %buildroot%_sysconfdir/dconf/db/local.d/01-deepin-disable-timeout-lockscreen <<EOF
[com/deepin/dde/power]
line-power-lock-delay=0
battery-lock-delay=0
EOF

%check
make test

%post
dconf update

%postun
dconf update

%files
%doc README.md
%doc LICENSE
%_datadir/glib-2.0/schemas/*
%_datadir/%name/
%exclude %_datadir/deepin-app-store/
%exclude %_datadir/deepin-appstore/
%_sysconfdir/dconf/profile/user
%_sysconfdir/dconf/db/local.d/01-deepin-disable-timeout-lockscreen

%changelog
* Mon Feb 07 2022 Leontiy Volodin <lvol@altlinux.org> 5.10.2-alt1
- New version (5.10.2).
- Built with internal golang submodules.

* Fri Aug 20 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.18-alt1
- New version (5.9.18).

* Fri Jul 30 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.16-alt2
- Fixed broken lockscreen after 15 minutes.

* Thu Jul 01 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.16-alt1
- New version (5.9.16).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.11-alt1
- New version (5.9.11) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.8-alt1
- New version (5.9.8) with rpmgs script.

* Fri Mar 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.5-alt1
- New version (5.9.5) with rpmgs script.

* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.44-alt1
- New version (5.8.44).

* Wed Dec 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.42-alt1
- New version (5.8.0.42) with rpmgs script.

* Tue Dec 01 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.32-alt1
- New version (5.8.0.32) with rpmgs script.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.20-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
