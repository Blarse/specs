%define _unpackaged_files_terminate_build 1
%define oname watchdog

%def_with check

Name: python3-module-%oname
Version: 2.1.3
Release: alt1

Summary: Filesystem events monitoring
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/watchdog/

BuildArch: noarch

# https://github.com/gorakhargosh/watchdog.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(flaky)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_timeout)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
%endif

%add_python3_req_skip AppKit FSEvents _watchdog_fsevents

Conflicts: python-module-%oname

%description
Python API and shell utilities to monitor file system events.

%prep
%setup
%autopatch -p1

%build
%python3_build_debug

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --no-deps -vvr -s false

%files
%doc AUTHORS *.rst
%_bindir/watchmedo
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Tue Jul 20 2021 Stanislav Levin <slev@altlinux.org> 2.1.3-alt1
- 0.8.3 -> 2.1.3.

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8.3-alt4.git20150727.1
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.3-alt3.git20150727.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.3-alt3.git20150727
- Rebuilt to update provides.
- Cleaned up spec.
- Enabled tests.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt2.git20150727.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt2.git20150727.1
- NMU: Use buildreq for BR.

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.8.3-alt2.git20150727
- Rebuild with "def_disable check"
- Cleanup buildreq

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20150727
- New snapshot

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20150222
- New snapshot

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20150211
- Version 0.8.3

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20141031
- Version 0.8.2

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20140916
- Initial build for Sisyphus

