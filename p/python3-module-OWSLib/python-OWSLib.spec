%define modulename OWSLib

Name:           python3-module-%modulename
Version:        0.31.0
Release:        alt1

Summary:        Client library for OGC web services
License:        BSD
Group:   	Development/Python
URL:            http://geopython.github.io/OWSLib

Packager:	Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-module-distribute
BuildRequires:  python3-module-setuptools

Provides:	python-%modulename = %version-%release

BuildArch:      noarch

Source0:	%modulename-%version.tar
#VCS:		git://github.com/geopython/OWSLib.git

%description
Package for client programming with Open Geospatial Consortium (OGC) web
service (hence OWS) interface standards, and their related content
models.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/owslib/
%python3_sitelibdir/*.egg-info

%changelog
* Sun May 12 2024 Andrey Cherepanov <cas@altlinux.org> 0.31.0-alt1
- New version.

* Mon Mar 11 2024 Andrey Cherepanov <cas@altlinux.org> 0.30.0-alt1
- New version.

* Thu Nov 09 2023 Andrey Cherepanov <cas@altlinux.org> 0.29.3-alt1
- New version.

* Sun May 21 2023 Andrey Cherepanov <cas@altlinux.org> 0.29.2-alt1
- New version.

* Tue Apr 18 2023 Andrey Cherepanov <cas@altlinux.org> 0.29.1-alt1
- New version.

* Sun Apr 09 2023 Andrey Cherepanov <cas@altlinux.org> 0.29.0-alt1
- New version.

* Fri Feb 24 2023 Andrey Cherepanov <cas@altlinux.org> 0.28.1-alt1
- New version.

* Mon Feb 20 2023 Andrey Cherepanov <cas@altlinux.org> 0.28.0-alt1
- New version.

* Sun Aug 28 2022 Andrey Cherepanov <cas@altlinux.org> 0.27.2-alt1
- New version.

* Mon Jun 13 2022 Andrey Cherepanov <cas@altlinux.org> 0.26.0-alt1
- New version.

* Tue Aug 24 2021 Andrey Cherepanov <cas@altlinux.org> 0.25.0-alt1
- New version.

* Tue May 11 2021 Andrey Cherepanov <cas@altlinux.org> 0.24.1-alt1
- New version.

* Mon May 10 2021 Andrey Cherepanov <cas@altlinux.org> 0.24.0-alt1
- New version.

* Sat Feb 06 2021 Andrey Cherepanov <cas@altlinux.org> 0.23.0-alt1
- New version.

* Thu Jan 21 2021 Andrey Cherepanov <cas@altlinux.org> 0.22.0-alt1
- New version.

* Wed Dec 09 2020 Andrey Cherepanov <cas@altlinux.org> 0.21.0-alt1
- New version.

* Mon Jun 08 2020 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1
- New version.

* Mon Apr 20 2020 Andrey Cherepanov <cas@altlinux.org> 0.19.2-alt2
- Package as Python3 module.

* Sat Mar 14 2020 Andrey Cherepanov <cas@altlinux.org> 0.19.2-alt1
- New version.

* Mon Feb 03 2020 Andrey Cherepanov <cas@altlinux.org> 0.19.1-alt1
- New version.

* Wed Dec 11 2019 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1
- New version.

* Tue Jun 25 2019 Andrey Cherepanov <cas@altlinux.org> 0.18.0-alt1
- New version.

* Sun Jan 13 2019 Andrey Cherepanov <cas@altlinux.org> 0.17.1-alt1
- New version.

* Thu Sep 20 2018 Andrey Cherepanov <cas@altlinux.org> 0.17.0-alt1
- New version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.16.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Dec 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.16.0-alt1
- New version.

* Thu Sep 14 2017 Andrey Cherepanov <cas@altlinux.org> 0.15.0-alt1
- New version

* Sun Jan 15 2017 Andrey Cherepanov <cas@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Mon Sep 26 2016 Andrey Cherepanov <cas@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Wed Sep 14 2016 Andrey Cherepanov <cas@altlinux.org> 0.12.0-alt1
- new version 0.12.0

* Wed Jun 08 2016 Andrey Cherepanov <cas@altlinux.org> 0.11.2-alt1
- new version 0.11.2

* Wed Jul 16 2014 Andrey Cherepanov <cas@altlinux.org> 0.8.8-alt1
- Import to ALT Linux from Fedora

* Mon Jul  7 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.8-1
- New upstream release

* Wed Jul  2 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.7-3
- Changed package summary

* Tue Jul  1 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.7-2
- Correct BR python-setuptools-devel to python-setuptools

* Mon Jun 30 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.7-1
- Initial package for Fedora
