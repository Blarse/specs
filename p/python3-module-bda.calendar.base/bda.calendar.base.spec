%define _unpackaged_files_terminate_build 1
%define mname bda.calendar
%define oname %mname.base

%def_with check

Name: python3-module-%oname
Version: 1.2.5
Release: alt1
Summary: Base common calendaring features: Convinience or not coverd yet
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/bda.calendar.base/
#Git: https://github.com/bluedynamics/bda.calendar.base.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pytz
BuildRequires: python3-module-zope.interface

%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires zope.interface

%add_python3_self_prov_path %buildroot%python3_sitelibdir/bda/calendar/base

%description
bda.calendar.base contains functions adressing programmers all-day tasks
not (or only partly) covered by pythons datetime or zopes DateTime.

Major part of these function is timezone aware. Also ist easy to deal
with timezones. An TimezoneFactory can be provided in the specific
application to i.e. be aware of the users timezone (i.e. in case of
webapps).

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/bda/calendar/__init__.py \
	%buildroot%python3_sitelibdir/bda/calendar/

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/bda/calendar/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/bda/calendar/__init__.py*
%exclude %python3_sitelibdir/*.pth

%files -n python3-module-%mname
%dir %python3_sitelibdir/bda/calendar
%python3_sitelibdir/bda/calendar/__init__.py*

%changelog
* Thu Apr 27 2023 Anton Vyatkin <toni@altlinux.org> 1.2.5-alt1
- 1.2.3 -> 1.2.5

* Fri Sep 24 2021 Nikolai Kostrigin <nickel@altlinux.org> 1.2.3-alt1
- 1.2.2 -> 1.2.3
  + switch to github upstream
- spec: remove erroneous %%py3_requires bda

* Sat Jan 11 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.2.2-alt2
- NMU: Remove python2 module build

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.2-alt1.1
- (AUTO) subst_x86_64.

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus

