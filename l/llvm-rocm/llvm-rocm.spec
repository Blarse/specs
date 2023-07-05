%define _unpackaged_files_terminate_build 1

%filter_from_requires /python[0-9.]\+(Reporter)/d
%filter_from_requires /python[0-9.]\+(optpmap)/d
%filter_from_requires /python[0-9.]\+(libscanbuild[.].*)/d
# Self-provided by python3(lldb14.0) in a custom path.
%filter_from_requires /python[0-9.]\+(lldb)/d

%global proj rocm
# rocm llvm uses llvm16 as codebase
%global v_major 16
%global v_minor 0
%global v_full %{v_major}.%{v_minor}.0

%global llvm_name llvm-%proj
%global clang_name clang-%proj
%global lld_name lld-%proj

%global llvm_default_name llvm%_llvm_version
%global clang_default_name clang%_llvm_version
%global lld_default_name lld%_llvm_version

%global llvm_prefix %_prefix/lib/llvm-%proj
%global llvm_bindir %llvm_prefix/bin
%global llvm_libdir %llvm_prefix/%_lib
%global llvm_includedir %llvm_prefix/include
%global llvm_libexecdir %llvm_prefix/libexec
%global llvm_datadir %llvm_prefix/share
%global llvm_man1dir %llvm_datadir/man/man1
%global llvm_docdir %llvm_datadir/doc
%global llvm_python3_libdir %llvm_libdir/python3
%global llvm_python3_sitelibdir %llvm_python3_libdir/site-packages

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%ifarch aarch64
%define optflags_debug -g0
#define __nprocs 1
%else
%define optflags_debug -g1
%endif

# LTO-related flags are set by CMake.
# LTO causes LLVM to break badly on %%ix86 see
# https://github.com/llvm/llvm-project/issues/57740
# will enable it conditionally per platform
%global optflags_lto %nil

%def_disable tests
%def_with clang

Name: %llvm_name
Version: 5.6.0
Release: alt0.2
Summary: The LLVM Compiler Infrastructure with ROCm additions

Group: Development/C
License: Apache-2.0 with LLVM-exception
Url: https://github.com/RadeonOpenCompute/llvm-project.git
# Source-URL: https://github.com/RadeonOpenCompute/llvm-project/archive/refs/tags/rocm-%version.tar.gz
Source: llvm-project-%{version}.tar
Patch1: clang-alt-triple.patch
Patch2: 0001-alt-llvm-config-Ignore-wrappers-when-looking-for-current.patch
Patch3: llvm-alt-fix-linking.patch
Patch4: clang-alt-aarch64-dynamic-linker-path.patch
Patch5: clang-cmake-resolve-symlinks-in-ClangConfig.cmake.patch
Patch6: clang-ALT-bug-40628-grecord-command-line.patch
Patch7: clang-tools-extra-alt-gcc-0001-clangd-satisfy-ALT-gcc-s-Werror-return-type.patch
Patch8: llvm-10-alt-python3.patch
Patch9: RH-0010-PATCH-clang-Produce-DWARF4-by-default.patch
Patch10: llvm-cmake-pass-ffat-lto-objects-if-using-the-GNU-toolcha.patch
Patch11: lld-compact-unwind-encoding.h.patch
Patch12: llvm-alt-cmake-build-with-install-rpath.patch
Patch13: clang-16-alt-rocm-device-libs-path.patch
Patch14: llvm-gcc-13-fix.patch

%if_with clang
# https://bugs.altlinux.org/show_bug.cgi?id=34671
%set_verify_elf_method lint=skip
%endif

# ThinLTO requires /proc/cpuinfo to exist; so the same does llvm
BuildPreReq: /proc

# Obtain %%__python3 at prep stage.
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-llvm-common

BuildRequires(pre): cmake >= 3.4.3
BuildRequires: rpm-build >= 4.0.4-alt112 libncursesw-devel
BuildRequires: libstdc++-devel libffi-devel perl-Pod-Parser perl-devel
BuildRequires: python3-module-recommonmark zip zlib-devel binutils-devel ninja-build hsa-rocr-devel = %version
%if_with clang
BuildRequires: %clang_default_name %llvm_default_name-devel %lld_default_name
%else
BuildRequires: gcc-c++
%endif

%define requires_filesystem Requires: %name-filesystem = %EVR
%requires_filesystem
Requires: llvm >= %_llvm_version

# limit to x86_64 due hsa-rocr requirements
ExclusiveArch: x86_64

