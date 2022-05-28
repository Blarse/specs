# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: blktrace
Version: 1.3.0
Release: alt2
Summary: Block queue IO tracer
License: GPL-2.0-only
Group: Development/Debuggers
Url: https://git.kernel.dk/cgit/blktrace/
Vcs: git://git.kernel.dk/blktrace.git

Source: %name-%version.tar
BuildRequires: libaio-devel
%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm fio}}

# Avoid: "forbidden requires: python-base
# sisyphus_check: check-deps ERROR: package dependencies violation"
AutoReqProv: nopython noshebang

%description
blktrace is a block layer IO tracing mechanism which provides detailed
information about request queue operations up to user space.

  blkiomon - Monitor block device I/O based o blktrace data
  blkparse - Produce formatted output of event streams of block devices
  blkrawverify - Verifies an output file produced by blkparse
  blktrace - Generate traces of the I/O traffic on block devices
  bno_plot.py - Generate interactive 3D plot of IO blocks and sizes
  btrace - Perform live tracing for block devices
  btrecord & btreplay - Recreate IO loads recorded by blktrace
  btt - Analyse block I/O traces produces by blktrace
  iowatcher - Create visualizations from blktrace results
  verify_blkparse - Verifies an output file produced by blkparse

%prep
%setup

%build
%make_build CFLAGS="%optflags"
# No building docs to avoid bringing texlive monster.

%install
%makeinstall_std \
	prefix=%prefix \
	mandir=%_mandir

%check
%buildroot%_bindir/blkparse -V
%buildroot%_bindir/btreplay -V
%buildroot%_bindir/btrecord -V
%buildroot%_bindir/btt -V
%buildroot%_bindir/blkiomon -V
# blktrace itself will just segfault, becasue no access to `/sys/devices/system/cpu/online`.
# Other proggies do not support `-V`.

truncate -s 11M disk.img
PATH=%buildroot%_bindir:$PATH
# 9p have bugs which prevent blktrace correctly working
vm-run --kvm=cond --udevd --drive=$PWD/disk.img,format=raw "cd /tmp; $PWD/.gear/tests.sh"

%files
%doc README doc/blktrace.tex
%_bindir/*
%_man1dir/*
%_man8dir/*

%changelog
* Sat May 28 2022 Vitaly Chikunov <vt@altlinux.org> 1.3.0-alt2
- Update to blktrace-1.3.0-3-g7f5d2c5 (2021-10-21).
- Fix %%check failure on 9pfs.

* Wed Jun 16 2021 Vitaly Chikunov <vt@altlinux.org> 1.3.0-alt1
- Update to blktrace-1.3.0 (2021-06-14).
- spec: Add tests in %%check.

* Sat Aug 08 2020 Vitaly Chikunov <vt@altlinux.org> 1.2.0-alt1
- Update to blktrace-1.2.0-37-ga021a33 (2020-05-13).
- spec: Do not build blktrace.pdf (read blktrace.tex instead).
- spec: Remove python dependency for rarely useful bno_plot.py.

* Mon Mar 12 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1.1
- NMU: fixed build with new texlive

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 1.0.5-alt1
- 1.0.5

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt1.1
- Rebuild with Python-2.7

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 1.0.3-alt1
- 1.0.3

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.1
- Rebuilt with python 2.6

* Fri Oct 30 2009 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1
- 1.0.1
- reworked gear repo style

* Sat Jun 14 2008 Michael Shigorin <mike@altlinux.org> 0.99.3-alt1
- built for ALT Linux (based on btrace.spec in source repo)
  + commit 84a26fcd9adebd1537bf2c4eee69d1ca23ccbc5f
    (seems working while last release is a bit dated)
- spec fixup/cleanup
- buildreq

* Mon Oct 10 2005 - axboe@suse.de
- Initial version
