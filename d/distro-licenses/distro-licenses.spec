%define _unpackaged_files_terminate_build 1

Name: distro-licenses
Version: 1.3
Release: alt1
License: CC0-1.0
Summary: Texts of various distribution licenses
Group: System/Base
BuildArch: noarch

Source: %name-%version.tar

%description
Texts of various distribution licenses

%prep
%setup -q

%build

%install
%makeinstall_std

%files
%dir %_datadir/%name
%_datadir/%name
%_bindir/*

%changelog
* Fri Aug 11 2023 Evgeny Sinelnikov <sin@altlinux.org> 1.3-alt1
- Initial ALT_Product_License Common default license for products:
 + ALT Workstation
 + ALT Workstation K
 + ALT Education
 + ALT Virtualization Server

* Thu Aug 10 2023 Evgeny Sinelnikov <sin@altlinux.org> 1.2-alt1
- Update distro licenses installation process.
- Update license for ALT Server distribution (ALT_Server_License).
- Initial licenses for ALT SP (ALT_SP_License) and Simply Linux
  (ALT_Simply_License) distributions.

* Sat May 13 2023 Evgeny Sinelnikov <sin@altlinux.org> 1.1-alt1
- Add distro-license-check utility with distbranch and target validation.

* Wed Apr 26 2023 Evgeny Sinelnikov <sin@altlinux.org> 1.0-alt1
- Initial release (Suggested by Igor Chudov <nir@altlinux.org>).

