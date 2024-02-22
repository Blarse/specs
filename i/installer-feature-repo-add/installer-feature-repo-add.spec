Name: installer-feature-repo-add
Version: 0.4
Release: alt1

Summary: Add the installation media to APT configuration
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch
Provides: %name-stage2
Obsoletes: %name-stage2

Conflicts: alterator-pkg < 2.6.18-alt1

%description
%summary


%prep
%setup

%install
%makeinstall

%files
%_datadir/install2/postinstall.d/*

%changelog
* Wed Feb 21 2024 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- Ensure that CDROMDEV is not empty.

* Mon Feb 12 2024 Anton Midyukov <antohami@altlinux.org> 0.3-alt4
- detect file system on local drive (e.g. usb flash drive)
- failed if install from local drive and .disk/info not found

* Thu Dec 08 2022 Dmitry Terekhin <jqt4@altlinux.org> 0.3-alt3
- use PARTUUID to identify ISO9660 partition

* Tue Mar 04 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt2
- flash repo under UEFI fixed

* Mon Mar 03 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- use both for cdroms and for flash disks
- make usable both for stage2 and stage3

* Mon Jan 13 2014 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- further cdrom restrictions (see #29704)

* Mon Jan 13 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk

