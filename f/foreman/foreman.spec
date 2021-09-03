Name:          foreman
Version:       2.5.0
Release:       alt0.2
Summary:       An application that automates the lifecycle of servers
License:       GPLv3
Group:         System/Servers
Url:           https://theforeman.org
Vcs:           https://github.com/theforeman/foreman.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       database.yml
Source2:       foreman.sysconfig
Source3:       foreman.logrotate
Source4:       foreman.cron.d
Source5:       foreman.tmpfiles
Source6:       foreman.service
Source7:       settings.yml
Source9:       manifest.js
# Source10:      node_modules.tar.gz
Source11:      foreman-jobs.service
Source12:      foreman-jobs.sysconfig
# TODO remove sass patch part when patternfly-sass gem will be upgraded to new font-awesome-sass v5
Patch:         foreman.patch
Patch4:        1.24.3.2.alt5.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-macros-webserver-common
BuildRequires: elfutils
BuildRequires: glibc-core
BuildRequires: libX11-devel
BuildRequires: libnss-devel
BuildRequires: libnspr-devel
BuildRequires: fontconfig
BuildRequires: libfreetype-devel
BuildRequires: node-sass
BuildRequires: gem(sass) >= 3.2
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(sass-rails) >= 0
# BuildRequires: gem(compass) >= 0
BuildRequires: gem(rails) >= 6.0.3.1 gem(rails) < 7
BuildRequires: gem(rest-client) >= 2.0.0 gem(rest-client) < 3
BuildRequires: gem(audited) >= 4.9.0 gem(audited) < 6
BuildRequires: gem(will_paginate) >= 3.1.7 gem(will_paginate) < 4
BuildRequires: gem(ancestry) >= 3.2.0 gem(ancestry) < 5
BuildRequires: gem(scoped_search) >= 4.1.8 gem(scoped_search) < 5
BuildRequires: gem(ldap_fluff) >= 0.5.0 gem(ldap_fluff) < 1.0
BuildRequires: gem(apipie-rails) >= 0.5.17 gem(apipie-rails) < 0.6.0
BuildRequires: gem(apipie-dsl) >= 2.2.6
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rabl) >= 0.14.2 gem(rabl) < 0.15
BuildRequires: gem(oauth) >= 0.5.4 gem(oauth) < 1
BuildRequires: gem(deep_cloneable) >= 3 gem(deep_cloneable) < 4
BuildRequires: gem(validates_lengths_from_database) >= 0.5 gem(validates_lengths_from_database) < 1
BuildRequires: gem(friendly_id) >= 5.3.0 gem(friendly_id) < 6
BuildRequires: gem(secure_headers) >= 6.3 gem(secure_headers) < 7
BuildRequires: gem(safemode) >= 1.3.5 gem(safemode) < 2
BuildRequires: gem(fast_gettext) >= 1.4 gem(fast_gettext) < 2
BuildRequires: gem(gettext_i18n_rails) >= 1.8 gem(gettext_i18n_rails) < 2
BuildRequires: gem(rails-i18n) >= 6.0 gem(rails-i18n) < 7
BuildRequires: gem(i18n) >= 1.1 gem(i18n) < 2
BuildRequires: gem(logging) >= 1.8.0 gem(logging) < 3.0.0
BuildRequires: gem(fog-core) >= 2.1.0 gem(fog-core) < 3
BuildRequires: gem(net-scp) >= 0
BuildRequires: gem(net-ssh) >= 4.2.0 gem(net-ssh) < 7
BuildRequires: gem(net-ldap) >= 0.16.0
BuildRequires: gem(net-ping) >= 0
BuildRequires: gem(activerecord-session_store) >= 2.0.0 gem(activerecord-session_store) < 3
BuildRequires: gem(sprockets) >= 4.0 gem(sprockets) < 5
BuildRequires: gem(sprockets-rails) >= 3.0 gem(sprockets-rails) < 4
BuildRequires: gem(record_tag_helper) >= 1.0 gem(record_tag_helper) < 2
BuildRequires: gem(responders) >= 3.0 gem(responders) < 4
BuildRequires: gem(roadie-rails) >= 2.0 gem(roadie-rails) < 3
BuildRequires: gem(deacon) >= 1.0 gem(deacon) < 2
BuildRequires: gem(webpack-rails) >= 0.9.8 gem(webpack-rails) < 0.10
BuildRequires: gem(mail) >= 2.7 gem(mail) < 3
BuildRequires: gem(sshkey) >= 1.9 gem(sshkey) < 2
BuildRequires: gem(dynflow) >= 1.4.4 gem(dynflow) < 2.0.0
BuildRequires: gem(daemons) >= 0
BuildRequires: gem(bcrypt) >= 3.1 gem(bcrypt) < 4
BuildRequires: gem(get_process_mem) >= 0
BuildRequires: gem(rack-cors) >= 1.0.2 gem(rack-cors) < 2
BuildRequires: gem(jwt) >= 2.2.1 gem(jwt) < 3
BuildRequires: gem(graphql) >= 1.8.0 gem(graphql) < 2
BuildRequires: gem(graphql-batch) >= 0
BuildRequires: gem(fog-aws) >= 3.6.2 gem(fog-aws) < 4
BuildRequires: gem(fog-ovirt) >= 2.0.1 gem(fog-ovirt) < 3
BuildRequires: gem(fog-libvirt) >= 0.8.0
BuildRequires: gem(ruby-libvirt) >= 0.5 gem(ruby-libvirt) < 1
BuildRequires: gem(fog-vsphere) >= 3.5.0 gem(fog-vsphere) < 4.0
BuildRequires: gem(rbvmomi) >= 2.0 gem(rbvmomi) < 3
BuildRequires: gem(logging-journald) >= 2.0 gem(logging-journald) < 3
BuildRequires: gem(puma) >= 5.1 gem(puma) < 6
BuildRequires: gem(pg) >= 0.18 gem(pg) < 2.0
BuildRequires: gem(facter) >= 0
BuildRequires: gem(activerecord-nulldb-adapter) >= 0
BuildRequires: gem(fog-google) >= 1.11.0 gem(fog-google) < 2
BuildRequires: gem(redis) >= 4.0 gem(redis) < 5
BuildRequires: gem(sidekiq) >= 5.0 gem(sidekiq) < 6
BuildRequires: gem(gitlab-sidekiq-fetcher) >= 0
BuildRequires: gem(sd_notify) >= 0.1 gem(sd_notify) < 1
BuildRequires: gem(rack-openid) >= 1.3 gem(rack-openid) < 2
BuildRequires: gem(prometheus-client) >= 1.0 gem(prometheus-client) < 3
BuildRequires: gem(statsd-instrument) < 4
BuildRequires: gem(maruku) >= 0.7 gem(maruku) < 1
BuildRequires: gem(gettext) >= 3.2.1 gem(gettext) < 4.0.0
BuildRequires: gem(immigrant) >= 0.1 gem(immigrant) < 1
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-rails) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry-doc) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(pry-remote) >= 0
BuildRequires: gem(rainbow) >= 2.2.1
BuildRequires: gem(bullet) >= 6.1.0
BuildRequires: gem(parallel_tests) >= 0
BuildRequires: gem(spring) >= 1.0 gem(spring) < 3
BuildRequires: gem(benchmark-ips) >= 2.8.2
BuildRequires: gem(bootsnap) >= 0
BuildRequires: gem(graphiql-rails) >= 1.7 gem(graphiql-rails) < 2
BuildRequires: gem(wirb) >= 1.0 gem(wirb) < 3.0
BuildRequires: gem(amazing_print) >= 1.1 gem(amazing_print) < 2
BuildRequires: gem(rack-jsonp) >= 0
BuildRequires: gem(jquery-ui-rails) >= 6.0 gem(jquery-ui-rails) < 7
BuildRequires: gem(patternfly-sass) >= 3.59.4 gem(patternfly-sass) < 4
BuildRequires: gem(gettext_i18n_rails_js) >= 1.0 gem(gettext_i18n_rails_js) < 2
BuildRequires: gem(execjs) >= 1.4.0 gem(execjs) < 3.0
BuildRequires: gem(uglifier) >= 1.0.3
BuildRequires: gem(sass-rails) >= 6.0 gem(sass-rails) < 7
BuildRequires: gem(coffee-rails) >= 5.0.0 gem(coffee-rails) < 5.1
BuildRequires: gem(fog-openstack) >= 1.0.8 gem(fog-openstack) < 2.0.0
BuildRequires: gem(mocha) >= 1.11 gem(mocha) < 2
BuildRequires: gem(single_test) >= 0.6 gem(single_test) < 1
BuildRequires: gem(minitest) >= 5.1 gem(minitest) < 6
BuildRequires: gem(minitest-retry) >= 0.0 gem(minitest-retry) < 1
BuildRequires: gem(minitest-spec-rails) >= 6.0 gem(minitest-spec-rails) < 7
BuildRequires: gem(ci_reporter_minitest) >= 0
BuildRequires: gem(capybara) >= 3.0 gem(capybara) < 3.32.1
BuildRequires: gem(show_me_the_cookies) >= 5.0 gem(show_me_the_cookies) < 6
BuildRequires: gem(database_cleaner) >= 1.3 gem(database_cleaner) < 3
BuildRequires: gem(launchy) >= 2.4 gem(launchy) < 3
BuildRequires: gem(factory_bot_rails) >= 5.0 gem(factory_bot_rails) < 7
BuildRequires: gem(selenium-webdriver) >= 0
BuildRequires: gem(shoulda-matchers) >= 4.0 gem(shoulda-matchers) < 5
BuildRequires: gem(shoulda-context) >= 1.2 gem(shoulda-context) < 3
BuildRequires: gem(as_deprecation_tracker) >= 1.4 gem(as_deprecation_tracker) < 2
BuildRequires: gem(rails-controller-testing) >= 1.0 gem(rails-controller-testing) < 2
BuildRequires: gem(rfauxfactory) >= 0.1.5 gem(rfauxfactory) < 1
BuildRequires: gem(robottelo_reporter) >= 0.1 gem(robottelo_reporter) < 1
BuildRequires: gem(theforeman-rubocop) >= 0.0.6 gem(theforeman-rubocop) < 0.1
BuildRequires: gem(webmock) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findreq_skiplist %_libexecdir/%name/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %_libexecdir/%name/**/*
%ruby_use_gem_dependency statsd-instrument >= 3.0,statsd-instrument < 4
%ruby_use_gem_dependency rack-cors >= 1.0,rack-cors < 2
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency jwt >= 2.2.1,jwt < 3
%ruby_use_gem_dependency audited >= 5.0.1,audited < 6
%ruby_use_gem_dependency net-ssh >= 6.1.0,net-ssh < 7
%ruby_use_gem_dependency rails >= 6.1.3.2,rails < 7
%ruby_use_gem_dependency prometheus-client >= 2.0.0,prometheus-client < 3
%ruby_use_gem_dependency puma >= 5.2.2,puma < 6
%ruby_use_gem_dependency graphql >= 1.9.6,graphql < 2
%ruby_use_gem_dependency fog-core >= 2.2.4,fog-core < 3
%ruby_use_gem_dependency patternfly-sass >= 3.59.5,patternfly-sass < 4
%ruby_use_gem_dependency ancestry >= 4.0.0,ancestry < 5
%ruby_use_gem_dependency friendly_id >= 5.4.1,friendly_id < 6
%ruby_use_gem_dependency fog-google >= 1.13.0,fog-google < 2
%ruby_use_gem_dependency database_cleaner >= 2.0.1,database_cleaner < 3
%ruby_use_gem_dependency factory_bot_rails >= 6.2.0,factory_bot_rails < 7
%ruby_use_gem_dependency shoulda-matchers >= 4.5.1,shoulda-matchers < 5
%ruby_use_gem_dependency shoulda-context >= 2.0.0,shoulda-context < 3
Requires:      gem-scoped-search gem-friendly-id gem-fog-google
Requires:      gem(rails) >= 6.0.3.1 gem(rails) < 7
Requires:      gem(rest-client) >= 2.0.0 gem(rest-client) < 3
Requires:      gem(audited) >= 4.9.0 gem(audited) < 6
Requires:      gem(will_paginate) >= 3.1.7 gem(will_paginate) < 4
Requires:      gem(ancestry) >= 3.2.0 gem(ancestry) < 5
Requires:      gem(scoped_search) >= 4.1.8 gem(scoped_search) < 5
Requires:      gem(ldap_fluff) >= 0.5.0 gem(ldap_fluff) < 1.0
Requires:      gem(apipie-rails) >= 0.5.17 gem(apipie-rails) < 0.6.0
Requires:      gem(apipie-dsl) >= 2.2.6
Requires:      gem(rdoc) >= 0 gem(rdoc) < 7
Requires:      gem(rabl) >= 0.14.2 gem(rabl) < 0.15
Requires:      gem(oauth) >= 0.5.4 gem(oauth) < 1
Requires:      gem(deep_cloneable) >= 3 gem(deep_cloneable) < 4
Requires:      gem(validates_lengths_from_database) >= 0.5 gem(validates_lengths_from_database) < 1
Requires:      gem(friendly_id) >= 5.3.0 gem(friendly_id) < 6
Requires:      gem(secure_headers) >= 6.3 gem(secure_headers) < 7
Requires:      gem(safemode) >= 1.3.5 gem(safemode) < 2
Requires:      gem(fast_gettext) >= 1.4 gem(fast_gettext) < 2
Requires:      gem(gettext_i18n_rails) >= 1.8 gem(gettext_i18n_rails) < 2
Requires:      gem(rails-i18n) >= 6.0 gem(rails-i18n) < 7
Requires:      gem(i18n) >= 1.1 gem(i18n) < 2
Requires:      gem(logging) >= 1.8.0 gem(logging) < 3.0.0
Requires:      gem(fog-core) >= 2.1.0 gem(fog-core) < 3
Requires:      gem(net-scp) >= 0
Requires:      gem(net-ssh) >= 4.2.0 gem(net-ssh) < 7
Requires:      gem(net-ldap) >= 0.16.0
Requires:      gem(net-ping) >= 0
Requires:      gem(activerecord-session_store) >= 2.0.0 gem(activerecord-session_store) < 3
Requires:      gem(sprockets) >= 4.0 gem(sprockets) < 5
Requires:      gem(sprockets-rails) >= 3.0 gem(sprockets-rails) < 4
Requires:      gem(record_tag_helper) >= 1.0 gem(record_tag_helper) < 2
Requires:      gem(responders) >= 3.0 gem(responders) < 4
Requires:      gem(roadie-rails) >= 2.0 gem(roadie-rails) < 3
Requires:      gem(deacon) >= 1.0 gem(deacon) < 2
Requires:      gem(webpack-rails) >= 0.9.8 gem(webpack-rails) < 0.10
Requires:      gem(mail) >= 2.7 gem(mail) < 3
Requires:      gem(sshkey) >= 1.9 gem(sshkey) < 2
Requires:      gem(dynflow) >= 1.4.4 gem(dynflow) < 2.0.0
Requires:      gem(daemons) >= 0
Requires:      gem(bcrypt) >= 3.1 gem(bcrypt) < 4
Requires:      gem(get_process_mem) >= 0
Requires:      gem(rack-cors) >= 1.0.2 gem(rack-cors) < 2
Requires:      gem(jwt) >= 2.2.1 gem(jwt) < 3
Requires:      gem(graphql) >= 1.8.0 gem(graphql) < 2
Requires:      gem(graphql-batch) >= 0
Requires:      gem(fog-aws) >= 3.6.2 gem(fog-aws) < 4
Requires:      gem(fog-ovirt) >= 2.0.1 gem(fog-ovirt) < 3
Requires:      gem(fog-libvirt) >= 0.8.0
Requires:      gem(ruby-libvirt) >= 0.5 gem(ruby-libvirt) < 1
Requires:      gem(fog-vsphere) >= 3.5.0 gem(fog-vsphere) < 4.0
Requires:      gem(rbvmomi) >= 2.0 gem(rbvmomi) < 3
Requires:      gem(logging-journald) >= 2.0 gem(logging-journald) < 3
Requires:      gem(puma) >= 5.1 gem(puma) < 6
Requires:      gem(pg) >= 0.18 gem(pg) < 2.0
Requires:      gem(facter) >= 0
Requires:      gem(activerecord-nulldb-adapter) >= 0
Requires:      gem(fog-google) >= 1.11.0 gem(fog-google) < 2
Requires:      gem(redis) >= 4.0 gem(redis) < 5
Requires:      gem(sidekiq) >= 5.0 gem(sidekiq) < 6
Requires:      gem(gitlab-sidekiq-fetcher) >= 0
Requires:      gem(sd_notify) >= 0.1 gem(sd_notify) < 1
Requires:      gem(rack-openid) >= 1.3 gem(rack-openid) < 2
Requires:      gem(prometheus-client) >= 1.0 gem(prometheus-client) < 3
Requires:      gem(statsd-instrument) < 4
Requires:      gem(maruku) >= 0.7 gem(maruku) < 1
Requires:      gem(gettext) >= 3.2.1 gem(gettext) < 4.0.0
Requires:      gem(immigrant) >= 0.1 gem(immigrant) < 1
Requires:      gem(byebug) >= 0
Requires:      gem(pry) >= 0 gem(pry) < 1
Requires:      gem(pry-rails) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry-doc) >= 0
Requires:      gem(pry-stack_explorer) >= 0
Requires:      gem(pry-remote) >= 0
Requires:      gem(rainbow) >= 2.2.1
Requires:      gem(bullet) >= 6.1.0
Requires:      gem(parallel_tests) >= 0
Requires:      gem(spring) >= 1.0 gem(spring) < 3
Requires:      gem(benchmark-ips) >= 2.8.2
Requires:      gem(foreman) >= 0
Requires:      gem(bootsnap) >= 0
Requires:      gem(graphiql-rails) >= 1.7 gem(graphiql-rails) < 2
Requires:      gem(wirb) >= 1.0 gem(wirb) < 3.0
Requires:      gem(amazing_print) >= 1.1 gem(amazing_print) < 2
Requires:      gem(rack-jsonp) >= 0
Requires:      gem(jquery-ui-rails) >= 6.0 gem(jquery-ui-rails) < 7
Requires:      gem(patternfly-sass) >= 3.59.4 gem(patternfly-sass) < 4
Requires:      gem(gettext_i18n_rails_js) >= 1.0 gem(gettext_i18n_rails_js) < 2
Requires:      gem(execjs) >= 1.4.0 gem(execjs) < 3.0
Requires:      gem(uglifier) >= 1.0.3
Requires:      gem(sass-rails) >= 6.0 gem(sass-rails) < 7
Requires:      gem(coffee-rails) >= 5.0.0 gem(coffee-rails) < 5.1
Requires:      gem(fog-openstack) >= 1.0.8 gem(fog-openstack) < 2.0.0
Requires:      gem(mocha) >= 1.11 gem(mocha) < 2
Requires:      gem(single_test) >= 0.6 gem(single_test) < 1
Requires:      gem(minitest) >= 5.1 gem(minitest) < 6
Requires:      gem(minitest-retry) >= 0.0 gem(minitest-retry) < 1
Requires:      gem(minitest-spec-rails) >= 6.0 gem(minitest-spec-rails) < 7
Requires:      gem(ci_reporter_minitest) >= 0
Requires:      gem(capybara) >= 3.0 gem(capybara) < 3.32.1
Requires:      gem(show_me_the_cookies) >= 5.0 gem(show_me_the_cookies) < 6
Requires:      gem(database_cleaner) >= 1.3 gem(database_cleaner) < 3
Requires:      gem(launchy) >= 2.4 gem(launchy) < 3
Requires:      gem(factory_bot_rails) >= 5.0 gem(factory_bot_rails) < 7
Requires:      gem(selenium-webdriver) >= 0
Requires:      gem(shoulda-matchers) >= 4.0 gem(shoulda-matchers) < 5
Requires:      gem(shoulda-context) >= 1.2 gem(shoulda-context) < 3
Requires:      gem(as_deprecation_tracker) >= 1.4 gem(as_deprecation_tracker) < 2
Requires:      gem(rails-controller-testing) >= 1.0 gem(rails-controller-testing) < 2
Requires:      gem(rfauxfactory) >= 0.1.5 gem(rfauxfactory) < 1
Requires:      gem(robottelo_reporter) >= 0.1 gem(robottelo_reporter) < 1
Requires:      gem(theforeman-rubocop) >= 0.0.6 gem(theforeman-rubocop) < 0.1
Requires:      gem(webmock) >= 0
Requires:      wget
Requires:      vixie-cron
Requires:      postgresql-server
Requires:      libX11
Requires:      libnss
Requires:      libnspr
Requires:      fontconfig
Requires:      libfreetype
Requires:      node-sass
Requires:      dynflow


