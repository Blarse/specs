Name: python3-module-bleak
Version: 0.17.0
Release: alt1

Summary: Bluetooth Low Energy platform Agnostic Klient
License: MIT
Group: Development/Python
Url: https://pypi.org/project/bleak/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)

%description
Bleak is a GATT client software, capable of connecting to BLE devices
acting as GATT servers. It is designed to provide a asynchronous,
cross-platform Python API to connect and communicate with e.g. sensors.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# filter out non-linux backend's reqs
%add_python3_req_skip CoreBluetooth Foundation libdispatch objc
%add_python3_req_skip android.broadcast android.permissions
%add_python3_req_skip bleak_winrt.windows.devices.bluetooth
%add_python3_req_skip bleak_winrt.windows.devices.bluetooth.advertisement
%add_python3_req_skip bleak_winrt.windows.devices.bluetooth.genericattributeprofile
%add_python3_req_skip bleak_winrt.windows.devices.enumeration
%add_python3_req_skip bleak_winrt.windows.foundation
%add_python3_req_skip bleak_winrt.windows.storage.streams

%files
%python3_sitelibdir/bleak
%python3_sitelibdir/bleak-%version.dist-info

%changelog
* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.17.0-alt1
- 0.17.0 released
