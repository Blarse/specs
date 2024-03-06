%set_verify_elf_method unresolved=relaxed
%def_without separate_trikruntime
%def_without sanitize
%def_without debug
%define appname trik-studio-junior

Name: trikStudioJunior
Version: 2021.3
Release: alt1.1
Summary: Intuitive graphical programming environment
Summary(ru_RU.UTF-8): Интуитивно-понятная графическая среда программирования
License: Apache-2.0
Group: Education
Url: https://github.com/trikset/trik-studio

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: gcc-c++ qt5-base-devel qt5-svg-devel qt5-script-devel qt5-multimedia-devel libusb-devel libudev-devel libgmock-devel
BuildRequires: libqscintilla2-qt5-devel zlib-devel python3-dev
BuildRequires: quazip-qt5-devel
# Workaround due project build with -fsanitize=undefined natively
# https://bugzilla.altlinux.org/show_bug.cgi?id=38106
#if_with sanitize
BuildRequires: libubsan-devel-static
#endif
BuildRequires: rsync qt5-tools

Requires: %name-data

%description

An intuitive programming environment allows you to program with
using a sequence of pictures. TRIK Studio Junior is an opportunity
build a continuous learning process, do programming
simple and fun.

The environment has a common interface with the TRIK Studio robot programming environment,
allows you to program a simulation model and a real robot
Python and JavaScript are both visual and text devices.

%description -l ru_RU.UTF-8
Интуитивно-понятная среда программирования позволяет программировать с
помощью последовательности картинок. TRIK Studio Junior — это возможность
построить непрерывный процесс образования, сделать обучение программированию
простым и увлекательным.

Среда имеет общий интерфейс со средой программирования роботов TRIK Studio,
позволяющей программировать имитационную модель и реальные робототехнические
устройства на визуальном языке и текстовых языках Python и JavaScript.


%package data
Summary: Data files for %name
Group: Education
BuildArch: noarch

%description data
Data files for %name

%prep
%setup
%patch -p1
sed -e '2 a export LD_LIBRARY_PATH=%_libdir\/%name\/' -i installer/platform/trikStudio.sh
sed -e 's|^trik-studio|%_libdir/%name/trik-studio|' -i installer/platform/trikStudio.sh

%ifarch loongarch64 riscv64
# gold does not work on these architectures
sed -e '/use_gold_linker/d' -i global.pri
%endif


tar -xf ./.gear/qslog.tar.bz2
tar -xf ./.gear/checkapp.tar.bz2

pushd qrgui/thirdparty
tar -xf qt-solutions.tar.bz2
popd

%build
%qmake_qt5 -r \
    LIBS+="`pkg-config --libs quazip1-qt5`" \
    INCLUDEPATH+="`pkg-config --cflags-only-I quazip1-qt5 |
      sed 's/-I//g'`" \
%if_with debug
    CONFIG+=debug CONFIG-=release \
%else
    CONFIG-=debug CONFIG+=release \
%endif
    QMAKE_LFLAGS+=-Wl,-rpath-link=%_builddir/%name-%version/bin/release \
    QMAKE_LFLAGS+=-Wl,-rpath=%_libdir/%name \
%if_with sanitize
    CONFIG+=!nosanitizers \
%endif
    CONFIG+=no_rpath \
    PREFIX=%_prefix LIBDIR=%_libdir TRIK_STUDIO_VERSION=Junior-%version studio.pro
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install
mv %buildroot%_libdir/*.so* %buildroot%_libdir/%name
mv %buildroot%_bindir/%appname %buildroot%_libdir/%name/
ln -fs %name %buildroot%_bindir/%appname

rm -rf %buildroot%_sysconfdir/trik
rm -f %buildroot%_prefix/lib/libqslog*.so*
rm -f %buildroot%_prefix/lib/libtrik*.so*
rm -rf %buildroot%_datadir/trikRuntime
rm -rf %buildroot%_prefix/local/share/qslog/
rm -rf %buildroot%_includedir/trik*
rm -rf %buildroot%_includedir/qslog*
rm -rf %buildroot%_includedir/QsLog*

rm -f %buildroot/lib/*PythonQt_QtAll* %buildroot/include/PythonQt_QtAll.h
rm -f %buildroot%_libdir/%name/plugins/tools/kitPlugins/librobots-null-interpreter.so

pushd bin/release
for d in examples help translations images; do
    cp -fr $d %buildroot%_datadir/%name/
done
#cp -fr trikSharp %buildroot%_libdir/%name/

%files
%_bindir/*
%_libdir/%name
%_sysconfdir/%appname.config

%files data
%_datadir/%name
%_miconsdir/*
%_liconsdir/*
%_niconsdir/*
%_desktopdir/*
%doc LICENSE NOTICE README.md

%changelog
* Wed Mar 06 2024 Ivan A. Melnikov <iv@altlinux.org> 2021.3-alt1.1
- NMU: don't use gold on loongarch64 and riscv64 (fixes build
  on these architectures).

* Wed Feb 09 2022 Valery Sinelnikov <greh@altlinux.org> 2021.3-alt1
- Update to jr2021.3

* Tue Feb 08 2022 Valery Sinelnikov <greh@altlinux.org> 2020.2-alt3
- Rebuild with RPATH due upgraded lib.req which sets "library not found"
  warnings to errors.
- Fixed desktop file for trikStudioJunior

* Sat Jan 01 2022 Anton Midyukov <antohami@altlinux.org> 2020.2-alt2
- fix build with qt5-quazip1
- clean add_findreq_skiplist
- drop old Conflicts
- fix Requires

* Tue Jun 23 2020 Valery Sinelnikov <greh@altlinux.org> 2020.2-alt1
- Initial build for Sisyphus

