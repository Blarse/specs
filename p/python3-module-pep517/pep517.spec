%define _unpackaged_files_terminate_build 1
%define pypi_name pep517

%def_with check

Name: python3-module-%pypi_name
Version: 0.13.1
Release: alt1

Summary: API to call PEP 517 hooks for building Python packages

Group: Development/Python3
License: MIT
Url: https://github.com/pypa/pep517

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit_core)

%if_with check
BuildRequires: python3(setuptools)
BuildRequires: python3(testpath)
BuildRequires: python3(pytest)
BuildRequires: python3(tomli)
%endif

%description
PEP 517 specifies a standard API for systems which build Python packages.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/pep517/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Feb 05 2024 Anton Vyatkin <toni@altlinux.org> 0.13.1-alt1
- New version 0.13.1.

* Fri Jan 26 2024 Grigory Ustinov <grenka@altlinux.org> 0.13.0-alt3
- Fixed FTBFS.

* Thu Nov 10 2022 Stanislav Levin <slev@altlinux.org> 0.13.0-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 0.13.0-alt1
- 0.12.0 -> 0.13.0.

* Tue Jan 11 2022 Stanislav Levin <slev@altlinux.org> 0.12.0-alt1
- 0.10.0 -> 0.12.0.

* Thu Apr 22 2021 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt2
- initial build for ALT Sisyphus

* Tue Apr 20 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 0.10.0-alt1
- new version (0.10.0) with rpmgs script



