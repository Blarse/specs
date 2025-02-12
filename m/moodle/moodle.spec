%define php_version 8.2
%def_without pam

Name: moodle
Version: 4.3.5
Release: alt1

Summary: The world's open source learning platform
License: GPLv3
Group: Networking/WWW

Url: http://moodle.org/
Packager: Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch

BuildRequires(pre): rpm-macros-moodle
BuildRequires(pre): rpm-macros-apache2
BuildRequires(pre): perl-HTML-Parser
BuildRequires: fonts-ttf-freefont
BuildRequires: unzip

# Source-url: https://github.com/moodle/moodle/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: distrolib.php
Source2: %name.cron
Source3: %name.ini
Source10: %moodle_name.httpd.conf
Source20: %moodle_name.httpd2.conf
Source21: %moodle_name.start.extra.conf
Source22: %moodle_name.start.mods.conf
Source23: %moodle_name.httpd2.inc.conf

# Language files
# Download by elinks https://download.moodle.org/download.php/langpack/3.7/ru.zip for example
Source30: langpack.tar

%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%moodle_dir/filter/algebra/'

Requires: %name-base = %version-%release
%if_with pam
Requires: %name-auth-pam = %version-%release
%endif

AutoReq: yes,nonodejs

%description
Moodle is a learning platform designed to provide
educators, administrators and learners with a single robust, secure and
integrated system to create personalised learning environments.

Moodle is widely used around the world by universities, schools, companies and
all manner of organisations and individuals.

Moodle is provided freely as open source software, under the GNU General Public
License <https://docs.moodle.org/dev/License>.

Moodle is written in PHP and JavaScript and uses an SQL database for storing
the data.

See <https://docs.moodle.org> for details of Moodle's many features.

%package base
Summary: Base part for Moodle CMS
Group: Networking/WWW

Requires(pre): webserver-common
Requires(pre): %_sbindir/web-condstop-rpm
Requires(pre): %_sbindir/web-condstart-rpm
Requires: %webserver_webappsdir
Requires: texlive-base-bin ImageMagick
Requires: iconv
Requires: php-engine
Requires: php%php_version-curl
Requires: php%php_version-dom
Requires: php%php_version-exif
Requires: php%php_version-fileinfo
Requires: php%php_version-fpm-fcgi
Requires: php%php_version-gd2
Requires: php%php_version-intl
Requires: php%php_version-ldap
Requires: php%php_version-mbstring
Requires: php%php_version-opcache
Requires: php%php_version-openssl
Requires: php%php_version-soap
Requires: php%php_version-sodium
Requires: php%php_version-xmlreader
Requires: php%php_version-zip
Provides: %moodle_dir
Provides: %moodle_admindir
Provides: %moodle_authdir
Provides: %moodle_blocksdir
Provides: %moodle_calendardir
Provides: %moodle_coursedir
Provides: %moodle_docdir
Provides: %moodle_enroldir
Provides: %moodle_filesdir
Provides: %moodle_filterdir
Provides: %moodle_langdir
Provides: %moodle_libdir
Provides: %moodle_logindir
Provides: %moodle_moddir
Provides: %moodle_pixdir
Provides: %moodle_questiondir
Provides: %moodle_questionformatdir
Provides: %moodle_themedir
Provides: %moodle_datadir
Provides: %name-lang-en = %EVR

%description base
%summary

Part of the standard components of Moodle, is not included
in this package is moved to subpackages.

%package apache2
Summary: apache2-related config for Moodle CMS
Group: Networking/WWW

Requires: apache2-base > 2.2.17-alt2
Requires: %apache2_extra_available
Requires: %apache2_extra_enabled
Requires: %apache2_extra_start
Requires: %apache2_mods_start
Requires: %apache2_confdir_inc
Requires: %name-base = %version-%release
Requires: %moodle_dir
Requires: %moodle_datadir
Requires: apache2-mod_php%php_version
Provides: %moodle_name-apache2 = %version-%release

%description apache2
%summary

%package local-mysql
Summary: installed mysql-server on localhost for Moodle
Group: Networking/WWW

