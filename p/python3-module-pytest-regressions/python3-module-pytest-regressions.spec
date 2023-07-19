%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-regressions

# unstable tests
%def_with check

Name: python3-module-%pypi_name
Version: 2.4.2
Release: alt2
Summary: Pytest plugin for regression testing
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-regressions/
Vcs: https://github.com/ESSS/pytest-regressions
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter tox restructuredtext-lint
%pyproject_builddeps_metadata_extra dev
%endif

%description
Fixtures to write regression tests.

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
%pyproject_run_pytest -ra tests -Wignore

%files
%doc README.rst
%python3_sitelibdir/pytest_regressions/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 17 2023 Stanislav Levin <slev@altlinux.org> 2.4.2-alt2
- Fixed FTBFS (numpy 1.25.0).

* Mon Apr 24 2023 Stanislav Levin <slev@altlinux.org> 2.4.2-alt1
- 2.4.1 -> 2.4.2.

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 2.4.1-alt1
- initial build for Sisyphus

