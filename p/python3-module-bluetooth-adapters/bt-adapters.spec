Name: python3-module-bluetooth-adapters
Version: 0.15.3
Release: alt1

Summary: Tools to enumerate and find Bluetooth Adapters
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/bluetooth-adapters/

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(bleak)
BuildRequires: python3(usb_devices)

%description
%summary

%prep
%setup

%build
%pyproject_deps_resync_build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/bluetooth_adapters
%python3_sitelibdir/bluetooth_adapters-%version.dist-info

%changelog
* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.15.3-alt1
- 0.15.3 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.15.2-alt1
- 0.15.2 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt1
- 0.6.0 released

* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- 0.4.1 released
