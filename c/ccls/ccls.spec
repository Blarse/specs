Name: ccls
Version: 0.20220729
Release: alt3

Summary: C/C++/Objective-C language server
License: Apache-2.0
Group: Development/C
Url: https://github.com/MaskRay/ccls

Source: %name-%version-%release.tar

BuildRequires: cmake libstdc++-devel zlib-devel
BuildRequires: pkgconfig(RapidJSON)
BuildRequires: clang-devel llvm-devel

%description
%summary

%prep
%setup

%build
%define optflags_lto %nil
export CC=clang
export CXX=clang++
%cmake -DCCLS_VERSION=%version-%release
%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSE README.md
%_bindir/ccls

%changelog
* Fri Jun 16 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20220729-alt3
- unpinned clang version and rebuilt with current clang15

* Wed Jan 18 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20220729-alt2
- 0.20220729-4-g8bc39595

* Wed Aug 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20220729-alt1
- 0.20220729 released

* Thu May 05 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20210330-alt1
- initial