%description
Foreman is a free open source project that gives you the power to easily
automate repetitive tasks, quickly deploy applications, and proactively manage
your servers lifecyle, on-premises or in the cloud. From provisioning and
configuration to orchestration and monitoring, Foreman integrates with your
existing infrastructure to make operations easier. Using Puppet, Ansible, Chef,
Salt and Foreman's smart proxy architecture, you can easily automate repetitive
tasks, quickly deploy applications, and proactively manage change, both
on-premise with VMs and bare-metal or in the cloud. Foreman provides
comprehensive, interaction facilities including a web frontend, CLI and RESTful
API which enables you to build higher level business logic on top of a solid
foundation.


#%package       -n gem-font-awesome-sass
#Version:       4.7.0
#Release:       alt1
#Summary:       Font-Awesome SASS
#Group:         Development/Ruby
#BuildArch:     noarch
#
#Requires:      gem(sass) >= 3.2
#Provides:      gem(font-awesome-sass) = 4.7.0
#
#%description   -n gem-font-awesome-sass
#Font-Awesome SASS gem for use in Ruby projects
#
#
#%package       -n gem-font-awesome-sass-doc
#Version:       4.7.0
#Release:       alt1
#Summary:       Font-Awesome SASS documentation files
#Summary(ru_RU.UTF-8): Файлы сведений для самоцвета font-awesome-sass
#Group:         Development/Documentation
#BuildArch:     noarch
#
#Requires:      gem(font-awesome-sass) = 4.7.0
#
#%description   -n gem-font-awesome-sass-doc
#Font-Awesome SASS documentation files.
#
#Font-Awesome SASS gem for use in Ruby projects
#
#%description   -n gem-font-awesome-sass-doc -l ru_RU.UTF-8
#Файлы сведений для самоцвета font-awesome-sass.
#
#
#%package       -n gem-font-awesome-sass-devel
#Version:       4.7.0
#Release:       alt1
#Summary:       Font-Awesome SASS development package
#Summary(ru_RU.UTF-8): Файлы для разработки самоцвета font-awesome-sass
#Group:         Development/Ruby
#BuildArch:     noarch
#
#Requires:      gem(font-awesome-sass) = 4.7.0
#Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
#Requires:      gem(rake) >= 0 gem(rake) < 14
#Requires:      gem(sass-rails) >= 0
#Requires:      gem(compass) >= 0
#
#%description   -n gem-font-awesome-sass-devel
#Font-Awesome SASS development package.
#
#Font-Awesome SASS gem for use in Ruby projects
#
#%description   -n gem-font-awesome-sass-devel -l ru_RU.UTF-8
#Файлы для разработки самоцвета font-awesome-sass.
#
#
%package       -n foreman-doc
Version:       2.5.0
Release:       alt0.1
Summary:       An application that automates the lifecycle of servers documentation files
Group:         Documentation

