%define oname keystoneclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 5.4.0
Release: alt1

Summary: Client Library for OpenStack Identity

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-keystoneclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-packaging >= 20.4
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-tempest >= 17.1.0

%if_with check
BuildRequires(pre): openssl
BuildRequires: python3-module-lxml >= 4.5.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-hacking >= 6.1.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-keyring >= 5.5.1
BuildRequires: python3-module-oauthlib >= 0.6.2
BuildRequires: python3-module-os-client-config >= 1.28.0
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testresources >= 2.0.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-bandit >= 1.1.0
BuildRequires: python3-module-keystoneauth1-tests
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
Client library and command line utility for interacting with Openstack
Identity API.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rfv *.egg-info

%build
%pyproject_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%if_with docs
# install man page
install -pDm 644 man/python-%oname.1 %buildroot%_man1dir/%oname.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/python_keystoneclient-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Tue May 28 2024 Grigory Ustinov <grenka@altlinux.org> 5.4.0-alt1
- Automatically updated to 5.4.0.

* Mon Oct 16 2023 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt1.1
- Dropped build dependency on python3-module-reno.

* Fri Jul 28 2023 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt1
- Automatically updated to 5.1.0.

* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt1.1
- Moved on modern pyproject macros.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt1
- Automatically updated to 5.0.1.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt2
- Unify documentation building.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Automatically updated to 4.0.0.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 3.22.0-alt1
- Automatically updated to 3.22.0.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 3.21.0-alt1
- Automatically updated to 3.21.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 3.19.0-alt1
- Automatically updated to 3.19.0

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 3.17.0-alt1
- Updated to 3.17.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 3.10.0-alt1
- 3.10.0
- add test packages

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 3.5.1-alt1
- 3.5.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 3.5.0-alt1
- 3.5.0
- The `keystone` CLI has been removed, using the `openstack` CLI is recommended

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1.7.4-alt1
- 1.7.4

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
 (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.2-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.2-alt1
- 0.11.2
- add python3 package

* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.9.0-alt1
- New build for ALT (based on Fedora 0.9.0-2.fc21.src)

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.1.2-alt1
- Initial release for Sisyphus (based on Fedora)

