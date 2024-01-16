%define _unpackaged_files_terminate_build 1
%define pname integalert

Name:     %pname-source
Version:  0.4.3
Release:  alt2

Summary:  Osec-based integrity checking script and settings
License:  GPLv2
Group:    Monitoring
Url:      http://git.altlinux.org/people/manowar/packages/integalert.git

Packager: Paul Wolneykien <manowar@altlinux.org>

Source:   %name-%version.tar

Obsoletes: integ < 0.4.2-alt2

%description
Osec-based integrity checking script and settings.

%package -n %pname
Summary:  Osec-based integrity checking script and settings
Group:    Monitoring
BuildArch: noarch

Requires: systemd
Requires: osec-cronjob >= 1.3.1-alt2

%description -n %pname
Osec-based integrity checking script and settings.

%package -n installer-feature-integalert-stage2
Summary: Run integrity check after install (installer files)
Group: System/Configuration/Other
BuildArch: noarch

%description -n installer-feature-integalert-stage2
Run integrity check after install (installer files).

%package -n installer-feature-integalert-stage3
Summary: Run integrity check after install (chroot files)
Group: System/Configuration/Other
Requires: integalert = %version-%release
BuildArch: noarch

%description -n installer-feature-integalert-stage3
Run integrity check after install (chroot files).

%package -n %pname-vm-check
Summary: Run VM integrity check before VM target and every 5 mins
Group: Monitoring
BuildArch: noarch

%description -n %pname-vm-check
Includes service that 'integalert vm' is configured to run before
'vm.target' and every 5 mins (using a timer).

%package -n %pname-trigger-pve
Summary: Lock down PVE cluster VMs on integrity failure
Group: Monitoring
ExclusiveArch: x86_64 aarch64

%description -n %pname-trigger-pve
Lock down PVE cluster VMs on integalert_vm.service failure.

%prep
%setup

%install
install -D -m 0644 65-integrity.preset %buildroot/lib/systemd/system-preset/65-integrity.preset
install -D -m 0755 90-integrity-init.sh  %buildroot%_datadir/install2/postinstall.d/90-integrity-init.sh
install -D -m 0644 integalert.service %buildroot%_unitdir/integalert.service
install -D -m 0644 integalert_vm.service %buildroot%_unitdir/integalert_vm.service
install -D -m 0644 integalert_vm.timer %buildroot%_unitdir/integalert_vm.timer
install -D -m 0700 integalert %buildroot/sbin/integalert

install -D -m 0600 osec/integalert/dirs.conf %buildroot/%_sysconfdir/osec/integalert/dirs.conf
install -D -m 0600 osec/integalert_vm/dirs.conf %buildroot/%_sysconfdir/osec/integalert_vm/dirs.conf
install -D -m 0755 osec/integalert_vm/trigger.d/10-pve-lock-seabios %buildroot/%_sysconfdir/osec/integalert_vm/trigger.d/10-pve-lock-seabios
install -D -m 0755 osec/integalert_vm/trigger.d/20-pve-lock-ovmf %buildroot/%_sysconfdir/osec/integalert_vm/trigger.d/20-pve-lock-ovmf
install -D -m 0755 osec/integalert_vm/trigger.d/30-pve-lock-nodes %buildroot/%_sysconfdir/osec/integalert_vm/trigger.d/30-pve-lock-nodes
install -D -m 0600 osec/integalert_container/dirs.conf %buildroot/%_sysconfdir/osec/integalert_container/dirs.conf

mkdir -p %buildroot/%_sysconfdir/osec/integalert/trigger.d
mkdir -p %buildroot/%_sysconfdir/osec/integalert_container/trigger.d

%post -n %pname
if [ $1 -ge 2 ]; then
    if systemctl -q is-enabled integalert.service; then
        systemctl daemon-reload
        systemctl -q preset integalert.service
    fi
fi

%files -n installer-feature-integalert-stage2
%_datadir/install2/postinstall.d/90-integrity-init.sh

%files -n installer-feature-integalert-stage3

%files -n %pname
%_unitdir/integalert.service
/lib/systemd/system-preset/65-integrity.preset
/sbin/integalert
%dir %_sysconfdir/osec/integalert*
%config(noreplace) %_sysconfdir/osec/integalert*/*.conf

%files -n %pname-vm-check
%_unitdir/integalert_vm.service
%_unitdir/integalert_vm.timer

%files -n %pname-trigger-pve
%dir %_sysconfdir/osec/integalert/trigger.d
%dir %_sysconfdir/osec/integalert_vm/trigger.d
%dir %_sysconfdir/osec/integalert_container/trigger.d
%config(noreplace) %_sysconfdir/osec/integalert_vm/trigger.d/*-pve-*

%changelog
* Tue Dec 26 2023 Paul Wolneykien <manowar@altlinux.org> 0.4.3-alt2
- Make *-trigger-pve package exclusive arch: x86_64 aarch64.

* Tue Dec 19 2023 Paul Wolneykien <manowar@altlinux.org> 0.4.3-alt1
- Check that the selected osec profile exists before running osec.
- Add two more packages for VM checking and locking (PVE).
- Added 3 VM lock down scripts for PVE.
- Run triggers in /etc/osec/*/trigger.d after a failed
  check.
