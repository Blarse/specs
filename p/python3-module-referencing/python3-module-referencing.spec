%define pypi_name referencing

%def_with check

Name: python3-module-%pypi_name
Version: 0.29.1
Release: alt1

Summary: Cross-specification JSON referencing (JSON Schema, OpenAPI, and the one you just made up!)
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/referencing
VCS: https://github.com/python-jsonschema/referencing
BuildArch: noarch
Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-subtests
BuildRequires: python3-module-rpds-py
BuildRequires: python3-module-jsonschema
%endif

%description
An implementation-agnostic implementation of JSON reference resolution.
In other words, a way for e.g. JSON Schema tooling to resolve the $ref keyword
across all drafts without needing to implement support themselves.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %EVR

%description tests
An implementation-agnostic implementation of JSON reference resolution.
In other words, a way for e.g. JSON Schema tooling to resolve the $ref keyword
across all drafts without needing to implement support themselves.

This package contains tests for %pypi_name.

%prep
%setup -n %pypi_name-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.* COPYING
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%pypi_name/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Wed Jul 12 2023 Anton Vyatkin <toni@altlinux.org> 0.29.1-alt1
- Initial build for Sisyphus
