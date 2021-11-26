%define soname 7

Name: primecount
Version: 7.1
Release: alt1
Summary: Count the number of primes
License: BSD-2-Clause
Group: Sciences/Mathematics
Url: https://github.com/kimwalisch/primecount

Source: https://github.com/kimwalisch/primecount/archive/v%version.tar.gz#/%name-%version.tar.gz

BuildPreReq: rpm-build-ninja ctest
BuildRequires: gcc-c++ cmake asciidoc-a2x libprimesieve-devel

%description
primecount is a command-line program that counts the primes below an
integer x less than or equal to 10^31 using highly optimized implementations of the
combinatorial prime counting algorithms.

%package -n lib%name%soname
Summary: C/C++ library for counting prime numbers
Group: System/Libraries

%description -n lib%name%soname
This package contains the shared runtime library for primecount.

%package -n lib%name-devel
Summary: Development files for the primecount library
Group: Development/Other

%description -n lib%name-devel
This package contains the C/C++ header files and the configuration
files for developing applications that use the primecount library.

%prep
%setup

%build
%cmake \
    -GNinja \
    -DBUILD_LIBPRIMESIEVE=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_STATIC_LIBS=OFF \
    -DBUILD_MANPAGE=ON \
    -DBUILD_TESTS=ON \
    -DCMAKE_SKIP_RPATH:BOOL=OFF
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%check
cd %_cmake__builddir
ctest

%files
%doc README.md ChangeLog
%_bindir/primecount
%_man1dir/primecount.1*

%files -n lib%name%soname
%doc COPYING
%_libdir/libprimecount.so.%{soname}*

%files -n lib%name-devel
%doc doc/libprimecount.md
%_libdir/libprimecount.so
%_includedir/primecount.h
%_includedir/primecount.hpp

%changelog
* Fri Nov 26 2021 Leontiy Volodin <lvol@altlinux.org> 7.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for sagemath.
