%define _unpackaged_files_terminate_build 1
%define _runtimedir /run
%define _localstatedir /var
#Use GTK+ instead of Xlib
%def_with gtk

Name: spice-vdagent
Version: 0.22.1
Release: alt2
Epoch: 1
Summary: Agent for Spice guests
Group: Networking/Remote access
License: GPLv3+
Url: http://spice-space.org/

# VCS-git: https://gitlab.freedesktop.org/spice/linux/vd_agent.git
Source: %name-%version.tar
Source2: spice-vdagentd.init-alt
Patch: %name-%version.patch

BuildRequires(pre): rpm-macros-systemd
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.50
%{?_with_gtk:BuildRequires: pkgconfig(gtk+-3.0) >= 3.22}
BuildRequires: pkgconfig(xfixes) pkgconfig(xrandr) >= 1.3 pkgconfig(xinerama) pkgconfig(x11)
BuildRequires: pkgconfig(spice-protocol) >= 0.14.3
BuildRequires: pkgconfig(alsa) >= 1.0.22
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(pciaccess) >= 0.10
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(systemd) pkgconfig(libsystemd) >= 209
BuildRequires: pkgconfig(udev)
BuildRequires: desktop-file-utils

%description
Spice agent for Linux guests offering the following features:

Features:
* Client mouse mode (no need to grab mouse by client, no mouse lag)
  this is handled by the daemon by feeding mouse events into the kernel
  via uinput. This will only work if the active X-session is running a
  spice-vdagent process so that its resolution can be determined.
* Automatic adjustment of the X-session resolution to the client resolution
* Support of copy and paste (text and images) between the active X-session
  and the client

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
    %{subst_with gtk} \
	--with-session-info=auto \
	--with-init-script=systemd+redhat

%make_build

%install
%makeinstall_std tmpfilesdir=%_tmpfilesdir udevrulesdir=%_udevrulesdir systemdunitdir=%_unitdir userunitdir=%_user_unitdir
install -m 0755 %SOURCE2 %buildroot%_initdir/spice-vdagentd

# fix autostart in KDE Plasma
cp -ar %buildroot/%_sysconfdir/xdg/autostart/spice-vdagent{,-kde}.desktop
desktop-file-install --mode=0644 --dir %buildroot/%_sysconfdir/xdg/autostart \
	--add-not-show-in="KDE" \
	%buildroot/%_sysconfdir/xdg/autostart/spice-vdagent.desktop
desktop-file-install --mode=0644 --dir %buildroot/%_sysconfdir/xdg/autostart \
	--add-only-show-in="KDE" \
	--remove-key="X-GNOME-Autostart-Phase" \
	--set-key="Exec" --set-value="/usr/bin/spice-vdagent -x" \
	%buildroot/%_sysconfdir/xdg/autostart/spice-vdagent-kde.desktop

%post
%post_service spice-vdagentd
%systemd_user_post spice-vdagent.service

%preun
%preun_service spice-vdagentd
%systemd_user_preun spice-vdagent.service

%files
%doc COPYING CHANGELOG.md README.md
%_udevrulesdir/*.rules
%_tmpfilesdir/spice-vdagentd.conf
%_initddir/spice-vdagentd
%_unitdir/*
%_userunitdir/*
%_bindir/spice-vdagent
%_sbindir/spice-vdagentd
%_sysconfdir/xdg/autostart/spice-vdagent*.desktop
%_datadir/gdm/autostart/LoginWindow/spice-vdagent.desktop
%_datadir/gdm/greeter/autostart/spice-vdagent.desktop
%_man1dir/*

%changelog
* Mon Jun 24 2024 Alexey Shabalin <shaba@altlinux.org> 1:0.22.1-alt2
- fix use systemd rpm macros in spec

* Mon Sep 11 2023 Sergey V Turchin <zerg@altlinux.org> 1:0.22.1-alt1.1
- NMU: fix systemd user session startup loop (closes: 47329)

* Tue Jul 04 2023 Alexey Shabalin <shaba@altlinux.org> 1:0.22.1-alt1
- 0.22.1

* Mon Sep 26 2022 Slava Aseev <ptrnine@altlinux.org> 1:0.21.0-alt3
- fix autostart in KDE Plasma (attempt number 2)

* Fri Sep 23 2022 Sergey V Turchin <zerg@altlinux.org> 1:0.21.0-alt2
- fix autostart in KDE Plasma

* Thu Jan 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.21.0-alt1
- new version 0.21.0 (Fixes CVE-2020-25650, CVE-2020-25651, CVE-2020-25652, CVE-2020-25653).

* Wed Mar 25 2020 Alexey Shabalin <shaba@altlinux.org> 1:0.20.0-alt1
- new version 0.20.0

* Sun Jun 02 2019 Alexey Shabalin <shaba@altlinux.org> 1:0.19.0-alt1
- 0.19.0

* Tue Apr 23 2019 Alexey Shabalin <shaba@altlinux.org> 1:0.18.0-alt3
- downgrade to 0.18.0

* Tue Apr 16 2019 Alexey Shabalin <shaba@altlinux.org> 0.19.0-alt1
- 0.19.0

* Fri Apr 05 2019 Alexey Shabalin <shaba@altlinux.org> 0.18.0-alt2
- backport some patches from upstream
- Update all paths /var/run -> /run

* Mon Jul 09 2018 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt1
- 0.18.0
- Use GTK+ instead of Xlib

* Thu Jun 16 2016 Alexey Shabalin <shaba@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Fri Jul 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Fri Apr 25 2014 Alexey Shabalin <shaba@altlinux.ru> 0.15.0-alt1.git7d858d
- upstream git snaphot 7d858d5064fd0c26454b72bf9fe3e0472f31e34f

* Mon May 20 2013 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Thu Apr 11 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Tue Sep 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Tue Apr 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Wed Aug 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Mon Mar 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- initial build for ALT Linux Sisyphus
