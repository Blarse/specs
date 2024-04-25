Name: alt-rootfs-installer
Version: 0.5.11
Release: alt1
Summary: Installer rootfs archive to any specified block device
License: GPL-2.0-or-later
Group: System/Configuration/Other
Url:  https://git.altlinux.org/people/antohami/packages/alt-rootfs-installer.git
BuildArch: noarch
Source0: %name-%version.tar

%description
Allows one to first select a source rootfs archive installer. The rootfs must be
containing File Systems with u-boot for target board.
This fork arm-image-installer.

%prep
%setup

%install
install -d %buildroot%_datadir/%name
install -d %buildroot%_datadir/%name/socs.d
cp -a socs.d/* %buildroot%_datadir/%name/socs.d/
install -d %buildroot%_datadir/%name/boards.d
cp -a boards.d/* %buildroot%_datadir/%name/boards.d/
cp -a log %buildroot%_datadir/%name/
install -pm 644 SUPPORTED-BOARDS %buildroot%_datadir/%name

install -d %buildroot%_bindir
install -pm 0755 %name %buildroot%_bindir/

install -d %buildroot%_docdir/%name
install -pm 644 AUTHORS COPYING README SUPPORTED-BOARDS \
        %buildroot%_docdir/%name

%files
%doc %_docdir/%name
%_bindir/*
%_datadir/%name/

%changelog
* Thu Apr 25 2024 Anton Midyukov <antohami@altlinux.org> 0.5.11-alt1
- SUPPORTED-BOARDS: fix lists

* Fri Apr 05 2024 Anton Midyukov <antohami@altlinux.org> 0.5.10-alt1
- Update supported boards for u-boot 2024.04
- socs-utils: rename function update_cmdline.txt -> update_cmdline_txt
- alt-rootfs-installer: don't include socs-utils ahead of time
- alt-rootfs-installer: don't include logging ahead of time
- spec: drop obsoletes/provides arm-rootfs-installer

* Thu Jul 27 2023 Anton Midyukov <antohami@altlinux.org> 0.5.9-alt1
- alt-rootfs-installer: set serial console for grub also, cleanup quiet
- Update list of supported boards for u-boot 2023.07

* Tue May 23 2023 Anton Midyukov <antohami@altlinux.org> 0.5.8-alt1
- Add RBS Repka Pi 3 board support (thanks jqt4)

* Sat Feb 18 2023 Anton Midyukov <antohami@altlinux.org> 0.5.7-alt1
- Add Orangepi 4 support (Closes: 45187)

* Fri Jan 20 2023 Anton Midyukov <antohami@altlinux.org> 0.5.6-alt1
- add nvme support (Closes: 44408)
- socs-utils: fix clear_riscv64_bootloader_partition for /dev/mmcblkXpN
- socs-utils: use oflag=direct for dd when write image
- Update list of supported boards for u-boot 2023.01

* Sun Mar 13 2022 Anton Midyukov <antohami@altlinux.org> 0.5.5-alt1
- jetson_nano-aarch64.sh: extract archive to /root
- fix include logging function for portable version

* Wed Jan 26 2022 Anton Midyukov <antohami@altlinux.org> 0.5.4-alt1
- Fix rewrite bootloader with GPT partition table
- Add AllWinner riscv64 support (nezha, lichee_rv)

* Mon Jan 24 2022 Anton Midyukov <antohami@altlinux.org> 0.5.3-alt1
- Add new targets sifive_unleashed, sifive_unmatched
- Update supported boards with u-boot 2022.01
- Rockchips-aarch64.sh: add support u-boot-rockchip 2022.01

* Sat Dec 04 2021 Anton Midyukov <antohami@altlinux.org> 0.5.2-alt1
- Add HiFive Unmatched support (thanks jqt4@)
- socs-utils: fix find_firmware_partition
- alt-rootfs-installer: add new option --vnc
- riscv64: enable CONSOLE by default
- enable vnc for HiFive-Unleashed-*
- Update supported boards with u-boot 2021.10

* Mon Jul 26 2021 Anton Midyukov <antohami@altlinux.org> 0.5.1-alt1
- Prevent concurrent use of options --image-in and --image-out
- Fixed mounting ROOTPART when writing image
- Add option '--addconsole'
- Rockchips-aarch64.sh: use msdos partition table
- socs.d: Set START_SECTOR to 16 MiB for AllWinner and RPi
- Fixed output of the final message
- jetson_nano-aarch64.sh: require python2
- not create symlink arm-rootfs-installer more

* Fri Jun 11 2021 Anton Midyukov <antohami@altlinux.org> 0.5.0-alt2
- copy SUPPORTED-BOARDS file to %_datadir/%name (Closes: 40209)

* Mon Jun 07 2021 Anton Midyukov <antohami@altlinux.org> 0.5.0-alt1
- Added new logging subsystem (thanks arei@)
- Update message output

* Fri May 21 2021 Anton Midyukov <antohami@altlinux.org> 0.4.5-alt1
- Fixed unmounting MEDIA, when writing image
- Fixed imposition info messages
- Add --efi-mbr option

* Tue Mar 23 2021 Anton Midyukov <antohami@altlinux.org> 0.4.4-alt1
- Fix HiFive Unleashed OpenSBI script (Thanks arei@)
- Update supported boards with u-boot 2021.01
- Clean disklabel in prepare_media
- Fix GPT part table always
- mount FIRMPART to ROOTPART/boot/efi

* Sun Dec 27 2020 Anton Midyukov <antohami@altlinux.org> 0.4.3-alt1
- Fix resize root partition

* Fri Nov 27 2020 Anton Midyukov <antohami@altlinux.org> 0.4.2-alt1
- Fixed support newer u-boot for Rockchip
- Update supported boards
- Added HiFive Unleashed OpenSBI SoC (riscv64) support (Thanks arei@)
- Added --uefi option

* Thu Sep 17 2020 Anton Midyukov <antohami@altlinux.org> 0.4.1-alt1
- alt-rootfs-installer: Fix for empty $TMP
- rpi-aarch64.sh: Fix write bootloader on Raspberry Pi 4

* Tue Sep 01 2020 Anton Midyukov <antohami@altlinux.org> 0.4.0-alt1
- Restructure code in the socs.d (Thanks arei@)
- Many fixes.

* Wed May 27 2020 Anton Midyukov <antohami@altlinux.org> 0.3.4-alt1
- Added support Raspberry Pi 4 on armh 

* Thu May 14 2020 Anton Midyukov <antohami@altlinux.org> 0.3.3-alt1
- Fix typo

* Mon Apr 13 2020 Anton Midyukov <antohami@altlinux.org> 0.3.2-alt1
- Added resize option
- Replace LABEL to UUID /usr/share/u-boot/rpi_4/cmdline.txt
- Update supported boards (u-boot 2020.01)

* Wed Nov 13 2019 Anton Midyukov <antohami@altlinux.org> 0.3.1.2-alt1
- Simplified check for Raspberry Pi devices targets
- Add u-boot 2019.10 support
- Fix bbl-riscv64 (Thanks arei@)

* Tue Oct 08 2019 Anton Midyukov <antohami@altlinux.org> 0.3.1.1-alt1
- hot-fix for Nvidia Jetson Nano (unmount device)

* Fri Oct 04 2019 Anton Midyukov <antohami@altlinux.org> 0.3.1-alt1
- 0.3.1
- make messages userfriendly more

* Wed Sep 11 2019 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- 0.3.0
- Add the ability create images from tarball
- Add the ability write image to media
- Add support u-boot-*-201907
- bug fixes and typos

* Fri Aug 02 2019 Anton Midyukov <antohami@altlinux.org> 0.2.4.1-alt1
- hot fix release
- change interpreter on /bin/bash

* Mon Jul 22 2019 Anton Midyukov <antohami@altlinux.org> 0.2.4-alt1
- 0.2.4
- Add support Nvidia Jetson Nano
- Add support u-boot-sunxi-201907

* Wed Jun 26 2019 Anton Midyukov <antohami@altlinux.org> 0.2.3-alt1
- 0.2.3
- Simplified code, improved portability (thanks sem@ and arei@)

* Thu Apr 18 2019 Anton Midyukov <antohami@altlinux.org> 0.2.1-alt1
- 0.2.1
- support u-boot-* 2019.04

* Fri Mar 29 2019 Anton Midyukov <antohami@altlinux.org> 0.2-alt0.1
- 0.2-beta
- Renamed package arm-rootfs-installer to alt-rootfs-installer
- Add support riscv64 (thanks arei@)
- Update URL

* Sun Feb 24 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build

