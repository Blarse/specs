Name: python3-module-aioesphomeapi
Version: 23.0.0
Release: alt1

Summary: Python API to ESPHome devices
License: MIT
Group: Development/Python
Url: https://pypi.org/project/aioesphomeapi

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(cython)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/aioesphomeapi-*
%python3_sitelibdir/aioesphomeapi
%python3_sitelibdir/aioesphomeapi-%version.dist-info

%changelog
* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 23.0.0-alt1
- 23.0.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.0.1-alt1
- 21.0.1 released

* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.1.0-alt1
- 18.1.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 16.0.5-alt1
- 16.0.5 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 15.1.3-alt1
- 15.1.3 released

* Thu May 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.7.4-alt1
- 13.7.4 released

* Thu Jan 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.0.2-alt1
- 13.0.2 released

* Tue Nov 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.4.2-alt1
- 11.4.2 released

