Name: python3-module-turbojpeg
Version: 1.6.1
Release: alt1

Summary: A Python wrapper of libjpeg-turbo for decoding and encoding JPEG image.
License: MIT
Group: Development/Python
Url: https://pypi.org/project/PyTurboJPEG/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/turbojpeg.*
%python3_sitelibdir/*/turbojpeg.*
%python3_sitelibdir/PyTurboJPEG-%version-*-info

%changelog
* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.1-alt1
- initial