%description
LLVM is a compiler infrastructure designed for compile-time, link-time,
runtime, and idle-time optimization of programs from arbitrary
programming languages. The compiler infrastructure includes mirror sets
of programming tools as well as libraries with equivalent functionality.

%package filesystem
Group: Development/Other
Summary: Owns the installation prefix for LLVM

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description filesystem
This package owns the installation prefix for LLVM. It is designed to be
pulled in by all non-empty LLVM packages.

%package devel
Group: Development/C
Summary: Libraries and header files for LLVM
%requires_filesystem
Requires: llvm-devel >= %_llvm_version
Conflicts: llvm%{v_major}.%{v_minor}-devel
Requires: %name = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description devel
This package contains library and header files needed to develop new
native programs that use the LLVM infrastructure.

%package gold
Summary: gold linker plugin for LLVM
Group: Development/Tools
%requires_filesystem
# requires: libLLVM
Requires: %name-libs

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description gold
This package contains the gold plugin for LLVM objects.

%package libs
Group: Development/C
Summary: LLVM shared libraries
%requires_filesystem
Requires: %name-gold = %EVR
# LLD is hardwired in ROCm
Requires: %lld_name = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description libs
This package contains shared libraries needed to develop new
native programs that use LLVM.

%package -n %clang_name
Summary: A C language family frontend for LLVM
Group: Development/C
%requires_filesystem
# clang uses various parts of GNU crt bundled with gcc.
# Should they be packaged separately?
Requires: gcc
Requires: clang >= %_llvm_version

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name
clang: noun
    1. A loud, resonant, metallic sound.
    2. The strident call of a crane or goose.
    3. C-language family front-end toolkit.

The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extendable.

%package -n %clang_name-libs
Group: Development/C
Summary: clang shared libraries
%requires_filesystem
Requires: %clang_name-libs-support = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-libs
Shared libraries for the clang compiler.

%package -n %clang_name-libs-support
Group: Development/C
Summary: Support for Clang's shared libraries
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-libs-support
The Clang's shared libraries implement compilers for C and C++, and thus have
to bundle additional platform support headers and libraries for use within the
compilation product. This package contains the platform support.

%package -n %clang_name-libs-support-shared-runtimes
Group: Development/C
Summary: Shared runtimes for Clang's shared libraries
%requires_filesystem
Requires: %clang_name-libs-support = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-libs-support-shared-runtimes
This package contains shared runtime libraries for Scudo and sanitizers.

%package -n %clang_name-devel
Summary: Header files for clang
Group: Development/C
%requires_filesystem
Requires: clang-devel >= %_llvm_version
Requires: %clang_name = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-devel
This package contains header files for the Clang compiler.

%package -n %clang_name-devel-static
Summary: Static libraries for clang
Group: Development/C
%requires_filesystem
Requires: %clang_name-devel = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-devel-static
This package contains static libraries for the Clang compiler.

%package -n %clang_name-tools
Summary: Various clang-based tools
Group: Development/C
%requires_filesystem
Requires: %clang_name = %EVR
Requires: clang-tools >= %_llvm_version

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-tools
This package contains various code analysis and manipulation tools based on
libclang, including clang-format.

%package -n %lld_name
Summary: LLD - The LLVM Linker
Group: Development/C
%requires_filesystem
Requires: lld >= %_llvm_version

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %lld_name
LLD is a linker from the LLVM project. That is a drop-in replacement for system
linkers and runs much faster than them. It also provides features that are
useful for toolchain developers.

%package -n %lld_name-devel
Summary: Header files for LLD
Group: Development/C
%requires_filesystem
Requires: lld-devel >= %_llvm_version
Requires: %lld_name = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %lld_name-devel
This package contains header files for the LLD linker.

%prep
%setup -n llvm-project-%{version}
%patch1 -p1 -b .alt-triple
%patch2 -p1
sed -i 's)"%%llvm_bindir")"%llvm_bindir")' llvm/lib/Support/Unix/Path.inc
%patch3 -p1 -b .alt-fix-linking
%patch4 -p1 -b .alt-aarch64-dynamic-linker
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1 -b .clang-DWARF4
%patch10 -p1
%patch11 -p1
#%%patch12 -p1 -b .llvm-cmake-build-with-install-rpath
%patch13 -p1 -b .clang-rocm-device-path
%patch14 -p1 -b .llvm-gcc-13-fix

