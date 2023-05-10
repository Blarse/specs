%define _unpackaged_files_terminate_build 1
%define pypi_name python-daemon
%define mod_name daemon

%def_with check

Name: python3-module-%mod_name
Version: 3.0.1
Release: alt1
Summary: Library to implement a well-behaved Unix daemon process
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-daemon/
Vcs: https://pagure.io/python-daemon/
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A well-behaved Unix daemon process is tricky to get right, but the required
steps are much the same for every daemon program. A DaemonContext instance
holds the behaviour and configured process environment for the program; use the
instance as a context manager to enter a daemon state.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile pip-requirements/test.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc ChangeLog README
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed May 10 2023 Stanislav Levin <slev@altlinux.org> 3.0.1-alt1
- 2.3.0 -> 3.0.1.

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- new version 2.3.0 (with rpmrb script)
- cleanup spec, switch to build from pypi release
- disable tests (not compatible with new testtools 2.5)

* Mon Mar 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.2.4-alt1
- Version updated to 2.2.4

* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.2.3-alt2
- Build for python2 disabled.

* Mon Feb 18 2019 Stanislav Levin <slev@altlinux.org> 2.2.3-alt1
- 2.1.2 -> 2.2.3.
- Enable testing.
- Fixed build against setuptools 40.7.0+.

* Wed Mar 21 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.1.2-alt1
- Version 2.1.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.5-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.5-alt2
- NMU: added python-modules-json and python-module-setuptools to BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.5-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 19 2015 Terechkov Evgenii <evg@altlinux.org> 2.0.5-alt1
- Update to 2.0.5

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.5-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.5-alt2.1
- Rebuild with Python-2.7

* Fri Aug 13 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.5.5-alt2
- pidlockfile.py: add checking for stale {pid,lock}file

* Sun Apr 04 2010 Denis Klimov <zver@altlinux.org> 1.5.5-alt1
- Initial build for ALT Linux
