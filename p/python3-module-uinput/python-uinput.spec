%define oldname python-uinput

Name: python3-module-uinput
Version: 0.10.1
Release: alt6

Summary: Pythonic API to the Linux uinput kernel module

License: GPLv3
Group: Development/Python3
Url: http://pypi.python.org/pypi/python-uinput/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://pypi.python.org/packages/source/p/%oldname/%oldname-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: rdma-core-devel
BuildRequires: libudev-devel

# https://github.com/tuomasjjrasanen/python-uinput/issues/16
# setup.py parses /usr/include/linux/input.h
BuildRequires: glibc-kernheaders-generic

%description
Python-uinput is Python interface to the Linux uinput kernel module
which allows attaching userspace device drivers into kernel.

%prep
%setup

# Use unversioned .so
%__subst "s/libudev.so.0/libudev.so/" setup.py


# https://github.com/tuomasjjrasanen/python-uinput/issues/16
# use correct input file
[ -s /usr/include/linux/input-event-codes.h ] && \
    %__subst "s/input.h/input-event-codes.h/" setup.py

%build
%python3_build

%install
%python3_install

chmod a-x examples/*

%files
%doc COPYING NEWS README examples
%python3_sitelibdir/python_uinput-%version-py?.?.egg-info
%python3_sitelibdir/_libsuinput.*.so
%python3_sitelibdir/uinput/

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.10.1-alt6
- Drop python2 support.

* Thu May 09 2019 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt5
- build for ALT Sisyphus (with python2 support)

* Fri Apr 19 2019 Cronbuild Service <cronbuild@altlinux.org> 0.10.1-alt4_21
- rebuild to get rid of unmets

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt3_21
- update to new release by fcimport

* Mon Dec 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt3_20
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt3_18
- update to new release by fcimport

* Sat May 05 2018 Cronbuild Service <cronbuild@altlinux.org> 0.10.1-alt3_17
- rebuild to get rid of unmets

* Thu Mar 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt2_17
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt2_16
- update to new release by fcimport

* Mon Oct 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt2_15
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt2_10
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt2_9
- update to new release by fcimport

* Sat Apr 09 2016 Cronbuild Service <cronbuild@altlinux.org> 0.10.1-alt2_8
- rebuild to get rid of unmets

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_8
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_6
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_4
- update to new release by fcimport

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_2
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_4
- update to new release by fcimport

* Mon Apr 01 2013 Cronbuild Service <cronbuild@altlinux.org> 0.9-alt2_3
- rebuild to get rid of unmets

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_3
- update to new release by fcimport

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_2
- initial fc import

