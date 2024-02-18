%define modname translate

Name: translate-toolkit
Version: 3.12.2
Release: alt1

Summary: Tools and API for translation and localization engineering.

License: GPL-2.0-or-later
Group: Development/Python
Url: http://toolkit.translatehouse.org/
# Source-url: https://github.com/translate/translate/releases/download/%version/%name-%version.tar.gz
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3-devel
BuildRequires: python3-module-BeautifulSoup4
BuildRequires: python3-module-sphinx
BuildRequires: python3(sphinx_bootstrap_theme)
BuildRequires: python3-module-Levenshtein

Requires: python3-module-%modname = %version-%release

# it is not really required for the work
%add_python3_req_skip setuptools
# Remove garbage dependency
%filter_from_requires /python-module-setuptools/d

# these modules used in tools and marked deprecated by upstream
%add_python3_req_skip l20n.format.parser
%add_python3_req_skip l20n.format.serializer

%description
The Translate Toolkit is created by localizers for localizers. It contains
several utilities, as well as an API for building localization tools.

Some of the tools include:

* File format converters
* Quality checking tools
* Tools for counting, grepping, terminology extraction, and pseudo-localization

%package -n python3-module-%modname
Summary: Module for building localization tools
Group: Development/Python
Obsoletes: python-module-%modname

%description -n python3-module-%modname
Features of the API include:

* Support for multiple file formats
* Language information and language support code (including language detection)
* Code for translation memory, terminology matching and indexed search
* Several helper classes and functions for tools built on the Translate Toolkit.

%package -n %name-doc
Summary: Documentation for Translate Toolkit
Group: Development/Documentation

%description -n %name-doc
Documentation for Translate Toolkit

%prep
%setup -n %name-%version

# fix build documentation
pushd docs
sed -i 's/= sphinx-build/= sphinx-build-3/' Makefile
sed -i '/sphinx.ext.intersphinx/d' conf.py
popd

%build
%pyproject_build
pushd docs
%make_build man html
gzip -9 _build/man/*.1
#no hidden files
find _build -name '.?*' -exec rm '{}' \+
popd

%install
%pyproject_install

install -d %buildroot%_man1dir
install -pm 644 docs/_build/man/*.gz %buildroot%_man1dir
rm -fr %buildroot%python3_sitelibdir/%modname/docs/

# mercurial is an optional dependency. Code could work without it
%filter_from_requires /mercurial/d

# remove optional fluent
rm %buildroot%python3_sitelibdir/%modname/storage/fluent.py

%files
%doc docs/{features,history,license}.rst
%_bindir/*
%_man1dir/*

%files -n python3-module-%modname
%python3_sitelibdir/%modname
%python3_sitelibdir/translate_toolkit-%version.dist-info

%files -n %name-doc
%doc docs/_build/html

%changelog
* Thu Feb 08 2024 Anton Midyukov <antohami@altlinux.org> 3.12.2-alt1
- new version (3.12.2) with rpmgs script

* Mon Aug 28 2023 Anton Midyukov <antohami@altlinux.org> 3.10.0-alt2
- fix BuildRequires for build on p10

* Mon Aug 28 2023 Anton Midyukov <antohami@altlinux.org> 3.10.0-alt1
- new version (3.10.0) with rpmgs script
- migration to PEP517

* Fri May 7 2021 Vladimir Didenko <cow@altlinux.ru> 3.3.6-alt1
- New version

* Mon Apr 12 2021 Vladimir Didenko <cow@altlinux.ru> 3.3.4-alt1
- New version

* Thu Mar 4 2021 Vladimir Didenko <cow@altlinux.ru> 3.3.3-alt1
- New version

* Fri Jan 22 2021 Vladimir Didenko <cow@altlinux.ru> 3.3.0-alt1
- New version

* Fri Nov 13 2020 Vladimir Didenko <cow@altlinux.ru> 3.2.0-alt1
- New version

* Wed Sep 30 2020 Vladimir Didenko <cow@altlinux.ru> 3.1.1-alt1
- New version

* Tue Sep 15 2020 Vladimir Didenko <cow@altlinux.ru> 3.0.0-alt2
- Don't require mercurial (closes: #38939)

* Tue Jun 23 2020 Vladimir Didenko <cow@altlinux.ru> 3.0.0-alt1
- New version

* Tue May 12 2020 Vladimir Didenko <cow@altlinux.ru> 2.5.1-alt1
- New version

* Tue Feb 4 2020 Vladimir Didenko <cow@altlinux.ru> 2.5.0-alt1
- New version

* Tue Sep 24 2019 Vladimir Didenko <cow@altlinux.ru> 2.4.0-alt2
- Remove garbage dependency on python-module-setuptools

* Tue Sep 24 2019 Vladimir Didenko <cow@altlinux.ru> 2.4.0-alt1
- New version
- Switch to Python 3

* Tue Mar 19 2019 Vladimir Didenko <cow@altlinux.ru> 2.3.1-alt1
- New version

* Tue Jul 17 2018 Vladimir Didenko <cow@altlinux.ru> 2.3.0-alt1
- New version

* Mon Jan 15 2018 Vladimir Didenko <cow@altlinux.ru> 2.2.5-alt1
- New version
- add dependency to python-module-translate (closes: #34461)

* Wed Jul 5 2017 Vladimir Didenko <cow@altlinux.ru> 2.2.3-alt1
- New version

* Wed Mar 22 2017 Vladimir Didenko <cow@altlinux.ru> 2.1.0-alt1
- New version

* Thu Mar 16 2017 Vladimir Didenko <cow@altlinux.ru> 2.0.0-alt1
- New version

* Mon Dec 7 2015 Vladimir Didenko <cow@altlinux.ru> 1.13.0-alt1
- Initial build
