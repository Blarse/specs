%define        gemname patternfly-sass

Name:          gem-patternfly-sass
Version:       3.59.5
Release:       alt1.1
Summary:       Red Hat's Patternfly, converted to Sass and ready to drop into Rails
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://www.patternfly.org/
Vcs:           https://github.com/patternfly/patternfly-3.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         lost-file.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(sassc) > 2.0.1 gem(sassc) < 3.0
BuildRequires: gem(bootstrap-sass) >= 3.4.0 gem(bootstrap-sass) < 3.5
BuildRequires: gem(font-awesome-sass) >= 4.6.2 gem(font-awesome-sass) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency font-awesome-sass >= 4.6.2,font-awesome-sass < 6
Requires:      gem(sassc) > 2.0.1 gem(sassc) < 3.0
Requires:      gem(bootstrap-sass) >= 3.4.0 gem(bootstrap-sass) < 3.5
Requires:      gem(font-awesome-sass) >= 4.6.2 gem(font-awesome-sass) < 6
Provides:      gem(patternfly-sass) = 3.59.5


%description
This reference implementation of PatternFly is based on Bootstrap v3. Think of
PatternFly as a "skinned" version of Bootstrap with additional components and
customizations. For information on how to quickly get started using PatternFly,
see the Quick Start Guide. Looking for RCUE (Red Hat Common User Experience)
information? See the RCUE Quick Start Guide.


%package       -n gem-patternfly-sass-doc
Version:       3.59.5
Release:       alt1.1
Summary:       Red Hat's Patternfly, converted to Sass and ready to drop into Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета patternfly-sass
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(patternfly-sass) = 3.59.5

%description   -n gem-patternfly-sass-doc
Red Hat's Patternfly, converted to Sass and ready to drop into Rails
documentation files.

This reference implementation of PatternFly is based on Bootstrap v3. Think of
PatternFly as a "skinned" version of Bootstrap with additional components and
customizations. For information on how to quickly get started using PatternFly,
see the Quick Start Guide. Looking for RCUE (Red Hat Common User Experience)
information? See the RCUE Quick Start Guide.

%description   -n gem-patternfly-sass-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета patternfly-sass.


%prep
%setup
%patch -p1

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-patternfly-sass-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Fri Jul 23 2021 Pavel Skrylev <majioa@altlinux.org> 3.59.5-alt1.1
- ! spec

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.59.5-alt1
- ^ 3.59.4 -> 3.59.5

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.59.4-alt2.1
- fixed (!) changelog syntax

* Thu Sep 19 2019 Pavel Skrylev <majioa@altlinux.org> 3.59.4-alt2
- added (+) lost package.json to gem file list in gemspec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.59.4-alt1
- updated (^) 3.59.1 -> 3.59.4
- fixed (!) spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 3.59.1-alt1
- added (+) package as a gem with usage Ruby Policy 2.0.
