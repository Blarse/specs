%define repo utils

Name: gap-utils
Version: 0.72
Release: alt1
Summary: GAP: Utility functions in GAP
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/utils

Source: https://github.com/gap-packages/utils/releases/download/v%version/utils-%version.tar.gz
BuildPreReq: rpm-macros-gap
BuildRequires: xz

BuildArch: noarch
Requires: gap >= 4.8.8
Requires: gap-gapdoc >= 1.5.1
Requires: gap-polycyclic >= 2.11

%description
The Utils package provides a collection of utility functions gleaned
from many packages.

%prep
%setup -n utils-%version

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Tue May 24 2022 Leontiy Volodin <lvol@altlinux.org> 0.72-alt1
- New version.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 0.49-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
