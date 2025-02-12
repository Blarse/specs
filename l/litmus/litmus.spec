# SPEC file for litmus package

Name:    litmus
Version: 0.15.0
Release: alt1

Summary: a WebDAV server test suite
Summary(ru_RU.UTF-8): утилита тестирования серверов WebDAV

License: %gpl2plus
Group:   Networking/File transfer
URL:     https://notroj.github.io/litmus/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

# Sone code is missid in the Github repository, but referenced in the Makefile...
Source1: missed-on-github.tar

Patch1:  %name-0.14-alt-neon_0.31.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Jun 02 2024
# optimized out: libgpg-error perl pkg-config python-modules python2-base python3 python3-base python3-dev sh5
BuildRequires: libneon-devel perl-parent

%description
litmus is a WebDAV server test suite, which aims to test whether
a server is compliant with the  WebDAV protocol  as specified in
RFC2518.

Current tests covers  OPTIONS, PUT, GET, MKCOL, DELETE, COPY and
MOVE methods, property manipulation and querying, locking.

Note that a server which passes all these tests will not
necessarily work with any real DAV clients; though the chances
are good. litmus is built using the neon library, so supports
digest and basic authentication, TLS/SSL, and proxy servers.


%prep
%setup
%patch0 -p1

tar -x --strip-components=1 -f %SOURCE1

#%%patch1

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%autoreconf
./autogen.sh
%configure --with-ssl=openssl --with-neon \
	--enable-warnings \
	--with-ca-bundle=%_datadir/ca-certificates/ca-bundle.crt \
	--with-expat
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name
mv -- ChangeLog.CVS ChangeLog

%files  -f %name.lang
%doc FAQ README.md THANKS TODO NEWS
%doc --no-dereference COPYING

%_bindir/%name
%_libexecdir/%{name}*

%changelog
* Sun Jun 02 2024 Nikolay A. Fetisov <naf@altlinux.org> 0.15.0-alt1
- New version

* Wed Dec 07 2022 Nikolay A. Fetisov <naf@altlinux.org> 0.14.0-alt2.git.9fbc73d
- Restore from orphaned
- Rebuild with libneon 0.32

* Wed Jun 16 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.14.0-alt1.git.9fbc73d
- New version

* Sun Nov 24 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.13-alt2
- Rebuild with libneon 0.30

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.13-alt1
- New version

* Sun Mar 20 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.12.1-alt3
- Rebuild with libneon-0.29.5-alt1

* Mon Nov 23 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.12.1-alt2
- Rebuild with libneon-0.29.0-alt1

* Tue Jul 14 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.12.1-alt1
- Initial build for ALT Linux Sisyphus
