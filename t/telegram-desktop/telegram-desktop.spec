# TODO: build external, json11 separately
# Check https://github.com/EasyCoding/tgbuild for patches

%define ffmpeg_version 3.4
# require
%define tg_qt5_version 5.15.10
# upstream uses 6.5.2
#define tg_qt6_version 6.5.2
%define tg_qt6_version 6.4.2

# AppID for Basealt build
# got from https://core.telegram.org/api/obtaining_api_id
%define apiid 182015
%define apihash bb6c3f8fffd8fe6804fc5131a08e1c44

# TODO: def_with clang
%def_with qt6
%def_without wayland
%def_with x11
%def_with rlottie
%def_without gsl
%def_without ninja
%def_without ffmpeg_static
%def_without jemalloc

Name: telegram-desktop
Version: 4.9.9
Release: alt1

Summary: Telegram Desktop messaging app

License: GPLv3 with OpenSSL exception
Group: Networking/Instant messaging
Url: https://telegram.org/

# Source-url: https://github.com/telegramdesktop/tdesktop/releases/download/v%version/tdesktop-%version-full.tar.gz
Source: %name-%version.tar

# Source1-url: https://github.com/desktop-app/GSL/archive/refs/heads/main.zip
Source1: %name-gsl-%version.tar

Patch1: telegram-desktop-remove-tgvoip.patch
Patch2: telegram-desktop-set-native-window-frame.patch
Patch5: telegram-desktop-fix-missed-cstdint.patch
Patch6: telegram-desktop-disabled-icon-checkbox.patch
Patch7: telegram-desktop-fix-build-with-make.patch

# lacks few build deps, still
# [ppc64le] E: Couldn't find package libdispatch-devel
# [ppc64le] /usr/bin/ld.default: /usr/lib64/libtg_owt.a: error adding symbols: file in wrong format
ExcludeArch: ppc64le

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-compat >= 2.1.5
BuildRequires(pre): rpm-build-intro >= 2.1.5
%if_with ninja
BuildRequires(pre): rpm-macros-ninja-build
%endif

# use no more than system_memory/3000 build procs (see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
%_tune_parallel_build_by_procsize 3000

# minimalize memory using
%ifarch %ix86 armh
%define optflags_debug -g0
%define optflags_lto %nil
%endif

BuildRequires: gcc-c++ libstdc++-devel
# for -lstdc++fs
BuildRequires: libstdc++%__gcc_version-devel-static

BuildRequires: python3

# cmake 3.16 as in CMakeLists.txt
BuildRequires: cmake >= 3.16
BuildRequires: extra-cmake-modules

%if_with qt6
BuildRequires(pre): rpm-macros-qt6
BuildRequires: qt6-base-devel >= %tg_qt6_version
BuildRequires: qt6-svg-devel qt6-svg
BuildRequires: qt6-charts-devel qt6-charts
BuildRequires: qt6-5compat-devel
BuildRequires: qt6-imageformats
%{?_with_wayland:BuildRequires: qt6-wayland-devel}
# needs for smiles and emojicons
Requires: qt6-imageformats
%else
BuildRequires(pre): rpm-macros-qt5
BuildRequires: qt5-base-devel >= %tg_qt5_version
BuildRequires: qt5-svg-devel
BuildRequires: libqt5-core libqt5-network libqt5-gui qt5-imageformats

BuildRequires: kf5-kcoreaddons-devel

# needs for smiles and emojicons
Requires: qt5-imageformats

# run around https://bugzilla.altlinux.org/show_bug.cgi?id=34665
Requires: libqt5-core >= %_qt5_version

# for -lQt5PlatformSupport
BuildRequires: qt5-base-devel-static

%{?_with_wayland:BuildRequires: kf5-kwayland-devel qt5-wayland-devel}
%endif

BuildRequires: libenchant2-devel
BuildRequires: libhunspell-devel

# for autoupdater (included ever if disabled)
# TODO:
BuildRequires: liblzma-devel

