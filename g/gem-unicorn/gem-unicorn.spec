%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname unicorn

Name:          gem-unicorn
Version:       6.1.0.54
Release:       alt1
Summary:       Unicorn: Rack HTTP server for fast clients and Unix
License:       GPL-2.0+ or Ruby-1.8
Group:         System/Servers
Url:           https://unicorn.bogomips.org/
Vcs:           https://bogomips.org/unicorn.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rack) >= 0
BuildRequires: gem(test-unit) >= 3.0
BuildRequires: gem(raindrops) >= 0.7
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(raindrops) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(raindrops) >= 0.7
Conflicts:     gem(raindrops) >= 1
Provides:      gem(unicorn) = 6.1.0.54

%ruby_on_build_rake_tasks build
%ruby_use_gem_version unicorn:6.1.0.54

%description
Unicorn is an HTTP server for Rack applications designed to only serve fast
clients on low-latency, high-bandwidth connections and take advantage of
features in Unix/Unix-like kernels. Slow clients should only be served by
placing a reverse proxy capable of fully buffering both the the request and
response in between Unicorn and slow clients.


%package       -n unicorn
Version:       6.1.0.54
Release:       alt1
Summary:       Unicorn: Rack HTTP server for fast clients and Unix executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета unicorn
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(unicorn) = 6.1.0.54
Conflicts:     golang-tools

%description   -n unicorn
Unicorn: Rack HTTP server for fast clients and Unix executable(s).

Unicorn is an HTTP server for Rack applications designed to only serve fast
clients on low-latency, high-bandwidth connections and take advantage of
features in Unix/Unix-like kernels. Slow clients should only be served by
placing a reverse proxy capable of fully buffering both the the request and
response in between Unicorn and slow clients.
%description   -n unicorn -l ru_RU.UTF-8
Исполнямка для самоцвета unicorn.


%if_enabled    doc
%package       -n gem-unicorn-doc
Version:       6.1.0.54
Release:       alt1
Summary:       Unicorn: Rack HTTP server for fast clients and Unix documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета unicorn
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(unicorn) = 6.1.0.54

%description   -n gem-unicorn-doc
Unicorn: Rack HTTP server for fast clients and Unix documentation
files.

Unicorn is an HTTP server for Rack applications designed to only serve fast
clients on low-latency, high-bandwidth connections and take advantage of
features in Unix/Unix-like kernels. Slow clients should only be served by
placing a reverse proxy capable of fully buffering both the the request and
response in between Unicorn and slow clients.
%description   -n gem-unicorn-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета unicorn.
%endif


%if_enabled    devel
%package       -n gem-unicorn-devel
Version:       6.1.0.54
Release:       alt1
Summary:       Unicorn: Rack HTTP server for fast clients and Unix development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета unicorn
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(unicorn) = 6.1.0.54
Requires:      gem(rack) >= 0
Requires:      gem(test-unit) >= 3.0
Requires:      ragel6
Requires:      libruby-devel
Conflicts:     gem(test-unit) >= 4

%description   -n gem-unicorn-devel
Unicorn: Rack HTTP server for fast clients and Unix development
package.

Unicorn is an HTTP server for Rack applications designed to only serve fast
clients on low-latency, high-bandwidth connections and take advantage of
features in Unix/Unix-like kernels. Slow clients should only be served by
placing a reverse proxy capable of fully buffering both the the request and
response in between Unicorn and slow clients.
%description   -n gem-unicorn-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета unicorn.
%endif


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n unicorn
%doc README
%_bindir/unicorn
%_bindir/unicorn_rails
%_mandir/unicorn.1.xz
%_mandir/unicorn_rails.1.xz

%if_enabled    doc
%files         -n gem-unicorn-doc
%doc README
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-unicorn-devel
%doc README
%ruby_includedir/*
%endif


%changelog
* Thu Mar 14 2024 Pavel Skrylev <majioa@altlinux.org> 6.1.0.54-alt1
- ^ 6.1.0 -> 6.1.0p54

* Thu Sep 22 2022 Pavel Skrylev <majioa@altlinux.org> 6.1.0-alt2
- !fix rakefile to build a ragel task (closes #43835)

* Mon Jul 11 2022 Pavel Skrylev <majioa@altlinux.org> 6.1.0-alt1.1
- !fix dep to ragel6

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 6.1.0-alt1
- ^ 6.0.0 -> 6.1.0

* Sat Apr 24 2021 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt1
- ^ 5.5.4 -> 6.0.0

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 5.5.4-alt1
- ^ 5.5.0 -> 5.5.4
- ! spec syntax and tags

* Sat Apr 06 2019 Pavel Skrylev <majioa@altlinux.org> 5.5.0-alt3
- Fix lost gem dependencies
- Fix spec

* Mon Mar 18 2019 Pavel Skrylev <majioa@altlinux.org> 5.5.0-alt2
- Fix shebang line

* Mon Mar 18 2019 Andrey Cherepanov <cas@altlinux.org> 5.5.0-alt1
- New version.
- Rewrite spec according Ruby Policy 2.0.

* Sun Oct 14 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1.1
- Rebuild with Ruby 2.5.0

* Sun Dec 24 2017 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1
- New version.

* Wed Oct 04 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt1
- New version

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1.1
- Rebuild with Ruby 2.4.1

* Wed Jun 28 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- new version 5.2.0

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- new version 5.1.0

* Wed Nov 19 2014 Anton Gorlov <stalker@altlinux.ru> 4.8.3-alt1
- update to  new version

* Wed Mar 19 2014 Led <led@altlinux.ru> 4.7.0-alt1.1
- Rebuilt with ruby-2.0.0-alt1

* Sat Dec 07 2013 Anton Gorlov <stalker@altlinux.ru> 4.7.0-alt1
- update to  new version

* Wed Apr 24 2013 Anton Gorlov <stalker@altlinux.ru> 4.6.2-alt1
- update to  new version

* Fri Dec 07 2012 Led <led@altlinux.ru> 4.3.1-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri May 18 2012 Anton Gorlov <stalker@altlinux.ru> 4.3.1-alt1
- update to  new version

* Tue Mar 20 2012 Anton Gorlov <stalker@altlinux.ru> 4.2.0-alt1
- update to  new version

* Sat Sep 03 2011 Anton Gorlov <stalker@altlinux.ru> 4.1.1-alt1
- update to  new version

* Wed Aug 17 2011 Anton Gorlov <stalker@altlinux.ru> 4.0.1-alt3
- added examples to main package

* Sat Aug 13 2011 Anton Gorlov <stalker@altlinux.ru> 4.0.1-alt2
- fix conflict with with ruby-parseconfig-doc

* Sat Aug 13 2011 Anton Gorlov <stalker@altlinux.ru> 4.0.1-alt1
- initial build for ALTLinux
