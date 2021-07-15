%define oname pam

Summary:	PAM bindings for Python
Name:		python3-module-PAM
Version:	1.8.4
Release:	alt2
License:	%mit
Group:		Development/Python3

Source0:	%{name}-%{version}.tar
Url:		https://github.com/FirefighterBlu3/python-pam

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildPreReq: rpm-build-python3

BuildRequires: python3-devel python3-module-distribute python3-module-pip

%description
PAM (Pluggable Authentication Module) bindings for Python.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE README.md
%python3_sitelibdir/%{oname}*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/*.egg-*

%changelog
* Thu Jul 15 2021 Grigory Ustinov <grenka@altlinux.org> 1.8.4-alt2
- Drop python2 support.

* Thu Jul 11 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.4-alt1
- Build new version.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.3-alt2
- NMU: Rebuild with python3.7.

* Fri May 04 2018 Vladimir Didenko <cow@altlinux.org> 1.8.3-alt1
- New version (switch to fork from David Ford)
- Add Python 3 package
- Make package noarch

* Fri Mar 01 2013 Pavel Shilovsky <piastry@altlinux.org> 0.5.0-alt2
- Rename package to python-module-PAM

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.5.0-alt1
- Initial release for Sisyphus (based on Fedora)
