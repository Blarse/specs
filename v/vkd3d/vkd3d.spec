%def_disable demos
%def_disable tests
%define major 1

Name: vkd3d
Version: 1.12
Release: alt1
Summary: The vkd3d 3D Graphics Library

Group: System/Libraries
License: LGPL-2.1
Url: https://source.winehq.org/git/vkd3d.git/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Sat Mar 25 2023 (-ba)
BuildRequires: flex libvulkan-devel libspirv-tools-devel spirv-headers wine-devel-tools

%if_enabled demos
BuildRequires: libxcb-devel libxcbutil-devel libxcbutil-keysyms-devel libxcbutil-icccm-devel
%endif
%if_enabled tests
BuildRequires: vulkan-lvp
%endif

# same as wine
ExclusiveArch: %ix86 x86_64 aarch64

%description
Vkd3d is a 3D graphics library built on top of Vulkan. It has an API very
similar, but not identical, to Direct3D 12.

%package -n lib%{name}%{major}
Summary: %{name} libraries
Group: System/Libraries

%description -n lib%{name}%{major}
Vkd3d is a 3D graphics library built on top of Vulkan. It has an API very
similar, but not identical, to Direct3D 12.

%package devel
Summary: %name development package
Group: Development/C
Requires: lib%{name}%{major} = %EVR
Requires: %name-utils = %EVR

%description devel
Development headers for %name.

%package utils
Summary: %name utils
Group: Development/C
Requires: lib%{name}%{major} = %EVR

%description utils
%name utils.

%package demos
Summary: %name demos
Group: Development/C
Requires: lib%{name}%{major} = %EVR

%description demos
%name demos.

%prep
%setup
%patch -p1
%autoreconf
%configure \
  %{subst_enable demos} \
  %{subst_enable tests} \
  --with-spirv-tools
  %nil

%build
%make_build

# still fails
%if_enabled tests
%check
%make check
%endif

%install
%makeinstall
%if_enabled demos
mkdir -p %buildroot%_bindir
for f in demos/{gears,triangle}; do
  cp -a "$i" %buildroot%_bindir/%{name}_"$f";
done
%endif
# to make LTO checks happy
rm -f %buildroot%_libdir/*.a

%files -n lib%{name}%{major}
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files utils
%_bindir/vkd3d-compiler
%_bindir/vkd3d-dxbc

%if_enabled demos
%files demos
%_bindir/*
%exclude %_bindir/vkd3d-compiler
%endif

%changelog
* Mon Jun 03 2024 L.A. Kostis <lakostis@altlinux.ru> 1.12-alt1
- 1.12.

* Fri Mar 15 2024 L.A. Kostis <lakostis@altlinux.ru> 1.11-alt1
- 1.11.

* Tue Feb 06 2024 L.A. Kostis <lakostis@altlinux.ru> 1.10-alt1
- 1.10.

* Wed Sep 27 2023 L.A. Kostis <lakostis@altlinux.ru> 1.9-alt1
- 1.9.

* Thu Aug 17 2023 Mikhail Tergoev <fidel@altlinux.org> 1.8-alt1
- NMU: new version 1.8 (with rpmrb script)

* Sat Mar 25 2023 L.A. Kostis <lakostis@altlinux.ru> 1.7-alt1
- 1.7.
- Add tests knob.
- Fix LTO flags.

* Thu Feb 02 2023 L.A. Kostis <lakostis@altlinux.ru> 1.6-alt1
- 1.6.

* Tue Oct 04 2022 L.A. Kostis <lakostis@altlinux.ru> 1.5-alt1
- 1.5.

* Sat Jun 18 2022 L.A. Kostis <lakostis@altlinux.ru> 1.3-alt1
- 1.3.

* Mon Dec 06 2021 L.A. Kostis <lakostis@altlinux.ru> 1.2-alt1.2
- Fix wine BR (changed again).

* Mon Aug 30 2021 L.A. Kostis <lakostis@altlinux.ru> 1.2-alt1.1
- Fix LTO linking.

* Fri Oct 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt1
- Updated to upstream release version 1.2 (ALT #39002).

* Sun Jul 19 2020 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.6.g4bea4b8
- GIT 4bea4b8.
- Fix License.
- Add exclusivearch.

* Sat Jun 06 2020 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.5.gf68bf0d
- GIT f68bf0d.

* Sun May 10 2020 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.4.gc8c05c7
- GIT c8c05c7.

* Sun May 05 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.3.gbe4ca96
- GIT be4ca96.

* Thu Feb 07 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.2.gfd3d661
- GIT fd3d661.

* Mon Dec 03 2018 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.1
- Bump to 1.1 release.
- Disable demos and libxcb (can be enabled one day).

* Mon Jun 18 2018 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt0.1.g04b9d19
- Initial build for ALTLinux.
