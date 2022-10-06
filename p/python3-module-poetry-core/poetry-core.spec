%define _unpackaged_files_terminate_build 1
%define pypi_name poetry-core

%def_with check

# poetry bundles several packages some of which require poetry to be built
# enable to bootstrap poetry-core
%def_without vendored

%define build_filter_python_deps() %(for mod in %{*}; do echo -n "/python3(${mod}\\(\\..*\\)\\?)/d;"; done; )
%define python_deps() %(for mod in %{*}; do echo -n "python3(${mod}) "; done; )

%define vendored_list \\\
attr \\\
attrs \\\
packaging \\\
jsonschema \\\
lark \\\
pyparsing \\\
pyrsistent \\\
tomlkit \\\
typing_extensions \\\
%nil

Name: python3-module-%pypi_name
Version: 1.3.1
Release: alt1

Summary: Poetry Core
License: MIT
Group: Development/Python3
# Source-git: https://github.com/python-poetry/poetry-core.git
Url: https://pypi.org/project/poetry-core

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# this is a build backend and it's built with self-hosted backend,
# thereby, no external backend is required.

%if_without vendored
# unvendored packages
BuildRequires: %python_deps %vendored_list
%endif

%if_with check
# required to build C extension, e.g. test_build_wheel_extended
BuildRequires: gcc
BuildRequires: python3-devel

BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)

BuildRequires: /usr/bin/git
BuildRequires: python3(build)
%endif

BuildArch: noarch

# PEP503 name
%py3_provides %pypi_name

# namespace root
%py3_requires poetry

%if_with vendored
# drop deps on system packages which were bundled, poetry patches sys.path
%filter_from_requires %build_filter_python_deps %vendored_list

%add_findreq_skiplist %python3_sitelibdir/poetry/core/_vendor/*
%add_findprov_skiplist %python3_sitelibdir/poetry/core/_vendor/*
%endif

%if_without vendored
# unvendored packages that are not found as deps automatically
%py3_requires jsonschema
%py3_requires lark
%endif

%description
A PEP 517 build backend implementation developed for Poetry. This project is
intended to be a light weight, fully compliant, self-contained package allowing
PEP 517 compatible build frontends to build Poetry managed projects.

%prep
%setup
%autopatch -p1

# check if actual bundled modules list is synced to expected one
set -o pipefail
PYTHONPATH="$(pwd)" %__python3 - <<-'EOF' | sort -u > actual.pkg.list
import pkgutil
for mod in pkgutil.iter_modules(["./src/poetry/core/_vendor"]):
    if not mod.name.startswith("_"):
        print(mod.name)
EOF

echo "%vendored_list" | sed 's/[ ]*$//' | tr ' ' '\n' | sort -u > expected.pkg.list
diff -y expected.pkg.list actual.pkg.list

%if_without vendored
# unbundle packages
rm -r ./src/poetry/core/_vendor/*
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# override upstream's config (they use poetry for tox)
%tox_create_default_config
%tox_check_pyproject -- -vra tests/

%files
%doc README.md
%python3_sitelibdir/poetry/core/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 06 2022 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- 1.2.0 -> 1.3.1.

* Mon Sep 19 2022 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0.

* Tue Sep 13 2022 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.8 -> 1.1.0.

* Sat Mar 05 2022 Stanislav Levin <slev@altlinux.org> 1.0.8-alt1
- 1.0.7 -> 1.0.8.

* Fri Feb 04 2022 Stanislav Levin <slev@altlinux.org> 1.0.7-alt2
- Built without vendored distributions

* Fri Jan 28 2022 Stanislav Levin <slev@altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus.

