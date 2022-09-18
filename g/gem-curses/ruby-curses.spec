%define        gemname curses

Name:          gem-curses
Version:       1.4.4
Release:       alt1
Summary:       Ruby binding for curses, ncurses, and PDCurses
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/curses
Vcs:           https://github.com/ruby/curses.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libncursesw-devel
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names bench
Obsoletes:     ruby-curses < %EVR
Provides:      ruby-curses = %EVR
Provides:      gem(curses) = 1.4.4


%description
A Ruby binding for curses, ncurses, and PDCurses. curses is an extension library
for text UI applications. Formerly part of the Ruby standard library.


%package       -n gem-curses-doc
Version:       1.4.4
Release:       alt1
Summary:       Ruby binding for curses, ncurses, and PDCurses documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета curses
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(curses) = 1.4.4

%description   -n gem-curses-doc
Ruby binding for curses, ncurses, and PDCurses documentation files.

A Ruby binding for curses, ncurses, and PDCurses. curses is an extension library
for text UI applications. Formerly part of the Ruby standard library.

%description   -n gem-curses-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета curses.


%package       -n gem-curses-devel
Version:       1.4.4
Release:       alt1
Summary:       Ruby binding for curses, ncurses, and PDCurses development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета curses
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(curses) = 1.4.4
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-curses-devel
Ruby binding for curses, ncurses, and PDCurses development package.

A Ruby binding for curses, ncurses, and PDCurses. curses is an extension library
for text UI applications. Formerly part of the Ruby standard library.

%description   -n gem-curses-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета curses.


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
%ruby_gemextdir

%files         -n gem-curses-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-curses-devel
%doc README.md


%changelog
* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.4.4-alt1
- ^ 1.4.2 -> 1.4.4

* Fri Oct 08 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt1
- ^ 1.4.0 -> 1.4.2

* Sat Apr 24 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- new version 1.4.0

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.2-alt1
- ^ 1.2.7 -> 1.3.2
- ! spec tags and syntax

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.7-alt1
- > Ruby Policy 2.0
- ^ 1.2.5 -> 1.2.7

* Tue Oct 16 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1.3
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1.2
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1.1
- Rebuild with Ruby 2.4.2

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.3-alt1.1
- Rebuild with Ruby 2.4.1

* Mon Jul 03 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.3-alt1
- New version

* Sat Apr 22 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1
- New version

* Mon Mar 27 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Wed Feb 22 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sat Feb 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- new version 1.1.3

* Tue Feb 07 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- new version 1.1.2

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- new version 1.1.1

* Fri Oct 21 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- Initial build in Sisyphus