Requires:      foreman = 2.5.0

%description   -n foreman-doc
An application that automates the lifecycle of servers documentation files.

%description   -n foreman-doc -l ru_RU.UTF-8
Файлы сведений для приложения foreman.


%package       -n foreman-devel
Version:       2.5.0
Release:       alt0.1
Summary:       An application that automates the lifecycle of servers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rails) >= 6 gem(rails) < 7
Requires:      gem(graphql) >= 1.9 gem(graphql) < 2
Requires:      gem(jquery-ui-rails) >= 6.0 gem(jquery-ui-rails) < 7
Requires:      gem(patternfly-sass) >= 3.38 gem(patternfly-sass) < 4
Requires:      gem(fog-core) >= 2.1 gem(fog-core) < 3
Requires:      gem(prometheus-client) >= 2.0 gem(prometheus-client) < 3
Requires:      gem(sprockets) >= 4.0 gem(sprockets) < 5
Requires:      gem(sass-rails) >= 6.0 gem(sass-rails) < 7
Requires:      gem(net-ssh) >= 6.0 gem(net-ssh) < 7

%description   -n foreman-devel
An application that automates the lifecycle of servers development
package.

Foreman is a free open source project that gives you the power to easily
automate repetitive tasks, quickly deploy applications, and proactively manage
your servers lifecyle, on-premises or in the cloud. From provisioning and
configuration to orchestration and monitoring, Foreman integrates with your
existing infrastructure to make operations easier. Using Puppet, Ansible, Chef,
Salt and Foreman's smart proxy architecture, you can easily automate repetitive
tasks, quickly deploy applications, and proactively manage change, both
on-premise with VMs and bare-metal or in the cloud. Foreman provides
comprehensive, interaction facilities including a web frontend, CLI and RESTful
API which enables you to build higher level business logic on top of a solid
foundation.

