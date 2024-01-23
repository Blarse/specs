%define pypi_name xsdata

%def_with check

Name:    python3-module-%pypi_name
Version: 24.1
Release: alt1

Summary: Naive XML & JSON Bindings for python

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/xsdata
VCS:     https://github.com/tefra/xsdata

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-benchmark
BuildRequires: python3-module-lxml
BuildRequires: python3-module-typing-extensions
BuildRequires: python3-module-click
BuildRequires: python3-module-toposort
BuildRequires: python3-module-docformatter
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-requests
BuildRequires: python3-module-click-default-group
BuildRequires: ruff
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 24.1-alt1
- Automatically updated to 24.1.

* Thu Dec 28 2023 Grigory Ustinov <grenka@altlinux.org> 23.8-alt1
- Initial build for Sisyphus.
