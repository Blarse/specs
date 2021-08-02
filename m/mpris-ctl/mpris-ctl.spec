Name: mpris-ctl
Version: 0.8.4
Release: alt1

Summary: CLI tool for controlling MPRIS-enabled audio players
License: MIT
Group: Sound
Url: https://github.com/mariusor/mpris-ctl

Source: %name-%version-%release.tar

BuildRequires: /usr/bin/scdoc
BuildRequires: pkgconfig(dbus-1)

%description
Minimalistic cli tool for controlling audio players exposing a MPRIS DBus
interface, targeted at keyboard based WMs.

%prep
%setup

%build
CC=gcc make release

%install
make DESTDIR=%buildroot INSTALL_PREFIX=%_prefix install

%files
%doc README* LICENSE
%_bindir/mpris-ctl
%_man1dir/mpris-ctl.1*

%changelog
* Mon Aug 02 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.4-alt1
- 0.8.4 released
