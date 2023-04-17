
# openblas does not build with LTO
%global optflags_lto %nil

%def_without lapack
%ifnarch %e2k
%def_enable dynamic_arch
%endif

%ifarch armh
%define oblas_target ARMV7
%endif
%ifarch aarch64
%define oblas_target ARMV8
%endif
%ifarch riscv64
%define oblas_target RISCV64_GENERIC
%endif
%ifarch %mips
%define oblas_target MIPS32_GENERIC
%endif


Name: openblas
Version: 0.3.19
Release: alt1.2

Summary: Optimized BLAS library based on GotoBLAS2 1.13 
License: BSD
Group: Sciences/Mathematics
Url: https://github.com/xianyi/OpenBLAS

# http://github.com/xianyi/OpenBLAS
Source: %name-%version.tar
Patch2000: %name-e2k.patch

BuildRequires: gcc-fortran
%ifarch ppc64le
BuildRequires: libgomp-devel
%endif

%description
GotoBLAS2 has been released by the Texas Advanced Computing Center as
open source software under the BSD license. This product is no longer
under active development by TACC, but it is being made available to the
community to use, study, and extend. GotoBLAS2 uses new algorithms and
memory techniques for optimal performance of the BLAS routines. The
changes in this final version target new architecture features in
microprocessors and interprocessor communication techniques; also, NUMA
controls enhance multi-threaded execution of BLAS routines on node.

OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD
version. OpenBLAS is an open source project supported by Lab of Parallel
Software and Computational Science, ISCAS.

%package -n lib%name
Summary: Shared library of GotoBLAS2
Group: System/Libraries

%description -n lib%name
GotoBLAS2 has been released by the Texas Advanced Computing Center as
open source software under the BSD license. This product is no longer
under active development by TACC, but it is being made available to the
community to use, study, and extend. GotoBLAS2 uses new algorithms and
memory techniques for optimal performance of the BLAS routines. The
changes in this final version target new architecture features in
microprocessors and interprocessor communication techniques; also, NUMA
controls enhance multi-threaded execution of BLAS routines on node.

OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD
version. OpenBLAS is an open source project supported by Lab of Parallel
Software and Computational Science, ISCAS.

This package contains shared library of OpenBLAS.

%package -n lib%name-devel
Summary: Development files of GotoBLAS2
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
GotoBLAS2 has been released by the Texas Advanced Computing Center as
open source software under the BSD license. This product is no longer
under active development by TACC, but it is being made available to the
community to use, study, and extend. GotoBLAS2 uses new algorithms and
memory techniques for optimal performance of the BLAS routines. The
changes in this final version target new architecture features in
microprocessors and interprocessor communication techniques; also, NUMA
controls enhance multi-threaded execution of BLAS routines on node.

OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD
version. OpenBLAS is an open source project supported by Lab of Parallel
Software and Computational Science, ISCAS.

This package contains development files of OpenBLAS.

%prep
%setup
%ifarch %e2k
%patch2000 -p1
%endif

%build
FLAGS="%optflags %optflags_shared"

# FC/CC - path to compiler
# F_COMPILER/C_COMPILER - compiler type (GCC, CLANG, GFORTRAN, etc.)
# COMMON_OPT - compiler options
FC="gfortran" F77="g77" CC="gcc" \
F_COMPILER="GFORTRAN" C_COMPILER="GCC" \
%make_build SMP=1 MAKE_NB_JOBS=${NPROCS:-%__nprocs} \
%if "%_lib" == "lib64"
	BINARY=64 \
	BINARY64=1 \
%else
	BINARY=32 \
%endif
%ifarch %ix86
	STATIC_ALLOCATION=1 \
%endif
	%{?oblas_target:TARGET=%oblas_target} \
	COMMON_OPT="$FLAGS" \
	%{?_enable_dynamic_arch:DYNAMIC_ARCH=1} \
	ALLOC_HUGETLB=1 \
	%{?_without_lapack:NO_LAPACK=1} \
	%{nil}

%install
%make_install OPENBLAS_LIBRARY_DIR=%buildroot%_libdir \
	      OPENBLAS_INCLUDE_DIR=%buildroot%_includedir/openblas \
	      install
sed -i 's,%buildroot,,' %buildroot%_pkgconfigdir/openblas.pc

%check
%make_build tests \
	MAKE_NB_JOBS=${NPROCS:-%__nprocs} \
	%{?oblas_target:TARGET=%oblas_target} \
	%{?_enable_dynamic_arch:DYNAMIC_ARCH=1} \
	%{?_without_lapack:NO_LAPACK=1} \
	%{nil}

%files -n lib%name
%doc README* *.txt
%_libdir/*-r*.so
%_libdir/*.so.*

%files -n lib%name-devel
%exclude %_libdir/*-r*.so
%_libdir/*.so
%_pkgconfigdir/openblas.pc
%_libdir/cmake/%name/
%_includedir/openblas

%changelog
* Mon Apr 17 2023 Michael Shigorin <mike@altlinux.org> 0.3.19-alt1.2
- spec fixes mentioned by slazav@ back in 2019
- added cmake files

* Thu Jan 20 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.3.19-alt1.1
- e2k patch update

* Mon Dec 20 2021 Ivan A. Melnikov <iv@altlinux.org> 0.3.19-alt1
- Version 0.3.19
- %%mips support

* Thu Aug 26 2021 Ivan A. Melnikov <iv@altlinux.org> 0.3.17-alt1
- Version 0.3.17
- riscv64 support
- disable LTO

* Sat Jun 05 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.3.9-alt2
- fixed passing of compiler options, added check
- added patch with e2k architecture support (no optimizations)

* Sat Apr 25 2020 Kirill Maslinsky <kirill@altlinux.org> 0.3.9-alt1
- Version 0.3.9

* Wed May 15 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.20-alt2
- Added BR: libgomp-devel on ppc64le architecture.

* Tue May 22 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.20-alt1
- 0.2.20 released

* Mon Jun 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.14-alt1.git20150324
- Version 0.2.14

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt2.git20140629
- Version 0.2.9

* Mon Jun 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt1.rc2.git20140306
- Version 0.2.9.rc2

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt1.git20130801
- Version 0.2.8

* Tue Apr 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt2.git20130302
- Fixed cblas.h

* Sun Apr 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt1.git20130302
- Version 0.2.6

* Thu Feb 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.git20121215
- New snaphsot

* Tue Nov 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.git20121127
- Version 0.2.5

* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus

