Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ libX11-devel libqt4-devel libquazip-devel pkgconfig(lcms2) pkgconfig(libopenjp2) pkgconfig(libtiff-4) qt5-phonon-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname texstudio
Name:           texstudio
Version:        4.0.4
Release:        alt1

Summary:        A feature-rich editor for LaTeX documents
# texstudio binary: GPLv3 due to static linkage of bundled qcodeedit
# texstudio data and image files: GPLv2+
License:        GPLv2+ and GPLv3
URL:            https://www.texstudio.org

Source0:        https://github.com/texstudio-org/texstudio#/archive/%{name}-%{version}.tar.gz
Source1:        texstudio.desktop
Patch1:         texstudio-use-system-qtsingleapplication-instead-of-bundled-on.patch
Patch2:         texstudio-disable-update-check.patch
# don't muck with default build flags
Patch3:         texstudio-wtf_flags.patch

BuildRequires:  qt5-base-devel
BuildRequires:  qt5-tools qt5-tools-devel
BuildRequires:  qt5-tools-devel qt5-tools-devel-static
BuildRequires:  qt5-svg-devel
BuildRequires:  qt5-script-devel
BuildRequires:  hunspell-utils libhunspell-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext gettext-tools
BuildRequires:  libpoppler-qt5-devel
BuildRequires:  libqtsingleapplication-devel
BuildRequires:  libqtsingleapplication-qt5-devel
BuildRequires:  libqtermwidget-devel
BuildRequires:  libquazip-qt5-devel
BuildRequires:  zlib-devel libpoppler-cpp-devel qt5-declarative-devel

Requires:       tex(latex)
Requires:       tex(preview.sty)
Requires:       texlive
Requires:       libqt5-svg libqt5-qml
Requires:       libqtermwidget
Provides:       bundled(qcodeedit) 
Provides:       texmakerx = %{version}-%{release}
Obsoletes:      texmakerx < 2.2-1
Source44: import.info
%description
TeXstudio gives you an environment where you can 
easily create and manage LaTeX documents.
It provides modern writing support, like interactive spell checking, 
code folding, syntax highlighting, integrated pdf viewer
and various assistants. 
Also it serves as a starting point from where you can easily run 
all necessary LaTeX tools.

%prep
%setup -q -n %{name}-%{version}
#patch1 -p1 -b .qtsingle
%patch2 -p1 -b .update_check
#patch3 -p1 -b .wtf_flags

rm -rf {hunspell,qtsingleapplication,quazip}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%qmake_qt5 \
%ifnarch %{ix86} x86_64 %{arm}
    NO_CRASH_HANDLER=1 \
%endif
    USE_SYSTEM_HUNSPELL=1 \
    USE_SYSTEM_QTSINGLEAPPLICATION=1 \
    INTERNAL_TERMINAL=1 \
    USE_SYSTEM_QUAZIP=1 QUAZIP_LIB=-lquazip5 QUAZIP_INCLUDE=%{_includedir}/quazip5/ \
    ../texstudio.pro
popd

%make_build -C %{_target_platform}

%install
make install INSTALL_ROOT=$RPM_BUILD_ROOT -C %{_target_platform}

install -Dp -m 0644 utilities/texstudio16x16.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio22x22.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio32x32.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio48x48.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio64x64.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/46x46/apps/texstudio.png


rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/{AUTHORS,COPYING,*.desktop,tex*.png,CHANGELOG.txt}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/{*.dic,*.aff}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/qt_*.qm

%find_lang %{name} --with-qt

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files -f %{name}.lang
%{_bindir}/texstudio
%dir %{_datadir}/texstudio/
%{_datadir}/texstudio/*.png
%{_datadir}/texstudio/usermanual.css
%{_datadir}/texstudio/latex2e.*
%{_datadir}/texstudio/*.stopWords
%{_datadir}/texstudio/*.stopWords.level2
%{_datadir}/texstudio/de_DE.badWords
%{_datadir}/texstudio/template_*.tex
%{_datadir}/texstudio/template_*.zip
%{_datadir}/texstudio/*.json
%{_datadir}/texstudio/*.js
%{_datadir}/texstudio/th_*.dat
%{_datadir}/texstudio/usermanual_*.html
%{_datadir}/applications/texstudio.desktop
%{_datadir}/metainfo/texstudio.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg

%doc utilities/AUTHORS utilities/COPYING utilities/manual/CHANGELOG.txt

%changelog
* Sun Nov 07 2021 Ilya Mashkin <oddity@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Mon Nov 01 2021 Ilya Mashkin <oddity@altlinux.ru> 4.0.3-alt1
- 4.0.3

* Sat Oct 23 2021 Ilya Mashkin <oddity@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Wed Oct 13 2021 Ilya Mashkin <oddity@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Tue Sep 28 2021 Ilya Mashkin <oddity@altlinux.ru> 4.0.0-alt1
- 4.0.0.

* Sun Aug 01 2021 Ilya Mashkin <oddity@altlinux.ru> 3.1.2-alt2
- Build for Sisyphus, thanks for Igor Vlasenko
- Build with bundled qtsingleapplication

* Sun Jul 25 2021 Igor Vlasenko <viy@altlinux.org> 3.1.2-alt1_1
- new version

