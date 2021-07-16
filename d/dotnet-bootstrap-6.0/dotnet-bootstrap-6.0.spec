%define _unpackaged_files_terminate_build 1

%define _dotnet_major 6.0
%define _dotnet_corerelease 6.0.0-preview.6.21352.12
%define _dotnet_sdkmanifestsrelease 6.0.100
%define _dotnet_sdkrelease 6.0.100-preview.6.21355.2
%define _dotnet_aspnetcorerelease 6.0.0-preview.6.21355.2
%define _dotnet_templatesrelease 6.0.0-preview.6.21355.2
%define _dotnet_coreapprefrelease 6.0.0-preview.6.21352.12
%define _dotnet_aspnetcoreapprefrelease 6.0.0-preview.6.21355.2
%define _dotnet_netstandartrelease 2.1.0
%define preview .preview.6
%define _dotnet_coreshortrelease 6.0.0%preview
%define _dotnet_sdkshortrelease 6.0.100%preview

%define _dotnetdir %_libdir/%name

Name: dotnet-bootstrap-%_dotnet_major
Version: 6.0.0%preview
Release: alt1

Summary: .NET Core SDK binaries

License: MIT
Url: https://github.com/dotnet
Group: Development/Other

# To check we manually update download url
# from https://github.com/dotnet/core/tree/master/release-notes/6.0

# x86_64
# Source-url: https://download.visualstudio.microsoft.com/download/pr/45f9f84c-dbe6-458e-bea1-c1e931802486/995edcbcd852a07b0a285626f30afb33/dotnet-sdk-6.0.100-preview.6.21355.2-linux-x64.tar.gz
Source: %name-%version.tar

# aarch64
# Source2-url: https://download.visualstudio.microsoft.com/download/pr/8a6a12fc-35bb-47ca-9353-b1e97d569382/61221db91a720e7ae5833460f2ea53d2/dotnet-sdk-6.0.100-preview.6.21355.2-linux-arm64.tar.gz
Source2: %name-aarch64-%version.tar

ExclusiveArch: x86_64 aarch64

#Requires: /proc
#BuildPreReq: /proc

%set_verify_elf_method textrel=relaxed
AutoReq: no,lib,shell
AutoProv: no

BuildRequires(pre): rpm-macros-dotnet >= 6.0

BuildRequires: libunwind >= 1.1
BuildRequires: liblttng-ust >= 2.8.0
BuildRequires: libcurl
BuildRequires: libkrb5

# for System.Security.Cryptography.Native.OpenSsl.so
# but already required by libkrb5
#Requires: libcrypto10 libssl10

# it is not linked directly (need the same version like in libicu-devel)
# there are icu detection in a version range
Requires: libicu

Provides: dotnet-bootstrap-runtime-%_dotnet_major = %_dotnet_coreshortrelease
Provides: dotnet-bootstrap-sdk-%_dotnet_major = %_dotnet_sdkshortrelease

%description
This package contains full .NET %_dotnet_major SDK binaries, needed for bootstrap build.

%prep
%setup
%ifarch aarch64
rm -rf packs/ host/ shared/
tar xfv %SOURCE2
%endif

%install
mkdir -p %buildroot%_libdir/%name/
cp -a * %buildroot%_libdir/%name/

# due missed lldb (https://bugzilla.altlinux.org/show_bug.cgi?id=33411)
rm -f %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/libsosplugin.so
%__subst "s|libsosplugin.so|libsos.so|g" %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/Microsoft.NETCore.App.deps.json

cd %buildroot%_libdir/%name

# See also https://bugzilla.altlinux.org/show_bug.cgi?id=37413
strip \
	shared/Microsoft.NETCore.App/%_dotnet_corerelease/libmscordbi.so \
	shared/Microsoft.NETCore.App/%_dotnet_corerelease/libmscordaccore.so \
	shared/Microsoft.NETCore.App/%_dotnet_corerelease/libhostpolicy.so \
	shared/Microsoft.NETCore.App/%_dotnet_corerelease/libdbgshim.so \
	shared/Microsoft.NETCore.App/%_dotnet_corerelease/libcoreclrtraceptprovider.so \
	shared/Microsoft.NETCore.App/%_dotnet_corerelease/libcoreclr.so \
	shared/Microsoft.NETCore.App/%_dotnet_corerelease/libclrjit.so \
	shared/Microsoft.NETCore.App/%_dotnet_corerelease/libSystem.Security.Cryptography.Native.OpenSsl.so \
	shared/Microsoft.NETCore.App/%_dotnet_corerelease/libSystem.Net.Security.Native.so \
	shared/Microsoft.NETCore.App/%_dotnet_corerelease/libSystem.Native.so \
	shared/Microsoft.NETCore.App/%_dotnet_corerelease/libSystem.IO.Compression.Native.so \
	shared/Microsoft.NETCore.App/%_dotnet_corerelease/createdump \
	sdk/%_dotnet_sdkrelease/AppHostTemplate/apphost \
	packs/Microsoft.NETCore.App.Host.%_dotnet_rid/%_dotnet_corerelease/runtimes/%_dotnet_rid/native/libnethost.so \
	packs/Microsoft.NETCore.App.Host.%_dotnet_rid/%_dotnet_corerelease/runtimes/%_dotnet_rid/native/apphost \
	host/fxr/%_dotnet_corerelease/libhostfxr.so \
	dotnet \
	#

