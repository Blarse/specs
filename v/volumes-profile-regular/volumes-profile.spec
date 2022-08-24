Name: volumes-profile-regular
Version: 0.4.3
Release: alt1

Summary: Volumes description for ALT Linux Regular builds
License: GPL
Group: System/Configuration/Other

Url: http://en.altlinux.org/regular
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
%summary
(and Starterkits)

%prep
%setup

%install
%define hookdir %_datadir/install2/initinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Aug 24 2022 Anton Midyukov <antohami@altlinux.org> 0.4.3-alt1
- 10-vm-profile.sh: fix calculation $max_disk for multiple disks

* Tue Mar 01 2022 Anton Midyukov <antohami@altlinux.org> 0.4.2-alt1
- 10-vm-profile.sh: add support nvme*, mmc*

* Fri Aug 20 2021 Michael Shigorin <mike@altlinux.org> 0.4.1-alt1
- E2K: increase /boot size from 512 Mb to 1 Gb for serviceability

* Fri Mar 02 2018 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- e2k support (/boot)

* Tue Nov 28 2017 Mikhail Efremov <sem@altlinux.org> 0.3-alt1
- Fix profile for disks > 120Gb.

* Fri Nov 17 2017 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Don't create separate /home if disk size <=120Gb.
- Take in account disks in KVM too.
- Don't use RAID in KVM.

* Mon Sep 07 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on -lite package)