Requires: %name-base = %version-%release
Requires: /usr/sbin/mysqld
Requires: php%php_version-mysqli
Provides: %moodle_name-local-mysql = %version-%release

%description local-mysql
%summary

%if_with pam
%package auth-pam
Summary: PAM authentication for Moodle
Group: Networking/WWW

Requires: pecl-pam
Requires: %name-base = %version-%release
Requires: %moodle_authdir

%description auth-pam
PAM (Pluggable Authentication Modules) authentication methods for Moodle
%endif

%prep
%setup

rm -f filter/tex/*mimetex*
rm -f lib/default.ttf

%build

%install
# install moodle
mkdir -p %buildroot%moodle_dir/
mkdir -p %buildroot%moodle_datadir/
cp -rp * %buildroot%moodle_dir/

# create empty config.php (for ghost packing)
touch %buildroot%moodle_dir/config.php

%define mimetexlinux_filter %moodle_filterdir/tex/mimetex.linux
ln -srf %buildroot%webserver_cgibindir/mimetex.cgi %buildroot%mimetexlinux_filter

%define default_ttf %moodle_libdir/default.ttf
ln -srf %buildroot%_datadir/fonts/ttf/freefont/FreeSans.ttf %buildroot%default_ttf

# install distrolib.php
install -pD -m0644 %SOURCE1 %buildroot%moodle_dir/install/distrolib.php

# TODO: install apache config
# install -pD -m0644 %SOURCE10 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/%name.conf

# install apache2 config
install -pD -m0644 %SOURCE20 %buildroot%apache2_extra_available/%name.conf
install -pD -m0644 %SOURCE21 %buildroot%apache2_extra_start/100-%name.conf
install -pD -m0644 %SOURCE22 %buildroot%apache2_mods_start/100-%name.conf
install -pD -m0644 %SOURCE23 %buildroot%apache2_confdir_inc/Directory_%{moodle_name}_default.conf

mkdir -p %buildroot%apache2_extra_enabled/
touch %buildroot%apache2_extra_enabled/%name.conf

#Disclosure of the macros
find %buildroot%moodle_dir/install/distrolib.php %buildroot%_sysconfdir -type f -print0 \
	| xargs -r0 sed -ri "
s@%%(\{name\}|name([[:space:]/'\"=]))@%name\2@g
s@%%(\{webserver_datadir\}|webserver_datadir([[:space:]/'\"=]))@%webserver_datadir\2@g
s@%%(\{moodle_name\}|moodle_name([[:space:]/'\"=]))@%moodle_name\2@g
s@%%(\{moodle_dir\}|moodle_dir([[:space:]/'\"=]))@%moodle_dir\2@g
s@%%(\{moodle_datadir\}|moodle_datadir([[:space:]/'\"=]))@%moodle_datadir\2@g
"

# Install language files
mkdir -p %buildroot%moodle_langdir
tar xvf %SOURCE30 -C %buildroot%moodle_langdir
cd %buildroot%moodle_langdir
for ar in *.zip;do unzip "$ar" >/dev/null && rm -f "$ar";done

# Install cron scripts
install -Dpm0644 %SOURCE2 %buildroot%_sysconfdir/cron.d/%name

# Install PHP configuration for Moodle
install -Dpm0644 %SOURCE3 %buildroot%_sysconfdir/%php_version/apache2-mod_php/php.d/moodle.ini

%post apache2
# Disable mod_php7 if it is enabled
/usr/sbin/apachectl2 -M | grep -q php7_module && ( a2dismod mod_php7 &>/dev/null; %_initdir/httpd2 condreload ) ||:

%files

%files base
%dir %attr(2775,root,%webserver_group) %moodle_dir/
%ghost %config(noreplace) %moodle_dir/config.php
%config(noreplace) %moodle_dir/install/distrolib.php
%config(noreplace) %_sysconfdir/cron.d/%name
%moodle_dir/*
%if_with pam
%exclude %moodle_authdir/pam/
%endif
%dir %attr(2770,root,%webserver_group) %moodle_datadir
%dir %attr(775,root,%webserver_group) %moodle_moddir
%dir %attr(775,root,%webserver_group) %moodle_themedir
%dir %attr(775,root,%webserver_group) %moodle_enroldir

%files apache2
%config(noreplace) %apache2_extra_available/%name.conf
%ghost %apache2_extra_enabled/%name.conf
%config(noreplace) %apache2_confdir_inc/Directory_%{moodle_name}_default.conf
%config(noreplace) %apache2_extra_start/100-%name.conf
%config(noreplace) %apache2_mods_start/100-%name.conf
%config(noreplace) %_sysconfdir/%php_version/apache2-mod_php/php.d/moodle.ini

%files local-mysql

%if_with pam
%files auth-pam
%moodle_authdir/pam/
%endif

%changelog
* Sat Jun 08 2024 Andrey Cherepanov <cas@altlinux.org> 4.3.5-alt1
- New version.
- Security fixes: CVE-2023-6661, CVE-2023-6662, CVE-2023-6663, CVE-2023-6664,
  CVE-2023-6665, CVE-2023-6666, CVE-2023-6667, CVE-2023-6668, CVE-2023-6669,
  CVE-2023-6670, CVE-2024-25978, CVE-2024-25979, CVE-2024-25980,
  CVE-2024-25981, CVE-2024-25982, CVE-2024-25983, CVE-2024-33996,
  CVE-2024-33997, CVE-2024-33998, CVE-2024-33999, CVE-2024-34000,
  CVE-2024-34001, CVE-2024-34002, CVE-2024-34003, CVE-2024-34004,
  CVE-2024-34005, CVE-2024-34006, CVE-2024-34007, CVE-2024-34008,
  CVE-2024-34009

* Wed Oct 11 2023 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.
- Use PHP 8.2.
- Security fixes: CVE-2023-40316, CVE-2023-40317, CVE-2023-40318,
  CVE-2023-40319, CVE-2023-40320, CVE-2022-39369, CVE-2023-40322,
  CVE-2023-40323, CVE-2023-40324, CVE-2023-40325
- Requires exif PHP module.
- Set PHP parameter max_input_vars=5000.

* Fri Jul 21 2023 Andrey Cherepanov <cas@altlinux.org> 3.11.15-alt3
- Require PHP module fpm-fcgi.
- Fix write permission for mod, theme and enroll directories.

* Thu Jul 13 2023 Andrey Cherepanov <cas@altlinux.org> 3.11.15-alt2
- Return vendor subdirectories.

* Fri Jun 16 2023 Andrey Cherepanov <cas@altlinux.org> 3.11.15-alt1
- New version.
- Security fixes: CVE-2023-30944, CVE-2023-1402, CVE-2023-28336,
  CVE-2023-28333, CVE-2023-28332, CVE-2023-28331, CVE-2023-28330,
  CVE-2023-28329, CVE-2023-23923, CVE-2023-23921, CVE-2022-45152,
  CVE-2022-45151, CVE-2022-45150, CVE-2022-45149, CVE-2021-23414,
  CVE-2022-40208, CVE-2022-40316, CVE-2022-40315, CVE-2022-40314,
  CVE-2022-40313, CVE-2022-2986, CVE-2022-0323

* Thu Sep 01 2022 Andrey Cherepanov <cas@altlinux.org> 3.11.8-alt2
- Disable mod_php7 if it is enabled.

* Tue Aug 23 2022 Andrey Cherepanov <cas@altlinux.org> 3.11.8-alt1
- New version.
- Use PHP 8.0.

* Sun Mar 13 2022 Andrey Cherepanov <cas@altlinux.org> 3.11.6-alt1
- New version.

* Mon Jan 17 2022 Andrey Cherepanov <cas@altlinux.org> 3.11.5-alt2
- Remove vendor subdirectories.
- Add cron rule.

* Sat Jan 15 2022 Andrey Cherepanov <cas@altlinux.org> 3.11.5-alt1
- New version.

* Wed Nov 10 2021 Andrey Cherepanov <cas@altlinux.org> 3.11.4-alt1
- New version.

* Mon Sep 13 2021 Andrey Cherepanov <cas@altlinux.org> 3.11.3-alt1
- New version.

* Fri Aug 06 2021 Andrey Cherepanov <cas@altlinux.org> 3.11.2-alt3
- Requires recommended php7-sodium.

* Fri Aug 06 2021 Andrey Cherepanov <cas@altlinux.org> 3.11.2-alt2
- Remove requirements of deprecated helper scripts.

* Thu Jul 29 2021 Andrey Cherepanov <cas@altlinux.org> 3.11.2-alt1
- New version.

* Sun Jul 11 2021 Andrey Cherepanov <cas@altlinux.org> 3.11.1-alt1
- New version.

* Sat May 22 2021 Andrey Cherepanov <cas@altlinux.org> 3.11.0-alt1
- New version.

* Sun May 09 2021 Andrey Cherepanov <cas@altlinux.org> 3.10.4-alt1
- New version.

* Thu Mar 25 2021 Andrey Cherepanov <cas@altlinux.org> 3.10.3-alt1
- New version.

* Mon Mar 08 2021 Andrey Cherepanov <cas@altlinux.org> 3.10.2-alt1
- New version.

* Sun Jan 17 2021 Andrey Cherepanov <cas@altlinux.org> 3.10.1-alt1
- New version.

* Sat Nov 07 2020 Andrey Cherepanov <cas@altlinux.org> 3.10.0-alt1
- New version.

* Thu Oct 15 2020 Andrey Cherepanov <cas@altlinux.org> 3.9.2-alt1
- New version.

* Sun Jun 14 2020 Andrey Cherepanov <cas@altlinux.org> 3.9.0-alt1
- New version.

* Sun May 10 2020 Andrey Cherepanov <cas@altlinux.org> 3.8.3-alt1
- New version.

* Tue Mar 10 2020 Andrey Cherepanov <cas@altlinux.org> 3.8.2-alt1
- New version.

* Fri Jan 10 2020 Andrey Cherepanov <cas@altlinux.org> 3.8.1-alt1
- New version.

* Sun Nov 17 2019 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Sat Nov 09 2019 Andrey Cherepanov <cas@altlinux.org> 3.7.3-alt1
- New version.

* Tue Oct 08 2019 Andrey Cherepanov <cas@altlinux.org> 3.7.2-alt2
- Add Russian localization to main package.

* Sat Sep 07 2019 Andrey Cherepanov <cas@altlinux.org> 3.7.2-alt1
- New version.

* Fri Jul 12 2019 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1
- New version.

* Tue Jun 18 2019 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version.

* Thu Apr 25 2019 Andrey Cherepanov <cas@altlinux.org> 3.6.3-alt1
- Rename to moodle and build new version.
- Use PHP7.

* Mon Jul 16 2018 Oleg Solovyov <mcpain@altlinux.org> 3.3.3-alt2
- fix config for new Apache (Closes: #34984)

* Mon Nov 13 2017 Konstantin Kondratyuk <kondratyuk@altlinux.org> 3.3.3-alt1
- new version 3.3.3 (with rpmrb script)

* Sun Oct 22 2017 Konstantin Kondratyuk <kondratyuk@altlinux.org> 3.3.2-alt1
- new version (3.3.2) with rpmgs script

* Thu Aug 10 2017 Konstantin Kondratyuk <kondratyuk@altlinux.org> 3.3.1-alt1
- new version (3.3.1) with rpmgs script

* Thu Jul 13 2017 Konstantin Kondratyuk <kondratyuk@altlinux.org> 3.3.0-alt3
*- increase limits in httpd2 config

* Tue Jun 27 2017 Konstantin Kondratyuk <kondratyuk@altlinux.org> 3.3.0-alt2
- fix apache config

* Thu Jun 15 2017 Konstantin Kondratyuk <kondratyuk@altlinux.org> 3.3.0-alt1
- new version (3.3.0) with rpmgs script
