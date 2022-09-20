Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 2

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-sayura
Version:    5.0.8
Release:    alt1_%autorelease
Summary:    Sinhala Transe IME engine for Fcitx5
License:    GPLv2+
URL:        https://github.com/fcitx/fcitx5-sayura
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  ctest cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  gettext gettext-tools
BuildRequires:  /usr/bin/appstream-util
Requires:       icon-theme-hicolor
Requires:       fcitx5-data
Source44: import.info

%description
Fcitx-Sayura is a Sinhala input method
for Fcitx input method framework ported
from IBus-Sayura.

%prep
%setup -q


%build
%{fedora_v2_cmake} -GNinja
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install

# convert symlinked icons to copied icons, this will help co-existing with
# fcitx4
for iconfile in $(find %{buildroot}%{_datadir}/icons -type l)
do
  origicon=$(readlink -f ${iconfile})
  rm -f ${iconfile}
  cp ${origicon} ${iconfile}
done 
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}

%files -f %{name}.lang
%doc --no-dereference LICENSES/GPL-2.0-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/sayura.so
%{_datadir}/fcitx5/addon/sayura.conf
%{_datadir}/fcitx5/inputmethod/sayura.conf
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Sayura.metainfo.xml


%changelog
* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.8-alt1_2
- new version