# for SourceFiles/mtproto/connection.cpp
BuildRequires: libzip-devel

BuildRequires: zlib-devel >= 1.2.8
BuildRequires: libxxhash-devel
BuildRequires: liblz4-devel
BuildRequires: libcrc32c-devel
BuildRequires: libfmt-devel

BuildRequires: libminizip-devel libpcre2-devel libexpat-devel libssl-devel libselinux-devel bison

%if_with x11
#BuildRequires: libxcbutil-keysyms-devel
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-record)
BuildRequires: pkgconfig(xcb-screensaver)
%endif

#BuildRequires: libgtk+3-devel
BuildRequires: libglibmm2.68-devel >= 2.77
BuildRequires: gobject-introspection-devel

BuildRequires: libopus-devel
# TODO:
# libdee-devel

#BuildRequires: libopenal-devel >= 1.22.2
# p10
BuildRequires: libopenal-devel >= 1.21.1
# libportaudio2-devel libxcb-devel
# used by qt imageformats: libwebp-devel
BuildRequires: libva-devel libdrm-devel

# Telegram fork of OWT
BuildRequires: libowt-tg-devel >= 4.3.0.10
BuildRequires: librnnoise-devel
#BuildRequires: libvpx-devel
BuildRequires: libjpeg-devel

# No rule to make target '/usr/lib64/libopenh264.so', needed by 'telegram-desktop'
BuildRequires: libopenh264-devel

# No rule to make target '/usr/lib64/libXcomposite.so', needed by 'telegram-desktop'
BuildRequires: libXcomposite-devel

# No rule to make target '/usr/lib64/libXdamage.so', needed by 'telegram-desktop'
BuildRequires: libXdamage-devel
BuildRequires: libXrandr-devel libXext-devel libXfixes-devel libXrender-devel libXtst-devel


#see hack below (used directly in Telegram/ThirdParty/tgcalls/tgcalls/desktop_capturer/DesktopCaptureSourceHelper.cpp)
BuildRequires: libyuv-devel

# Just to disable noise like Package 'libffi', required by 'gobject-2.0', not found
# See https://bugzilla.altlinux.org/30001
BuildRequires: libffi-devel libmount-devel libXdmcp-devel libblkid-devel
BuildRequires: bzlib-devel libbrotli-devel gstreamer1.0-devel

BuildRequires: boost-program_options-devel

# uses forked version, tag e0ea6af518345c4a46195c4951e023e621a9eb8f
BuildRequires: librlottie-devel >= 0.1.1
BuildRequires: libqrcodegen-cpp-devel

# C++ sugar
%if_with gsl
BuildRequires: libmicrosoft-gsl-devel >= 1:4.0.0-alt2
%endif

# https://github.com/telegramdesktop/tdesktop/issues/8471
#BuildRequires: libvariant-devel
BuildRequires: libexpected-devel
BuildRequires: librange-v3-devel >= 0.11.0
BuildRequires: libdispatch-devel

# for bundled cldr3
BuildRequires: libprotobuf-devel libprotobuf-lite-devel protobuf-compiler

# need for /usr/lib64/cmake/Qt5XkbCommonSupport/Qt5XkbCommonSupportConfig.cmake
BuildRequires: libxkbcommon-devel

%if_with ninja
BuildRequires: ninja-build
%endif

# FIXME: libva need only for linking, extra deps?

Provides: telegram = %version-%release
Provides: tdesktop = %version-%release
Obsoletes: tdesktop


%if_with ffmpeg_static
BuildRequires: libffmpeg-devel-static >= %ffmpeg_version
%else
BuildRequires: libavfilter-devel >= %ffmpeg_version
BuildRequires: libavcodec-devel >= %ffmpeg_version
BuildRequires: libavformat-devel >= %ffmpeg_version
BuildRequires: libavutil-devel >= %ffmpeg_version
BuildRequires: libswscale-devel >= %ffmpeg_version
BuildRequires: libswresample-devel >= %ffmpeg_version
%endif

Requires: dbus

