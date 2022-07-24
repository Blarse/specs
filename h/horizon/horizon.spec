Name: horizon
Version: 2.2.0
Release: alt1

Summary: Horizon is a free EDA package
License: GPL-3.0
Group: Engineering
Url: https://github.com/horizon-eda/horizon

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Patch1: fix_build_without_glm.pc.patch
Patch2: disable-link-with-static-libs.patch

BuildRequires: gcc-c++ libgtkmm3-devel
BuildRequires: libsqlite3-devel
BuildRequires: libzip-devel
BuildRequires: libuuid-devel
BuildRequires: libepoxy-devel
BuildRequires: librsvg-devel
BuildRequires: libpodofo-devel
BuildRequires: libzeromq-cpp-devel
BuildRequires: libgit2-devel
BuildRequires: libcurl-devel
BuildRequires: libglm-devel
BuildRequires: boost-devel-headers
BuildRequires: opencascade-devel

%description
%summary

%prep
%setup
%autopatch -p1

%build
#configure
%make_build

%install
%makeinstall_std PREFIX=%prefix

%files
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*
%doc *.md

%changelog
* Fri Apr 15 2022 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- NMU: new version for opencascade-7.1.0

* Wed Dec 29 2021 Anton Midyukov <antohami@altlinux.org> 1.1.1-alt2
- fix build without glm.pc (thanks aris@)

* Mon May 03 2021 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1.1
- NMU: rebuild with opencascade-devel

* Tue May 12 2020 Anton Midyukov <antohami@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
