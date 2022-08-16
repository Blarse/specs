%define _unpackaged_files_terminate_build 1
%define pypi_name black

%define typing_extensions %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 10)))')

# tomli is tomllib(stdlib) on Python 3.11
%define tomli %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 11)))')

%def_with check

Name: python3-module-%pypi_name
Version: 22.6.0
Release: alt1

Summary: The Uncompromising Code Formatter
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/black/
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
# install_requires=
BuildRequires: python3(click)
BuildRequires: python3(platformdirs)
BuildRequires: python3(pathspec)
BuildRequires: python3(mypy_extensions)
%if %tomli
BuildRequires: python3(tomli)
%endif
%if %typing_extensions
BuildRequires: python3(typing_extensions)
%endif

# tests
BuildRequires: python3(aiohttp)
BuildRequires: python3(aiohttp.test_utils)
BuildRequires: python3(click.testing)
BuildRequires: python3(parameterized)
BuildRequires: python3(pytest)
%endif

%if %typing_extensions
%py3_requires typing_extensions
%endif

%if %tomli
%py3_requires tomli
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

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.md LICENSE
%_bindir/black
%_bindir/blackd
%python3_sitelibdir/__pycache__/_black_version.cpython*
%python3_sitelibdir/_black_version.py
%python3_sitelibdir/black/
%python3_sitelibdir/blackd/
%python3_sitelibdir/blib2to3/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Aug 15 2022 Stanislav Levin <slev@altlinux.org> 22.6.0-alt1
- 22.3.0 -> 22.6.0.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 22.3.0-alt1
- 22.1.0 -> 22.3.0.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 22.1.0-alt1
- 21.12b0 -> 22.1.0.

* Fri Jan 14 2022 Stanislav Levin <slev@altlinux.org> 21.12b0-alt1
- 21.10b0 -> 21.12b0.

* Mon Nov 01 2021 Stanislav Levin <slev@altlinux.org> 21.10b0-alt1
- 21.9b0 -> 21.10b0.

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