%description   -n foreman-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman.




%prep
%setup
# %setup -a 10
%patch -p1
sed -e "s/a2x/asciidoctor/" -e "s/-f/-b/" -i Rakefile.dist # NOTE patching a2x to asciidoctor
sed "s,gem 'turbolinks'.*,gem 'gitlab-turbolinks-classic'," -i Gemfile
rm -rf ./node_modules/node-sass/ ./node_modules/.bin/node-sass
install -Dm0755 %SOURCE9 app/assets/config/manifest.js
rm -rf ./extras/noVNC/websockify
rm -rf ./node_modules/jstz
rm -rf ./node_modules/node-gyp
rm -rf ./node_modules/npm/node_modules/node-gyp
rm -rf ./node_modules/railroad-diagrams
# Set correct python3 executable in shebang
subst 's|#!.*python$|#!%__python3|' $(grep -Rl '#!.*python$' *) \
    $(find ./ -type f \( -name '*.py' -o -name '%name' \))
# Add record to end of scss order
echo "@import 'fix-views';" >> app/assets/stylesheets/application.scss


%build
%ruby_build
make -C locale all-mo

%install
%ruby_install

rm -rf %buildroot%_libexecdir/%name/extras/{jumpstart,spec}
rm -rf %buildroot%_bindir/{bundle,rails,rake,spring}
rm -rf %buildroot%_sysconfdir/%name
rm -rf %buildroot%_libexecdir/%name/config
rm -rf %buildroot%ruby_sitelibdir
rm -rf %buildroot%_libexecdir/%name/lib
rm -rf %buildroot%_localstatedir/%name
cp -rf config %buildroot%_libexecdir/%name/config
cp -rf lib %buildroot%_libexecdir/%name/
mkdir -p %buildroot%webserver_datadir \
         %buildroot%_sbindir \
         %buildroot/run/%name \
         %buildroot%_spooldir/%name/tmp \
         %buildroot%_cachedir/%name/_ \
         %buildroot%_localstatedir/%name \
         %buildroot%_cachedir/%name/openid-store \
         %buildroot%_sysconfdir/%name/plugins

