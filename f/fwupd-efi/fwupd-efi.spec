%define _unpackaged_files_terminate_build 1

Summary: EFI Application used by uefi-capsule plugin in fwupd
Name: fwupd-efi
Version: 1.1
Release: alt1
License: LGPLv2+
Group: System/Configuration/Hardware
Url: https://github.com/fwupd/fwupd-efi
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch
ExclusiveArch: x86_64 aarch64
BuildRequires: meson
BuildRequires: gnu-efi

%description
fwupd-efi is the UEFI binary used with fwupd for installing UEFI firmware updates

%prep
%setup
%patch0 -p1

%build
%meson \
    -Defi_sbat_distro_id="altlinux" \
    -Defi_sbat_distro_summary="ALT Linux" \
    -Defi_sbat_distro_pkgname="%name" \
    -Defi_sbat_distro_version="%version-%release" \
    -Defi_sbat_distro_url="http://git.altlinux.org/gears/f/%{name}.git"

%meson_build

%install
%meson_install

%files
%_libdir/efi/fwupd*.efi
%_libdir/pkgconfig/fwupd-efi.pc

%changelog
* Wed Jun 23 2021 Egor Ignatov <egori@altlinux.org> 1.1-alt1
- first build for ALT
