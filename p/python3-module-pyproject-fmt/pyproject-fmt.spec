%define _unpackaged_files_terminate_build 1
%define pypi_name pyproject-fmt

%def_with check

Name: python3-module-%pypi_name
Version: 0.13.1
Release: alt1
Summary: Format pyproject.toml file
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyproject-fmt
VCS: https://github.com/tox-dev/pyproject-fmt.git
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
%summary.

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
%doc README.md
%_bindir/%pypi_name
%python3_sitelibdir/pyproject_fmt/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Aug 14 2023 Stanislav Levin <slev@altlinux.org> 0.13.1-alt1
- 0.13.0 -> 0.13.1.

* Fri Jul 21 2023 Stanislav Levin <slev@altlinux.org> 0.13.0-alt1
- 0.12.1 -> 0.13.0.

* Wed Jun 21 2023 Stanislav Levin <slev@altlinux.org> 0.12.1-alt1
- 0.12.0 -> 0.12.1.

* Tue Jun 20 2023 Stanislav Levin <slev@altlinux.org> 0.12.0-alt1
- 0.11.2 -> 0.12.0.

* Wed May 10 2023 Stanislav Levin <slev@altlinux.org> 0.11.2-alt1
- 0.11.1 -> 0.11.2.

* Tue May 02 2023 Stanislav Levin <slev@altlinux.org> 0.11.1-alt1
- 0.10.0 -> 0.11.1.

* Tue Apr 25 2023 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- 0.9.2 -> 0.10.0.

* Wed Mar 01 2023 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1
- 0.4.1 -> 0.9.2.

* Thu Nov 24 2022 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1
- 0.4.0 -> 0.4.1.

* Wed Nov 23 2022 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- 0.3.5 -> 0.4.0.

* Sat Aug 13 2022 Stanislav Levin <slev@altlinux.org> 0.3.5-alt1
- 0.3.3 -> 0.3.5.

* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus.
