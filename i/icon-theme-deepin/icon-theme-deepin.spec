Name: icon-theme-deepin
Version: 2023.11.16
Release: alt1

Summary: Icons for the Deepin Desktop Environment

License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-icon-theme

Source: %url/archive/%version/deepin-icon-theme-%version.tar.gz

BuildArch: noarch

BuildRequires: python3-devel gtk-update-icon-cache xcursorgen

%description
%summary.

%prep
%setup -n icon-theme-deepin-%version

sed -i 's|python|python3|' Makefile
sed -i 's|/usr/bin/env python|/usr/bin/env python3|' \
	$(find ./ -name '*.py')

%build
%make -j1

%install
%makeinstall DESTDIR=%buildroot
cp -a ./Sea ./bloom-fantacy ./usr/share/icons/hicolor %buildroot%_iconsdir/

%files
%doc LICENSE
%_iconsdir/hicolor/*/status/*.svg
%_iconsdir/hicolor/*/apps/*.svg
%_iconsdir/bloom-classic-dark/
%_iconsdir/bloom-classic/
%_iconsdir/bloom-dark/
%_iconsdir/bloom-fantacy/
%_iconsdir/bloom/
%_iconsdir/Sea/
%_iconsdir/vintage/

%changelog
* Fri Nov 24 2023 Leontiy Volodin <lvol@altlinux.org> 2023.11.16-alt1
- New version 2023.11.16.

* Mon Apr 10 2023 Leontiy Volodin <lvol@altlinux.org> 2023.04.03-alt1
- New version 2023.04.03.

* Tue Mar 15 2022 Leontiy Volodin <lvol@altlinux.org> 2021.11.24-alt1
- New version (2021.11.24).
- Fixed missing icons (ALT #41363).

* Wed Nov 03 2021 Leontiy Volodin <lvol@altlinux.org> 2021.08.19-alt1
- New version (2021.08.19) with rpmgs script.
- Fixed installation error.

* Fri Oct 09 2020 Leontiy Volodin <lvol@altlinux.org> 2020.09.25-alt1
- New version (2020.09.25) with rpmgs script.

* Wed Aug 21 2019 Leontiy Volodin <lvol@altlinux.org> 15.12.71-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
