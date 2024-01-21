%define _unpackaged_files_terminate_build 1
%define oname zope.authentication

%def_with check

Name: python3-module-%oname
Version: 5.0
Release: alt2

Summary: Definition of authentication basics for the Zope Framework
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.authentication/
Vcs: https://github.com/zopefoundation/zope.authentication.git

Source: %name-%version.tar

# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %oname} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.browser
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.security
%endif

%py3_requires zope zope.browser zope.component zope.i18nmessageid
%py3_requires zope.interface zope.schema zope.security

%description
This package provides a definition of authentication concepts for use in
Zope Framework.

%package tests
Summary: Tests for zope.authentication
Group: Development/Python3
Requires: %name = %version-%release

%description tests
This package provides a definition of authentication concepts for use in
Zope Framework.

This package contains tests for zope.authentication.

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
%python3_sitelibdir/zope/authentication
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests

%changelog
* Sun Jan 21 2024 Anton Vyatkin <toni@altlinux.org> 5.0-alt2
- Fixed FBTFS.

* Wed Aug 23 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1.1
- Map PyPI name to distro's one.

* Thu May 18 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Thu Sep 23 2021 Nikolai Kostrigin <nickel@altlinux.org> 4.5.0-alt1
- 4.4.0 -> 4.5.0

* Thu Apr 02 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.4.0-alt2
- Fix tests by adding zope.security to BR:
- Fix license

* Thu Dec 19 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.4.0-alt1
- NMU: 4.2.1 -> 4.4.0
- Remove python2 module build
- Add unittests execution

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.0-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Dec 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1
- Version 4.2.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Initial build for Sisyphus

