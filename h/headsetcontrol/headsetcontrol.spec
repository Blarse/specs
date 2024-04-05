
%define _unpackaged_files_terminate_build 1
%add_optflags -Wno-error=unused-result

Name:     headsetcontrol
Version:  3.0.0
Release:  alt1

Summary:  A tool to control certain aspects of USB-connected headsets on Linux
License:  GPL-3.0
Group:    System/Configuration/Hardware
Url:      https://github.com/Sapd/HeadsetControl

Source:   %name-%version.tar
Patch:    %name-%version-%release.patch

BuildRequires: cmake ctest libhidapi-devel

%description
A tool to control certain aspects of USB-connected headsets on
Linux.  Currently, support is provided for adjusting sidetone,
getting battery state, controlling LEDs, and setting the inactive
time.  Supported headsets include Logitech G930, G533, G633, G933,
SteelSeries Arctis 1/7/9/PRO 2019, Corsair VOID (Pro) and others.

%prep
%setup
%autopatch -p1

%build
%cmake -D udev_rules_dir=%_udevrulesdir
%cmake_build

%install
%cmakeinstall_std

%check
%cmake_build -t check

%files
%_bindir/%name
%_udevrulesdir/70-headsets.rules
%doc README.md

%changelog
* Tue Apr 02 2024 Ivan A. Melnikov <iv@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue May 02 2023 Ivan A. Melnikov <iv@altlinux.org> 2.7.0-alt1
- 2.7.0

* Mon Jul 18 2022 Ivan A. Melnikov <iv@altlinux.org> 2.6.1-alt1
- 2.6.1

* Tue Nov 16 2021 Ivan A. Melnikov <iv@altlinux.org> 2.6-alt1
- 2.6

* Wed May 26 2021 Ivan A. Melnikov <iv@altlinux.org> 2.4-alt1.git0a1c2ef
- initial build
  + build from snapshot for Steelseries Arctics 1 battery support
