%define sover 292

Name: libplacebo
Version: 6.292.1
Release: alt0.1
Summary: libplacebo is essentially the core rendering algorithms and ideas of mpv turned into a library
Group: System/Libraries
License: LGPL-2.1+
Url: https://github.com/haasn/libplacebo
Source0: %url/%name/archive/v%version/%name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires: libshaderc-devel libvulkan-devel python3-module-jinja2 python3-module-glad2 liblcms2-devel gcc-c++
%ifnarch %e2k
BuildRequires: libunwind-devel libdovi-devel
%endif

%description
libplacebo is essentially the core rendering algorithms and ideas of mpv turned
into a library.

%package -n %{name}%{sover}
Summary: %name is essentially the core rendering algorithms and ideas of mpv turned into a library
Group: System/Libraries

%description -n %{name}%{sover}
libplacebo is essentially the core rendering algorithms and ideas of mpv turned
into a library.

%package -n %name-devel
Summary: Development files for %name
Group: Development/C
Requires: %{name}%{sover} = %EVR

%description -n %name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p1

%build
%meson

%install
%meson_install

%files -n %{name}%{sover}
%_libdir/%name.so.%{sover}

%files -n %name-devel
%_includedir/*
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Tue Sep 05 2023 L.A. Kostis <lakostis@altlinux.ru> 6.292.1-alt0.1
- v6.292.1.

* Tue Aug 29 2023 L.A. Kostis <lakostis@altlinux.ru> 6.292.0-alt0.2
- Rebuild w/ new ffmpeg.

* Sun Jul 16 2023 L.A. Kostis <lakostis@altlinux.ru> 6.292.0-alt0.1
- v6.292.0.

* Fri May 26 2023 Michael Shigorin <mike@altlinux.org> 5.264.1-alt0.2
- E2K: avoid missing BRs

* Fri May 26 2023 L.A. Kostis <lakostis@altlinux.ru> 5.264.1-alt0.1
- v5.264.1.

* Thu Mar 16 2023 L.A. Kostis <lakostis@altlinux.ru> 5.264.0-alt0.1
- v5.264.0.
- BR: added libdovi.

* Fri Dec 09 2022 L.A. Kostis <lakostis@altlinux.ru> 5.229.1-alt0.1
- v5.229.1.
- Update soname.
- Update BR:
  - mako -> jinja2
  - libepoxy -> glad2
  + add libunwind support.

* Mon Oct 03 2022 L.A. Kostis <lakostis@altlinux.ru> 4.208.0-alt0.1
- v4.208.0.
- Update soname.

* Tue Nov 16 2021 L.A. Kostis <lakostis@altlinux.ru> 4.157.0-alt0.2
- Use libshaderc instead glslang.

* Fri Nov 12 2021 L.A. Kostis <lakostis@altlinux.ru> 4.157.0-alt0.1
- v4.157.0.
- Update soname.

* Mon Jun 14 2021 L.A. Kostis <lakostis@altlinux.ru> 3.120.1-alt0.1
- v3.120.1.

* Mon Jul 20 2020 L.A. Kostis <lakostis@altlinux.ru> 2.88.0-alt0.1
- Initial build for ALTLinux.
