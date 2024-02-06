# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

%define optflags_lto -flto=thin

# Based on https://github.com/iovisor/bpftrace/blob/master/INSTALL.md

Name: bpftrace
Version: 0.19.1
Release: alt2
Summary: High-level tracing language for Linux eBPF
Group: Development/Debuggers
License: Apache-2.0
URL: https://github.com/iovisor/bpftrace
# Docs: https://github.com/iovisor/bpftrace/blob/master/docs/reference_guide.md
# Docs: https://github.com/iovisor/bpftrace/blob/master/docs/tutorial_one_liners.md
# Docs: http://www.brendangregg.com/BPF/bpftrace-cheat-sheet.html
# Docs: http://www.brendangregg.com/ebpf.html#bpftrace
# PR: https://lwn.net/Articles/793749/
# PR: http://www.brendangregg.com/blog/2018-10-08/dtrace-for-linux-2018.html

Source: %name-%version.tar
# Submodules are maintained with gear-submodule-update.
Source1: bcc-0.tar
Source2: blazesym-0.tar
Source3: bpftool-0.tar
Source4: libbpf-0.tar
Source5: libbpf-1.tar
Source6: libbpf-2.tar
ExclusiveArch:	x86_64 aarch64

%define llvm_min 11
BuildRequires(pre): rpm-macros-cmake
BuildRequires: binutils-devel
BuildRequires: cereal-devel
BuildRequires: clangd >= %llvm_min
BuildRequires: clang-devel >= %llvm_min
BuildRequires: clang-devel-static >= %llvm_min
BuildRequires: clang-tools >= %llvm_min
BuildRequires: cmake
BuildRequires: flex
BuildRequires: libbcc-devel
BuildRequires: libbpf-devel
BuildRequires: libdw-devel
BuildRequires: libelf-devel
BuildRequires: libpcap-devel
BuildRequires: libstdc++-devel
BuildRequires: libstdc++-devel-static
BuildRequires: lld >= %llvm_min
BuildRequires: llvm-devel >= %llvm_min
BuildRequires: llvm-devel-static >= %llvm_min
BuildRequires: python3-module-setuptools
BuildRequires: /proc
# Assuming 'kernel' dependency will bring un-def kernel
%{?!_without_check:%{?!_disable_check:
BuildRequires: kernel-headers-modules-un-def
BuildRequires: rpm-build-vm
}}

%description
bpftrace is a high-level tracing language for Linux enhanced Berkeley
Packet Filter (eBPF) available in recent Linux kernels (4.x). bpftrace
uses LLVM as a backend to compile scripts to BPF-bytecode and makes use of
BCC for interacting with the Linux BPF system, as well as existing Linux
tracing capabilities: kernel dynamic tracing (kprobes), user-level dynamic
tracing (uprobes), and tracepoints. The bpftrace language is inspired by
awk and C, and predecessor tracers such as DTrace and SystemTap. bpftrace
was created by Alastair Robertson.

%prep
%setup
tar xf %SOURCE1 -C .
tar xf %SOURCE2 -C bcc/libbpf-tools
tar xf %SOURCE3 -C bcc/libbpf-tools
tar xf %SOURCE4 -C bcc/libbpf-tools/bpftool
tar xf %SOURCE5 -C bcc/src/cc
tar xf %SOURCE6 -C .
sed -i 's/\bpython\b/python3/' tests/runtime/call
sed -i 's/@.*@/True/' tests/runtime/engine/cmake_vars.py

%build
%remove_optflags -frecord-gcc-switches
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
export Clang_DIR=/usr/share/cmake/Modules/clang
# -DBUILD_TESTING:BOOL=ON will require googletest and try to clone it from github
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_TESTING:BOOL=OFF \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DLLVM_DIR=$(llvm-config --cmakedir) \
	-DOFFLINE_BUILDS:BOOL=ON \
	-DALLOW_UNSAFE_PROBE:BOOL=ON \
	-DUSE_SYSTEM_BPF_BCC:BOOL=ON \
	%nil
%cmake_build

%install
%cmake_install
find %buildroot%_datadir/%name/tools -name '*.bt' | xargs chmod a+x

# Fix man pages.
pushd %buildroot%_man8dir
 rename '' bpftrace- *.gz
popd

# Need to keep BEGIN_trigger and END_trigger
# https://github.com/iovisor/bpftrace/issues/954
%brp_strip_debug %_bindir/bpftrace

%check
%_cmake__builddir/src/bpftrace --version	 # not requires root
vm-run %_cmake__builddir/src/bpftrace --info # should be fast enough even w/o kvm
[ -w /dev/kvm ] && vm-run %_cmake__builddir/src/bpftrace -l 'kprobe:*_sleep_*'
if [ -w /dev/kvm ]; then
	# Great run-time tests

	# Some fail due to no BUILD_TESTING
	.gear/delete-blocks syscalls:	tests/runtime/*
	.gear/delete-blocks testprogs	tests/runtime/*
	.gear/delete-blocks uprobe	tests/runtime/*
	.gear/delete-blocks usdt	tests/runtime/usdt
	.gear/delete-blocks vfs_read	tests/runtime/*     # TIMEOUT
	.gear/delete-blocks hardware	tests/runtime/probe # TIMEOUT
	.gear/delete-blocks k.*_order	tests/runtime/probe # TIMEOUT
	.gear/delete-blocks watchpoint:	tests/runtime/watchpoint
	.gear/delete-blocks string_args	tests/runtime/other
	.gear/delete-blocks interval_order tests/runtime/probe
	.gear/delete-blocks tracepoint_order tests/runtime/probe
	.gear/delete-blocks uint64_t	tests/runtime/signed_ints
	.gear/delete-blocks tracepoint:random:random_read tests/runtime/variable
	.gear/delete-blocks tracepoint:sched:sched_wakeup tests/runtime/regression
%ifarch aarch64
	# TIMEOUT on aarch64
	.gear/delete-blocks python	tests/runtime/json-output
%endif
	export BPFTRACE_RUNTIME_TEST_EXECUTABLE=$PWD/%_cmake__builddir/src/
	sed -i 's/xattr.h/user.h/' tests/runtime/basic
	vm-run --kvm=cond --sbin tests/runtime-tests.sh
fi

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING-TOOLS.md
%doc docs/reference_guide.md docs/tutorial_one_liners.md
%_bindir/*
%_datadir/%name
%_man8dir/*

%changelog
* Tue Feb 06 2024 Grigory Ustinov <grenka@altlinux.org> 0.19.1-alt2
- Fixed FTBFS.

* Sun Nov 12 2023 Vitaly Chikunov <vt@altlinux.org> 0.19.1-alt1
- Update to v0.19.1 (2023-10-04).

* Wed Aug 30 2023 Vitaly Chikunov <vt@altlinux.org> 0.16.0-alt3
- Fix FTBFS errors and crash for LLVM 15.

* Mon Dec 19 2022 Vitaly Chikunov <vt@altlinux.org> 0.16.0-alt2
- Fix SIGSEGV when vmlinux is not available and loading BTF data failed.

* Sun Oct 09 2022 Vitaly Chikunov <vt@altlinux.org> 0.16.0-alt1
- Update to v0.16.0 (2022-08-30).

* Sat May 28 2022 Vitaly Chikunov <vt@altlinux.org> 0.15.0-alt1
- Updated to v0.15.0 (2022-05-24).

* Fri Jan 21 2022 Vitaly Chikunov <vt@altlinux.org> 0.13.1-alt1
- Updated to v0.13.1 (2021-12-21).
- Do not strip BEGIN/END triggers from bpftrace (closes: #41750).

* Thu Sep 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.12.1-alt3
- Rebuilt with LTO.

* Wed May 12 2021 Arseny Maslennikov <arseny@altlinux.org> 0.12.1-alt2
- NMU: spec: adapt to new cmake macros.

* Fri Apr 30 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.1-alt1
- Update to v0.12.1 (2021-04-16).
- spec: Build with default Clang/LLVM (>= 11).

* Mon Nov 30 2020 Vitaly Chikunov <vt@altlinux.org> 0.11.4-alt1
- Update to v0.11.4 (2020-11-13).

* Tue Aug 25 2020 Vitaly Chikunov <vt@altlinux.org> 0.11.0-alt3
- Rename man pages with bpftrace- prefix.
- Rebuild with debuginfo.

* Mon Aug 10 2020 Vitaly Chikunov <vt@altlinux.org> 0.11.0-alt2
- Rebuild with clang10.

* Fri Jul 17 2020 Vitaly Chikunov <vt@altlinux.org> 0.11.0-alt1
- Update to v0.11.0.

* Sat Jul 04 2020 Vitaly Chikunov <vt@altlinux.org> 0.10.0-alt2
- Fix build with libbcc-devel-0.15.0.

* Wed Apr 15 2020 Vitaly Chikunov <vt@altlinux.org> 0.10.0-alt1
- Update to v0.10.0 released at 2020-04-12. New features: kfuncs,
  C++ Symbol demangling, if-else control flow.

* Sat Mar 28 2020 Vitaly Chikunov <vt@altlinux.org> 0.9.4-alt2
- spec: Rework BuildRequires.

* Sat Mar 14 2020 Vitaly Chikunov <vt@altlinux.org> 0.9.4-alt1
- Update to v0.9.4.
- Update license tag from ASL 2.0 to Apache-2.0.
- Add %%check with some tests.

* Fri May 17 2019 Vitaly Chikunov <vt@altlinux.org> 0.9.0.0.169.ga4bf870-alt1
- First import v0.9-169-ga4bf870.
