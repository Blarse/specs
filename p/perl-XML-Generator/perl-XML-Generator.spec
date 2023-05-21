%define _unpackaged_files_terminate_build 1
%define dist XML-Generator
Name: perl-%dist
Version: 1.13
Release: alt1

Summary: Perl extension for generating XML 
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/T/TI/TIMLEGGE/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Tue Apr 20 2010
BuildRequires: perl-Tie-IxHash perl-XML-DOM perl-devel
BuildArch: noarch

%description
A module to help in generating XML documents.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/XML*

%changelog
* Sun May 21 2023 Igor Vlasenko <viy@altlinux.org> 1.13-alt1
- automated CPAN update

* Wed Apr 19 2023 Igor Vlasenko <viy@altlinux.org> 1.11-alt1
- automated CPAN update

* Wed Feb 23 2022 Igor Vlasenko <viy@altlinux.org> 1.09-alt1
- automated CPAN update

* Fri Feb 18 2022 Igor Vlasenko <viy@altlinux.org> 1.08-alt1
- automated CPAN update

* Wed Sep 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- 0.99 -> 1.03

* Sun Dec 12 2004 Andrey Brindeew <abr@altlinux.org> 0.99-alt2
- Updated BuildRequires list

* Sun Dec 12 2004 Andrey Brindeew <abr@altlinux.org> 0.99-alt1
- First build for ALT Linux

