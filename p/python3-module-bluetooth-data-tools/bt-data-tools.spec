Name: python3-module-bluetooth-data-tools
Version: 0.4.0
Release: alt1

Summary: Tools for converting bluetooth data and packets
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/bluetooth-data-tools/

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildRequires(pre): rpm-build-pyproject
BuildRequires: gcc-c++
BuildRequires: python3(cython)
%pyproject_builddeps_build
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)

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
%python3_sitelibdir/bluetooth_data_tools
%python3_sitelibdir/bluetooth_data_tools-%version.dist-info

%changelog
* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.0-alt1
- 0.4.0 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1 released

