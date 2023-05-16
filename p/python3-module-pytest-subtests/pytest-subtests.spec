%define  oname pytest-subtests

%def_with check

Name:    python3-module-%oname
Version: 0.11.0
Release: alt1

Summary: Support for unittest subTest() and subtests fixture

License: MIT
Group:   Development/Python3
URL:     https://github.com/pytest-dev/pytest-subtests

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-attrs
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3

%files
%doc *.rst
%python3_sitelibdir/pytest_subtests.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/pytest_subtests-%version.dist-info

%changelog
* Tue May 16 2023 Grigory Ustinov <grenka@altlinux.org> 0.11.0-alt1
- Automatically updated to 0.11.0.

* Tue Apr 25 2023 Stanislav Levin <slev@altlinux.org> 0.10.0-alt2
- Fixed FTBFS (pytest 7.3.1).

* Thu Feb 16 2023 Grigory Ustinov <grenka@altlinux.org> 0.10.0-alt1
- Automatically updated to 0.10.0.

* Sun Oct 30 2022 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt1
- Automatically updated to 0.9.0.

* Thu Jul 21 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus.