# instead of internal fonts OpenSans
# works with system fonts, see https://bugzilla.altlinux.org/show_bug.cgi?id=38986
#Requires: fonts-ttf-open-sans

# some problems with t_assert
%add_optflags -fpermissive -DNDEBUG

# disable some warnings
%add_optflags -Wno-strict-aliasing -Wno-unused-variable -Wno-sign-compare -Wno-switch

%add_optflags -fstack-protector-all -fstack-clash-protection -D_GLIBCXX_ASSERTIONS
%ifarch x86_64
%add_optflags -fcf-protection
%endif


%description
Telegram is a messaging app with a focus on speed and security, it's super-fast, simple and free.
You can use Telegram on all your devices at the same time - your messages
sync seamlessly across any number of your phones, tablets or computers.

With Telegram, you can send messages, photos, videos and files of any type (doc, zip, mp3, etc),
as well as create groups for up to 1000 people or channels for broadcasting to unlimited audiences.
You can write to your phone contacts and find people by their usernames.
As a result, Telegram is like SMS and email combined - and can take care of all your personal
or business messaging needs.


%prep
%setup -a1
%patch1 -p2
%patch2 -p2
%patch5 -p2
%if_without qt6
%patch6 -p2
%endif
#patch7 -p2

%if_without gsl
test -d /usr/share/cmake/Microsoft.GSL/ && echo "External Microsoft GSL is incompatible with buggy libstd++ (see https://gcc.gnu.org/bugzilla/show_bug.cgi?id=106547), remove libmicrosoft-gsl-devel to correct build" && exit 1
%endif

