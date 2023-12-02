%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libseccomp
Version: 2.5.5
Release: alt1
Summary: High level interface to the Linux Kernel's seccomp filter
License: LGPLv2.1+
Group: System/Libraries
Url: https://github.com/seccomp/libseccomp

Source: %name-%version.tar

BuildRequires: gperf
%{?!_without_check:%{?!_disable_check:
BuildRequires: /proc
}}

%description
The libseccomp library provides and easy to use, platform independent,
interface to the Linux Kernel's syscall filtering mechanism: seccomp.
The libseccomp API is designed to abstract away the underlying BPF based
syscall filter language and present a more conventional function-call
based filtering interface that should be familiar to, and easily adopted
by application developers.

%package devel
Summary: Development files of %name
Group: Development/C
Requires: %name = %EVR

%description devel
The libseccomp library provides and easy to use, platform independent,
interface to the Linux Kernel's syscall filtering mechanism: seccomp.
The libseccomp API is designed to abstract away the underlying BPF based
syscall filter language and present a more conventional function-call
based filtering interface that should be familiar to, and easily adopted
by application developers.

This package contains development files of %name.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure --disable-static
%make_build V=1

%install
%makeinstall_std V=1

# Relocate shared library from %_libdir/ to /%_lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
        t=$(readlink -v "$f")
        ln -rsnf %buildroot/%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

install -p tools/scmp_api_level     %buildroot%_bindir
install -p tools/scmp_app_inspector %buildroot%_bindir
install -p tools/scmp_arch_detect   %buildroot%_bindir
install -p tools/scmp_bpf_disasm    %buildroot%_bindir
install -p tools/scmp_bpf_sim       %buildroot%_bindir

%check
unset MAKEFLAGS
export  LIBSECCOMP_TSTCFG_JOBS=0 \
	LIBSECCOMP_TSTCFG_TYPE=live \
	LIBSECCOMP_TSTCFG_MODE_LIST=c
%make_build check V=1

%define _customdocdir %_docdir/%name

%files
/%_lib/lib*.so.*

%files devel
%doc CHANGELOG CREDITS *.md src/syscalls.csv
%_bindir/scmp_*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_man1dir/*
%_man3dir/*

%changelog
* Sat Dec 02 2023 Vitaly Chikunov <vt@altlinux.org> 2.5.5-alt1
- Update to v2.5.5 (2023-12-01).

* Mon Mar 27 2023 Vitaly Chikunov <vt@altlinux.org> 2.5.4-alt3
- spec: Move doc and developer tools into -devel package.

* Wed Feb 01 2023 Vitaly Chikunov <vt@altlinux.org> 2.5.4-alt2
- spec: Verbose build and add %%check section.

* Fri Jun 03 2022 Alexey Shabalin <shaba@altlinux.org> 2.5.4-alt1
- new version 2.5.4

* Sat Nov 06 2021 Alexey Shabalin <shaba@altlinux.org> 2.5.3-alt1
- new version 2.5.3

* Mon Oct 11 2021 Alexey Shabalin <shaba@altlinux.org> 2.5.2-alt1
- new version 2.5.2

* Tue Dec 08 2020 Alexey Shabalin <shaba@altlinux.org> 2.5.1-alt1
- new version 2.5.1

* Fri Aug 07 2020 Alexey Shabalin <shaba@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Fri May 08 2020 Alexey Shabalin <shaba@altlinux.org> 2.4.3-alt1
- new version 2.4.3

* Thu Jan 30 2020 Anton Farygin <rider@altlinux.ru> 2.4.2-alt2
- add upstream fix for chrony FTBFS

* Fri Dec 13 2019 Alexey Shabalin <shaba@altlinux.org> 2.4.2-alt1
- new version 2.4.2

* Wed Apr 24 2019 Alexey Shabalin <shaba@altlinux.org> 2.4.1-alt1
- 2.4.1

* Fri Mar 22 2019 Alexey Shabalin <shaba@altlinux.org> 2.4.0-alt1
- 2.4.0
- do not build python bindings
- Fixes for the following security vulnerabilities:
  + CVE-2019-9893 64-bit argument comparisons do not work correctly

* Tue Jan 22 2019 Alexey Shabalin <shaba@altlinux.org> 2.3.3-alt2
- Removed ubt macros.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Feb 13 2018 Alexey Shabalin <shaba@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Fri Dec 15 2017 Alexey Shabalin <shaba@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Tue Jun 14 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2.3-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Dec 17 2015 Alexey Shabalin <shaba@altlinux.ru> 2.2.3-alt1
- 2.2.3
- relocate shared libraries from %_libdir/ to /%_lib/.

* Thu Aug 27 2015 Afanasov Dmitry <ender@altlinux.org> 2.1.1-alt2.git20141021
- fix version in pkg-config file

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20141021
- Initial build for Sisyphus