%files
%dir %_dotnetdir/
%_dotnetdir/dotnet
%dir %_dotnetdir/templates/
%_dotnet_templates/
%dir %_dotnetdir/packs/
%dir %_dotnetdir/packs/Microsoft.NETCore.App.Host.%_dotnet_rid/
%_dotnet_coreapphost/
%dir %_dotnetdir/packs/Microsoft.NETCore.App.Ref/
%_dotnet_coreappref/
%dir %_dotnetdir/packs/Microsoft.AspNetCore.App.Ref/
%_dotnet_aspnetcoreappref/
%dir %_dotnetdir/packs/NETStandard.Library.Ref/
%_dotnet_netstandart/
%dir %_dotnetdir/host/
%dir %_dotnetdir/host/fxr/
%_dotnet_hostfxr/
%dir %_dotnetdir/sdk/
%_dotnet_sdk/
%dir %_dotnetdir/sdk-manifests/
%_dotnet_sdkmanifests/
%dir %_dotnetdir/shared/
%dir %_dotnetdir/shared/Microsoft.NETCore.App/
%_dotnet_coreapp/
%dir %_dotnetdir/shared/Microsoft.AspNetCore.App/
%_dotnet_aspnetcoreapp/
%_dotnetdir/LICENSE.txt
%_dotnetdir/ThirdPartyNotices.txt

%changelog
* Fri Jul 16 2021 Vitaly Lipatov <lav@altlinux.ru> 6.0.0.preview.6-alt1
- .NET 6.0.preview.6

* Tue Feb 23 2021 Vitaly Lipatov <lav@altlinux.ru> 6.0.0.preview.1-alt1

* Wed Feb 17 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.3-alt1
- .NET 5.0.3 and .NET SDK 5.0.103
- CVE-2021-1721: .NET Core Denial of Service Vulnerability
- CVE-2021-24112: .NET 5 and .NET Core Remote Code Execution Vulnerability

* Thu Jan 14 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.2-alt1
- .NET 5.0.2 and .NET SDK 5.0.102

* Sun Aug 02 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.6-alt1
- new version 3.1.6 (with rpmrb script) (ALT bug 38744)
- .NET Core 3.1.6 - July 14, 2020
- CVE-2020-1108: .NET Core Denial of Service Vulnerability
- CVE-2020-1147: NET Core Remote Code Execution Vulnerability

* Mon Dec 16 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- new version (3.1.0) with rpmgs script
- .NET Core 3.1.0 - December 3, 2019

* Fri Nov 08 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.0.0-alt1.qa1
- Dropped hack for ld-linux path on aarch64.

* Sat Oct 05 2019 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version (3.0.0) with rpmgs script
- .NET Core 3.0.0 - September 23, 2019

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt1
- new version 2.1.9 (with rpmrb script)
- includes .NET Core 2.1.9, ASP.NET Core 2.1.9 and .NET Core SDK 2.1.505
- CVE-2019-0657: .NET Core NuGet Tampering Vulnerability

* Tue Dec 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- new version 2.1.6 (with rpmrb script)
- includes .NET Core 2.1.6, ASP.NET Core 2.1.6 and .NET Core SDK 2.1.500

* Fri Oct 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.5-alt1
- NMU: new version (2.1.5) (based on changes by lav@)
- includes .NET Core 2.1.5, ASP.NET Core 2.1.5 and .NET Core SDK 2.1.403

* Sat Sep 15 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- new version (2.1.4) with rpmgs script
- includes .NET Core 2.1.4, ASP.NET Core 2.1.4 and .NET Core SDK 2.1.402

* Mon Sep 03 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- new version (2.1.3) with rpmgs script
- includes .NET Core 2.1.3, ASP.NET Core 2.1.3 and .NET Core SDK 2.1.401

* Mon Feb 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version (2.0.5) with rpmgs script
- CVE-2018-0764, CVE-2018-0786

* Thu Nov 23 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version (2.0.3) with rpmgs script

* Sun Aug 27 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3
- new version (2.0.0) with rpmgs script

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview2
- enable autoreq for libs, shell
- fix buildreqs to correct generated requires

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview2
- add provides with .NET Core runtime/SDK versions

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview2
- .NET Core Runtime 2.0.0 Preview 2 build 25407-01
- .NET Core SDK 2.0.0 Preview 2 build 006497

* Thu May 11 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1.005977
- .NET Core Runtime 2.0.0 Preview 1 build 002111
- .NET Core SDK 2.0.0 Preview 1 build 005977

* Fri Apr 28 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version (1.1.1) with rpmgs script (SDK 1.0.3)

* Fri Apr 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial release for ALT Sisyphus
