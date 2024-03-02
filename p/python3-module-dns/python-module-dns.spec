%define oname dnspython

# Testing requires network access
%def_with check

Name: python3-module-dns
Version: 2.6.1
Release: alt1
Epoch: 1

Summary: DNS toolkit

License: ISC
Group: Development/Python
Url: http://www.dnspython.org

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-hatchling
BuildRequires: pytest3

# optional
%add_python3_req_skip curio curio.socket
%add_python3_req_skip aioquic aioquic.quic.configuration aioquic.quic.connection aioquic.quic.events

%py3_provides %oname
Provides: python3-module-%oname

%description
dnspython is a DNS toolkit for Python. It supports almost all
record types. It can be used for queries, zone transfers, and dynamic
updates.  It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set.  The low level classes allow
direct manipulation of DNS zones, messages, names, and records.

%prep
%setup
rm -f examples/._*

%build
%pyproject_build

%install
%pyproject_install
%python3_prune

%check
py.test3 -v

%files
%doc README.md examples/ LICENSE
%python3_sitelibdir/*

%changelog
* Sat Mar 02 2024 Vitaly Lipatov <lav@altlinux.ru> 1:2.6.1-alt1
- new version 2.6.1, change license to ISC
- switch to pyproject_build
- CVE-2023-29483

* Sat May 06 2023 Anton Zhukharev <ancieg@altlinux.org> 1:2.2.0-alt2
- (NMU) Added missing provides.

* Sat Feb 12 2022 Anton Midyukov <antohami@altlinux.org> 1:2.2.0-alt1
- new version (2.2.0) with rpmgs script
- enable check

* Wed Nov 18 2020 Vitaly Lipatov <lav@altlinux.ru> 1:1.16.0-alt2
- return to 1.16.0 due https://github.com/eventlet/eventlet/issues/619

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0 (with rpmrb script)

* Sun Mar 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1.16.0-alt1
- new version 1.16.0 (with rpmrb script)
- build from tarball
- no more doc build

* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.15.0-alt2
- NMU: rebuilt with python-3.6.

* Wed Jul 12 2017 Terechkov Evgenii <evg@altlinux.org> 1.15.0-alt1
- 1.15.0

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.12.0-alt1.git20150613.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.12.0-alt1.git20150613.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.0-alt1.git20150613
- Version 1.12.0

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.1-alt1.git20140411
- New snapshot

* Tue Dec 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.1-alt1.git20130902
- Version 1.11.1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.10.0-alt2
- Version 1.10.0 (py3)
- Build for Python-3
- Rename package to python3-module-dns

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.10.0-alt2
- Version 1.10.0
- Obsoletes python-module-dnspython (ALT #28727)

* Sun Oct 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.2-alt1.1
- Rebuild with Python-2.7

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.2-alt1
- Version 1.9.2

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- cleanup spec
- new version (1.8.0) import in git

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.3.4-alt1.1
- Rebuilt with python-2.5.

* Mon Oct 03 2005 Andrey Orlov <cray@altlinux.ru> 1.3.4-alt1
- initial release

