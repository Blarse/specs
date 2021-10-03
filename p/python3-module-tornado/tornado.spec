%define module_name tornado

Name: python3-module-%module_name
Version: 6.1.0
Release: alt1
Summary: Scalable, non-blocking web server and tools

License: Apache-2.0
Group: Development/Python3
Url: http://www.tornadoweb.org

# https://github.com/tornadoweb/tornado.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
Requires: ca-certificates python3-module-certifi
%add_python3_req_skip MySQLdb pycurl

%description
Tornado is an open source version of the scalable, non-blocking web
server and tools.

The framework is distinct from most mainstream web server frameworks
(and certainly most Python frameworks) because it is non-blocking and
reasonably fast. Because it is non-blocking and uses epoll, it can
handle thousands of simultaneous standing connections, which means it is
ideal for real-time web services.

%prep
%setup
# remove shebang from files
sed -i.orig -e '/^#!\//, 1d' *py tornado/*.py tornado/*/*.py

%build
%python3_build

%install
%python3_install
pushd %buildroot%python3_sitelibdir/%module_name
rm -rf ca-certificates.crt
ln -sf /usr/share/ca-certificates/ca-bundle.crt ca-certificates.crt

# do not install tests
rm -r %buildroot%python3_sitelibdir/tornado/test

%check
export ASYNC_TEST_TIMEOUT=10
%__python3 -m tornado.test.runtests --verbose

%files
%python3_sitelibdir/*
%python3_sitelibdir/*.egg-*

%changelog
* Sun Oct 03 2021 Grigory Ustinov <grenka@altlinux.org> 6.1.0-alt1
- Build new version (Closes: #40697).
- Fix license tag.
- Enable check.

* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 5.1.1-alt3
- Drop python2 support.

* Wed Jan 30 2019 Stanislav Levin <slev@altlinux.org> 5.1.1-alt2
- Added dependency on python futures.

* Thu Jan 24 2019 Grigory Ustinov <grenka@altlinux.org> 5.1.1-alt1
- Build new version.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.2-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Nov 21 2016 Lenar Shakirov <snejok@altlinux.ru> 4.4.2-alt2
- Requires: python-module-certifi added

* Tue Oct 18 2016 Vladimir Didenko <cow@altlinux.org> 4.4.2-alt1
- update version
- update requires for Python 2 version

* Thu Sep 08 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 4.4.1-alt1.1.1
- (NMU) update version

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.1-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.2.1-alt1.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1
- Version 4.2.1

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Mon Dec 1 2014 Vladimir Didenko (REAL) <cow@altlinux.org> 4.0.2-alt2
- Add dependency to python-module-backports.ssl_match_hostname

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Mon Sep 09 2013 Alexey Shabalin <shaba@altlinux.ru> 3.1.1-alt1
- 3.1.1

* Sat Mar 02 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Fri Jun 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.1
- Added module for Python 3

* Wed Nov 23 2011 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- initial build for ALT Linux Sisyphus
