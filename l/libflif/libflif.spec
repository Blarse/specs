Name: libflif
Version: 0.4
Release: alt1

Summary: Free Lossless Image Format

License: LGPLv3+ and Apache-2.0
Group: Development/C
Url: http://flif.info/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/FLIF-hub/FLIF/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: libpng-devel

%description
FLIF is a lossless image format based on MANIAC compression.
MANIAC (Meta-Adaptive Near-zero Integer Arithmetic Coding)
is a variant of CABAC (context-adaptive binary arithmetic coding),
where the contexts are nodes of decision trees
which are dynamically learned at encode time.

FLIF outperforms PNG, FFV1, lossless WebP,
lossless BPG and lossless JPEG2000 in terms of compression ratio.

Moreover, FLIF supports a form of progressive interlacing
(essentially a generalization/improvement of PNG's Adam7)
which means that any prefix (e.g. partial download)
of a compressed file can be used as a reasonable
lossy encoding of the entire image.

%package -n flif
Summary: CLI to the FLIF compression
License: LGPLv3+ and Apache-2.0
Group: File tools

%description -n flif
FLIF is a lossless image format based on MANIAC compression.
MANIAC (Meta-Adaptive Near-zero Integer Arithmetic Coding)
is a variant of CABAC (context-adaptive binary arithmetic coding),
where the contexts are nodes of decision trees
which are dynamically learned at encode time.

%package -n libflifdec
Summary: Library implementing the FLIF decompressor
License: Apache-2.0
Group: System/Libraries

%description -n libflifdec
FLIF is a lossless image format based on MANIAC compression.
MANIAC (Meta-Adaptive Near-zero Integer Arithmetic Coding)
is a variant of CABAC (context-adaptive binary arithmetic coding),
where the contexts are nodes of decision trees
which are dynamically learned at encode time.

%package devel
Summary: Development files for %name
License: LGPLv3+ and Apache-2.0
Group: Development/C++
Requires: %name = %version-%release

%description devel
Development files for the %name library.

%prep
%setup
sed -i "s|/usr/local|%_prefix|g" src/Makefile
sed -i "s|/lib\([/ ]\)|/%_lib\1|g" src/Makefile
sed -i "s|/lib$|/%_lib|g" src/Makefile
%ifarch %e2k
# lcc 1.23 does that differently
sed -i "s|-fwhole-program||" src/Makefile
%endif

%build
cd src
%make_build
%make_build decoder

%install
cd src
%makeinstall_std install-decoder install-dev
rm -f %buildroot%_libdir/libflif.so %buildroot%_libdir/libflif_dec.so
ln -s libflif.so.0 %buildroot%_libdir/libflif.so
ln -s libflif_dec.so.0 %buildroot%_libdir/libflif_dec.so

%check
#LD_LIBRARY_PATH=$(pwd)
cd src
#make test

%files -n flif
%_bindir/flif
%_bindir/dflif
%_bindir/apng2flif
%_bindir/gif2flif
%_man1dir/flif*

%files
%_libdir/libflif.so.0

%files devel
%_includedir/*
%_libdir/libflif.so
%_libdir/libflif_dec.so

%files -n libflifdec
%_libdir/libflif_dec.so.0

%changelog
* Thu Mar 28 2024 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- new version 0.4 (fixes: CVE-2017-14232, CVE-2018-10971,
  CVE-2018-11507, CVE-2018-12109, CVE-2018-14876, CVE-2019-14373)

* Sat Mar 21 2020 Michael Shigorin <mike@altlinux.org> 0.3-alt3
- E2K: avoid lcc-unsuported option
- minor spec cleanup

* Tue Jul 30 2019 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt2
- fix package description

* Mon May 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- initial build for ALT Sisyphus
