%define rname ytmusicapi

Name: python3-module-%rname
Version: 0.24.1
Release: alt1

Group: Development/Python3
Summary: YouTube Music Unofficial API
Url: https://github.com/sigma67/%rname
License: MIT

%add_python3_req_skip ytmusicapi.parsers

Source: %rname-%version.tar
Patch1: alt-setuptools-version.patch
Patch2: alt-project-version.patch
Patch3: alt-locales-dir.patch

# Automatically added by buildreq on Mon Apr 24 2023 (-bi)
# optimized out: elfutils libgpg-error python-modules python2-base python3 python3-base python3-dev python3-module-Cython python3-module-PasteDeploy python3-module-Pillow python3-module-Pygments python3-module-automat python3-module-babel python3-module-black python3-module-cffi python3-module-charset-normalizer python3-module-docutils python3-module-importlib-metadata python3-module-jinja2 python3-module-lingua python3-module-markupsafe python3-module-mypy python3-module-packaging python3-module-paste python3-module-pkg_resources python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-sphinx python3-module-tables python3-module-zipp python3-module-zope rpm-build-file rpm-build-gir rpm-build-python3 rpm-macros-python3 sh4 tzdata
#BuildRequires: meson python3-module-chardet python3-module-hypothesis python3-module-markdown python3-module-markups python3-module-mpl_toolkits python3-module-nose python3-module-pyproject-installer python3-module-tempora python3-module-wheel python3-module-ytmusicapi
#BuildRequires: python3-module-chardet python3-module-hypothesis python3-module-markdown python3-module-markups python3-module-mpl_toolkits python3-module-nose python3-module-pyproject-installer python3-module-tempora python3-module-wheel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools) python3(wheel)

%description
ytmusicapi is a Python 3 library to send requests to the YouTube Music API.
It emulates YouTube Music web client requests using the user's cookie data for authentication.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -i 's|@VERSION@|%version|' pyproject.toml
sed -i 's|@VERSION@|%version|' ytmusicapi/__init__.py

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot/%_datadir/%rname/
mv %buildroot/%python3_sitelibdir_noarch/%rname/locales %buildroot/%_datadir/%rname/

rm -rf %buildroot/%python3_sitelibdir_noarch/%{pyproject_distinfo %rname} ||:

%files
%doc README.rst
#%_bindir/%rname
%python3_sitelibdir_noarch/%rname/
%_datadir/%rname/

%changelog
* Mon Apr 24 2023 Sergey V Turchin <zerg@altlinux.org> 0.24.1-alt1
- initial build
