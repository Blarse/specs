%define _unpackaged_files_terminate_build 1
%define oname black

%define typing_extensions %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 10)))')

%def_with check

Name: python3-module-%oname
Version: 21.9b0
Release: alt1

Summary: The Uncompromising Code Formatter
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/black/
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm

%if_with check
# install_requires=
BuildRequires: python3(click)
BuildRequires: python3(platformdirs)
BuildRequires: python3(tomli)
BuildRequires: python3(regex)
BuildRequires: python3(pathspec)
BuildRequires: python3(mypy_extensions)
%if %typing_extensions
BuildRequires: python3(typing_extensions)
%endif

# tests
BuildRequires: python3(aiohttp)
BuildRequires: python3(aiohttp.test_utils)
BuildRequires: python3(aiohttp_cors)
BuildRequires: python3(click.testing)
BuildRequires: python3(parameterized)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%if %typing_extensions
%py3_requires typing_extensions
%endif

%description
Black is the uncompromising Python code formatter. By using it, you agree to
cede control over minutiae of hand-formatting. In return, Black gives you
speed, determinism, and freedom from pycodestyle nagging about formatting. You
will save time and mental energy for more important matters.

Blackened code looks the same regardless of the project you're reading.
Formatting becomes transparent after a while and you can focus on the content
instead.

Black makes code review faster by producing the smallest diffs possible.

%prep
%setup
%autopatch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
commands =
    {envpython} -m pytest {posargs} -m 'not python2'
EOF

export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%doc README.md LICENSE
%_bindir/black
%_bindir/blackd
%_bindir/black-primer
%python3_sitelibdir/__pycache__/_black_version.cpython*
%python3_sitelibdir/_black_version.py
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/black_primer/
%python3_sitelibdir/blackd/
%python3_sitelibdir/blib2to3/

%changelog
* Mon Oct 18 2021 Stanislav Levin <slev@altlinux.org> 21.9b0-alt1
- 21.8b0 -> 21.9b0.

* Tue Sep 07 2021 Stanislav Levin <slev@altlinux.org> 21.8b0-alt1
- 21.7b0 -> 21.8b0.

* Mon Jul 26 2021 Stanislav Levin <slev@altlinux.org> 21.7b0-alt1
- 21.6b0 -> 21.7b0.

* Tue Jun 22 2021 Stanislav Levin <slev@altlinux.org> 21.6b0-alt1
- 21.5b1 -> 21.6b0.

* Tue May 11 2021 Stanislav Levin <slev@altlinux.org> 21.5b1-alt1
- 20.8b1 -> 21.5b1.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 20.8b1-alt1
- Initial build for Sisyphus.