# See https://github.com/desktop-app/tg_owt/pull/82
# TODO: there are incorrect using and linking libyuv
subst 's|third_party/libyuv/include/libyuv.h|libyuv.h|' Telegram/ThirdParty/tgcalls/tgcalls/desktop_capturer/*.cpp
# TODO: ld: lib_webview/liblib_webview.a(webview_linux_webkit_gtk.cpp.o): undefined reference to symbol 'dlclose@@GLIBC_2.2.5
# TODO: ld: /tmp/.private/lav/ccfxvz2E.ltrans115.ltrans.o: неопределённая ссылка на символ «ARGBScale»
#subst "s|\(desktop-app::external_rnnoise\)|\1 -lyuv|" Telegram/cmake/lib_tgcalls.cmake

# Unbundling libraries...
# TODO: minizip
for i in \
%if_with gsl
	Telegram/ThirdParty/GSL \
%endif
	Telegram/ThirdParty/QR \
	Telegram/ThirdParty/expected \
	Telegram/ThirdParty/jemalloc \
	Telegram/ThirdParty/fcitx-qt5 \
	Telegram/ThirdParty/fcitx5-qt \
	Telegram/ThirdParty/hime \
	Telegram/ThirdParty/hunspell \
	Telegram/ThirdParty/lz4 \
	Telegram/ThirdParty/nimf \
	Telegram/ThirdParty/range-v3 \
	Telegram/ThirdParty/xxHash \
%if_with rlottie
	Telegram/ThirdParty/rlottie \
%endif
	Telegram/ThirdParty/libtgvoip \
	Telegram/ThirdParty/tgcalls/tgcalls/legacy \
	%nil ; do
	echo "Removing $i ..."
	rm -r $i
done

%build
%if_with ffmpeg_static
export PKG_CONFIG_PATH=%_libdir/ffmpeg-static/%_lib/pkgconfig/
%endif

%if_with clang
%remove_optflags -frecord-gcc-switches
export CC=clang
%endif

# due precompiled headers
export CCACHE_SLOPPINESS=pch_defines,time_macros

# CMAKE_BUILD_TYPE should always be Release due to some hardcoded checks.
#    -DCMAKE_BUILD_TYPE=RelWithDebInfo \

%cmake_insource \
%if_with ninja
    -G Ninja \
%endif
    -DDESKTOP_APP_USE_PACKAGED=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DTDESKTOP_API_ID=%apiid \
    -DTDESKTOP_API_HASH=%apihash \
    -DDESKTOP_APP_USE_PACKAGED:BOOL=ON \
    -DDESKTOP_APP_USE_PACKAGED_FONTS:BOOL=ON \
    -DDESKTOP_APP_DISABLE_CRASH_REPORTS:BOOL=ON \
    -DDESKTOP_APP_DISABLE_SPELLCHECK:BOOL=OFF \
%if_with qt6
    -DQT_VERSION_MAJOR=6 \
%else
    -DQT_VERSION_MAJOR=5 \
%endif
%if_without jemalloc
    -DDESKTOP_APP_DISABLE_JEMALLOC=ON \
%endif
%if_with wayland
    -DDESKTOP_APP_DISABLE_WAYLAND_INTEGRATION:BOOL=OFF \
%else
    -DDESKTOP_APP_DISABLE_WAYLAND_INTEGRATION:BOOL=ON \
%endif
%if_with x11
    -DDESKTOP_APP_DISABLE_X11_INTEGRATION:BOOL=OFF \
%else
    -DDESKTOP_APP_DISABLE_X11_INTEGRATION:BOOL=ON \
%endif
%if_with rlottie
    -DDESKTOP_APP_USE_PACKAGED_RLOTTIE=ON \
# FIXME: lottie_cache.h:9:10: fatal error: ffmpeg/ffmpeg_utility.h: No such file or directory
#    -DDESKTOP_APP_LOTTIE_USE_CACHE:BOOL=OFF \
%else
    -DDESKTOP_APP_USE_PACKAGED_RLOTTIE=OFF \
%endif
    %nil

%if_with ninja
%ninja_build
%else
%make_build VERBOSE=1
%endif

%install
%if_with ninja
%ninja_install
%else
%makeinstall_std
%endif
# XDG files
#install -m644 -D lib/xdg/tg.protocol %buildroot%_Kservices/tg.protocol

ln -s %name %buildroot%_bindir/Telegram
ln -s %name %buildroot%_bindir/telegram
ln -s %name %buildroot%_bindir/telegramdesktop

%files
%_bindir/%name
%_bindir/telegramdesktop
%_bindir/Telegram
%_bindir/telegram
%_desktopdir/*.desktop
%_datadir/dbus-1/services/*.service
%_datadir/metainfo/*.metainfo.xml
%_iconsdir/hicolor/16x16/apps/telegram.png
%_iconsdir/hicolor/32x32/apps/telegram.png
%_iconsdir/hicolor/48x48/apps/telegram.png
%_iconsdir/hicolor/64x64/apps/telegram.png
%_iconsdir/hicolor/128x128/apps/telegram.png
%_iconsdir/hicolor/256x256/apps/telegram.png
%_iconsdir/hicolor/512x512/apps/telegram.png
#_man1dir/*
%doc README.md

%changelog
* Fri Sep 22 2023 Vitaly Lipatov <lav@altlinux.ru> 4.9.9-alt1
- new version 4.9.9 (with rpmrb script)

* Wed Sep 20 2023 Vitaly Lipatov <lav@altlinux.ru> 4.9.8-alt1
- new version 4.9.8 (with rpmrb script)
- add Requires: qt6-imageformats
- build with embedded GSL

* Tue Aug 01 2023 Vitaly Lipatov <lav@altlinux.ru> 4.8.4-alt1
- new version (4.8.4) with rpmgs script
- add Provides: telegram
- switch to build with Qt6
- needs glibmm 2.76
- switch to libpcre2-devel
- add BR: libselinux-devel

* Wed Jun 14 2023 Anton Midyukov <antohami@altlinux.org> 4.3.1-alt3
- NMU: rebuild without unused appindicator-gtk3

* Fri Apr 28 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.3.1-alt2
- rebuilt on arm arches

* Wed Nov 23 2022 Vitaly Lipatov <lav@altlinux.ru> 4.3.1-alt1
- new version 4.3.1 (with rpmrb script)
- switched to glibmm-2.68

* Fri Sep 30 2022 Vitaly Lipatov <lav@altlinux.ru> 4.2.4-alt1
- new version 4.2.4 (with rpmrb script)

* Fri Sep 30 2022 Vitaly Lipatov <lav@altlinux.ru> 4.2.3-alt1
- new version 4.2.3 (with rpmrb script)

* Mon Aug 29 2022 Vitaly Lipatov <lav@altlinux.ru> 4.1.1-alt1
- new version 4.1.1 (with rpmrb script)

* Fri Aug 05 2022 Vitaly Lipatov <lav@altlinux.ru> 4.0.4-alt1
- new version 4.0.4 (with rpmrb script)

* Mon Jun 27 2022 Vitaly Lipatov <lav@altlinux.ru> 4.0.2-alt2
- merge git repo with p10 (with -s ours)

* Sat Jun 25 2022 Vitaly Lipatov <lav@altlinux.ru> 4.0.2-alt1
- new version 4.0.2 (with rpmrb script)

* Sat Jun 25 2022 Vitaly Lipatov <lav@altlinux.ru> 4.0.1-alt1
- new version 4.0.1 (with rpmrb script)

* Thu Jun 23 2022 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- new version 4.0.0 (with rpmrb script)

* Sun Jun 19 2022 Vitaly Lipatov <lav@altlinux.ru> 3.7.6-alt1
- new version 3.7.6 (with rpmrb script)
- fix build with Qt5

* Sun Jun 19 2022 Vitaly Lipatov <lav@altlinux.ru> 3.7.5-alt2
- add support for build with Qt6
- settings: make icon checkbox with disabled state (ALT bug 42548)

* Wed Jun 15 2022 Vitaly Lipatov <lav@altlinux.ru> 3.7.5-alt1
- new version 3.7.5 (with rpmrb script)

* Tue Apr 26 2022 Vitaly Lipatov <lav@altlinux.ru> 3.7.3-alt1
- new version 3.7.3 (with rpmrb script)

* Tue Apr 26 2022 Vitaly Lipatov <lav@altlinux.ru> 3.7.2-alt1
- new version 3.7.2 (with rpmrb script)

* Sun Apr 17 2022 Vitaly Lipatov <lav@altlinux.ru> 3.7.0-alt1
- new version 3.7.0 (with rpmrb script)
- disable wayland integration (is not ported to Qt5)
- drop webkit require (used without headers now)
- build with external libdispatch-devel

* Sun Apr 10 2022 Vitaly Lipatov <lav@altlinux.ru> 3.6.1-alt2
- enable system window frame by default (ALT bug 41888)

* Sat Apr 09 2022 Vitaly Lipatov <lav@altlinux.ru> 3.6.1-alt1
- new version 3.6.1 (with rpmrb script)

* Fri Dec 03 2021 Vitaly Lipatov <lav@altlinux.ru> 3.2.8-alt1
- new version 3.2.8 (with rpmrb script)

* Fri Nov 26 2021 Vitaly Lipatov <lav@altlinux.ru> 3.2.5-alt1
- new version 3.2.5 (with rpmrb script)

* Tue Oct 12 2021 Andrey Sokolov <keremet@altlinux.org> 3.1.8-alt2
- fix crashes on video call (closes: 38897)

* Sat Oct 09 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.8-alt1
- new version 3.1.8 (with rpmrb script)

* Fri Oct 08 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.6-alt1
- new version 3.1.6 (with rpmrb script)
- build with external range-v3
- rearrange bundled libraries removing
- fix gtk3 integration
- add control for build with x11, wayland, webkit, and external libtgvoip

* Wed Sep 29 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.5-alt1
- new version 3.1.5 (with rpmrb script)

* Tue Sep 14 2021 Vitaly Lipatov <lav@altlinux.ru> 3.0.4-alt1
- new version 3.0.4 (with rpmrb script)

* Thu Sep 02 2021 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- new version 3.0.1 (with rpmrb script)

* Wed Sep 01 2021 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version 3.0.0 (with rpmrb script)

* Tue Aug 24 2021 Vitaly Lipatov <lav@altlinux.ru> 2.9.11-alt1
- new version 2.9.11 (with rpmrb script)

* Wed Aug 11 2021 Vitaly Lipatov <lav@altlinux.ru> 2.9.2-alt1
- new version 2.9.2 (with rpmrb script)

* Fri Jul 30 2021 Vitaly Lipatov <lav@altlinux.ru> 2.9.0-alt1
- new version 2.9.0 (with rpmrb script)

* Mon Jul 19 2021 Vitaly Lipatov <lav@altlinux.ru> 2.8.11-alt1
- new version 2.8.11 (with rpmrb script)

* Wed Jul 07 2021 Vitaly Lipatov <lav@altlinux.ru> 2.8.6-alt1
- new version 2.8.6 (with rpmrb script)
- add BR: libjemalloc-devel

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 2.8.1-alt2
- fix build with updated libowt-tg

* Sun Jun 27 2021 Vitaly Lipatov <lav@altlinux.ru> 2.8.1-alt1
- new version 2.8.1 (with rpmrb script)

* Sat Jun 26 2021 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt1
- new version 2.8.0 (with rpmrb script)

* Sun Mar 21 2021 Vitaly Lipatov <lav@altlinux.ru> 2.7.1-alt1
- new version 2.7.1 (with rpmrb script)

* Thu Feb 25 2021 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt1
- new version 2.6.1 (with rpmrb script)
- needs Qt5 >= 5.15.2

* Thu Feb 25 2021 Vitaly Lipatov <lav@altlinux.ru> 2.6.0-alt2
- disable WAYLAND_INTEGRATION for Qt < 5.15

* Wed Feb 24 2021 Vitaly Lipatov <lav@altlinux.ru> 2.6.0-alt1
- new version 2.6.0 (with rpmrb script)
- disable WEBRTC_INTEGRATION (still segfaults)

* Mon Feb 01 2021 Vitaly Lipatov <lav@altlinux.ru> 2.5.8-alt1
- new version 2.5.8 (with rpmrb script)

* Sat Oct 31 2020 Vitaly Lipatov <lav@altlinux.ru> 2.4.5-alt1
- new version 2.4.5 (with rpmrb script)
- drop BR: libvariant-devel

* Sun Aug 23 2020 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt1
- new version 2.3.1 (with rpmrb script)
- enable WebRTC integration (libtgvoip is legacy now)
- temp. disable armh (due tg_owt failed build)
- temp. disable ppc64le, aarch64 (tg_owt is not ready for them yet)

* Thu Aug 20 2020 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- new version 2.3.0 (with rpmrb script)
- build with bundled libtgvoip
- temp. disable webrtc integration

* Thu Jul 30 2020 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Wed Jul 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.18-alt1
- new version 2.1.18 (with rpmrb script)

* Sat Jul 04 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.17-alt1
- new version 2.1.17 (with rpmrb script)

* Tue Jun 30 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.14-alt1
- new version 2.1.14 (with rpmrb script)

* Wed Jun 24 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.13-alt1
- new version 2.1.13 (with rpmrb script)

* Thu Jun 18 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.12-alt1
- new version 2.1.12 (with rpmrb script)

* Fri Jun 05 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.10-alt1
- new version 2.1.10 (with rpmrb script)

* Thu Jun 04 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.8-alt1
- new version 2.1.8 (with rpmrb script)

* Sat May 30 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.7-alt1
- new version 2.1.7 (with rpmrb script)

* Thu May 14 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- new version 2.1.6 (with rpmrb script)

* Wed May 13 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.5-alt1
- new version 2.1.5 (with rpmrb script)

* Sun May 10 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- new version 2.1.4 (with rpmrb script)

* Fri May 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- new version 2.1.3 (with rpmrb script)

* Mon May 04 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)

* Thu Apr 30 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version 2.1.0 (with rpmrb script)

* Tue Mar 31 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version 2.0.1 (with rpmrb script)

* Mon Mar 30 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0 (with rpmrb script)

* Sun Mar 29 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.22-alt1
- new version 1.9.22 (with rpmrb script)

* Tue Mar 17 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.21-alt1
- new version 1.9.21 (with rpmrb script)

* Sun Mar 15 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.20-alt1
- new version 1.9.20 (with rpmrb script)

* Tue Feb 18 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.14-alt1
- new version 1.9.14 (with rpmrb script)

* Fri Feb 14 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.13-alt1
- new version 1.9.13 (with rpmrb script)

* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.10-alt1
- new version 1.9.10 (with rpmrb script)

* Wed Feb 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.9-alt2
- return to build from full tarball

* Wed Jan 29 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.9-alt1
- new version 1.9.9 (with rpmrb script)
- enable TDESKTOP_FORCE_GTK_FILE_DIALOG
- dropped tg.protocol packing

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.8-alt1
- new version (1.9.8) with rpmgs script
- build with system libqrcodegen-cpp-devel
- return build settings

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.7-alt1
- new version 1.9.7 (with rpmrb script)
- switched to the upstream cmake build

* Thu Nov 14 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.15-alt2
- enable build for i586 (with -g0)

* Tue Oct 08 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.15-alt1
- new version 1.8.15 (with rpmrb script)
- build codegen separately
- disable debug due memory usage overhead
- enable ppc64le build

* Thu Oct 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.12-alt1
- new version 1.8.12 (with rpmrb script)

* Sat Sep 28 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.9-alt1
- new version 1.8.9 (with rpmrb script)

* Wed Sep 11 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.8-alt1
- new version 1.8.8 (with rpmrb script)

* Fri Sep 06 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.4-alt1
- new version (1.8.4) with rpmgs script

* Fri Sep 06 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.3-alt1
- new version 1.8.3 (with rpmrb script)

* Thu Aug 22 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt1
- new version 1.8.2 (with rpmrb script)

* Tue Aug 13 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)

* Fri Aug 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Sat Jul 13 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.14-alt3
- use official fix: Use private Qt color API only in official build

* Thu Jul 11 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.14-alt2
- reenable GTK file chooser possibility:
  - drop TDESKTOP_DISABLE_GTK_INTEGRATION
  - add  TDESKTOP_FORCE_GTK_FILE_DIALOG

* Tue Jul 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.14-alt1
- new version (1.7.14) with rpmgs script
- fix build with current Qt (thanks, arseerfc@)

* Sun Jul 07 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.13-alt1
- new version 1.7.13 (with rpmrb script)
- use external librlottie instead of internal qtlottie

* Thu Jun 27 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.10-alt1
- new version 1.7.10 (with rpmrb script)

* Mon Jun 24 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.9-alt1
- new version 1.7.9 (with rpmrb script)

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.7-alt1
- new version 1.7.7 (with rpmrb script)

* Sun Jun 02 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.3-alt1
- new version 1.7.3 (with rpmrb script) (ALT bug 36838)

* Sun May 12 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- new version 1.7.0 (with rpmrb script)

* Thu Apr 18 2019 Vitaly Lipatov <lav@altlinux.ru> 1.6.7-alt1
- new version 1.6.7 (with rpmrb script)

* Wed Mar 27 2019 Vitaly Lipatov <lav@altlinux.ru> 1.6.3-alt1
- new version (1.6.3) with rpmgs script

* Sat Feb 23 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.15-alt1
- new version 1.5.15 (with rpmrb script)

* Tue Feb 05 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.11-alt1
- new version 1.5.11 (with rpmrb script)

* Fri Feb 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.10-alt1
- new version 1.5.10 (with rpmrb script)

* Wed Jan 16 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.7-alt2
- enable build on aarch64
- add fonts-ttf-open-sans require and drop OpenSans from resources
- drop external locales patches

* Mon Jan 14 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.7-alt1
- new version 1.5.7 (with rpmrb script)

* Mon Dec 31 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.6-alt1
- new version 1.5.6 (with rpmrb script)

* Tue Dec 25 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt2
- fix registration process (set correct api_id and api_hash)

* Mon Dec 24 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt1
- new version 1.5.4 (with rpmrb script)

* Sun Dec 16 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version 1.5.2 (with rpmrb script)

* Tue Dec 11 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version (1.5.1) with rpmgs script
- disable build on i586

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.4.8-alt1
- new version 1.4.8 (with rpmrb script)

* Sat Sep 29 2018 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version (1.4.0) with rpmgs script

* Sat Sep 08 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.16-alt1
- new version (1.3.16) with rpmgs script
 + Update libtgvoip, fix crash in calls.
 + Improved local caching for images and GIF animations.
 + Control how much disk space is used by the cache
   and for how long the cached files are stored.

* Tue Aug 28 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.14-alt1
- new version 1.3.14 (with rpmrb script)

* Thu Aug 23 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.12-alt1
- new version 1.3.12 (with rpmrb script)

* Sat Jul 14 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.10-alt1
- new version 1.3.10 (with rpmrb script)

* Sat Jul 14 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.9-alt2
- restrict __nprocs with _tune_parallel_build_by_procsize
- drop libpixman-devel buildreq

* Tue Jul 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.9-alt1
- new version 1.3.9 (with rpmrb script)

* Mon Jun 25 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.8-alt1
- new version 1.3.8 (with rpmrb script)

* Thu Jun 14 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.7-alt1
- new version 1.3.7 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt1
- new version 1.3.5 (with rpmrb script)

* Fri Jun 01 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Sat May 26 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2.23-alt1
- new version 1.2.23 (with rpmrb script)

* Thu Feb 22 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2.8-alt1
- new version (1.2.8) with rpmgs script

* Thu Dec 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Sun Dec 03 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.26-alt1
- new version 1.1.26 (with rpmrb script)

* Thu Nov 30 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.24-alt1
- new version 1.1.24 (with rpmrb script)
- build with librange-v3-include
- disable GTK integration (ALT bug 34182)

* Sat Oct 21 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.23-alt3
- fix old lang code in settings
- fix CVE-2016-10351: Insecure cWorkingDir permissions
- sync CMakeLists.txt with Gentoo, fix build with new Qt 5.9.2

* Fri Sep 29 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.23-alt2
- add support for build with static ffmpeg

* Sat Sep 23 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.23-alt1
- new version 1.1.23 (with rpmrb script)
- add qt5-imageformats (fixes missed smiles and emojicons)

* Wed Aug 02 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.19-alt1
- new version 1.1.19 (with rpmrb script)

* Sun Jul 30 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.18-alt1
- new version 1.1.18 (with rpmrb script)
- update translations

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt2
- cleanup build requires (drop opus, pulseaudio, webp, xcb, exif, X*)

* Fri Jul 21 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt1
- new version 1.1.14 (with rpmrb script)
- build with custom API ID
- update translations
- language list now downloading from cloud

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt2
- use correct executable path (fix restart)
- open localized FAQ for ru/uk/be
- get initial language name and country name from QLocale
- fix crash in video player seeking (66662e02a)

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt1
- new version (1.1.7) with rpmgs script

* Thu May 18 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt5
- add /usr/bin/telegram-desktop, fix icons name (ALT bug #33001)

* Fri Dec 23 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt4
- get language name and country name from QLocale
- disable user desktop file generation
- fix hack for restart via Updater, use direct /usr/bin path

* Wed Dec 21 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt3
- add Belarusian Russian Ukrainian French Turkish Czech languages

* Mon Dec 19 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt2
- add desktop file, icons
- cleanup spec

* Sat Dec 17 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt1
- new version 0.10.19 (with rpmrb script)

* Sun Dec 20 2015 Hihin Ruslan <ruslandh@altlinux.ru> 0.9.15-alt1
- initial build for ALT Linux Sisyphus
