%define _unpackaged_files_terminate_build 1
%define oname transitions

%def_with check

Name: python3-module-%oname
Version: 0.8.8
Release: alt1

Summary: A lightweight, object-oriented Python state machine implementation
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/transitions/
BuildArch: noarch

# https://github.com/pytransitions/transitions.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires:
BuildRequires: python3(six)

BuildRequires: graphviz
BuildRequires: python3(graphviz)
BuildRequires: python3(pygraphviz)
BuildRequires: python3(pycodestyle)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_xdist)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

%description
A lightweight, object-oriented finite state machine implementation in
Python.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --no-deps --console-scripts -vvr -s false

%files
%doc *.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Fri Jul 23 2021 Stanislav Levin <slev@altlinux.org> 0.8.8-alt1
- 0.2.3 -> 0.8.8.
- Enabled testing.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.3-alt1.git20150114.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.3-alt1.git20150114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20150114
- Initial build for Sisyphus

