%define oname port-for

%def_with check

Name: python3-module-%oname
Version: 0.6.2
Release: alt1

Summary: Utility that helps with local TCP ports managment

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/port-for/
BuildArch: noarch

# https://github.com/kmike/port-for.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
%endif

%description
port-for is a command-line utility and a python library that helps with
local TCP ports management.

It can find an unused TCP localhost port and remember the association.

%prep
%setup
%patch1 -p1

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*

%changelog
* Thu May 26 2022 Grigory Ustinov <grenka@altlinux.org> 0.6.2-alt1
- Automatically updated to 0.6.2.

* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 0.4-alt3
- Drop python2 support.

* Mon Sep 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4-alt2
- Fixed build.

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4-alt1
- Updated to upstream version 0.4.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.git20140827.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1.git20140827.1
- NMU: Use buildreq for BR.

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20140827
- Initial build for Sisyphus

