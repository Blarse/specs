%define        gemname libxml-ruby

Name:          gem-libxml-ruby
Version:       3.2.3
Release:       alt1
Summary:       Ruby language bindings for the GNOME Libxml2 XML toolkit
License:       MIT
Group:         Development/Ruby
Url:           http://xml4r.github.io/libxml-ruby
Vcs:           https://github.com/xml4r/libxml-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libxml2-devel
BuildRequires: zlib-devel
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(minitest) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     libxml-ruby
Provides:      libxml-ruby
Provides:      gem(libxml-ruby) = 3.2.3


%description
The LibXML/Ruby project provides Ruby language bindings for the GNOME Libxml2
XML toolkit.


%package       -n gem-libxml-ruby-doc
Version:       3.2.3
Release:       alt1
Summary:       Ruby language bindings for the GNOME Libxml2 XML toolkit documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета libxml-ruby
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(libxml-ruby) = 3.2.3
Obsoletes:     libxml-ruby-doc
Provides:      libxml-ruby-doc

%description   -n gem-libxml-ruby-doc
Ruby language bindings for the GNOME Libxml2 XML toolkit documentation files.

%description   -n gem-libxml-ruby-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета libxml-ruby.


%package       -n gem-libxml-ruby-devel
Version:       3.2.3
Release:       alt1
Summary:       Ruby language bindings for the GNOME Libxml2 XML toolkit development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета libxml-ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(libxml-ruby) = 3.2.3
Requires:      gem(rake-compiler) >= 0
Requires:      gem(minitest) >= 0

%description   -n gem-libxml-ruby-devel
Ruby language bindings for the GNOME Libxml2 XML toolkit development package.

%description   -n gem-libxml-ruby-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета libxml-ruby.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-libxml-ruby-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-libxml-ruby-devel
%doc README.rdoc
%ruby_includedir/*


%changelog
* Tue Sep 13 2022 Pavel Skrylev <majioa@altlinux.org> 3.2.3-alt1
- ^ 3.1.0 -> 3.2.3

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt2.3
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt2.2
- fixed (!) spec according to changelog rules

* Fri Aug 02 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt2.1
- fixed (!) spec

* Wed Apr 10 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt2
- Use Ruby Policy 2.0

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1.1
- Rebuild with Ruby 2.5.0

* Fri Feb 09 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version

* Tue Sep 13 2016 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1
- New version
- Disable tests

* Wed Mar 19 2014 Led <led@altlinux.ru> 2.6.0-alt3
- Rebuilt with ruby-2.0.0-alt1

* Sat Mar 15 2014 Led <led@altlinux.ru> 2.6.0-alt2
- upstream fixes

* Fri Apr 12 2013 Led <led@altlinux.ru> 2.6.0-alt1
- 2.6.0
- cleaned up %%description
- updated URL
- fixed Group for %gem-libxml-ruby-doc subpackage

* Fri Dec 07 2012 Led <led@altlinux.ru> 1.1.3-alt2
- Rebuilt with ruby-1.9.3-alt1
- fixed build with ruby 1.9
- updated BuildRequires
- disabled check

* Fri May 08 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.3-alt1
- [1.1.3]

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 0.8.3-alt1
- [0.8.3]

* Fri Feb 02 2007 Sir Raorn <raorn@altlinux.ru> 0.3.8.4-alt1
- Built for Sisyphus
