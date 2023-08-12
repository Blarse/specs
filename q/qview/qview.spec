%define _unpackaged_files_terminate_build 1

Name: qview
Version: 6.0
Release: alt1
Summary: Practical and minimal image viewer
License: GPLv3
Group: Graphics
Url: https://github.com/jurplel/qView
Source: %name-%version.tar

BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: qt5-x11extras-devel

%description
qView is an image viewer designed with minimalism and usability in mind.

%prep
%setup
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -name '*.cpp' -o -name '*.h' -print0 |
	xargs -r0 sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
export PREFIX=/usr
qmake-qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot
# NB: it's not %%_licensedir
rm -rf %buildroot%_datadir/licenses/%name

%files
%_bindir/%name
%_desktopdir/com.interversehq.qView.desktop
%_datadir/metainfo/com.interversehq.qView.appdata.xml
%_iconsdir/hicolor/*x*/apps/com.interversehq.qView.png
%_iconsdir/hicolor/scalable/apps/com.interversehq.qView.svg
%_iconsdir/hicolor/symbolic/apps/com.interversehq.qView-symbolic.svg
%doc LICENSE

%changelog
* Fri Aug 11 2023 Alexander Makeenkov <amakeenk@altlinux.org> 6.0-alt1
- Updated to version 6.0.

* Sun Jan 23 2022 Alexander Makeenkov <amakeenk@altlinux.org> 5.0-alt1
- Updated to version 5.0

* Wed Jan 06 2021 Alexander Makeenkov <amakeenk@altlinux.org> 4.0-alt1
- Updated to version 4.0

* Thu Jan 23 2020 Alexander Makeenkov <amakeenk@altlinux.org> 3.0-alt1
- New version

* Thu Jun 20 2019 Michael Shigorin <mike@altlinux.org> 2.0-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24
- minor spec cleanup

* Mon May 27 2019 Alexander Makeenkov <amakeenk@altlinux.org> 2.0-alt1
- Initial build for ALT
