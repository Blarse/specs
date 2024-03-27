# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name:     kernelshark
Version: 2.3.1
Release: alt1
# Epoch incremented, because previously kernelshark is packaged from trace-cmd
# spec which have much bigger version number (2.9.1).
Epoch:    1
Summary:  KernelShark is a front-end reader of tracing data
License:  GPL-2.0 and LGPL-2.1
Group:    Development/Debug
Url:      https://kernelshark.org/
Vcs:      https://git.kernel.org/pub/scm/utils/trace-cmd/kernel-shark.git

Requires: fonts-ttf-freefont
Requires: trace-cmd

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: fontconfig
BuildRequires: fonts-ttf-freefont
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: libaudit-devel
BuildRequires: libfreeglut-devel
BuildRequires: libjson-c-devel
BuildRequires: libtracecmd-devel
BuildRequires: libtraceevent-devel
BuildRequires: libtracefs-devel
BuildRequires: libXi-devel
BuildRequires: libxml2-devel
BuildRequires: polkit
BuildRequires: qt6-base-devel
BuildRequires: qt6-scxml-devel
BuildRequires: trace-cmd

%define _metainfodir /usr/share/metainfo

%description
KernelShark is a front end reader of trace-cmd(1) output. It reads a
trace-cmd.dat(5) formatted file and produces a graph and list view of
the data.

%prep
%setup

%build
%define optflags_lto %nil
%add_optflags %(getconf LFS_CFLAGS)
%define _cmake__builddir build
%cmake -D_INSTALL_PREFIX=%_prefix -D_LIBDIR=%_libdir
%cmake_build

%install
%cmake_install --component kernelshark
%cmake_install --component polkit-policy
# There is also libkshark-devel component which we don't need.

# error: value "1.1.0" for key "Version" in group "Desktop Entry" is not a known version
sed -i '/Version/d'   %buildroot/%_datadir/applications/kernelshark.desktop
desktop-file-validate %buildroot/%_datadir/applications/kernelshark.desktop
install -Dm644 -t %buildroot%_metainfodir .gear/*.appdata.xml
appstream-util validate-relax --nonet %buildroot%_metainfodir/*.appdata.xml

%files
%doc README LICENSES/* icons/CC_*
%_bindir/kernelshark
%_bindir/kshark-record
%_bindir/kshark-su-record
%_libdir/libkshark*.so.*
%_libdir/kernelshark/
%_datadir/applications/kernelshark.desktop
%_datadir/icons/kernelshark
%_datadir/polkit-1/actions/org.freedesktop.kshark-record.policy
%_metainfodir/*.appdata.xml

%changelog
* Wed Mar 27 2024 Vitaly Chikunov <vt@altlinux.org> 1:2.3.1-alt1
- Update to kernelshark-v2.3.1 (2024-03-20).

* Wed Dec 06 2023 Vitaly Chikunov <vt@altlinux.org> 1:2.3.0-alt1
- Update to kernelshark-v2.3.0 (2023-11-19): switch to Qt 6.

* Mon Jun 26 2023 Vitaly Chikunov <vt@altlinux.org> 1:2.2.1-alt1
- Update to kernelshark-v2.2.1 (2023-06-07).

* Thu May 18 2023 Vitaly Chikunov <vt@altlinux.org> 1:2.2.0-alt4
- Fix graphics display because of missing FreeSans.ttf (ALT#46184).
- Fix capturing when directory name contains a space (ALT#46185).

* Thu May 11 2023 Vitaly Chikunov <vt@altlinux.org> 1:2.2.0-alt3
- Fix 'QLocalSocket::connectToServer: Invalid name' on Capture (ALT#46083).
- Fix segfault in libkshark-tepdata (ALT#46079).

* Mon May 08 2023 Vitaly Chikunov <vt@altlinux.org> 1:2.2.0-alt2
- Add dependence on trace-cmd (ALT#46075).

* Thu Apr 27 2023 Alexey Shabalin <shaba@altlinux.org> 1:2.2.0-alt1
- Updated to kernelshark-v2.2.0 (2023-01-21).

* Tue Aug 30 2022 Vitaly Chikunov <vt@altlinux.org> 1:2.1.1-alt1
- Updated to kernelshark-v2.1.1 (2022-04-26).

* Tue Jan 25 2022 Vitaly Chikunov <vt@altlinux.org> 1:2.1.0-alt1
- Updated to kernelshark-v2.1.0 (2022-01-18).
- First build as separate package with proper version number.

* Sun Dec 06 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt5
- Enable pkexec (RM#24461) in a way compatible with old cmake (for p9).

* Sat Dec 05 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt4
- Allow connect from pkexec'd process (RM#24461).

* Fri Dec 04 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt3
- Enable pkexec (RM#24461).

* Sun Sep 27 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt2
- Build kernelshark, libs, devel, and python3 packages.