# Create VERSION file
install -pm0644 VERSION %buildroot%_libexecdir/%name/VERSION
# cp -r node_modules/.bin %buildroot%_libexecdir/%name/node_modules/

install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/%name/database.yml
install -Dm0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -Dm0644 %SOURCE3 %buildroot%_logrotatedir/%name
install -Dm0644 %SOURCE4 %buildroot%_sysconfdir/cron.d/%name
install -Dm0644 %SOURCE5 %buildroot%_tmpfilesdir/%name.conf
install -Dm0755 %SOURCE6 %buildroot%_unitdir/%name.service
install -Dm0644 %SOURCE7 %buildroot%_sysconfdir/%name/settings.yml
install -Dm0640 /dev/null %buildroot%_sysconfdir/%name/encryption_key.rb
install -Dm0640 /dev/null %buildroot%_sysconfdir/%name/local_secret_token.rb
install -Dm0644 %SOURCE11 %buildroot%_unitdir/%{name}-jobs.service
install -Dm0644 %SOURCE12 %buildroot%_sysconfdir/sysconfig/%{name}-jobs

mv %buildroot%_libexecdir/%name/public %buildroot%webserver_datadir/%name
ln -svr %buildroot%webserver_datadir/%name %buildroot%_libexecdir/%name/public
ln -svr %buildroot%_sysconfdir/%name/plugins %buildroot%_libexecdir/%name/config/settings.plugins.d
ln -svr %buildroot%_sysconfdir/%name/settings.yml %buildroot%_libexecdir/%name/config/settings.yaml
ln -svr %buildroot%_sysconfdir/%name/database.yml %buildroot%_libexecdir/%name/config/database.yml
ln -svr %buildroot%_sysconfdir/%name/encryption_key.rb %buildroot%_libexecdir/%name/config/initializers/encryption_key.rb
ln -svr %buildroot%_sysconfdir/%name/local_secret_token.rb %buildroot%_libexecdir/%name/config/initializers/local_secret_token.rb
#ln -svr %buildroot%_spooldir/%name/tmp %buildroot%_libexecdir/%name/tmp
#ln -svr %buildroot%_cachedir/%name/_ %buildroot%_spooldir/%name/tmp/cache
ln -svr %buildroot%_cachedir/%name/openid-store %buildroot%_libexecdir/%name/db/openid-store
ln -svr %buildroot%_libexecdir/%name/script/foreman-rake %buildroot%_sbindir/foreman-rake
install -d %buildroot%_logdir/%name

