%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: gamescope
Version: 3.11.26
Release: alt1
Summary: SteamOS session compositing window manager
Group: System/X11
License: BSD-2-Clause
Url: https://github.com/Plagman/gamescope

# https://github.com/Plagman/gamescope.git
Source: %name-%version.tar

# Create stb.pc to satisfy dependency('stb')
# Taken from Fedora
Source1: stb.pc

# watch file
Source100: %name.watch

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: libwlroots-devel
BuildRequires: libliftoff-devel
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
BuildRequires: wayland-protocols
BuildRequires: libxkbcommon-devel
BuildRequires: libcap-devel
BuildRequires: libSDL2-devel
BuildRequires: libstb-devel
BuildRequires: glslang-devel
# Missing dependency of libwlroots-devel
BuildRequires: libinput-devel

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
%setup

# Install stub pkgconfig file
mkdir -p pkgconfig
cp %SOURCE1 pkgconfig/stb.pc

%build
export PKG_CONFIG_PATH=pkgconfig
%meson \
	-Dpipewire=enabled \
	-Dforce_fallback_for=[] \
	%nil

%meson_build -v

%install
%meson_install

%files
%doc LICENSE
%doc README.md
%_bindir/gamescope

%changelog
* Wed Mar 02 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.26-alt1
- Updated to upstream version 3.11.26.

* Mon Feb 28 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.25-alt1
- Updated to upstream version 3.11.25.

* Tue Feb 22 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.23-alt1
- Initial build for ALT.
