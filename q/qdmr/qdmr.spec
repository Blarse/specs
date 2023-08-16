
Name: qdmr
Version: 0.11.3
Release: alt1

Summary: GUI application and command-line-tool to program DMR radios
License: GPLv3+
Group: Engineering

Url: https://dm3mat.darc.de/qdmr
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libusb-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-location-devel
BuildRequires: qt5-serialport-devel
BuildRequires: qt5-tools-devel
BuildRequires: rpm-macros-cmake
BuildRequires: findutils

%description
QDMR is a friendly code-plug programming software for DMR radios.
QDMR supports radios by several vendors, and stores code-plug in
a human readable format.

%package -n libdmrconf
Summary: DMR radios programming library
Group: System/Libraries

%description -n libdmrconf
QDMR is a friendly code-plug programming software for DMR radios.
libdmrconf handles the actual programming of radios via UART and
conversion of code-plug between human readable and vendor-specific
binary formats.

%package -n libdmrconf-devel
Summary: DMR radios programming library - development files
Group: Development/KDE and QT
Requires: qt5-base-devel
Requires: libyaml-cpp-devel

%description -n libdmrconf-devel
QDMR is a friendly code-plug programming software for DMR radios.
libdmrconf handles the actual programming of radios via UART and
conversion of code-plug between human readable and vendor-specific
binary formats. This package is useful for developing software
with libdmrconf. It is not required for QDMR users.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmakeinstall_std
if [ -d %buildroot/etc/udev/rules.d ]; then
	# XXX: relocate udev rules to /lib/udev/rules.d
	mkdir -p %buildroot/%_udevrulesdir
	find %buildroot/etc/udev/rules.d -type f -print0 | \
	xargs -0 -r mv -f --target-directory=%buildroot/%_udevrulesdir
fi

%files
%doc README.md
%_bindir/qdmr
%_bindir/dmrconf
%_udevrulesdir/*
%_datadir/icons/hicolor/*/*.png
%_datadir/applications/qdmr.desktop

%files -n libdmrconf
%prefix/%_lib/libdmrconf.so.*

%files -n libdmrconf-devel
%prefix/%_lib/libdmrconf.so
%prefix/include/libdmrconf/*.hh
%prefix/include/libdmrconf/*.h

%changelog
* Wed Aug 16 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.11.3-alt1
- v0.11.3, amongst other things
  + Fixed crash on missing access rights for TyT devices
  + Fixed encoding for AnyTone devices (programmable keys, mic gain, etc)

* Thu Mar 30 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.11.2-alt2
- Relocated udev rules to /lib/udev, no functional changes intended

* Wed Feb 08 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.11.2-alt1
- v0.11.2, amongst other things
  + BTECH DMR-6X2UV support
  + Call-sign DB for BTECH DM-1701, Retevis RT-84

* Wed Nov 30 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.10.4-alt1
- v0.10.3
- Amongst other things fixes detection of DM-1701

* Sun May 22 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.10.2.2-alt1
- Initial build
