%define oname hyperlink

%def_with check

Name: python3-module-hyperlink
Version: 21.0.0
Release: alt1

Summary: A featureful, correct URL for Python

Url: https://github.com/mahmoud/hyperlink
License: BSD
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-idna
%endif

%description
The humble, but powerful, URL runs everything around us. Chances
are you've used several just to read this text.

Hyperlink is a featureful, pure-Python implementation of the URL, with
an emphasis on correctness.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test-3 -v

%files
%doc LICENSE *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Fri Aug 05 2022 Grigory Ustinov <grenka@altlinux.org> 21.0.0-alt1
- Build new version.
- Build with check.

* Thu Aug 05 2021 Grigory Ustinov <grenka@altlinux.org> 19.0.0-alt2
- Drop python2 support.

* Sun Jun 09 2019 Vitaly Lipatov <lav@altlinux.ru> 19.0.0-alt1
- new version 19.0.0 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 17.3.0-alt1.qa1
- NMU: applied repocop patch

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 17.3.0-alt1
- new version 17.3.0 (with rpmrb script)

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 17.1.1-alt1
- initial build for ALT Sisyphus

