%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: gamescope
Version: 3.14.2
Release: alt2

Summary: SteamOS session compositing window manager

Group: System/X11
License: BSD-2-Clause
Url: https://github.com/Plagman/gamescope

Source: %name-%version.tar
Source1: submodules-%name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libstb-devel
BuildRequires: libliftoff-devel
BuildRequires: libbenchmark-devel
BuildRequires: libglm-devel
BuildRequires: hwdata-devel
BuildRequires: libwlroots-devel
BuildRequires: pipewire-libs-devel
BuildRequires: libX11-devel
BuildRequires: libXdamage-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXrender-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXtst-devel
BuildRequires: libXres-devel
BuildRequires: libdrm-devel
BuildRequires: libvulkan-devel
BuildRequires: libwayland-server-devel
BuildRequires: libwayland-client-devel
BuildRequires: wayland-protocols
BuildRequires: libxkbcommon-devel
BuildRequires: libcap-devel
BuildRequires: libSDL2-devel
BuildRequires: libstb-devel
BuildRequires: glslang-devel
BuildRequires: libinput-devel
BuildRequires: libXmu-devel
BuildRequires: libdisplay-info-devel
BuildRequires: libXcursor-devel
BuildRequires: libavif-devel
BuildRequires: spirv-headers
BuildRequires: libopenvr-devel

ExclusiveArch: x86_64

%description
In an embedded session usecase, gamescope does the same thing as steamcompmgr,
but with less extra copies and latency:
*   It's getting game frames through Wayland by way of Xwayland,
    so there's no copy within X itself before it gets the frame.
*   It can use DRM/KMS to directly flip game frames to the screen,
    even when stretching or when notifications are up, removing another copy.
*   When it does need to composite with the GPU, it does so with async Vulkan
    compute, meaning you get to see your frame quick even if the game already
    has the GPU busy with the next frame.

It also runs on top of a regular desktop,
the 'nested' usecase steamcompmgr didn't support.
*   Because the game is running in its own personal Xwayland sandbox desktop,
    it can't interfere with your desktop and your desktop can't interfere with it.
*   You can spoof a virtual screen with a desired resolution and refresh rate
    as the only thing the game sees, and control/resize the output as needed.
    This can be useful in exotic display configurations like ultrawide
    or multi-monitor setups that involve rotation.

It runs on Mesa + AMD or Intel, and could be made to run
on other Mesa/DRM drivers with minimal work.
AMD requires Mesa 20.3+, Intel requires Mesa 21.2+.
Can support NVIDIA if/when they support
atomic KMS + accelerated Xwayland + Vulkan DMA-BUF extensions.
See https://github.com/Plagman/gamescope/issues/151 for NVIDIA support state.

If running RadeonSI clients with older cards (GFX8 and below),
currently have to set R600_DEBUG=nodcc,
or corruption will be observed until the stack picks up DRM modifiers support.

%prep
%setup -a1

# use system stb
sed -i "s|dependency('stb')|declare_dependency(include_directories: include_directories('/usr/include/stb'))|g" src/meson.build

# use system spirv headers
sed -i 's^../thirdparty/SPIRV-Headers/include/spirv/^/usr/include/spirv/^' src/meson.build

%build
%meson \
	-Dpipewire=enabled \
	-Denable_openvr_support=true \
	-Dforce_fallback_for=[] \
	%nil

%meson_build -v

%install
%meson_install

# remove vkroots devel files
rm -vr %buildroot%_includedir/vkroots.h
rm -vr %buildroot/%_pkgconfigdir/vkroots.pc

%files
%doc LICENSE README.md
%_bindir/gamescope
%_libdir/libVkLayer_FROG_gamescope_wsi_*.so
%_datadir/vulkan/implicit_layer.d/VkLayer_FROG_gamescope_wsi.*.json

%changelog
* Mon Mar 18 2024 Mikhail Tergoev <fidel@altlinux.org> 3.14.2-alt2
- Added support OpenVR.
- Used system spirv headers.

* Mon Mar 11 2024 Mikhail Tergoev <fidel@altlinux.org> 3.14.2-alt1
- 3.14.2

* Thu Sep 14 2023 Mikhail Tergoev <fidel@altlinux.org> 3.12.5-alt1
- 3.12.5
- Revert to git.

* Tue Aug 01 2023 Mikhail Tergoev <fidel@altlinux.org> 3.12.0-alt1
- New version (3.12.0) with rpmgs script.
- Moved to update from tarball.

* Wed Mar 02 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.26-alt1
- Updated to upstream version 3.11.26.

* Mon Feb 28 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.25-alt1
- Updated to upstream version 3.11.25.

* Tue Feb 22 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.23-alt1
- Initial build for ALT.
