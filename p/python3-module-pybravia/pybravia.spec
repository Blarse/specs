Name: python3-module-pybravia
Version: 0.3.3
Release: alt1

Summary: Async interface for controlling Sony Bravia TVs
License: MIT
Group: Development/Python
Url: https://pypi.org/project/pybravia

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
%summary

%prep
%setup

%build
%pyproject_deps_resync_build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/pybravia
%python3_sitelibdir/pybravia-%version.dist-info

%changelog
* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.3-alt1
- 0.3.3 released

* Thu Jan 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.5-alt1
- 0.2.5 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.2-alt1
- 0.2.2 releasead
