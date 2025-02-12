%define soname 5

%def_enable clang

Name: dtkdeclarative
Version: 5.6.26
Release: alt1
Summary: Widget development toolkit for Deepin
Summary(ru): Инструментарий по разработке виджетов для Deepin
License: LGPL-3.0+
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dtkdeclarative

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

%if_enabled clang
ExcludeArch: armh
%endif

Provides: dtk5-declarative = %EVR
Obsoletes: dtk5-declarative < %EVR

BuildRequires(pre): rpm-build-ninja rpm-macros-qt5
%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
#BuildRequires: doxygen graphviz qt5-base-doc
# Automatically added by buildreq on Fri Oct 20 2023
# optimized out: alt-os-release clang17.0 clang17.0-support cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libclang-cpp17 libdouble-conversion3 libdtkcore-devel libglvnd-devel libgpg-error libgsettings-qt libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libqt5-svg libqt5-widgets libqt5-xml libsasl2-3 libssl-devel libstdc++-devel llvm-common llvm17.0-libs pkg-config python3 python3-base qt5-base-devel qt5-declarative-devel qt5-tools sh5
BuildRequires: cmake libdtkgui-devel qt5-quickcontrols2-devel qt5-tools-devel

Requires: libqt5-qml = %_qt5_version libqt5-quick = %_qt5_version libqt5-quickcontrols2 = %_qt5_version

%description
dtkdeclarative is a widget development toolkit based on QtQuick/QtQml, which is
a brand new substitute for dtkwidget. dtkdeclarative is developed based on
qtdeclarative. It covers all existing QML widgets and adds plenty of DTK
friendly visual effects and color schemes. Compared to dtkwidget. It has:

- A primitive Qt and Qml code style.
- Adapted APIs with traditional Qml.
- Simple and quick development interfaces.
- Unified widget theme style.
- Abundant effects and colors.

%description -l ru
dtkdeclarative - это инструментарий для разработки виджетов, основанный на
QtQuick / QtQml, который является совершенно новым заменителем dtkwidget.
dtkdeclarative разрабатывается на основе qtdeclarative. Он охватывает все
существующие виджеты QML и добавляет множество дружественных DTK визуальных
эффектов и цветовых схем. По сравнению с дтквиджетом. Имеет:

- Примитивный стиль кода Qt и Qml.
- Адаптированные API с традиционным Qml.
- Простые и быстрые интерфейсы разработки.
- Унифицированный стиль темы виджета.
- Обильные эффекты и цвета.

%package -n lib%name%soname
Summary: Libraries for %name
Summary(ru): Библиотеки для %name
Group: System/Libraries
Requires: libqt5-core = %_qt5_version libqt5-gui = %_qt5_version libqt5-qml = %_qt5_version libqt5-qmlmodels = %_qt5_version libqt5-quick = %_qt5_version

%description -n lib%name%soname
The package provides libraries for %name.

%description -n lib%name%soname -l ru
Пакет содержит библиотеки для %name.

%package -n lib%name-devel
Summary: Development files for %name
Summary(ru): Файлы разработки для %name
Group: Development/KDE and QT
Provides: dtk5-declarative-devel = %EVR
Obsoletes: dtk5-declarative-devel < %EVR

%description -n lib%name-devel
The package provides development files for %name.

%description -n lib%name-devel -l ru
Пакет содержит библиотеки для %name.

%package -n qt-creator-data-%name
Summary: QtCreator Data files for %name
Summary(ru): Файлы данных QtCreator для %name
Group: Development/Tools
BuildArch: noarch

%description -n qt-creator-data-%name
QtCreator Data files for %name.

%description -n qt-creator-data-%name -l ru
Файлы данных QtCreator для %name.

%prep
%setup
%patch -p1

%build
export PATH=%_qt5_bindir:$PATH

%if_enabled clang

export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"

%endif

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_DOCS=OFF \
  -DMKSPECS_INSTALL_DIR=%_qt5_archdatadir/mkspecs/modules/ \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DINCLUDE_INSTALL_DIR=include \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DLIB_INSTALL_DIR=%_lib \
  -DDTK_VERSION=%version \
  -DVERSION=%version \
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/dtk-exhibition
%_qt5_qmldir/QtQuick/Controls.2/Chameleon/*
%dir %_qt5_qmldir/org/deepin/
%dir %_qt5_qmldir/org/deepin/dtk/
%_qt5_qmldir/org/deepin/dtk/libdtkdeclarativeplugin.so
%_qt5_qmldir/org/deepin/dtk/qmldir
%dir %_datadir/dtk5/
%_datadir/dtk5/DDeclarative/

%files -n lib%name%soname
%_libdir/libdtkdeclarative.so.%{soname}*

%files -n lib%name-devel
%_includedir/*
%_libdir/libdtkdeclarative.so
%_pkgconfigdir/dtkdeclarative.pc
%dir %_libdir/cmake/DtkDeclarative/
%_libdir/cmake/DtkDeclarative/*.cmake
%_qt5_archdatadir/mkspecs/modules/qt_lib_dtkdeclarative.pri

%files -n qt-creator-data-%name
%_datadir/qtcreator/templates/wizards/projects/qml-app-template/

%changelog
* Fri Mar 29 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.26-alt1
- New version 5.6.26.

* Wed Mar 20 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.25-alt1
- New version 5.6.25.

* Fri Mar 01 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.24-alt1
- New version 5.6.24.
- Requires: libqt5-core = %%_qt5_version.

* Thu Jan 11 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.21-alt1
- New version 5.6.21.

* Fri Oct 20 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.18-alt1
- New version 5.6.18.
- Renamed subpackages:
  + dtk5-declarative -> dtkdeclarative.
  + dtk5-declarative-devel -> libdtkdeclarative-devel.
- Cleanup BRs.

* Tue Jun 27 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.12-alt1
- New version 5.6.12.
- Fixed FTBFS on i586.

* Wed Feb 22 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.8-alt1
- New version (5.6.8).
- Built using cmake instead qmake (by upstream).
- Fixed underlinked libraries.

* Tue Nov 29 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.0-alt1
- Initial build for ALT Sisyphus.
