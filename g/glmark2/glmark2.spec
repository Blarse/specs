%define flavors	x11-gl,drm-gl,x11-glesv2,drm-glesv2,wayland-gl,wayland-glesv2

Name:		glmark2
Version:	2021.12
Release:	alt4

Summary:	an OpenGL 2.0 and ES 2.0 benchmark
Url:		https://github.com/glmark2/glmark2
Group:		Graphics
License:	GPL-3.0-or-later

Vcs:		git://git.altlinux.org:/gears/g/glmark2.git
Source:		%name-%version-%release.tar

BuildRequires(pre): gcc-c++
BuildRequires:	/usr/bin/python3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libudev-devel

# GL support
BuildRequires:	libGL-devel
# GLESv2 support
BuildRequires:	libEGL-devel libglvnd-devel
# DRM support
BuildRequires:	libdrm-devel libgbm-devel
# Wayland support
BuildRequires:	libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel wayland-protocols

Requires:	%name-common

%package	es2
Summary:	an OpenGL 2.0 and ES 2.0 benchmark - ES 2.0 flavour
Group:		Graphics
Requires:	%name-common
Requires:	libGLES

%package	drm
Summary:	an OpenGL 2.0 and ES 2.0 benchmark - DRM flavor
Group:		Graphics
Requires:	%name-common

%package	es2-drm
Summary:	an OpenGL 2.0 and ES 2.0 benchmark - ES 2.0 DRM flavor
Group:		Graphics
Requires:	%name-common
Requires:	libGLES

%package	wayland
Summary:	an OpenGL 2.0 and ES 2.0 benchmark - Wayland flavor
Group:		Graphics
Requires:	%name-common

%package	es2-wayland
Summary:	an OpenGL 2.0 and ES 2.0 benchmark - ES 2.0 Wayland flavor
Group:		Graphics
Requires:	%name-common
Requires:	libGLES

%package	common
Summary:	Common graphical assets for an OpenGL 2.0 and ES 2.0 benchmark
Group:		Graphics
BuildArch:	noarch
Obsoletes:	%name-data < %version

%define common_descr \
glmark2 is an OpenGL 2.0 and ES 2.0 benchmark.\
\
glmark2 is developed by Alexandros Frantzis and Jesse Barker based on the\
original glmark benchmark by Ben Smith.


%description
%common_descr

%description	es2
%common_descr

This package contains ES 2.0 flavor.

%description	drm
%common_descr

This package contains DRM flavor.

%description	es2-drm
%common_descr

This package contains ES 2.0 DRM flavor.

%description	wayland
%common_descr

This package contains Wayland flavor.

%description	es2-wayland
%common_descr

This package contains ES 2.0 Wayland flavor.

%description	common
%common_descr

This package contains common graphical assets for OpenGL 2.0 and ES 2.0
benchmark.

%prep
%setup -n %name-%version-%release

%build
export CFLAGS="%optflags"
export CXXFLAGS="${CFLAGS}"
./waf configure \
	--with-flavors="%flavors" \
	--data-path=%_datadir/%name \
	--prefix=%prefix \
	#
./waf

%install
./waf install --destdir=%buildroot

%files
%_bindir/%name
%_man1dir/%name.1.*

%files es2
%_bindir/%name-es2
%_man1dir/%name-es2.1.*

%files drm
%_bindir/%name-drm
%_man1dir/%name-drm.1.*

%files es2-drm
%_bindir/%name-es2-drm
%_man1dir/%name-es2-drm.1.*

%files wayland
%_bindir/%name-wayland
%_man1dir/%name-wayland.1.*

%files es2-wayland
%_bindir/%name-es2-wayland
%_man1dir/%name-es2-wayland.1.*

%files common
%_datadir/%name

%changelog
* Sat Jun 10 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 2021.12-alt4
- Fixed python3.11 fallout

* Thu Mar 30 2023 Anton Midyukov <antohami@altlinux.org> 2021.12-alt3
- require libGLES for es2* subpackages (closes: #45706)

* Fri Jun 03 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 2021.12-alt2
- Fixed build failure with GCC 12

* Fri Apr 22 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 2021.12-alt1
- Updated to 2021.12 (closes: #42554)

* Tue Mar 30 2021 Alexey Sheplyakov <asheplyakov@altlinux.org> 2021.02-alt1
- Updated to 2021.02. Closes #39822

* Sun May 03 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2020.04-alt1.ed9ac85.1
- Updated to ed9ac857059f3b29fb4dd5ca3a2ec1256bdb0aae.
- Renamed glmark2-data to glmark2-common.

* Tue Nov 26 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.0.0.0.907.24a1139-alt2
- Fixed build dependency.

* Wed Nov 20 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.0.0.0.907.24a1139-alt1
- Updated to 0.0.0-907-g24a1139.
- Fixed license field.

* Mon Dec 12 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.0.0.0.834.f413c5b-alt1
- recent upstream commit
- added URL
- fixed CFLAGS and CXXFLAGS
- rebuilt against libpng15

* Fri Sep 09 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.0.0.0.833.gdc1b7fa-alt1
- Initial build.

