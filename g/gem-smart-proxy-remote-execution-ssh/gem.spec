%define        gemname smart_proxy_remote_execution_ssh

Name:          gem-smart-proxy-remote-execution-ssh
Version:       0.4.1
Release:       alt1
Summary:       Ssh remote execution provider for Foreman Smart-Proxy
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_remote_execution_ssh
Vcs:           https://github.com/theforeman/smart_proxy_remote_execution_ssh.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 1 gem(mocha) < 2
BuildRequires: gem(webmock) >= 1 gem(webmock) < 4
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rubocop) >= 0.82.0 gem(rubocop) < 2
BuildRequires: gem(smart_proxy_dynflow) >= 0.5 gem(smart_proxy_dynflow) < 1
BuildRequires: gem(net-ssh) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(smart_proxy_dynflow) >= 0.5 gem(smart_proxy_dynflow) < 1
Requires:      gem(net-ssh) >= 0
Provides:      gem(smart_proxy_remote_execution_ssh) = 0.4.1


%description
This a plugin for foreman smart-proxy allowing using ssh for the remote
execution.


%package       -n gem-smart-proxy-remote-execution-ssh-doc
Version:       0.4.1
Release:       alt1
Summary:       Ssh remote execution provider for Foreman Smart-Proxy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета smart_proxy_remote_execution_ssh
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(smart_proxy_remote_execution_ssh) = 0.4.1

%description   -n gem-smart-proxy-remote-execution-ssh-doc
Ssh remote execution provider for Foreman Smart-Proxy documentation files.

This a plugin for foreman smart-proxy allowing using ssh for the remote
execution.

%description   -n gem-smart-proxy-remote-execution-ssh-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета smart_proxy_remote_execution_ssh.


%package       -n gem-smart-proxy-remote-execution-ssh-devel
Version:       0.4.1
Release:       alt1
Summary:       Ssh remote execution provider for Foreman Smart-Proxy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета smart_proxy_remote_execution_ssh
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(smart_proxy_remote_execution_ssh) = 0.4.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 1 gem(mocha) < 2
Requires:      gem(webmock) >= 1 gem(webmock) < 4
Requires:      gem(rack-test) >= 0
Requires:      gem(rubocop) >= 0.82.0 gem(rubocop) < 2

%description   -n gem-smart-proxy-remote-execution-ssh-devel
Ssh remote execution provider for Foreman Smart-Proxy development package.

This a plugin for foreman smart-proxy allowing using ssh for the remote
execution.

%description   -n gem-smart-proxy-remote-execution-ssh-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета smart_proxy_remote_execution_ssh.


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

%files         -n gem-smart-proxy-remote-execution-ssh-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-smart-proxy-remote-execution-ssh-devel
%doc README.md


%changelog
* Tue Nov 09 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.1-alt1
- + packaged gem with Ruby Policy 2.0
