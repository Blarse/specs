Name:    solaar
Version: 1.1.13
Release: alt1

Summary: Device manager for Logitech Unifying Receiver
License: GPL-2.0
Group:   System/Configuration/Hardware
URL:     https://pwr-solaar.github.io/Solaar/

BuildArch: noarch

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir
BuildRequires:  python3-module-pyudev

Requires: unifying-receiver-udev

%add_python3_req_skip gi.repository.GObject gi.repository.Gdk

# require typelib(AyatanaAppIndicator3) instead typelib(AppIndicator3)
%add_typelib_req_skiplist typelib(AppIndicator3)

Source0: https://github.com/pwr/Solaar/archive/%{version}.tar.gz
Patch1: solaar-paths.patch

%description
Solaar is a device manager for Logitech's Unifying Receiver
peripherals. It is able to pair/unpair devices to the receiver, and
for most devices read battery status.

It comes in two flavors, command-line and GUI. Both are able to list
the devices paired to a Unifying Receiver, show detailed info for each
device, and also pair/unpair supported devices with the receiver.

%package doc
Summary: Documentation for Solaar
Group: Documentation
Requires: %name = %EVR

%description doc
This package provides documentation for Solaar, a device manager for
Logitech's Unifying Receiver peripherals.

%prep
%setup -n Solaar-%version
%patch1 -p1

%build
tools/po-compile.sh
%python3_build

%install
%python3_install
%find_lang %name

%files -f %name.lang
%doc COPYRIGHT share/README
%config(noreplace) %_sysconfdir/xdg/autostart/solaar.desktop
%config %attr (644,root,root) %_udevrulesdir/*.rules
%_bindir/solaar
%python3_sitelibdir/*
%_desktopdir/solaar.desktop
%_iconsdir/hicolor/scalable/apps/*.svg
%_iconsdir/hicolor/32x32/apps/*.png
%_datadir/metainfo/*.metainfo.xml

%files doc
%doc docs

%changelog
* Sun May 12 2024 Andrey Cherepanov <cas@altlinux.org> 1.1.13-alt1
- New version.

* Mon Apr 29 2024 Andrey Cherepanov <cas@altlinux.org> 1.1.12-alt1
- New version.

* Fri Feb 23 2024 Andrey Cherepanov <cas@altlinux.org> 1.1.11-alt1
- New version.

* Sun Sep 24 2023 Andrey Cherepanov <cas@altlinux.org> 1.1.10-alt1
- New version.

* Thu Apr 06 2023 Andrey Cherepanov <cas@altlinux.org> 1.1.9-alt1
- new version 1.1.9

* Mon Mar 27 2023 Andrey Cherepanov <cas@altlinux.org> 1.1.8-alt3
- Fix udev rules directory.

* Mon Mar 06 2023 Anton Midyukov <antohami@altlinux.org> 1.1.8-alt2
- NMU: require typelib(AyatanaAppIndicator3) instead typelib(AppIndicator3)

* Sun Dec 18 2022 Andrey Cherepanov <cas@altlinux.org> 1.1.8-alt1
- New version.

* Sat Nov 05 2022 Andrey Cherepanov <cas@altlinux.org> 1.1.7-alt1
- New version.

* Wed Oct 26 2022 Andrey Cherepanov <cas@altlinux.org> 1.1.6-alt1
- New version.

* Fri Sep 16 2022 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- New version.

* Sun Jul 10 2022 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1
- New version.

* Mon Apr 25 2022 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- New version.

* Tue Apr 12 2022 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt2
- Completed Russian translation (thanks Olesya Gerasimenko).

* Sun Mar 27 2022 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- New version.

* Sun Jan 02 2022 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- New version.

* Tue Dec 07 2021 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt3
- Fix Lighting translation.

* Mon Dec 06 2021 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2
- Complete Russian translation.

* Wed Dec 01 2021 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Thu Nov 11 2021 Andrey Cherepanov <cas@altlinux.org> 1.0.7-alt2
- Compile and package localization files.
- Package metainfo.
- Fix udev rules patch and fix install autostart and udev rules by patch.

* Sun Oct 03 2021 Andrey Cherepanov <cas@altlinux.org> 1.0.7-alt1
- New version.

* Mon Apr 26 2021 Andrey Cherepanov <cas@altlinux.org> 1.0.6-alt1
- New version.

* Sun Feb 28 2021 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- New version.

* Fri Oct 23 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- New version.

* Thu Aug 06 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- New version.
- Package udev rules.
- Fix License tag according to SPDX.

* Wed May 27 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- New version.

* Tue May 12 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- New version.

* Mon Apr 22 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.2.0.225.gitd021d87-alt1
- Build from recent commit for pyhon3.7 compatibility.

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.2-alt1.2
- rebuild

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- Build for Sisyphus from Fedora
