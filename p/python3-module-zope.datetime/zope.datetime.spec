%define _unpackaged_files_terminate_build 1
%define oname zope.datetime

# FIXME: one test always fails on i586
%ifarch %ix86 armh
%def_without check
%else
%def_with check
%endif

Name: python3-module-%oname
Version: 4.3.0
Release: alt2

Summary: Zope datetime

License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.datetime/
#Git: https://github.com/zopefoundation/zope.datetime.git

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-six
%endif

%py3_requires zope

%description
Commonly used date and time related utility functions.

%package tests
Summary: Tests for zope.datetime
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing

%description tests
Commonly used date and time related utility functions.

This package contains tests for zope.datetime.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/datetime/tests

%changelog
* Wed Jan 31 2024 Grigory Ustinov <grenka@altlinux.org> 4.3.0-alt2
- Moved on modern pyproject macros.

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 4.3.0-alt1
- new version (4.3.0) with rpmgs script
- cleanup build

* Wed Dec 25 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.2.0-alt1
- NMU: 4.1.0 -> 4.2.0
- Remove python2 module build
- Add unittests execution

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1
- Version 3.4.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