%check
%ruby_test

%pre
# Add the "foreman" user and group
getent group foreman >/dev/null || %_sbindir/groupadd -r foreman
getent passwd _foreman >/dev/null || \
   %_sbindir/useradd -r -g foreman -G foreman -M -d %_localstatedir/%name -s /bin/bash -c "Foreman" _foreman
getent group puppet >/dev/null || \
   %_sbindir/usermod -a -G puppet _foreman
rm -rf %_libexecdir/%name/db/openid-store
exit 0

%post
%post_service foreman
%post_service foreman-jobs

%preun
railsctl cleanup %name
%preun_service foreman
%preun_service foreman-jobs

%files
%doc README* CONTRIBUTING.md LICENSE
#%_sbindir/*
%_sbindir/%name-rake
%_libexecdir/%name
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/sysconfig/%name-jobs
%config(noreplace) %_sysconfdir/%name/plugins
%config(noreplace) %_sysconfdir/%name/settings.yml
%config(noreplace) %_sysconfdir/%name/database.yml
%attr(640,_foreman,foreman) %config(noreplace) %_sysconfdir/%name/encryption_key.rb
%attr(640,_foreman,foreman) %config(noreplace) %_sysconfdir/%name/local_secret_token.rb
%attr(770,_foreman,foreman) %_sysconfdir/cron.d/%name
%_tmpfilesdir/%name.conf
%_unitdir/*
%attr(770,_foreman,foreman) %webserver_datadir/%name
%attr(770,_foreman,foreman) %_spooldir/%name/tmp
%dir %attr(770,_foreman,foreman) %_cachedir/%name/openid-store
%dir %attr(770,_foreman,foreman) %_cachedir/%name/_
%dir %attr(770,_foreman,foreman) /run/%name
%dir %attr(770,_foreman,foreman) %_logdir/%name
%dir %attr(770,_foreman,foreman) %_localstatedir/%name
%dir %attr(770,_foreman,foreman) %_spooldir/%name
# %_man8dir/*.8*
#%attr(770,_foreman,foreman) %_cachedir/%name/bootsnap


#%files         -n gem-font-awesome-sass
#%doc README.md
#%ruby_gemspecdir/font-awesome-sass-4.7.0.gemspec
#%ruby_gemslibdir/font-awesome-sass-4.7.0
#
#%files         -n gem-font-awesome-sass-doc
#%doc README.md
#%ruby_gemsdocdir/font-awesome-sass-4.7.0
#
%files         -n foreman-doc
%ruby_sitedocdir/*

%files         -n foreman-devel


%changelog
* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt0.2
- ! require deps
- ! sitedocdir folder

* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt0.1
- ^ 1.24.3.2 -> 2.5.0(pre)

* Mon Jun 28 2021 Pavel Vasenkov <pav@altlinux.org> 1.24.3.2-alt5
- fixes #39935,#39936,#39937,#39938,#39939
- + set pyton3 declaration and correct python3 executable in shebang
- ! add record to end of scss order

* Sun Feb 14 2021 Pavel Skrylev <majioa@altlinux.org> 1.24.3.2-alt4
- ! spec folders to include
- ! default database config
- + foreman-jobs sysconfig and service

* Fri Jan 22 2021 Pavel Skrylev <majioa@altlinux.org> 1.24.3.2-alt3
- + deps to 4 module gems
- * right for some folders
- + _dynflow user to foreman group
- + foreman config

* Thu Dec 17 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.3.2-alt2
- ! to add modules

* Tue Dec 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.3.2-alt1
- ^ 1.24.3[1] -> 1.24.3[2]
- * updated embedded node packages
- ! path to images for some views
- ! scss files to conform new sprockets and sassc

* Thu Dec 03 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.3.1-alt1
- ^ 1.24.2 -> 1.24.3[1]

* Fri Jul 17 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt6.3
- > post services for foreman
- * moving user _foreman's home to /var/lib/foreman

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt6.2
- ! spec dep replace for net-ssh gem to 6.x
- ! spec post script
- + external manifest.js

* Wed Jun 10 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt6.1
- ! gems dep for sprockets to 4.0, and sass-rails to 6.0

* Fri May 19 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt6
- * tmpfiles.d file

* Fri May 15 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt5
- ! patches and requires

* Fri May 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt4
- + explicit require deps to gem-secure-headers
- - post call to railsctl on install
- ! service name call to railsctl in .service

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt3
- - post exec in spec
- * with service run using 'railsctl'
- ! gem rails deps to ~> 5.2

* Mon Mar 30 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt2
- * moving code from %%_libdir -> %%_libexecdir

* Mon Mar 02 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt1
- updated (^) 1.22.2 -> 1.24.2
- updated (^) node modules
- fixed (!) systemd service file, and spec deps

* Wed Feb 26 2020 Pavel Skrylev <majioa@altlinux.org> 1.22.2-alt1
- updated (^) 1.22.0 -> 1.22.2
- added (+) post script condition to initialize the foreman after the db is
  initialized and started
- fixed (!) rails db/migration
- fixed (!) post-install code

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1.22.0-alt3
- drop libnss-devel buildreq
- update node_modules with node.js >= 13

* Mon Nov 25 2019 Pavel Skrylev <majioa@altlinux.org> 1.22.0-alt2
- changed (*) license
- fixed (!) requires and required service
- added (+) vcs tag to spec
- fixed (!) post install procedure, running the postgres server to setup users
  and db

* Thu Sep 26 2019 Pavel Skrylev <majioa@altlinux.org> 1.22.0-alt1
- updated (^) 1.20.1 -> 1.22.0
- fixed (!) run and primarily work, js is bundled in

* Mon Jan 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.20.1-alt1
- Bump to 1.20.1.

* Thu Sep 27 2018 Pavel Skrylev <majioa@altlinux.org> 1.19.0-alt5
- Patch to support 5.2 rails from master.
- Rake tasks moved to named subfolder.
- Avoid aarch64

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.19.0-alt2
- Bumped to 1.19 with Gemfile fix.
- Enable auto req detection.

* Fri Sep 21 2018 Andrey Cherepanov <cas@altlinux.org> 1.19.0-alt1
- New version.

* Sun Jul 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.18.0-alt1
- New version.

* Fri May 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.17.1-alt1
- New version.

* Thu Apr 12 2018 Andrey Cherepanov <cas@altlinux.org> 1.17.0-alt1
- Initial build in Sisyphus
