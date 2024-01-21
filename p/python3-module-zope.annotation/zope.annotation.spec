%define _unpackaged_files_terminate_build 1
%define oname zope.annotation

%def_with check

Name: python3-module-%oname
Version: 5.0
Release: alt2

Summary: Object annotation mechanism
License: ZPL-2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.annotation
VCS: https://github.com/zopefoundation/zope.annotation.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.location
%endif

%description
This package provides a mechanism to store additional information about
objects without need to modify object class.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing zope.testrunner

%description tests
This package contains tests for %oname

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
%python3_sitelibdir/zope/annotation
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests

%changelog
* Sun Jan 21 2024 Anton Vyatkin <toni@altlinux.org> 5.0-alt2
- Fixed FTBFS.

* Mon Mar 27 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Tue Mar 07 2023 Anton Vyatkin <toni@altlinux.org> 4.8-alt1
- New version 4.8.

* Thu Dec 26 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.7.0-alt2
- Rollback to arch dependent build to guarantee all Zope modules
  are at the same location

* Wed Dec 18 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.7.0-alt1
- NMU: 4.6.0 -> 4.7.0
- Remove python2 module build
- Remove ubt tags from changelog
- Rearrange unittests execution

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.6.0-alt4
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.6.0-alt3
- NMU: remove ubt from release

* Mon Aug 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.6.0-alt2
- Fixed tests.

* Thu Feb 15 2018 Stanislav Levin <slev@altlinux.org> 4.6.0-alt1
- 4.4.2 -> 4.6.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.4.2-alt1.dev0.git20150613.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.2-alt1.dev0.git20150613.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.2-alt1.dev0.git20150613.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.4.2-alt1.dev0.git20150613.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.2-alt1.dev0.git20150613
- Version 4.4.2.dev0
- Enabled check

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.1-alt1
- Version 4.4.1

* Sat Dec 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1
- Version 4.3.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt3
- Added module for Python 3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt2
- Avoid requirement on ZODB3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1
- Version 4.2.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

