
%define _unpackaged_files_terminate_build 1
%define libname libsfizz1

Name:     sfizz
Version:  1.0.0
Release:  alt2.git07260b13

Summary:  SFZ parser and synthesizer
License:  BSD-2-Clause
Group:    Sound
#Vcs:     https://github.com/sfztools/sfizz
Url:      https://sfz.tools/sfizz/

ExcludeArch: %arm ppc64le


Source: %name-1.0.0-alt2.git07260b13.tar

# https://github.com/abseil/abseil-cpp.git
Source1000: abseil-cpp-997aaf3a28308eba1b9156aa35ab7bca9688e9f6.tar
# https://github.com/steinbergmedia/vst3_base.git
Source1001: vst3_base-985fe019276ee03c2751a1736ba3b390678e29f2.tar
# https://github.com/steinbergmedia/vst3_pluginterfaces.git
Source1002: vst3_pluginterfaces-b8566ef3b2a0cba60a96e3ef2001224c865c8b36.tar
# https://github.com/sfztools/vst3_public_sdk.git
Source1003: vst3_public_sdk-d69d011fa08c3977928f7da0010f8938f93fd370.tar
# https://github.com/steinbergmedia/vstgui.git
Source1004: vstgui-2cf61f5e1fefe4dcd3d19119ddf7b182719a2a5b.tar
# https://github.com/mackron/dr_libs.git
Source1005: dr_libs-cac1785cee4abb455817b43d5dee33b49d61be2f.tar
# https://github.com/dr-soft/miniaudio.git
Source1006: miniaudio-d1a166c83ab445b1c14bc83d37c84e18d172e5f5.tar
# https://github.com/sfztools/stb_vorbis.git
Source1007: stb_vorbis-fc0bd698b26888da0a632da33f4c49b90763e69b.tar
# https://github.com/sfztools/libaiff.git
Source1008: libaiff-78864a4a2e769e426be8cfd78ae7f5f72e236c33.tar
# https://github.com/sfztools/sfzt_auwrapper.git
Source1009: sfzt_auwrapper-014311ae45b86571e1ae3aaa03ebbd7db8b3a32e.tar
# https://github.com/gulrak/filesystem.git
Source1010: filesystem-2a8b380f8d4e77b389c42a194ab9c70d8e3a0f1e.tar
# https://github.com/simd-everywhere/simde.git
Source1011: simde-98075d0593f539762125dbb215d95e782a6ae344.tar
# https://github.com/nemequ/munit.git
Source1012: munit-da8f73412998e4f1adf1100dc187533a51af77fd.tar

BuildRequires: cmake ctest gcc-c++
# BuildRequires: libabseil-cpp-devel
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(gio-2.0)

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(pangoft2)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)


%description
sfizz is a sample-based musical synthesizer.

It features the well-established SFZ instrument format at its
core, which permits to use existing instrument libraries, or
create personal instruments with ease.

Not only is sfizz ready-to-use as an instrument plugin of its own,
the library allows developers to create instruments of their own,
taking advantage of the abilities of SFZ.


%package tools
Summary: SFZ parser and synthesizer tools
Group:   Sound

%description tools
sfizz is a sample-based musical synthesizer.

It features the well-established SFZ instrument format at its
core, which permits to use existing instrument libraries, or
create personal instruments with ease.

This package includes the following tools:
- sfizz_render: render a midi file through an SFZ file;
- sfizz_jack: standalone synthesizer for Jack.


%package -n lv2-%name-plugin
Summary: SFZ parser and synthesizer as LV2 plugin
Group:   Sound

%description -n lv2-%name-plugin
sfizz is a sample-based musical synthesizer.

It features the well-established SFZ instrument format at its
core, which permits to use existing instrument libraries, or
create personal instruments with ease.

This package includes LV2 plugins that enable use of
SFZ instruments in any LV2-compatible host.


%package -n %libname
Summary: SFZ parser and synthesizer library
Group:   Sound

%description  -n %libname
sfizz is a sample-based musical synthesizer.

It features the well-established SFZ instrument format at its
core, which permits to use existing instrument libraries, or
create personal instruments with ease.

Not only is sfizz ready-to-use as an instrument plugin of its own,
the library allows developers to create instruments of their own,
taking advantage of the abilities of SFZ.

This package includes its shared library.


%package -n %libname-devel
Summary: Development files for %libname
Group:   Development/C++

%description -n %libname-devel
sfizz is a sample-based musical synthesizer.

Not only is sfizz ready-to-use as an instrument plugin of its own,
the library allows developers to create instruments of their own,
taking advantage of the abilities of SFZ.

This package contains include files, libraries and other files
needed for developing applications that use libsfizz.

%prep
%setup -n %name

tar -xf %SOURCE1000 -C 'external/abseil-cpp' --strip-components 1
tar -xf %SOURCE1001 -C 'plugins/vst/external/VST_SDK/VST3_SDK/base' --strip-components 1
tar -xf %SOURCE1002 -C 'plugins/vst/external/VST_SDK/VST3_SDK/pluginterfaces' --strip-components 1
tar -xf %SOURCE1003 -C 'plugins/vst/external/VST_SDK/VST3_SDK/public.sdk' --strip-components 1
tar -xf %SOURCE1004 -C 'plugins/editor/external/vstgui4' --strip-components 1
tar -xf %SOURCE1005 -C 'external/st_audiofile/thirdparty/dr_libs' --strip-components 1
tar -xf %SOURCE1006 -C 'external/st_audiofile/thirdparty/dr_libs/tests/external/miniaudio' --strip-components 1
tar -xf %SOURCE1007 -C 'external/st_audiofile/thirdparty/stb_vorbis' --strip-components 1
tar -xf %SOURCE1008 -C 'external/st_audiofile/thirdparty/libaiff' --strip-components 1
tar -xf %SOURCE1009 -C 'plugins/vst/external/sfzt_auwrapper' --strip-components 1
tar -xf %SOURCE1010 -C 'external/filesystem' --strip-components 1
tar -xf %SOURCE1011 -C 'external/simde' --strip-components 1
tar -xf %SOURCE1012 -C 'external/simde/test/munit' --strip-components 1


%build
# TODO: -DSFIZZ_USE_SYSTEM_ABSEIL=ON -- currently this way it does not build

%cmake \
    -DLV2PLUGIN_INSTALL_DIR=%_libdir/lv2 \
    -DSFIZZ_LV2_PSA=ON \
    -DSFIZZ_VST=OFF \
    -DSFIZZ_USE_SNDFILE=ON \
    -DSFIZZ_TESTS=ON \
    -DSFIZZ_DEVTOOLS=ON

%cmake_build

%install
%cmakeinstall_std

%check
%cmake_build -t test


%files tools
%_bindir/*

%files -n lv2-%name-plugin
%_libdir/lv2/%{name}*

%files -n %libname
%_libdir/*.so.*
%doc README.md

%files -n %libname-devel
%_includedir/sfizz*
%_libdir/*.so
%_pkgconfigdir/sfizz*


%changelog
* Wed Jul 07 2021 Ivan A. Melnikov <iv@altlinux.org> 1.0.0-alt2.git07260b13
- Build from develop branch snapshot
  + fixes crash with Ardour 6+ (https://github.com/sfztools/sfizz/issues/884).
- Enable PSA for LV2 plugin

* Fri May 28 2021 Ivan A. Melnikov <iv@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
