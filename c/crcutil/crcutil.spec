Name: crcutil
Version: 1.0
Release: alt1.2

Summary: Fast CRC library
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/cloudera/crcutil
Vcs: https://github.com/cloudera/crcutil.git

Source: %name-%version.tar
Source1: lib%name.pc.in
Patch3500: crcutil-1.0-alt-nonx86.patch

BuildRequires: gcc-c++

%description
%summary.

%package -n lib%name
Group: System/Libraries
Summary: %name library
Requires: %name = %EVR

%description -n lib%name
Shared library for %name.

%package -n lib%name-devel
Group: System/Libraries
Summary: %name development files
Requires: lib%name = %EVR

%description -n lib%name-devel
Development files for %name.

%prep
%setup
%patch3500 -p1
%ifarch %e2k
sed -i "s/-DCRCUTIL_USE_MM_CRC32=1/-DHAVE_AARCH64/;s/-mcrc32/-mno-sse4.2/" autogen.sh
%endif

%build
./autogen.sh
./configure --prefix=%_prefix --libdir=%_libdir
%make_build

%install
%makeinstall_std INSTALLDIR="%buildroot%prefix"
rm -f %buildroot%_libdir/*.a
sed -e 's|@VERSION@|%version|g' -e 's|@LIBDIR@|%_libdir|g' -e 's|@INCLUDEDIR@|%_includedir/%name|' %SOURCE1 > lib%name.pc
install -d -m755 %buildroot%_pkgconfigdir
install -m644 lib%name.pc %buildroot%_pkgconfigdir

%check
./usage

%files
%doc AUTHORS ChangeLog COPYING NEWS README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%changelog
* Sat Feb 10 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.0-alt1.2
- NMU: fixed FTBFS on armv7 and LoongArch (and possibly riscv).

* Fri Jul 29 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.0-alt1.1
- Fixed build for Elbrus.

* Sat Dec 18 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt1
- Initial build for ALT.