# LLVM 12 and onward deprecate Python 2:
# https://releases.llvm.org/12.0.0/docs/ReleaseNotes.html
# Explicitly use python3 in hashbangs.
subst '/^#!.*python$/s|python$|python3|' $(grep -Rl '#!.*python$' *)

%build
PROJECTS="clang;compiler-rt;lld"
export NPROCS="%__nprocs"
if [ "$NPROCS" -gt 64 ]; then
	export NPROCS=64
fi
%define builddir %_cmake__builddir
%define _cmake_skip_rpath -DCMAKE_SKIP_RPATH:BOOL=OFF
%cmake -G Ninja -S llvm \
	-DPACKAGE_VENDOR="%vendor" \
	-DLLVM_VERSION_SUFFIX=rocm \
%if_with clang
	-DLLVM_PARALLEL_LINK_JOBS=1 \
%else
	-DLLVM_PARALLEL_LINK_JOBS=4 \
%endif
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=%llvm_prefix \
	%_cmake_skip_rpath \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
	-DCMAKE_BUILD_RPATH:STRING='' \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DLLVM_ENABLE_PROJECTS="$PROJECTS" \
	-DLLVM_TARGETS_TO_BUILD="AMDGPU;X86;AArch64;PowerPC" \
	-DLLVM_ENABLE_LIBCXX:BOOL=OFF \
	-DLLVM_ENABLE_ZLIB:BOOL=ON \
	-DLLVM_ENABLE_FFI:BOOL=ON \
	-DLLVM_ENABLE_RTTI:BOOL=ON \
	-DLLVM_OPTIMIZED_TABLEGEN:BOOL=ON \
	-DLLVM_BINUTILS_INCDIR="%_includedir/bfd" \
	%if_with clang
	-DCMAKE_C_COMPILER=clang \
	-DCMAKE_CXX_COMPILER=clang++ \
	-DCMAKE_RANLIB:PATH=%_bindir/llvm-ranlib \
	-DCMAKE_AR:PATH=%_bindir/llvm-ar \
	-DCMAKE_NM:PATH=%_bindir/llvm-nm \
	-DLLVM_ENABLE_LTO=Thin \
	-DLLVM_ENABLE_LLD:BOOL=ON \
	%else
	-DLLVM_ENABLE_LTO=Off \
	-DCMAKE_AR:PATH=%_bindir/gcc-ar \
	-DCMAKE_NM:PATH=%_bindir/gcc-nm \
	-DCMAKE_RANLIB:PATH=%_bindir/gcc-ranlib \
	%endif
	\
	-DLLVM_LIBDIR_SUFFIX="%_libsuff" \
	-DPYTHON_EXECUTABLE=%_bindir/python3

sed -i 's|man\ tools/lld/docs/docs-lld-html|man|' %builddir/build.ninja
ninja -vvv -j $NPROCS -C %builddir

%install
sed -i 's|man\ tools/lld/docs/docs-lld-html|man|' %builddir/build.ninja
sed -i '/^[[:space:]]*include.*tools\/lld\/docs\/cmake_install.cmake.*/d' %builddir/tools/lld/cmake_install.cmake
DESTDIR=%buildroot ninja -C %builddir install

if [ %_libsuff == 64 ]; then
mkdir -p %buildroot%llvm_prefix/lib ||:
mv %buildroot%llvm_libdir/{libear,libscanbuild} %buildroot%llvm_prefix/lib
fi

install -m 0755 %builddir/%_lib/LLVMHello.so %buildroot%llvm_libdir/
install -m 0755 %builddir/%_lib/BugpointPasses.so %buildroot%llvm_libdir/

# The following files are not used by LLVM builds for Linux.
rm -f %buildroot%llvm_bindir/argdumper
rm -f %buildroot%llvm_datadir/clang/clang-format-bbedit.applescript

# we don't need scanbuild tools and flang in rocm
rm -rf %buildroot{%_man1dir,%llvm_man1dir}
rm -f %buildroot%llvm_bindir/{analyze-build*,scan-build*,scan-view*,intercept-build*,flang*}

# Symlink executables to %_bindir.
mkdir -p %buildroot%_bindir
for b in %buildroot%llvm_bindir/*; do
	bb="$(basename "$b")"
	echo "$bb" | grep -q -- '-%proj$' && continue # if already appended
	ln -srv "$b" "%buildroot%_bindir/$bb-%proj"
done

# Symlink sonamed shared libraries in %llvm_prefix/%_libdir to %_libdir.
mkdir -p %buildroot%_libdir
find %buildroot%llvm_libdir/*.so* -type f,l \
	| grep -E '^%buildroot%llvm_libdir/.*(%v_major)' | sort | tee %_tmppath/shared-objects \
	| sed 's)%llvm_libdir)%_libdir)' > %_tmppath/shared-object-links
paste %_tmppath/shared-objects %_tmppath/shared-object-links | while read object link; do
	ln -srv "$object" "$link"
done

# List all packaged binaries in this source package.
find %buildroot%_bindir/*-%proj > %_tmppath/PATH-executables

# For paranoic reasons library packaging policy covers peculiar directory paths.
# If there are $A.a and $A.so in %llvm_libdir/clang, they should not end up in the
# same package (but can be co-installed on a system).
# Let's list all the $A.so for which $A.a exists into a separate package.
# We also consider i386-symlinks for iN86.
find %buildroot%llvm_libdir/clang -type f,l -name '*.a' -or -name '*.so' | \
    sed -r -n 's/^(\/.+)\.a$/\1/p; s/^(.+)\.so$/\1/p' | sort | uniq -d > %_tmppath/libclang-support-dupes
sed < %_tmppath/libclang-support-dupes 's)^%buildroot)); s/$/.a/' > %_tmppath/libclang-support-static-runtimes
sed < %_tmppath/libclang-support-dupes 's)^%buildroot)); s/$/.so/' > %_tmppath/libclang-support-shared-runtimes
sed < %_tmppath/libclang-support-shared-runtimes 's/^/%%exclude /' > %_tmppath/dyn-files-libclang-support
echo "Expelling likely redundant Clang shared runtimes:" && cat %_tmppath/dyn-files-libclang-support

# Emit a stanza list for %%files.
# A tool can be accompanied by a man page or not.
emit_filelist() {
    awk -F'\t' '
$1 ~ "bin" { print "%llvm_bindir/" $2; print "%_bindir/" $2 "-%proj"; }
'
}

# Emit executable list for %name.
emit_filelist >%_tmppath/dyn-files-%name <<EOExecutableList
bin	bugpoint
bin	diagtool
bin	dsymutil
bin	llc
bin	lli
bin	llvm-addr2line
bin	llvm-ar
bin	llvm-as
bin	llvm-bcanalyzer
bin	llvm-bitcode-strip
bin	llvm-cat
bin	llvm-cfi-verify
bin	llvm-cov
bin	llvm-c-test
bin	llvm-cvtres
bin	llvm-cxxdump
bin	llvm-cxxfilt
bin	llvm-cxxmap
bin	llvm-debuginfod-find
bin	llvm-debuginfod
bin	llvm-diff
bin	llvm-dis
bin	llvm-dlltool
bin	llvm-dwarfdump
bin	llvm-dwarfutil
bin	llvm-dwp
bin	llvm-exegesis
bin	llvm-extract
bin	llvm-gsymutil
bin	llvm-ifs
bin	llvm-install-name-tool
bin	llvm-jitlink
bin	llvm-lib
bin	llvm-libtool-darwin
bin	llvm-link
bin	llvm-lipo
bin	llvm-lto
bin	llvm-lto2
bin	llvm-mc
bin	llvm-mca
bin	llvm-ml
bin	llvm-modextract
bin	llvm-mt
bin	llvm-nm
bin	llvm-objcopy
bin	llvm-objdump
bin	llvm-opt-report
bin	llvm-otool
bin	llvm-pdbutil
bin	llvm-profdata
bin	llvm-profgen
bin	llvm-ranlib
bin	llvm-rc
bin	llvm-readelf
bin	llvm-readobj
bin	llvm-reduce
bin	llvm-remark-size-diff
bin	llvm-rtdyld
bin	llvm-size
bin	llvm-sim
bin	llvm-tapi-diff
bin	llvm-tli-checker
bin	llvm-windres
bin	llvm-split
bin	llvm-stress
bin	llvm-strings
bin	llvm-strip
bin	llvm-symbolizer
bin	llvm-tblgen
bin	llvm-debuginfo-analyzer
bin	llvm-remarkutil
bin	llvm-undname
bin	llvm-xray
bin	opt
bin	sancov
bin	sanstats
bin	verify-uselistorder

EOExecutableList

emit_filelist >%_tmppath/dyn-files-%clang_name <<EOExecutableList
bin	clang
bin	clang-%{v_major}
bin	clang++
bin	clang-cl
bin	clang-cpp
EOExecutableList

emit_filelist >%_tmppath/dyn-files-%clang_name-tools <<EOExecutableList
bin	amdgpu-offload-arch
bin	nvidia-arch
bin	offload-arch
bin	amdgpu-arch
bin	nvptx-arch
bin	c-index-test
bin	clang-build-select-link
bin	clang-nvlink-wrapper
bin	clang-offload-wrapper
bin	clang-check
bin	clang-extdef-mapping
bin	clang-format
bin	clang-linker-wrapper
bin	clang-offload-bundler
bin	clang-offload-packager
bin	clang-refactor
bin	clang-rename
bin	clang-repl
bin	clang-scan-deps
bin	clang-tblgen
bin	git-clang-format
bin	hmaptool
EOExecutableList

# Comment out file validation for CMake targets placed
# in a different package.
sed -i '
/APPEND _IMPORT_CHECK_TARGETS \(mlir-\|MLIR\)/ {s|^|#|}
/APPEND _IMPORT_CHECK_TARGETS \(tblgen-lsp-server\)/ {s|^|#|}
/APPEND _IMPORT_CHECK_TARGETS \(Polly\)/ {s|^|#|}
/APPEND _IMPORT_CHECK_TARGETS \(llvm-omp-device-info\|omptarget\)/ {s|^|#|}
' %buildroot%llvm_libdir/cmake/llvm/LLVMExports-*.cmake

# Comment out file validation for CMake targets producing executables
# that may be placed in a different package.
sed -i '
/APPEND _IMPORT_CHECK_FILES_FOR_.* .*[/]bin[/].*/ {s|^|#|}
' %buildroot%llvm_libdir/cmake/clang/ClangTargets-*.cmake

# cleanup
rm -rf %buildroot{%llvm_libexecdir,%llvm_datadir,%llvm_prefix/lib}

%check
%if_enabled tests
LD_LIBRARY_PATH=%buildroot%llvm_libdir:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH
ninja -C %builddir check-all || :
%endif

# Do not generate dependencies for clang-{format,rename} plugins.
%add_findreq_skiplist %llvm_datadir/clang/*

%files filesystem
%dir %llvm_prefix
%dir %llvm_bindir
%dir %llvm_libdir
%dir %llvm_libdir/cmake
%dir %llvm_includedir

%files -f %_tmppath/dyn-files-%name
%doc llvm/CREDITS.TXT llvm/LICENSE.TXT llvm/README.txt

%files libs
%llvm_libdir/libLTO.so.*
%_libdir/libLTO.so.*
%llvm_libdir/libRemarks.so.*
%_libdir/libRemarks.so.*

%files devel
%llvm_bindir/llvm-config
%_bindir/llvm-config-%proj
%llvm_includedir/llvm
%llvm_includedir/llvm-c
%llvm_libdir/libLTO.so
%llvm_libdir/libRemarks.so
%llvm_libdir/LLVMHello.so
%llvm_libdir/BugpointPasses.so
%llvm_libdir/cmake/llvm
%llvm_libdir/libLLVM*.a

%files gold
%llvm_libdir/LLVMgold.so

%files -n %clang_name -f %_tmppath/dyn-files-%clang_name

%files -n %clang_name-libs
%llvm_libdir/libclang*.so.*
%_libdir/libclang*.so.*

%files -n %clang_name-libs-support -f %_tmppath/dyn-files-libclang-support
%llvm_libdir/clang

%files -n %clang_name-libs-support-shared-runtimes -f %_tmppath/libclang-support-shared-runtimes

%files -n %clang_name-devel
%llvm_includedir/clang
%llvm_includedir/clang-c
%llvm_libdir/libclang*.so
%llvm_libdir/cmake/clang
%llvm_libdir/libclang*.a

%files -n %clang_name-tools -f %_tmppath/dyn-files-%clang_name-tools

%files -n %lld_name
%llvm_bindir/lld
%_bindir/lld-%proj
%llvm_bindir/lld-link
%_bindir/lld-link-%proj
%llvm_bindir/ld*.lld
%_bindir/ld*.lld-%proj
%llvm_bindir/wasm-ld
%_bindir/wasm-ld-%proj

%files -n %lld_name-devel
%dir %llvm_includedir/lld
%llvm_includedir/lld/*
# see Patch18: lld-compact-unwind-encoding.h.patch
%llvm_includedir/mach-o
%llvm_libdir/cmake/lld
%llvm_libdir/liblld*.a

%changelog
* Wed Jul 05 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt0.2
- Enable compiler-rt.

* Mon Jul 03 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt0.1
- Initial build as separate toolchain for ROCm applications.

