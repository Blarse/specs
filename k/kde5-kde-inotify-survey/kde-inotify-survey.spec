%define rname kde-inotify-survey

Name: kde5-%rname
Version: 23.04.0
Release: alt1
%K5init altplace no_appdata man

Group: Sound
Summary: Inotify state of the user
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Apr 25 2023 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libdbusmenu-qt52 libglvnd-devel libgpg-error libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-test libqt5-texttospeech libqt5-widgets libqt5-x11extras libsasl2-3 libssl-devel libstdc++-devel libxcbutil-keysyms python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-devel rpm-build-file rpm-build-python3 rpm-macros-python sh4 tzdata
#BuildRequires: appstream clang-tools extra-cmake-modules kf5-kauth-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-knotifications-devel python-modules-compiler python3-module-mpl_toolkits python3-module-setuptools python3-module-zope qt5-imageformats qt5-svg-devel qt5-wayland-devel qt5-webengine-devel tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-base-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kauth-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-knotifications-devel

%description
Have you ever wondered why dolphin or any other application stopped noticing file changes?
Chances are you ran out of inotify resources. kde-inotify-survey to the rescue!
Sporting a kded module to tell you when things are getting dicey and a CLI tool to inspect the state of affairs.

%prep
%setup -n %rname-%version

%build
%K5build \
    #

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/*
%_K5plug/kf5/kded/*inotify*.so
%_K5libexecdir/kauth/kded-inotify-helper
%_K5notif/*inotify*.notifyrc
%_K5dbus_sys_srv/*inotify*.service
%_K5dbus/system.d/*inotify*.conf
%_datadir/polkit-1/actions/*inotify*.policy

%changelog
* Tue Apr 25 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.0-alt1
- initial build
