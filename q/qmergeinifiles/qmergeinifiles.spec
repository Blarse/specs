
Name: qmergeinifiles
Version: 3.0.0
Release: alt1


Summary: Utility to merge INI-format files
Group: Development/Other
License: GPL

Source: %name-%version.tar


BuildRequires:make gcc-c++


%description
Utility to merge INI-format files


%prep

%setup -q

%build
%add_optflags %optflags_shared
%make_build CXXFLAGS="-pedantic %optflags"


%install
%makeinstall_std


%files
%_bindir/*

%changelog
* Thu Sep 14 2023 Daniil-Viktor Ratkin <krf10@altlinux.ru> 3.0.0-alt1
- remove Qt dependencies

* Fri Jul 05 2019 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt1
- fix to show usage info when debug output disabled

* Mon Jun 17 2019 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt2
- dont use ubt macro

* Wed Dec 20 2017 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1
- build with Qt5

* Fri Feb 10 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt0.M60P.1
- built for M60P

* Fri Feb 10 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt1
- new version

* Fri Oct 28 2011 Sergey V Turchin <zerg@altlinux.org> 1.91.0-alt0.M60P.1
- built for M60P

* Thu Oct 27 2011 Sergey V Turchin <zerg@altlinux.org> 1.91.0-alt1
- create General section only if exists according settings

* Wed Oct 26 2011 Sergey V Turchin <zerg@altlinux.org> 1.90.0-alt1
- rewrite to merge without recoding text

* Tue Jan 26 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- fix compile with new Qt

* Fri Nov 09 2007 Sergey V Turchin <zerg at altlinux dot org> 0.0.1-alt1
- initial specfile
