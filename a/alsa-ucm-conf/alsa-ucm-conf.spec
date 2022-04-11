Name: alsa-ucm-conf
Version: 1.2.6.3
Release: alt2

Summary: Advanced Linux Sound Architecture (ALSA) Use Case Manager data
License: BSD-3-Clause
Group: System/Libraries

Url: http://www.alsa-project.org
Source: %name-%version.tar

Patch1: 0001-ucm2-sof-essx8336-initial-support.patch
Patch2: 0002-ucm2-sof-essx8336-add-missing-symlink-from-conf.d-tr.patch
Patch3: 0003-ucm2-sof-essx8336-Fill-in-SectionVerb-session-at-HiF.patch
Patch4: 0004-ucm2-sof-essx8336-Fix-location-of-HiFi.conf.patch
Patch5: 0005-ucm2-sof-essx8336-Add-a-boot-sequence.patch
Patch6: 0006-ucm2-sof-essx8336-drop-conditional-control-settings.patch
Patch7: 0007-ucm2-sof-essx8336-use-the-right-mixers-for-speaker-h.patch

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
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build

%install
mkdir -p %buildroot%alsadata
cp -at %buildroot%alsadata -- ucm*

%files
%alsadata/*
%doc LICENSE

%changelog
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

