Name: python3-module-zabbix-api
Version: 0.5.3
Release: alt2
Summary: Zabbix API

Group: Development/Python3
License: GNU LGPL 2.1
Url: https://github.com/gescheit/scripts

Source: %name-%version.tar
Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python3

%description
Zabbix API

%prep
%setup

%build
cd zabbix
%python3_build

%install
cd zabbix
%python3_install

%files
%doc zabbix/README.md zabbix/examples
%python3_sitelibdir/zabbix_api*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.3-alt2
- Drop python2 support.

* Mon Feb 26 2018 Terechkov Evgenii <evg@altlinux.org> 0.5.3-alt1
- 0.5.3 (386aa22)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 21 2015 Terechkov Evgenii <evg@altlinux.org> 0.3-alt2
- Update code to work with unverified/selfsigned SSL certificates

* Thu Nov 19 2015 Terechkov Evgenii <evg@altlinux.org> 0.3-alt1
- 0.3
- python3 module

* Wed Oct  1 2014 Evgenii Terechkov <evg@altlinux.org> 0.2-alt1
- Update code to work with zabbix-2.4

* Sat Aug 31 2013 Terechkov Evgenii <evg@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus
