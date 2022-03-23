%def_disable clang

Name: deepin-editor
Version: 5.10.18
Release: alt1
Summary: Simple editor for Linux Deepin
License: GPL-3.0+
Group: Editors
Url: https://github.com/linuxdeepin/deepin-editor

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-editor-5.10.18-gcc11.patch

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja desktop-file-utils
BuildRequires: cmake
BuildRequires: libfreeimage-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-syntax-highlighting-devel
BuildRequires: dtk5-widget-devel
BuildRequires: libexif-devel
BuildRequires: libexif-devel
BuildRequires: libxcbutil-devel
BuildRequires: libXtst-devel
BuildRequires: libpolkitqt5-qt5-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-linguist
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: libgtest-devel
BuildRequires: libgmock-devel
BuildRequires: dtk5-common
BuildRequires: libuchardet-devel
BuildRequires: libenca-devel
BuildRequires: libchardet-devel
# Requires: deepin-session-shell deepin-qt5integration

%description
%summary.

%prep
%setup
%if_disabled clang
%patch -p1
%endif
sed -i 's|lrelease|lrelease-qt5|; s|lupdate|lupdate-qt5|' translate_generation.sh
# use system libuchardet.a
# sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../3rdparty/lib/lib/libuchardet.a|%%_libdir/libuchardet.a|' \
# 	src/CMakeLists.txt \
# 	tests/CMakeLists.txt

%build
%if_enabled clang
%define optflags_lto -flto=thin
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
%cmake \
    -GNinja \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DCMAKE_BUILD_TYPE=Release \
    -DAPP_VERSION=%version \
    -DVERSION=%version \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
%if_enabled clang
    -DLLVM_PARALLEL_LINK_JOBS=1 \
    -DLLVM_TARGETS_TO_BUILD="all" \
    -DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD='AVR' \
    -DLLVM_ENABLE_LIBCXX:BOOL=OFF \
    -DLLVM_ENABLE_ZLIB:BOOL=ON \
%endif
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang %name

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files -f %name.lang
%doc README.md LICENSE
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/editor/

%changelog
* Fri Mar 18 2022 Leontiy Volodin <lvol@altlinux.org> 5.10.18-alt1
- New version (5.10.18).

* Mon Oct 04 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.14-alt1
- New version (5.9.14).

* Fri Aug 27 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.11-alt1
- New version (5.9.11).
- Checkout from euler into dev branch.

* Wed Jun 30 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.7-alt1
- New version (5.9.7).

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.0.49-alt1
- New version (5.9.0.49) with rpmgs script.

* Fri Mar 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.0.32-alt1
- New version (5.9.0.32) with rpmgs script.

* Wed Dec 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.9.0.16-alt1
- New version (5.9.0.16) with rpmgs script.

* Tue Dec 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.9.0.12-alt1
- New version (5.9.0.12) with rpmgs script.

* Tue Nov 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.9.0.11-alt1
- New version (5.9.0.11) with rpmgs script.

* Fri Oct 23 2020 Leontiy Volodin <lvol@altlinux.org> 5.9.0.6-alt1
- New version (5.9.0.6) with rpmgs script.

* Thu Oct 22 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.37-alt1
- New version (5.6.37) with rpmgs script.

* Fri Oct 16 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.36-alt1
- New version (5.6.36) with rpmgs script.
- Added new BR.

* Tue Aug 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.28-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
