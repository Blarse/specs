%define        gemname redfish_client

Name:          gem-redfish-client
Version:       0.5.4
Release:       alt1
Summary:       Simple Redfish client library
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/xlab-steampunk/redfish-client-ruby
Vcs:           https://github.com/xlab-steampunk/redfish-client-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(excon) >= 0.71 gem(excon) < 1
BuildRequires: gem(server_sent_events) >= 0.1 gem(server_sent_events) < 1
BuildRequires: gem(rake) >= 11.0
BuildRequires: gem(rspec) >= 3.7
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(webmock) >= 3.4 gem(webmock) < 4
BuildRequires: gem(yard) >= 0
BuildRequires: gem(rubocop) >= 0.54.0 gem(rubocop) < 2
BuildRequires: gem(pry) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(excon) >= 0.71 gem(excon) < 1
Requires:      gem(server_sent_events) >= 0.1 gem(server_sent_events) < 1
Provides:      gem(redfish_client) = 0.5.4


%description
This repository contains source code for redfish_client gem that can be used to
connect to Redfish services.


%package       -n gem-redfish-client-doc
Version:       0.5.4
Release:       alt1
Summary:       Simple Redfish client library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redfish_client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redfish_client) = 0.5.4

%description   -n gem-redfish-client-doc
Simple Redfish client library documentation files.

This repository contains source code for redfish_client gem that can be used to
connect to Redfish services.

%description   -n gem-redfish-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redfish_client.


%package       -n gem-redfish-client-devel
Version:       0.5.4
Release:       alt1
Summary:       Simple Redfish client library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redfish_client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redfish_client) = 0.5.4
Requires:      gem(rake) >= 11.0
Requires:      gem(rspec) >= 3.7
Requires:      gem(simplecov) >= 0
Requires:      gem(webmock) >= 3.4 gem(webmock) < 4
Requires:      gem(yard) >= 0
Requires:      gem(rubocop) >= 0.54.0 gem(rubocop) < 2
Requires:      gem(pry) >= 0

%description   -n gem-redfish-client-devel
Simple Redfish client library development package.

This repository contains source code for redfish_client gem that can be used to
connect to Redfish services.

%description   -n gem-redfish-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета redfish_client.


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

%files         -n gem-redfish-client-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-redfish-client-devel
%doc README.md


%changelog
* Mon Nov 08 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.4-alt1
- + packaged gem with Ruby Policy 2.0
