%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-env
%define mod_name pytest_env

%def_with check

Name: python3-module-%pypi_name
Version: 0.8.1
Release: alt1
Summary: py.test plugin that allows you to add environment variables
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-env
Vcs: https://github.com/pytest-dev/pytest-env
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
This is a pytest plugin that enables you to set environment variables in a
pytest.ini or pyproject.toml file.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu May 04 2023 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus.
