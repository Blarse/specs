%set_gcc_version 12

Name: alacenc
Version: 0.3.0
Release: alt1.2

Summary: encode audio into the Apple Lossless Audio Codec (ALAC) format
License: MIT
Group: Sound

URL: https://github.com/flacon/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: %arm ppc64le

# https://github.com/flacon/%name/archive/v%version/%name-%version.tar.gz
Source: https://github.com/flacon/%name/archive/v%version/%name-%version.tar

BuildRequires: cmake
BuildRequires: gcc12-c++

%description
%name - encode audio into the Apple Lossless Audio Codec (ALAC) format

%prep
%setup
%ifarch %e2k
# should be named WhitelistedUnportable
sed -i "s/__aarch64__/__e2k__/" vendor/alac/codec/EndianPortable.c
%endif

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name

%changelog
* Sat Jul 01 2023 Nazarov Denis <nenderus@altlinux.org> 0.3.0-alt1.2
- Fix FTBFS

* Wed May 18 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.3.0-alt1.1
- Fixed build for Elbrus

* Mon May 16 2022 Nazarov Denis <nenderus@altlinux.org> 0.3.0-alt1
- Initial build for ALT Linux
