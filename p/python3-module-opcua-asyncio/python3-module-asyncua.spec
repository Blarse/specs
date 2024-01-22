%define pypi_name opcua-asyncio
%define module_name asyncua

%ifarch %arm
%def_disable check
%endif

Name:    python3-module-%pypi_name
Version: 1.0.6
Release: alt2

Summary: OPC UA library for python >= 3.7
License: LGPL-3.0
Group:   Development/Python3
URL:     https://github.com/FreeOpcUa/opcua-asyncio

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

%if_disabled check
%else
BuildRequires: pytest3
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3(dateutil)
BuildRequires: python3(pytz)
BuildRequires: python3(aiofiles)
BuildRequires: python3(cryptography)
BuildRequires: python3(sortedcontainers)
BuildRequires: python3(sqlite3)
BuildRequires: python3(aiosqlite)
BuildRequires: python3(OpenSSL)
#BuildRequires: python3-module-pytest-timeout
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%package -n %pypi_name
Summary: Tools for OPC UA
Group: Engineering
Requires: %name = %EVR

%description -n %pypi_name
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
#%%tox_check_pyproject
# disable tests, where require external resources
# also disable "test_publish[client]" because of python 3.12:
# https://github.com/FreeOpcUa/opcua-asyncio/pull/1528
pytest3 -v -k "not (test_xml_import_companion_specifications[client]) \
	and not (test_xml_import_companion_specifications[server]) \
	and not (test_publish[client])"

%files
%doc *.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %module_name}

%files -n %pypi_name
%_bindir/*

%changelog
* Mon Jan 22 2024 Anton Midyukov <antohami@altlinux.org> 1.0.6-alt2
- disable pytest "test_publish[client]" because of python 3.12

* Fri Dec 22 2023 Anton Midyukov <antohami@altlinux.org> 1.0.6-alt1
- new version 1.0.6
- pack tools

* Sun Nov 12 2023 Anton Midyukov <antohami@altlinux.org> 1.0.5-alt1
- new version 1.0.5

* Sat Oct 28 2023 Anton Midyukov <antohami@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus
