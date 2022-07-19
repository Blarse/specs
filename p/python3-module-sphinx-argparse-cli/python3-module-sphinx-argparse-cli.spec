%define modname sphinx-argparse-cli
%define _modname sphinx_argparse_cli
%def_enable check

Name: python3-module-%modname
Version: 1.9.0
Release: alt1

Summary: CLI arguments renderer for Sphinx
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

Vcs: https://github.com/gaborbernat/sphinx-argparse-cli.git
Source: https://pypi.io/packages/source/s/%_modname/%_modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 >= 0.1.19
BuildRequires: python3-module-setuptools python3-module-setuptools_scm python3-module-wheel
%{?_enable_check:BuildRequires: python3-module-sphinx-tests python3-module-pytest-cov}

%description
Render CLI arguments (sub-commands friendly) defined by the argparse module.

%prep
%setup -n %_modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
#py.test3
%tox_check

%files
%python3_sitelibdir_noarch/*
%doc README* CHANGELOG*


%changelog
* Fri Jun 24 2022 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- 1.9.0
- spec ported to %%pyproject/%%tox macros

* Wed Dec 29 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Wed Nov 24 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Mon Oct 18 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Thu Sep 30 2021 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- first build for Sisyphus





