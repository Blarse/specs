%define		php_extension	apcu
%define 	real_name	APCu

Name:	 	php%_php_suffix-%php_extension
Version:	5.1.20
Epoch:		1
Release:	%php_release.%php_version

Summary:	PHP extension APCu - APC User Cache

License:	PHP-3.01
Group:		System/Servers
URL:		http://pecl.php.net/package/APCu
#URL:		https://github.com/krakjoe/apcu

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	php-%php_extension-%version.tar
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh


BuildRequires(pre): rpm-build-php8.0-version
# Automatically added by buildreq on Tue Jun 13 2017
# optimized out: gnu-config perl php7-libs python-base python-modules python3 python3-base
BuildRequires: glibc-devel-static

BuildRequires: php-devel = %php_version
BuildRequires: php%_php_suffix = %php_version

%description
PHP extension APCu is an APC stripped of opcode caching in
preparation for the deployment of Zend Optimizer+ as the
primary solution to opcode caching in future versions of PHP.

APCu only supports userland caching (and dumping) of variables,
providing an upgrade path for the APC users. The tried and 
tested APC codebase provides far superior support for local
storage of PHP variables.

%prep
%setup -c

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
	--with-%php_extension \
	--with-libdir=%_lib \
	--enable-apc \
	--enable-apc-mmap \
	#

%php_make

%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%check
NO_INTERACTION=1 make test

%files
%doc README.md TECHNOTES.txt NOTICE LICENSE

%php_extconf/%php_extension
%php_extdir/*

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} 1:%version-%release
- Rebuild with php-devel = %php_version-%php_release

* Fri Jan 26 2018 Nikolay A. Fetisov <naf@altlinux.org> 7.1.12-alt1.S1
- New externsion version 5.1.9

* Tue Jun 13 2017 Nikolay A. Fetisov <naf@altlinux.org> 7.1.6-alt1.S1
- Initial build for ALT Linux Sisyphus
