%def_disable snapshot
%define _unpackaged_files_terminate_build 1
%define pypi_name cleo

%def_disable check

Name: python3-module-%pypi_name
Version: 1.0.0a5
Release: alt0.1

Summary: Command-line interfaces Python library
License: MIT
Group: Development/Python3
Url: https://python-poetry.org/

%if_disabled snapshot
Source: https://github.com/python-poetry/cleo/archive/%version/%pypi_name-%version.tar.gz
%else
Vcs: https://github.com/python-poetry/cleo.git
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(poetry-core)

%{?_enable_check:BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(crashtest)
BuildRequires: python3(pylev)
BuildRequires: /usr/bin/poetry}

%description
Cleo allows you to create beautiful and testable command-line interfaces.

%prep
%setup -n %pypi_name-%version
sed -i 's|\(crashtest = "^0.\)3.1|\14.0|' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%tox_check

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%doc README.md CHANGELOG.md 

%changelog
* Mon Sep 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.0a5-alt0.1
- 1.0.0a5

* Thu May 05 2022 Ilya Mashkin <oddity@altlinux.ru> 0.8.1-alt1
- Build for Sisyphus

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.10

* Sat Oct 03 2020 Fabio Valentini <decathorpe@gmail.com> - 0.8.1-1
- Update to version 0.8.1.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.6-3
- Rebuilt for Python 3.9

* Sun Dec 08 2019 Fabio Valentini <decathorpe@gmail.com> - 0.7.6-1
- Update to version 0.7.6.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.8-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.8-2
- Rebuilt for Python 3.8

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.8-1
- Initial package.





