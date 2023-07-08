%define oname txredisapi

Name: python3-module-%oname
Epoch: 1
Version: 1.4.10
Release: alt1

Summary: non-blocking redis client for python

License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/txredisapi
VCS: https://github.com/IlyaSkriblovsky/txredisapi

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
txredisapi is a non-blocking client driver for the redis database, written
in Python. It uses Twisted for the asynchronous communication with redis.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.* LICENSE
%python3_sitelibdir/__pycache__/txredisapi.*
%python3_sitelibdir/txredisapi.py
%python3_sitelibdir/%{pyproject_distinfo %oname}


%changelog
* Fri Jul 07 2023 Anton Vyatkin <toni@altlinux.org> 1:1.4.10-alt1
- New version 1.4.10.

* Tue Mar 21 2023 Anton Vyatkin <toni@altlinux.org> 1:1.4.9-alt1
- New version 1.4.9.

* Mon Mar 06 2023 Anton Vyatkin <toni@altlinux.org> 1:1.4.7-alt2
- Fix BuildRequires

* Fri Sep 18 2020 Vitaly Lipatov <lav@altlinux.ru> 1:1.4.7-alt1
- new version 1.4.7 (with rpmrb script)

* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:1.2-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:1.2-alt1.git20140728.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.2-alt1.git20140728.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1:1.2-alt1.git20140728.1
- NMU: Use buildreq for BR.

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2-alt1.git20140728
- Version 1.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20101029-alt1.1
- Rebuild with Python-2.7

* Tue Feb 01 2011 Sergey Alembekov <rt@altlinux.ru> 20101029-alt1
- initial build

