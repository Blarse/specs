%define _unpackaged_files_terminate_build 1
%define pypi_name junos-eznc
%define mod_name junos

# depends on deprecated nose
%def_without check

Name: python3-module-%pypi_name
Version: 2.6.7
Release: alt2
Summary: Junos 'EZ' automation for non-programmers
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/junos-eznc/
VCS: https://github.com/Juniper/py-junos-eznc
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

# for some reason not detected automatically
%py3_requires scp

# provide PyPI's name(dash and underscore)
%py3_provides %pypi_name
%py3_provides junos_eznc

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Junos PyEZ is a Python library to remotely manage/automate Junos
devices. The user is NOT required: (a) to be a "Software Programmer",
(b) have sophisticated knowledge of Junos, or (b) have a complex
understanding of the Junos XML API.

%prep
%setup
%autopatch -p1

# hotfix for python3.12
sed -i 's/SafeConfigParser/ConfigParser/' versioneer.py
sed -i 's/readfp/read_file/' versioneer.py
# workaround for versioneer
grep -qsF ' export-subst' .gitattributes || exit 1
vers_f="$(sed -n 's/ export-subst//p' .gitattributes)"
grep -qs '^[ ]*git_refnames[ ]*=[ ]*".*"[ ]*$' "$vers_f" || exit 1
sed -i 's/^\([ ]*\)git_refnames[ ]*=[ ]*".*"[ ]*$/\1git_refnames = " (tag: v%version, upstream\/master)"/' "$vers_f"

%build
%pyproject_build

%install
%pyproject_install

%check

%files
# jnpr is the namespace package, don't own that directory
%python3_sitelibdir/junos_eznc-%version-py%_python3_version-nspkg.pth
%python3_sitelibdir/jnpr/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jan 25 2024 Grigory Ustinov <grenka@altlinux.org> 2.6.7-alt2
- Fixed FTBFS.

* Wed Mar 01 2023 Stanislav Levin <slev@altlinux.org> 2.6.7-alt1
- 2.6.6 -> 2.6.7.

* Tue Feb 07 2023 Stanislav Levin <slev@altlinux.org> 2.6.6-alt1
- 2.6.3 -> 2.6.6.

* Mon Mar 21 2022 Stanislav Levin <slev@altlinux.org> 2.6.3-alt1
- 2.6.2 -> 2.6.3.
- Disabled testing (depends on unmaintained `nose`).

* Sat Jul 24 2021 Stanislav Levin <slev@altlinux.org> 2.6.2-alt1
- 2.0.1 -> 2.6.2.
- Enabled testing.

* Tue Jul 13 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt2
- Drop python2 support.

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 2.0.1-alt1
- New version

* Thu Jun 16 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt2
- Do not move jnpr/junos stuff to jnpr directory (ALT#32198)
  (thx Andrey Cherepanov cas@).
- %%python_req_hier -- for more detailed self-satisfied autoreqs (jnpr.*),
  without the general UNMET python2.X(jnpr).

* Thu Jun 16 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt2

* Fri Jun 10 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.3.1-alt1
- New version

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.1.2-alt1
- New version

* Thu Oct 30 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.0.2-alt1
- Initial build for ALT

