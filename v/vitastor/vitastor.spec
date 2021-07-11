
%global _unpackaged_files_terminate_build 1

Name: vitastor
Version: 0.6.5
Release: alt1
Summary: Vitastor, a fast software-defined clustered block storage
Group: System/Base

License: VNPL-1.1
Url: https://vitastor.io/
Source0: %name-%version.tar
Source2: cpp-btree.tar
Source3: json11.tar

Patch: %name-%version.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

BuildRequires: pkgconfig(liburing)
BuildRequires: libgperftools-devel
BuildRequires: node >= 10
BuildRequires: libjerasure-devel
BuildRequires: libgf-complete-devel
BuildRequires: rdma-core-devel

%description
Vitastor is a small, simple and fast clustered block storage (storage for VM drives),
architecturally similar to Ceph which means strong consistency, primary-replication,
symmetric clustering and automatic data distribution over any number of drives of any
size with configurable redundancy (replication or erasure codes/XOR).

%package common
Summary: Vitastor SDS Common
Group: System/Base
BuildArch: noarch

%description common
Common utilities for Vitastor.

%package mon
Summary: Vitastor SDS monitor service
Group: System/Base
BuildArch: noarch
Requires: node
Requires: lp_solve
Requires: %name-common = %EVR

%description mon
Vitastor SDS monitor service.
Monitor is a separate daemon that watches cluster state and handles failures.

%package osd
Summary: Vitastor SDS Object Storage Daemon
Group: System/Base
Requires: %name-common = %EVR

%description osd
Vitastor SDS Object Storage Daemon is a process that stores data and serves read/write requests.

%package nbd
Summary: Vitastor SDS NBD proxy
Group: System/Base

%description nbd
Vitastor SDS NBD proxy for kernel mounts.

%package -n lib%name-client
Group: System/Libraries
Summary: Vitastor SDS user-space client library
License: VNPL-1.1 OR GPL-2.0+

%description -n lib%name-client
Vitastor SDS user-space client library.

%package -n lib%name-blk
Group: System/Libraries
Summary: Vitastor SDS blk library

%description -n lib%name-blk
Vitastor SDS blk library.

%package -n lib%name-devel
Group: Development/C++
Summary: Vitastor SDS headers of client and blk library
License: VNPL-1.1 OR GPL-2.0+
Requires: lib%name-blk = %EVR lib%name-client = %EVR

%description -n lib%name-devel
This package contains libraries and headers needed to develop programs
that use Vitastor SDS library.

%prep
%setup
%patch -p1
tar -xf %SOURCE2 -C cpp-btree
tar -xf %SOURCE3 -C json11

%build
%cmake \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DWITH_QEMU=OFF \
	-DWITH_FIO=OFF
%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot{%_datadir,%_localstatedir}/%name
cp -r mon %buildroot%_datadir/%name

%pre common
groupadd -r -f %name 2>/dev/null ||:
useradd  -r -g %name -s /sbin/nologin -c "Vitastor daemons" -M -d %_localstatedir/%name %name 2>/dev/null ||:

#%post mon
#%post_service vitastor-mon

#%preun mon
#%preun_service vitastor-mon

#%post osd
#systemctl daemon-reload ||:
#if [ "$1" -eq 1 ]; then
#        systemctl -q preset vitastor-osd@\*.service vitastor-osd.target ||:
#else
#        systemctl try-restart vitastor-osd.target ||:
#fi

#%preun osd
#if [ "$1" -eq 0 ]; then
#        systemctl --no-reload -q disable vitastor-osd@\*.service vitastor-osd.target ||:
#        systemctl stop vitastor-osd@\*.service  vitastor-osd.target ||:
#fi

%files common
%doc README.md README-ru.md VNPL-1.1.txt GPL-2.0.txt
%attr(770,root,%name) %dir %_localstatedir/%name

%files osd
%_bindir/%name-osd
# ? may be to utils package?
%_bindir/%name-dump-journal
%_bindir/%name-rm

%files mon
%_datadir/%name

%files nbd
%_bindir/%name-nbd

%files -n lib%name-blk
%_libdir/lib%{name}_blk.so.*

%files -n lib%name-client
%_libdir/lib%{name}_client.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%changelog
* Sun Jul 11 2021 Alexey Shabalin <shaba@altlinux.org> 0.6.5-alt1
- 0.6.5

* Fri Jul 02 2021 Alexey Shabalin <shaba@altlinux.org> 0.6.4-alt2
- build master snapshot 30bb6026818b66bbe05bde38d70673e4633313e9
- package client header to devel package
- merge blk and client devel packages

* Wed May 19 2021 Alexey Shabalin <shaba@altlinux.org> 0.6.4-alt1
- 0.6.4

* Thu May 06 2021 Alexey Shabalin <shaba@altlinux.org> 0.6.3-alt1
- 0.6.3

* Mon Apr 19 2021 Alexey Shabalin <shaba@altlinux.org> 0.6.2-alt1
- 0.6.2

* Fri Mar 19 2021 Alexey Shabalin <shaba@altlinux.org> 0.5.10-alt1
- Initial build.

