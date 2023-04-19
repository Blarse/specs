%define _unpackaged_files_terminate_build 1
%define pypi_name pdm-backend
%def_without vendored

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.6
Release: alt1

Summary: The build backend used by PDM that supports latest packaging standards
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pdm-backend/
VCS: https://github.com/pdm-project/pdm-backend
BuildArch: noarch
Source: %name-%version.tar
%if_without vendored
Source1: debundler.py.in
%endif
Source2: pyproject_deps.json
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
# namespace root
%py3_requires pdm

%if_without vendored
%pyproject_runtimedeps -- vendored
%endif

%py3_provides %pypi_name

# self-dependencies
%filter_from_requires /python3(pdm\.backend\._vendor\..*)/d

%if_with vendored
# self-contained deps
%add_findreq_skiplist %python3_sitelibdir/pdm/backend/_vendor/*
%add_findprov_skiplist %python3_sitelibdir/pdm/backend/_vendor/*
%endif

BuildRequires(pre): rpm-build-pyproject
BuildRequires: /usr/bin/git

%pyproject_builddeps_build

%if_without vendored
%pyproject_builddeps -- vendored
%endif

%if_with check
%pyproject_builddeps_metadata

# installed directly via pip
BuildRequires: python3(pytest)
BuildRequires: python3(setuptools)
BuildRequires: python3(editables)
BuildRequires: python3-devel
%endif

%description
This is the backend for PDM projects that is fully-compatible with PEP 517 spec,
but you can also use it alone. It reads the metadata of PEP 621 format and
coverts it to Core metadata.

%prep
%setup
%autopatch -p1

%if_without vendored
%pyproject_deps_resync vendored pip_reqfile src/pdm/backend/_vendor/vendor.txt

# unbundle packages
VENDORED_PATH='src/pdm/backend/_vendor'
UNVENDORED_PATH="$VENDORED_PATH/__init__.py"
rm -r "$VENDORED_PATH"
mkdir "$VENDORED_PATH"
cp "%SOURCE1" "$UNVENDORED_PATH"
sed -i \
    -e 's/@VENDORED_ROOT@/"pdm.backend._vendor"/' \
    -e 's/@VENDORED_FAKE_PACKAGES@/None/' \
    "$UNVENDORED_PATH"
%endif

# for pdm scm version
# https://pdm.fming.dev/latest/pyproject/build/#dynamic-version-from-scm
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests

%files
%doc README.md
%python3_sitelibdir/pdm/backend/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Apr 18 2023 Stanislav Levin <slev@altlinux.org> 2.0.6-alt1
- 2.0.5 -> 2.0.6.

* Tue Mar 28 2023 Michael Shigorin <mike@altlinux.org> 2.0.5-alt2
- NMU:
  + fix build --without check
  + minor spec cleanup

* Tue Feb 28 2023 Stanislav Levin <slev@altlinux.org> 2.0.5-alt1
- 2.0.3 -> 2.0.5.

* Mon Feb 27 2023 Stanislav Levin <slev@altlinux.org> 2.0.3-alt1
- 2.0.2 -> 2.0.3.

* Fri Feb 10 2023 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1
- 1.1.2 -> 2.0.2.

* Fri Feb 10 2023 Stanislav Levin <slev@altlinux.org> 1.1.2-alt1
- 1.1.1 -> 1.1.2.

* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.0.6 -> 1.1.1.

* Thu Nov 24 2022 Stanislav Levin <slev@altlinux.org> 1.0.6-alt1
- 1.0.5 -> 1.0.6.

* Mon Oct 24 2022 Stanislav Levin <slev@altlinux.org> 1.0.5-alt1
- 1.0.4 -> 1.0.5.

* Wed Oct 05 2022 Stanislav Levin <slev@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus.
