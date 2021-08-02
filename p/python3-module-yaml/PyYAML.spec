%define project PyYAML

Name: python3-module-yaml
Version: 5.4.1
Release: alt2

Summary: PyYAML, a YAML parser and emitter for Python

License: MIT
Group: Development/Python3
Url: https://github.com/yaml/pyyaml
#BuildArch: noarch

# Source-url: https://github.com/yaml/pyyaml/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.0.0

BuildRequires: libyaml-devel
BuildRequires(pre): rpm-build-python3 python3-module-Cython

%description
YAML is a data serialization format designed for human readability
and interaction with scripting languages.

PyYAML is a YAML parser and emitter for the Python programming
language.  PyYAML features a complete YAML 1.1 parser, Unicode
support, and relatively sensible error messages.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing

%python3_build build_ext

%install
%python3_install

%files
%doc CHANGES README
%python3_sitelibdir/*

%changelog
* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 5.4.1-alt2
- Drop python2 support.

* Fri Feb 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.4.1-alt1
- 5.4.1 released

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.3.1-alt1
- 5.3.1 released

* Wed Feb 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.3-alt1
- 5.3 released

* Wed Dec 11 2019 Grigory Ustinov <grenka@altlinux.org> 5.2-alt1
- Build new version 5.2.

* Mon Aug 05 2019 Grigory Ustinov <grenka@altlinux.org> 5.1.2-alt1
- Build new version.

* Wed Jul 10 2019 Grigory Ustinov <grenka@altlinux.org> 5.1.1-alt1
- Build new version.

* Tue Mar 19 2019 Grigory Ustinov <grenka@altlinux.org> 5.1-alt1
- Build new version.

* Tue Dec 25 2018 Grigory Ustinov <grenka@altlinux.org> 3.13-alt1
- Build new version.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.12-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Oct 22 2017 Vitaly Lipatov <lav@altlinux.ru> 3.12-alt1
- new version 3.12 (with rpmrb script) (ALT bug 34046)

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.11-alt1.hg20141128.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.11-alt1.hg20141128
- New snapshot

* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.11-alt1.hg20140326
- Version 3.11

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt2.hg20121224
- Snapshot from Mercurial

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.10-alt2.1
- Rebuild with Python-3.3

* Sat Apr 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt2
- Dont' rename _yaml.*.so -> _yaml.so

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt1
- Version 3.10
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.05-alt2.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.05-alt2.1
- Rebuilt with python 2.6

* Sun Jul 20 2008 Alexander Myltsev <avm@altlinux.ru> 3.05-alt2
- Fix #16285 (package lost directory).
- Pull a minor bugfix from SVN (a single dot is not a valid float).

* Fri Nov 16 2007 Alex V. Myltsev <avm@altlinux.ru> 3.05-alt1
- Initial build for Sisyphus.

