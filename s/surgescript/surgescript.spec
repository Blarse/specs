Name: surgescript
Summary: A scripting language for games

# All of SurgeScript's original code is licensed under ASL 2.0.
#
# There are a couple files borrowed from other projects
# that use different licenses.
#
# BSD:
# - src/surgescript/util/uthash.h
# - src/surgescript/util/xxh3.h
# - src/surgescript/util/xxhash.c
# - src/surgescript/util/xxhash.h
# Public Domain:
# - src/surgescript/util/xoroshiro128plus.c
# - src/surgescript/util/utf8.c
# - src/surgescript/util/utf8.h
%global license_main  Apache-2.0
%global license_devel Apache-2.0 and BSD and Public Domain

License: %license_main

Version: 0.5.6.1
Release: alt1

Group: System/Libraries
Url: https://opensurge2d.org

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make

%description
SurgeScript is a scripting language for games. It has been designed
with the specific needs of games in mind. Its features include:
- The state-machine pattern: objects are state machines,
  making it easy to create in-game entities
- The composition approach: you may design complex objects
  and behaviors by means of composition
- The hierarchy system: objects have a parent and may have children,
  in a tree-like structure
- The game loop: it's defined implicitly
- Automatic garbage collection, object tagging and more!

SurgeScript is meant to be used in games and in interactive applications.
It's easy to integrate it into existing code, it's easy to extend,
it features a C-like syntax, and it's free and open-source software.

SurgeScript has been designed based on the experience of its developer
dealing with game engines, applications related to computer graphics and so on.
Some of the best practices have been incorporated into the language itself,
making things really easy for developers and modders.

%package devel
Summary: Files for developing applications using %name
License: %license_devel
Group: System/Libraries
Requires: %name = %version

%description devel
This package contains files required for
developing applications using %name.

%package static
Summary: Files for developing applications using %name
License: %license_devel
Group: System/Libraries
Requires: %name-devel = %version

%description static
This package contains files required for
developing applications using %name,
using static linking.

%prep
%setup
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%build
%cmake \
	-DWANT_SHARED=ON  \
	-DWANT_STATIC=ON  \
	-DWANT_EXECUTABLE=ON  \
	-DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%doc docs/
%doc README.md
%doc LICENSE
%_bindir/%name
%_pixmapsdir/%name.png
%_datadir/metainfo/%name.appdata.xml
%_libdir/lib%name.so.0.6.0

%files devel
%_includedir/%name.h
%_includedir/%name/
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%files static
%_libdir/lib%name-static.a
%_pkgconfigdir/%name-static.pc

%changelog
* Fri May 26 2023 Artyom Bystrov <arbars@altlinux.org> 0.5.6.1-alt1
- update to new version

* Sat Sep 17 2022 Artyom Bystrov <arbars@altlinux.org> 0.5.6-alt1
- update to new version

* Fri Aug 27 2021 Artyom Bystrov <arbars@altlinux.org> 0.5.5-alt2
- add link-time optimization
- delete "Packager" tag

* Thu Aug 12 2021 Artyom Bystrov <arbars@altlinux.org> 0.5.5-alt1
- initial build for ALT Sisyphus