- Added VM check service and timer.
- Clarify the unit's description.
- Isolate the emergency.target on failure, set to required by
  sysinit.target.
- Don't directly write to TTY: rely on StandardError=tty.
- Use /etc/osec/*/sender script to write down the report and
  to send a summary message to the system log.
- Allow to explicitly specify the 'check' mode ('integalert check').
- Use the same /etc/osec/*/ config both for 'check' and 'fix' modes.
- Write logs to /var/log/integalert* and /var/log/integalert*_logs.

* Fri Nov 03 2023 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt4
- Rename installer packages to installer-feature-integalert-*.

* Thu Nov 02 2023 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt3
- Obsolete integ < 0.4.2-alt2.

* Wed Nov 01 2023 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt2
- Remove 65-settings.sh and the corresponding package.
- Rename package to "integalert".
- Don't require 'checker' package.
- Add dirs.conf for "vm" and "container" profiles.

* Tue Apr 25 2023 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt1
- Provide the default dirs.conf for 'integalert' profile as a part of
  the 'integ' package.
- Output a warning and exit if dirs.conf is empty.
- Support for 'container' and 'vm' profiles.

* Fri Oct 02 2020 Paul Wolneykien <manowar@altlinux.org> 0.4.1-alt1
- Set integalert service state from its preset after system
  installation.

* Thu Oct 01 2020 Paul Wolneykien <manowar@altlinux.org> 0.4-alt1
- Setup OSEC for full journal output after integrity database
  initialization after install.
- Update: Make integ inself require osec-controls.
- Moved postinstall.d/90-integrity-init.sh to the new stage2 package.
- Use "IMMUTABLE_DATABASE" configuration option for read-only osec runs.
  This requires osec-cronjob >= 1.3.1-alt2.
- Don't modify the main pipe.conf file after 'integ' package
  installation.
- Always create /var/log/lastosec_logs.
- Don't display a warning in "fix" mode.
- Run osec using 'integalert' and 'integalert_fix' sub-configs.
- Initialize OSEC after install, don't initialize it at first boot.
- Setup osec.cron for read-only use and full journal output after
  install.

* Mon Sep 07 2020 Denis Medvedev <nbr@altlinux.org> 0.3-alt3
- added missing requires, set control of osec to journal
(essential).

* Mon Sep 07 2020 Denis Medvedev <nbr@altlinux.org> 0.3-alt2
- revert direct execution of osec from integalert,
lastosec data is needed too.

* Sat Sep 05 2020 Alexey Shabalin <shaba@altlinux.org> 0.3-alt1
- update systemd unit
- not requires plymouth
- improve failure output
- direct execute osec for check integrity in integalert

* Mon Oct 28 2019 Denis Medvedev <nbr@altlinux.org> 0.2-alt5
- reenable service (to switch from required to wanted from sysinit)
only when it is an upgrade, not on initial install.

* Fri Oct 11 2019 Denis Medvedev <nbr@altlinux.org> 0.2-alt4
- force systemd reconfigure dependencies, fix archiving of osec messages

* Wed Oct 09 2019 Denis Medvedev <nbr@altlinux.org> 0.2-alt3
- force plymouth quit on integrity error

* Wed Oct 09 2019 Denis Medvedev <nbr@altlinux.org> 0.2-alt2
- integalert wanted, not required for sysinit by default

* Wed Oct 09 2019 Denis Medvedev <nbr@altlinux.org> 0.2-alt1
- fix integalert behavour, see nagwad package for modified osec.pipe. Also
disabled interruption of boot by default

* Mon Oct 07 2019 Denis Medvedev <nbr@altlinux.org> 0.1-alt4
- Fixed wrong separator in  Conflicts line. Also fixed permissions on a unit.

* Wed Sep 25 2019 Denis Medvedev <nbr@altlinux.org> 0.1-alt3
- latest update to sisyphus

* Thu Aug 22 2019 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.18
- fixed dependencies for integalert service, avoiding loops.

* Wed Mar 20 2019 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.17
- do not start service, it is needed only on boot.

* Mon Mar 18 2019 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.16
- fixes on integ integalert service

* Wed Mar 28 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.15
- grub is modified adding option in some other place. Removed
addition of duplicated entry

* Mon Mar 26 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.14
- fixed delimiters

* Mon Mar 26 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.13
- removed perl parts of settings

* Thu Mar 22 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.12
- fixed place of postinstall.d

* Wed Mar 21 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.11
- moved to postinstall.d, added features from branding

* Thu Mar 01 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.10
- separated to two packets: general settings and integrity service
Removed rhosts from skel: it harms selinux settings.

* Thu Jan 18 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.9
- integrity check strictly before user login now

* Wed Jan 17 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.8
- added "Before" to  unit to make it start before DM

* Wed Jan 17 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.7
- changed wanted to required in unit

* Wed Jan 17 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.6
- added alerting on integrity checks on boot

* Wed Dec 13 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.5
- added fixed rhosts, added dependency to custom settings checker

* Mon Dec 11 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.3
- Updated settings

* Fri Dec 01 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.2
- fixed permissions

* Wed Nov 29 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.1
- backport to c8

* Wed Nov 29 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt1
Initial release
