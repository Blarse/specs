Name:     jsonnet
Version:  0.18.0
Release:  alt1

Summary:  Jsonnet - The data templating language
License:  Apache-2.0
Group:    Other
Url:      https://github.com/google/jsonnet

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar
Patch1:   fix-build-ppc64le.patch

BuildRequires: gcc-c++
BuildRequires: python3

%description
%summary

%package -n lib%name
Summary:  Jsonnet library
Group: System/Libraries

%description -n lib%name
%summary

%package -n lib%name-devel
Summary:  Jsonnet development files
Group: Development/Other

%description -n lib%name-devel
%summary

%prep
%setup
%patch1 -p1

%build
%make_build

%install
mkdir -p %buildroot%_bindir
cp -p %name %{name}fmt -t %buildroot%_bindir
mkdir -p %buildroot%_libdir
cp -dp libjsonnet*.so* %buildroot%_libdir
mkdir -p %buildroot%_includedir
cp -p include/libjsonnet*.h %buildroot%_includedir

%check
make test

%files -n lib%name-devel
%_includedir/*
%_libdir/lib%{name}*.so

%files -n lib%name
%_libdir/lib%{name}*.so.*

%files
%_bindir/*
%doc *.md doc examples

%changelog
* Wed Mar 02 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.18.0-alt1
- new version 0.18.0
- add lib packages

* Tue Dec 15 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Wed Oct 28 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Tue Mar 31 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Wed Jul 24 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.0-alt1
- Initial build for Sisyphus
