Name: coz
Version: 0.2.2
Release: alt4

Packager: %packager

Summary: Coz: Finding Code that Counts with Causal Profiling
License: GPL
Group: Development/C
URL: https://github.com/plasma-umass/coz

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libelfin-devel python3-module-docutils

%description
Coz is a new kind of profiler that unlocks optimization opportunities
missed by traditional profilers. Coz employs a novel technique we call
causal profiling that measures optimization potential. This measurement
matches developers' assumptions about profilers: that optimizing highly-ranked
code will have the greatest impact on performance.

%prep
%setup
%ifarch %e2k
# unsupported as of lcc 1.25.23
sed -i '/-gdwarf-3/d' CMakeLists.txt libcoz/Makefile
%endif

%build
%ifarch %e2k
export CFLAGS="-I`pwd`/include %optflags -fPIC -Wl,--no-warn-shared-textrel"
%endif
%make prefix=%_exec_prefix bindir=%_bindir MANPREFIX=%_mandir

%install
%define docdir %_docdir/%name-%version

%makeinstall LIBDIR=%buildroot%_libdir prefix=%buildroot%_exec_prefix MANPREFIX=%_mandir pkglibdir=%buildroot%_libdir/coz-profiler

mkdir -p %buildroot%docdir
install -pm644 README.md %buildroot%docdir/
install -pm644 LICENSE.md %buildroot%docdir/
cp -R common.mk %buildroot%docdir/
cp -R benchmarks %buildroot%docdir/

%find_lang %name

%files
%_bindir/*
%_includedir/*
%_libdir/coz-profiler/*
%_man1dir/*

%dir %docdir
%docdir/*

%changelog
* Sat Oct 29 2022 Michael Shigorin <mike@altlinux.org> 0.2.2-alt4
- E2K: fix ftbfs with lcc

* Mon Jul 04 2022 Andrey Bergman <vkni@altlinux.org> 0.2.2-alt3
- Slightly update from upstream, update buildreq.

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt2
- NMU: drop unused BR

* Sat Oct 17 2020 Andrey Bergman <vkni@altlinux.org> 0.2.2-alt1
- Initial release for Sisyphus.
