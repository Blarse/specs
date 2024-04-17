%define _unpackaged_files_terminate_build 1
%define pypi_name tox

%def_with check

Name: python3-module-%pypi_name
Version: 3.27.1
Release: alt4

Summary: virtualenv-based automation of test activities
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/tox/
VCS: https://github.com/tox-dev/tox
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: /proc
%pyproject_builddeps_metadata_extra testing
# used in test_parallel_error_report,
# upstream relies on being run within venv
BuildRequires: python3-module-pip
%endif

%description
Tox as is a generic virtualenv management and test command line tool you
can use for:

* checking your package installs correctly with different Python
  versions and interpreters
* running your tests in each of the environments, configuring your test
  tool of choice
* acting as a frontend to Continuous Integration servers, greatly
  reducing boilerplate and merging CI and shell-based testing.

%prep
%setup
%patch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

pushd %buildroot%_bindir
for i in $(ls); do
        mv $i $i.py3
done
popd

%check
export VIRTUALENV_SYSTEM_SITE_PACKAGES=YES
export TOX_LIMITED_SHEBANG=1
export PIP_NO_BUILD_ISOLATION=NO
%pyproject_run_pytest -vra -m "not internet"

%files
%_bindir/tox.py3
%_bindir/tox-quickstart.py3
%python3_sitelibdir/tox/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Apr 17 2024 Stanislav Levin <slev@altlinux.org> 3.27.1-alt4
- Fixed FTBFS (setuptools 69.3.0).

* Mon Feb 12 2024 Stanislav Levin <slev@altlinux.org> 3.27.1-alt3
- Fixed FTBFS (Pytest 8).

* Fri Jan 26 2024 Stanislav Levin <slev@altlinux.org> 3.27.1-alt2
- Fixed FTBFS (Python 3.12).

* Mon Nov 14 2022 Stanislav Levin <slev@altlinux.org> 3.27.1-alt1
- 3.27.0 -> 3.27.1.

* Thu Oct 27 2022 Stanislav Levin <slev@altlinux.org> 3.27.0-alt1
- 3.26.0 -> 3.27.0.

* Thu Sep 22 2022 Stanislav Levin <slev@altlinux.org> 3.26.0-alt1
- 3.25.1 -> 3.26.0.

* Thu Jul 21 2022 Stanislav Levin <slev@altlinux.org> 3.25.1-alt1
- 3.24.5 -> 3.25.1.

* Thu Jan 13 2022 Stanislav Levin <slev@altlinux.org> 3.24.5-alt1
- 3.24.4 -> 3.24.5.

* Fri Sep 17 2021 Stanislav Levin <slev@altlinux.org> 3.24.4-alt1
- 3.24.3 -> 3.24.4.

* Fri Sep 10 2021 Stanislav Levin <slev@altlinux.org> 3.24.3-alt1
- 3.24.0 -> 3.24.3.

* Mon Jul 26 2021 Stanislav Levin <slev@altlinux.org> 3.24.0-alt1
- 3.23.1 -> 3.24.0.

* Fri May 07 2021 Stanislav Levin <slev@altlinux.org> 3.23.1-alt1
- 3.23.0 -> 3.23.1.

* Sat Apr 24 2021 Stanislav Levin <slev@altlinux.org> 3.23.0-alt1
- 3.20.1 -> 3.23.0.

* Fri Oct 23 2020 Stanislav Levin <slev@altlinux.org> 3.20.1-alt1
- 3.15.0 -> 3.20.1.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 3.15.0-alt3
- Stopped Python2 package build.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 3.15.0-alt2
- Unpinned pytest-mock.

* Tue May 12 2020 Stanislav Levin <slev@altlinux.org> 3.15.0-alt1
- 3.14.2 -> 3.15.0.

* Wed Apr 29 2020 Stanislav Levin <slev@altlinux.org> 3.14.2-alt2
- Fixed FTBFS.

* Thu Dec 12 2019 Stanislav Levin <slev@altlinux.org> 3.14.2-alt1
- 3.14.1 -> 3.14.2.

* Fri Nov 15 2019 Stanislav Levin <slev@altlinux.org> 3.14.1-alt1
- 3.14.0 -> 3.14.1.

* Fri Oct 11 2019 Stanislav Levin <slev@altlinux.org> 3.14.0-alt1
- 3.13.2 -> 3.14.0.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 3.13.2-alt2
- Fixed testing against Pytest 5.

* Fri Aug 02 2019 Stanislav Levin <slev@altlinux.org> 3.13.2-alt1
- 3.12.1 -> 3.13.2.

* Fri May 24 2019 Stanislav Levin <slev@altlinux.org> 3.12.1-alt1
- 3.11.1 -> 3.12.1.

* Thu May 16 2019 Stanislav Levin <slev@altlinux.org> 3.11.1-alt1
- 3.11.0 -> 3.11.1.

* Thu May 16 2019 Stanislav Levin <slev@altlinux.org> 3.11.0-alt1
- 3.10.0 -> 3.11.0.

* Mon May 13 2019 Stanislav Levin <slev@altlinux.org> 3.10.0-alt1
- 3.9.0 -> 3.10.0.

* Wed May 01 2019 Stanislav Levin <slev@altlinux.org> 3.9.0-alt1
- 3.7.0 -> 3.9.0.

* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- 3.6.1 -> 3.7.0.

* Mon Dec 31 2018 Stanislav Levin <slev@altlinux.org> 3.6.1-alt1
- 3.5.3 -> 3.6.1.

* Mon Oct 29 2018 Stanislav Levin <slev@altlinux.org> 3.5.3-alt1
- 3.5.2 -> 3.5.3.

* Thu Oct 04 2018 Stanislav Levin <slev@altlinux.org> 3.5.2-alt1
- 3.2.1 -> 3.5.2.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 3.2.1-alt1
- 3.0.0 -> 3.2.1.

* Wed Apr 11 2018 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.9.1 -> 3.0.0

* Thu Oct 19 2017 Stanislav Levin <slev@altlinux.org> 2.9.1-alt1
- Version 2.9.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Version 1.9.0

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1
- Version 1.8.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus

