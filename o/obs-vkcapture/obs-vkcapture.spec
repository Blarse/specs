%define _unpackaged_files_terminate_build 1

Name: obs-vkcapture
Version: 1.4.9
Release: alt1

Summary: OBS Linux Vulkan/OpenGL game capture

License: GPL-2.0
Group: Other
Url: https://github.com/nowrep/obs-vkcapture

Source: %name-%version.tar
Patch1: %name-loongarch-riscv.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libobs-devel libvulkan-devel libGL-devel libEGL-devel
BuildRequires: libX11-devel libxcb-devel libwayland-client-devel
BuildRequires: libXau-devel libXdmcp-devel libffi-devel

ExcludeArch: %ix86 armh

%description
%summary

Add Game Capture to your OBS scene.
Start the game with capture enabled obs-gamecapture command.
(Recommended) Start the game with only Vulkan capture enabled
env OBS_VKCAPTURE=1 command.

%prep
%setup
%patch1 -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%files
%doc *.md LICENSE
%_bindir/obs-gamecapture
%_bindir/obs-glcapture
%_bindir/obs-vkcapture
%_libdir/obs_glcapture/libobs_glcapture.so
%_libdir/libVkLayer_obs_vkcapture.so
%_libdir/obs-plugins/linux-vkcapture.so
%_datadir/obs/obs-plugins/linux-vkcapture/*
%_datadir/vulkan/implicit_layer.d/obs_vkcapture_64.json

%changelog
* Mon Feb 12 2024 Mikhail Tergoev <fidel@altlinux.org> 1.4.9-alt1
- 1.4.9

* Tue Dec 05 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.4.7-alt2
- NMU: fixed FTBFS on LoongArch (and possibly riscv64)

* Tue Dec 05 2023 Mikhail Tergoev <fidel@altlinux.org> 1.4.7-alt1
- 1.4.7

* Thu Oct 05 2023 Mikhail Tergoev <fidel@altlinux.org> 1.4.4-alt1
- 1.4.4

* Tue Sep 19 2023 Mikhail Tergoev <fidel@altlinux.org> 1.4.3-alt1
- 1.4.3

* Wed Sep 13 2023 Mikhail Tergoev <fidel@altlinux.org> 1.4.2-alt1
- 1.4.2
- Added BR: libXau-devel libXdmcp-devel libffi-devel

* Wed Aug 02 2023 Mikhail Tergoev <fidel@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
