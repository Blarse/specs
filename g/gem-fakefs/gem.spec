%define        gemname fakefs

Name:          gem-fakefs
Version:       1.3.2
Release:       alt1
Summary:       A fake filesystem. Use it in your tests
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fakefs/fakefs
Vcs:           https://github.com/fakefs/fakefs.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bump) >= 0.5.3 gem(bump) < 1
BuildRequires: gem(maxitest) >= 3.6 gem(maxitest) < 4
BuildRequires: gem(rake) >= 10.3 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.1 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 0.82.0 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bump >= 0.8.0,bump < 1
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Provides:      gem(fakefs) = 1.3.2


%description
A fake filesystem. Use it in your tests.


%package       -n gem-fakefs-doc
Version:       1.3.2
Release:       alt1
Summary:       A fake filesystem. Use it in your tests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fakefs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fakefs) = 1.3.2

%description   -n gem-fakefs-doc
A fake filesystem. Use it in your tests documentation files.

%description   -n gem-fakefs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fakefs.


%package       -n gem-fakefs-devel
Version:       1.3.2
Release:       alt1
Summary:       A fake filesystem. Use it in your tests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fakefs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fakefs) = 1.3.2
Requires:      gem(bump) >= 0.5.3 gem(bump) < 1
Requires:      gem(maxitest) >= 3.6 gem(maxitest) < 4
Requires:      gem(rake) >= 10.3 gem(rake) < 14
Requires:      gem(rspec) >= 3.1 gem(rspec) < 4
Requires:      gem(rubocop) >= 0.82.0 gem(rubocop) < 2

%description   -n gem-fakefs-devel
A fake filesystem. Use it in your tests development package.

%description   -n gem-fakefs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fakefs.


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

%files         -n gem-fakefs-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fakefs-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.2-alt1
- + packaged gem with Ruby Policy 2.0
