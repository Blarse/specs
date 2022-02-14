%define _unpackaged_files_terminate_build 1

%define oname astor

Name: python3-module-%oname
Version: 0.8.1
Release: alt1
Summary: Python AST read/write
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/berkerpeksag/astor

BuildArch: noarch

# https://github.com/berkerpeksag/astor.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest

%description
astor is designed to allow easy manipulation of Python source via the AST.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
PYTHONPATH=$(pwd) py.test3 -vv \
	--deselect=tests/test_rtrip.py::RtripTestCase::test_convert_stdlib \
	%nil

%files
%doc LICENSE
%doc AUTHORS README.rst
%python3_sitelibdir/%oname-%version-py3*.egg-info
%python3_sitelibdir/%oname

%changelog
* Mon Feb 14 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.1-alt1
- Initial build for ALT.
