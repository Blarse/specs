%define _name python-distutils-extra
%define ver_major 2.39

Name: python3-module-distutils-extra
Version: %ver_major
Release: alt2

Summary: Integrate more support into Python's distutils
Group: Development/Python3
License: GPLv2+
Url: https://launchpad.net/%_name

Source: https://launchpad.net/%_name/trunk/%ver_major/+download/%_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Enables you to easily integrate gettext support, themed icons and
documentation into Python's distutils.

%prep
%setup -n %_name-%version

%build
%python3_build

%install
%python3_install

chmod a+x %buildroot%python3_sitelibdir/DistUtilsExtra/command/build_extra.py

%files
%doc doc/*
%python3_sitelibdir/DistUtilsExtra/
%python3_sitelibdir/python_distutils_extra*.egg-info


%changelog
* Fri Jul 23 2021 Yuri N. Sedunov <aris@altlinux.org> 2.39-alt2
- python3-only build

* Tue Mar 28 2017 Yuri N. Sedunov <aris@altlinux.org> 2.39-alt1
- 2.39

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.38-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.38-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 24 2013 Yuri N. Sedunov <aris@altlinux.org> 2.38-alt1
- 2.38
- new python3 module

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.29-alt1.1
- Rebuild with Python-2.7

* Sat Oct 01 2011 Andrey Cherepanov <cas@altlinux.org> 2.29-alt1
- New verion 2.29

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1.1
- Rebuilt with python 2.6

* Fri Aug 04 2009 Paul Wolneykien <manowar@altlinux.ru> 2.6-alt1
- Initial build for ALTLinux

* Sat Aug 01 2009 Fabian Affolter <fabian@bernewireless.net> - 2.6-2
- Bump release

* Sat Aug 01 2009 Fabian Affolter <fabian@bernewireless.net> - 2.6-1
- Minor spec file changes
- Changed source to launchpad
- Updated to new upstream version 2.6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.91.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.91.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Fabian Affolter <fabian@bernewireless.net> - 1.91.2-2
- Changed license to GPLv2+

* Sat Nov 18 2008 Fabian Affolter <fabian@bernewireless.net> - 1.91.2-1
- Initial package for Fedora

