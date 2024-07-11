Name: alsa-ucm-conf
Version: 1.2.12
Release: alt1

Summary: Advanced Linux Sound Architecture (ALSA) Use Case Manager data
License: BSD-3-Clause
Group: System/Libraries

Url: http://www.alsa-project.org
Source: %name-%version.tar

Patch1: 0001-ucm.conf-turn-on-support-for-V2Module-and-V2Name-by-.patch
Patch2: 0002-ucm2-add-pinephone-pro-support.patch
Patch8: 0008-tegra-Add-UCM-for-RT5631-based-ASUS-Transformers.patch
Patch9: 0009-tegra-Add-UCM-for-WM8903-based-ASUS-Transformers.patch
Patch10: 0010-rt5631-add-headset-support.patch
Patch11: 0011-wm8903-replace-amic-control-element.patch
Patch12: 0012-ucm2-sof-essx8336-HiFi_fix_disdevall_and_EN_headset.patch
Patch13: 0013-ucm2-sof-essx8336-add-inv-headset-detect-near-DMic.patch
Patch14: 0014-sof-essx8336-update-strategy-and-add-support-for-es8.patch
Patch20: 0020-amd-acp3x-essx8336-add-support-for-a-new-driver.patch

BuildArch: noarch

%define alsadata %_datadir/alsa

%description
Advanced Linux Sound Architecture (ALSA) Use Case Manager data
used to sit in libalsa but have been factored out to be maintained
in a standalone repository.

%prep
%setup

%patch1 -p1
%patch2 -p1
#patch8 -p1
#patch9 -p1
#patch10 -p1
#patch11 -p1
#patch12 -p1
#patch13 -p1
#patch14 -p1
#patch20 -p1

%build



%install
mkdir -p %buildroot%alsadata
cp -at %buildroot%alsadata -- ucm*

%files
%alsadata/*
%doc LICENSE

%changelog
* Thu Jun 27 2024 Michael Shigorin <mike@altlinux.org> 1.2.12-alt1
- 1.2.12

* Tue Jan  2 2024 Artyom Bystrov <arbars@altlinux.org> 1.2.10-alt2
- Getting back Pinephone support patches

* Tue Dec 26 2023 Michael Shigorin <mike@altlinux.org> 1.2.10-alt1
- 1.2.10
- fix 15-years-old strl() related kludge in alsactl/init_sysdeps.c
- drop upstream commits as patches

* Mon Jun 19 2023 Vasiliy Kovalev <kovalev@altlinux.org> 1.2.8-alt8
- sof-essx8336: update strategy and add support for es8326 codec

* Fri Jun 16 2023 Andrew Savchenko <bircoph@altlinux.org> 1.2.8-alt7
- Add rk3399s (pinephone pro) configs

* Fri Jun 02 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.2.8-alt6
- ucm.conf: turn on support for V2Module and V2Name by default

* Thu Mar 02 2023 Vasiliy Kovalev <kovalev@altlinux.org> 1.2.8-alt5
- amd-acp3x-essx8336: add support for a new driver

* Mon Dec 19 2022 Vasiliy Kovalev <kovalev@altlinux.org> 1.2.8-alt4
- sof-essx8336: add inverse headset detection without DMic conflict

* Mon Nov 28 2022 Vasiliy Kovalev <kovalev@altlinux.org> 1.2.8-alt3
- sof-essx8336: remove unneeded upstream patches and add patch for
  HiFi.conf instead:
  + it forbids disabling all devices in the EnableSequence section,
    which blocked the detection of hdmi audio outputs and normal
    configuration in general
  + fix operation sequence section of the headset for correct
    configuration and avoiding conflict with the built-in microphone

* Wed Nov 23 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.8-alt2
- readd support for ASUS Transformers

* Sun Nov 20 2022 Michael Shigorin <mike@altlinux.org> 1.2.8-alt1
- 1.2.8

* Fri Aug 05 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.6.3-alt3
- add support for ASUS Transformers

* Fri Apr 08 2022 Nikolai Kostrigin <nickel@altlinux.org> 1.2.6.3-alt2
- add sof-essx8336 support patch set from upstream dev branch

* Thu Apr 07 2022 Michael Shigorin <mike@altlinux.org> 1.2.6.3-alt1
- 1.2.6.3

* Sat Dec 11 2021 Michael Shigorin <mike@altlinux.org> 1.2.6.2-alt1
- 1.2.6.2

* Wed Dec 08 2021 Michael Shigorin <mike@altlinux.org> 1.2.6-alt1
- 1.2.6

* Sat Jun 19 2021 Michael Shigorin <mike@altlinux.org> 1.2.5.1-alt1
- 1.2.5.1

* Sat Jun 05 2021 L.A. Kostis <lakostis@altlinux.ru> 1.2.5-alt1.1
- Apply fix from upstream:
  + HDA-Intel: the lookups are supported from syntax 4

* Tue Jun 01 2021 Michael Shigorin <mike@altlinux.org> 1.2.5-alt1
- 1.2.5

* Wed Oct 21 2020 Michael Shigorin <mike@altlinux.org> 1.2.4-alt1
- 1.2.4

* Wed Jun 10 2020 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- 1.2.3

* Thu Feb 20 2020 Michael Shigorin <mike@altlinux.org> 1.2.2-alt1
- 1.2.2

* Mon Dec 02 2019 Michael Shigorin <mike@altlinux.org> 1.2.1.2-alt1
- 1.2.1.2

* Mon Nov 18 2019 Michael Shigorin <mike@altlinux.org> 1.2.1-alt1
- initial release

