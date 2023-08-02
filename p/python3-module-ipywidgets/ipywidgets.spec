%define _unpackaged_files_terminate_build 1

%define oname ipywidgets

%def_with check

Name: python3-module-%oname
Version: 8.1.0
Release: alt1
Summary: Interactive Widgets for the Jupyter Notebook
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/ipywidgets
Vcs: https://github.com/jupyter-widgets/ipywidgets.git
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-traitlets
BuildRequires: python3-module-traitlets-tests
BuildRequires: python3-module-ipython
BuildRequires: python3-module-ipykernel
BuildRequires: python3-module-pytz
%endif

%description
ipywidgets, also known as jupyter-widgets or simply widgets,
are interactive HTML widgets for Jupyter notebooks and the IPython kernel.

Notebooks come alive when interactive widgets are used.
Users gain control of their data and can visualize changes in the data.

Learning becomes an immersive, fun experience.
Researchers can easily see how changing inputs to a model impact the results.
We hope you will add ipywidgets to your notebooks,
and we're here to help you get started.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
ipywidgets, also known as jupyter-widgets or simply widgets,
are interactive HTML widgets for Jupyter notebooks and the IPython kernel.

Notebooks come alive when interactive widgets are used.
Users gain control of their data and can visualize changes in the data.

Learning becomes an immersive, fun experience.
Researchers can easily see how changing inputs to a model impact the results.
We hope you will add ipywidgets to your notebooks,
and we're here to help you get started.

This package contains tests for %oname.

%prep
%setup

%build
cd python/ipywidgets/
%pyproject_build

%install
cd python/ipywidgets/
%pyproject_install

%check
cd python/ipywidgets/
%pyproject_run_pytest -v

%files
%doc README.md CONTRIBUTING.md LICENSE
%python3_sitelibdir/%oname-%version.dist-info
%python3_sitelibdir/%oname
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/widgets/tests

%files tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/widgets/tests

%changelog
* Wed Aug 02 2023 Anton Vyatkin <toni@altlinux.org> 8.1.0-alt1
- New version 8.1.0.

* Mon Jul 10 2023 Anton Vyatkin <toni@altlinux.org> 8.0.7-alt2
- FTBFS: fix BuildRequires.

* Wed Jul 05 2023 Anton Vyatkin <toni@altlinux.org> 8.0.7-alt1
- New version 8.0.7.

* Mon Jul 03 2023 Anton Vyatkin <toni@altlinux.org> 8.0.6-alt1
- New version 8.0.6.

* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 7.6.3-alt1
- Initial build for ALT.
