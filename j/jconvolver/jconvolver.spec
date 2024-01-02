# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define _localstatedir %_var

Name: jconvolver
Summary: Real-time Convolution Engine
Version: 1.1.0
Release: alt1
License: GPL-2.0-or-later
Group: Sound
Url: https://kokkinizita.linuxaudio.org

# Source-url: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%name-%version.tar.bz2
Source: %name-%version.tar
Patch: jconvolver-1.0.3-get_ldflags_from_jack_pc.patch

Obsoletes: jace <= 0.2.0
Provides: jace = %EVR
Obsoletes: jconv <= 0.8.1
Provides: jconv = %EVR

BuildRequires: gcc-c++
BuildRequires: clthreads-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libsndfile-devel
BuildRequires: zita-convolver-devel >= 4.0.0

%description
Jconvolver is a real-time convolution engine. It can execute up to a 64 by 64
convolution matrix (i.e. 4096 simultaneous convolutions) as long as your CPU(s)
can handle the load. It is designed to be efficient also for sparse (e.g.
diagonal) matrices. Unused matrix elements do not take any CPY time.

%prep
%setup
%autopatch -p1

# fix paths of configuration files
find config-files/ -name \*.conf \
  -exec sed -i -e "s|/audio/reverbs|%_datadir/%name/reverbs|g" {} \; \
  -exec sed -i -e "s|^#/cd |/cd |g" {} \;

# Fix optflags
%__subst 's|-march=native|%optflags|' source/Makefile

# Fix for build with pipewire
%__subst "s|-ljack|$(pkg-config --libs jack)|" source/Makefile

%build
%make_build -C source

%install
%makeinstall_std PREFIX=%prefix -C source

# install configuration files and demo reverbs
mkdir -p %buildroot%_datadir/%name
cp -a config-files/* %buildroot%_datadir/%name

%files
%doc AUTHORS README* COPYING
%_bindir/*
%_datadir/%name/

%changelog
* Tue Jan 02 2024 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Fri Sep 01 2023 Anton Midyukov <antohami@altlinux.org> 1.0.3-alt3
- rebuild with pipewire-jack-libs-devel
- clean Packager

* Fri Aug 16 2019 Anton Midyukov <antohami@altlinux.org> 1.0.3-alt2
- fix optflags

* Mon Feb 04 2019 Anton Midyukov <antohami@altlinux.org> 1.0.3-alt1
- new version 1.0.3

* Sun Nov 25 2018 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Sun May 21 2017 Anton Midyukov <antohami@altlinux.org> 0.9.2-alt1
- Initial build for ALT Linux Sisyphus.
