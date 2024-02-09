Name: portproton
Version: 1.4
Release: alt1

Summary: Installer for PortProton

License: MIT
Group: Games/Other
Url: https://github.com/Castro-Fidel/PortProton_ALT

Source: %name-%version.tar

Requires: bubblewrap cabextract zstd gawk tar xz pciutils coreutils file
Requires: curl icoutils wmctrl xdg-utils desktop-file-utils yad
Requires: libvulkan1 vulkan-tools libd3d libGL libMesaOpenCL gamemode fontconfig xrdb
Requires: libcurl libgio libnm libnsl1 libnss glibc-nss glibc-pthread
Requires: /usr/bin/convert

ExclusiveArch: x86_64

%description
Installer PortProton for Windows games.

%prep
%setup

%build
%install
install -Dm755 %name %buildroot%_bindir/%name
install -Dm644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm644 %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%doc LICENSE
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Fri Feb 09 2024 Mikhail Tergoev <fidel@altlinux.org> 1.4-alt1
- updated to v1.4
- update requires
- drop meta package 32-bit dependencies (it does not work as intended)

* Sun Dec 24 2023 Mikhail Tergoev <fidel@altlinux.org> 1.3-alt2
- added meta package for installation 32-bit dependencies
- update requires

* Fri Nov 24 2023 Mikhail Tergoev <fidel@altlinux.org> 1.3-alt1
- updated to v1.3

* Sat Nov 11 2023 Mikhail Tergoev <fidel@altlinux.org> 1.2-alt1
- updated to v1.2
- updated icon file (png to svg)

* Fri Nov 10 2023 Mikhail Tergoev <fidel@altlinux.org> 1.1-alt1
- updated to v1.1
- added gitlab.eterfund.ru for download scripts
- added installation path selection
- update desktop file

* Fri May 19 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt3
- install .desktop as a file
- add requires: fontconfig xrdb pciutils xdg-utils bc coreutils file desktop-file-utils wmctrl xz wget

* Sun Apr 02 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- fix Exec in desktop file
- add requires: gawk tar libd3d libMesaOpenCL /usr/bin/convert

* Sat Apr  1 2023 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1.1
- Add MimeType description in desktop file

* Mon Mar 20 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus
