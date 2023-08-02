%define _unpackaged_files_terminate_build 1
%define pypi_name zope.component
%define ns_name zope
%define mod_name component

%def_without check

Name: python3-module-%pypi_name
Version: 6.0
Release: alt2

Summary: Zope Component Architecture
License: ZPL-2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.component
Vcs: https://github.com/zopefoundation/zope.component.git
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%py3_requires zope
# setuptools(pkg_resources) is used by namespace root that is packaged
# separately at python3-module-zope
%add_pyproject_deps_runtime_filter setuptools
%pyproject_runtimedeps_metadata
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

This package represents the core of the Zope Component Architecture.
Together with the 'zope.interface' package, it provides facilities for
defining, registering and looking up components.

%package tests
Summary: Tests for zope.component (Python 3)
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing zope.testrunner

%description tests
This package contains tests for %pypi_name

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

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
%doc *.txt
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/
%exclude %python3_sitelibdir/%ns_name/%mod_name/testfiles/
%exclude %python3_sitelibdir/%ns_name/%mod_name/testing.py
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/testing.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/testlayer.py
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/testlayer.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/standalonetests.py
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/standalonetests.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/eventtesting.py
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/eventtesting.*

%files tests
%python3_sitelibdir/%ns_name/%mod_name/tests/
%python3_sitelibdir/%ns_name/%mod_name/testfiles/
%python3_sitelibdir/%ns_name/%mod_name/testing.py
%python3_sitelibdir/%ns_name/%mod_name/__pycache__/testing.*
%python3_sitelibdir/%ns_name/%mod_name/testlayer.py
%python3_sitelibdir/%ns_name/%mod_name/__pycache__/testlayer.*
%python3_sitelibdir/%ns_name/%mod_name/standalonetests.py
%python3_sitelibdir/%ns_name/%mod_name/__pycache__/standalonetests.*
%python3_sitelibdir/%ns_name/%mod_name/eventtesting.py
%python3_sitelibdir/%ns_name/%mod_name/__pycache__/eventtesting.*

%changelog
* Thu Jul 27 2023 Stanislav Levin <slev@altlinux.org> 6.0-alt2
- Mapped PyPI name to distro's one.
- Modernized packaging.

* Fri May 19 2023 Anton Vyatkin <toni@altlinux.org> 6.0-alt1
- New version 6.0.

* Wed Sep 22 2021 Nikolai Kostrigin <nickel@altlinux.org> 5.0.1-alt1
- 4.6.2 -> 5.0.1

* Mon Nov 16 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.6.2-alt1
- 4.6.1 -> 4.6.2

* Thu Apr 02 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.6.1-alt2
- Fix tests by adding zope.security to BR:

* Wed Apr 01 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.6.1-alt1
- 4.6 -> 4.6.1
- Rearrange check section according to upstream changes
- Fix license

* Fri Dec 20 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.6-alt1
- NMU: 4.5 -> 4.6
- Remove python2 module build
- Remove ubt tag from changelog
- Rearrange unittests execution

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.5-alt4
- NMU: remove rpm-build-ubt from BR:

* Tue Mar 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.5-alt3
- check disabled for build in p8

* Fri Mar 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.5-alt2
- requires fixed

* Wed Feb 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.5-alt1
- Version updated to 4.5

* Fri Feb 16 2018 Stanislav Levin <slev@altlinux.org> 4.4.1-alt1
- 4.2.3 -> 4.4.1

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.3-alt1.dev0.git20150604.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.3-alt1.dev0.git20150604.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.2.3-alt1.dev0.git20150604.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.3-alt1.dev0.git20150604
- Version 4.2.3.dev0

* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.2-alt1.dev0.git20150128
- Version 4.2.2.dev0

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1
- Version 4.2.1

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.1
- Use 'find... -exec...' instead of 'for ... $(find...'

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 4.1.0-alt1
- Version 4.1.0-alt1

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.1-alt1
- Version 3.12.1
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt1
- Version 3.12.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.10.0-alt4.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt3
- Add necessary requiresments
- Excludes *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt2
- Set archdep for package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt1
- Initial build for Sisyphus
