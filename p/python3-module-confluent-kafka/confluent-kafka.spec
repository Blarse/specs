%define  modulename confluent-kafka

# needs pyflakes.test
%def_without check

Name:    python3-module-%modulename
Version: 1.8.2
Release: alt1

Summary: Confluent's Kafka Python Client

License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/confluentinc/confluent-kafka-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: librdkafka-devel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-trivup
BuildRequires: python3-module-requests-mock
BuildRequires: python3-module-avro
BuildRequires: python3-module-fastavro
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-google-api-core
BuildRequires: python3-module-pyflakes
%endif

Source:  %name-%version.tar

%description
confluent-kafka-python is Confluent's Python client for Apache Kafka
and the Confluent Platform.

%prep
%setup

%build
%python3_build

%install
%python3_install

# Remove license file installed in weird place
rm -f  %buildroot/%_prefix/LICENSE.txt

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v

%files
%python3_sitelibdir/confluent_kafka
%python3_sitelibdir/*.egg-info

%changelog
* Thu May 26 2022 Grigory Ustinov <grenka@altlinux.org> 1.8.2-alt1
- Automatically updated to 1.8.2.

* Sat Jun 20 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus.
