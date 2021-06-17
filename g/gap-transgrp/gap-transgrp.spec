%define repo transgrp

Name: gap-transgrp
Version: 2.0.2
Release: alt1
Summary: GAP: Transitive Groups Library
License: Artistic-2.0 AND GPL-2.0-only AND GPL-3.0-only
Group: Sciences/Mathematics
Url: http://www.math.colostate.edu/~hulpke/transgrp

Source: https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/transgrp%version.tar.bz2

BuildArch: noarch
BuildRequires: rpm-macros-gap
Requires: gap >= 4.9
Requires: gap-gapdoc >= 1.5

%description
The TransGrp package provides the library of transitive groups.

%prep
%setup -n transgrp

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo/
%gap_sitelib/%repo/*

%changelog
* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 2.0.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
