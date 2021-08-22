%define        gemname rails-i18n

Name:          gem-rails-i18n
Version:       6.0.0
Release:       alt1
Summary:       Central point to collect locale data for use in Ruby on Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/svenfuchs/rails-i18n
Vcs:           https://github.com/svenfuchs/rails-i18n.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(i18n) >= 0.7 gem(i18n) < 2
BuildRequires: gem(railties) >= 6.0.0 gem(railties) < 7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(i18n) >= 0.7 gem(i18n) < 2
Requires:      gem(railties) >= 6.0.0 gem(railties) < 7
Obsoletes:     ruby-rails-i18n < %EVR
Provides:      ruby-rails-i18n = %EVR
Provides:      gem(rails-i18n) = 6.0.0


%description
Central point to collect locale data for use in Ruby on Rails.


%package       -n gem-rails-i18n-doc
Version:       6.0.0
Release:       alt1
Summary:       Central point to collect locale data for use in Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rails-i18n
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rails-i18n) = 6.0.0

%description   -n gem-rails-i18n-doc
Central point to collect locale data for use in Ruby on Rails documentation
files.

Central point to collect locale data for use in Ruby on Rails.

%description   -n gem-rails-i18n-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rails-i18n.


%prep
%setup

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

%files         -n gem-rails-i18n-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Jun 15 2021 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt1
- > Ruby Policy 2.0
- ^ 5.1.1 -> 6.0.0

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 5.1.1-alt1
- Initial gemified build for Sisyphus.
