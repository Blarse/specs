%define        gemname roadie-rails

Name:          gem-roadie-rails
Version:       2.2.0
Release:       alt1
Summary:       Making HTML emails comfortable for the Rails rockstars
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Mange/roadie-rails
Vcs:           https://github.com/mange/roadie-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(railties) >= 5.1 gem(railties) < 6.2
BuildRequires: gem(roadie) >= 3.1 gem(roadie) < 5.0
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(rails) >= 5.1 gem(rails) < 6.2
BuildRequires: gem(rspec) >= 3.8 gem(rspec) < 4
BuildRequires: gem(rspec-collection_matchers) >= 0
BuildRequires: gem(rspec-rails) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names rails_51,rails_52,rails_60
Requires:      gem(railties) >= 5.1 gem(railties) < 6.2
Requires:      gem(roadie) >= 3.1 gem(roadie) < 5.0
Obsoletes:     ruby-roadie-rails
Provides:      ruby-roadie-rails
Provides:      gem(roadie-rails) = 2.2.0


%description
This gem hooks up your Rails application with Roadie to help you generate HTML
emails.


%package       -n gem-roadie-rails-doc
Version:       2.2.0
Release:       alt1
Summary:       Making HTML emails comfortable for the Rails rockstars documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета roadie-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(roadie-rails) = 2.2.0

%description   -n gem-roadie-rails-doc
Making HTML emails comfortable for the Rails rockstars documentation
files.

This gem hooks up your Rails application with Roadie to help you generate HTML
emails.

%description   -n gem-roadie-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета roadie-rails.


%package       -n gem-roadie-rails-devel
Version:       2.2.0
Release:       alt1
Summary:       Making HTML emails comfortable for the Rails rockstars development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета roadie-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(roadie-rails) = 2.2.0
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(rails) >= 5.1 gem(rails) < 6.2
Requires:      gem(rspec) >= 3.8 gem(rspec) < 4
Requires:      gem(rspec-collection_matchers) >= 0
Requires:      gem(rspec-rails) >= 0

%description   -n gem-roadie-rails-devel
Making HTML emails comfortable for the Rails rockstars development
package.

This gem hooks up your Rails application with Roadie to help you generate HTML
emails.

%description   -n gem-roadie-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета roadie-rails.


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

%files         -n gem-roadie-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-roadie-rails-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- ^ 2.1.1 -> 2.2.0

* Wed Mar 11 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- ^ 2.1.0 -> 2.1.1
- ! spec

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- > Ruby Policy 2.0
- ^ 1.3.0 -> 2.1.0

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- Initial gemified build for Sisyphus
