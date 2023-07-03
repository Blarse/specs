%define sover 1
%define libchromaprint libchromaprint%sover

Name: chromaprint
Version: 1.5.1
Release: alt1
Summary: Library implementing the AcoustID fingerprinting

Group: Sound
License: LGPLv2+
Url: http://www.acoustid.org/chromaprint
Source: %name-%version.tar

Patch1: chromaprint-1.1-alt-libav9.patch
Patch2: chromaprint-1.1-alt-libav10.patch

# Automatically added by buildreq on Mon May 21 2012 (-bi)
# optimized out: boost-devel cmake-modules elfutils libavcodec-devel libavutil-devel libopencore-amrnb0 libopencore-amrwb0 libstdc++-devel pkg-config python-base
#BuildRequires: boost-devel-headers cmake gcc-c++ libavdevice-devel libavformat-devel libfftw3-devel libswscale-devel libtag-devel
BuildRequires: boost-devel cmake gcc-c++ libfftw3-devel libtag-devel
BuildRequires: cmake rpm-build-kf5
#BuildRequires: libavdevice-devel libavformat-devel libswscale-devel


%description
Chromaprint library is the core component of the AcoustID project. It's a
client-side library that implements a custom algorithm for extracting
fingerprints from raw audio sources.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

%package -n %libchromaprint
Summary: Library implementing the AcoustID fingerprinting
Group: System/Libraries
#Obsoletes: python-chromaprint < 0.6-alt1
%description -n %libchromaprint
Chromaprint library is the core component of the AcoustID project. It's a
client-side library that implements a custom algorithm for extracting
fingerprints from raw audio sources.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

%package -n libchromaprint-devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %libchromaprint = %version-%release
%description -n libchromaprint-devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%prep
%setup
#%patch1 -p1
#%patch2 -p1

%build
%K5build \
    -DBUILD_TOOLS=OFF \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_TESTS=OFF

%install
%K5install

ls -1 %buildroot/%_libdir/lib*.so.* 2>/dev/null | \
while read p
do
	[ -z `readlink $p` ] || continue
	[ -f "$p" ] || continue
	l=`basename "$p"| sed 's|\.so\..*$|.so|'`
	f=`basename "$p"`
	shortname=`echo `
	ln -s "$f" "%buildroot/%_libdir/$l"
done
rm -rf %buildroot/%_K5link ||:

#mkdir -p %buildroot/%_bindir
#[ -x %buildroot/%_bindir/fpcollect ] || install -m 0755 BUILD*/tools/fpcollect  %buildroot/%_bindir/

#%files
#%_bindir/*

%files -n %libchromaprint
%doc NEWS.txt README.md
%_libdir/libchromaprint.so.%sover
%_libdir/libchromaprint.so.%sover.*

%files -n libchromaprint-devel
%_includedir/chromaprint.h
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc

%changelog
* Mon Jul 03 2023 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt1
- new version

* Wed Sep 29 2021 Sergey V Turchin <zerg@altlinux.org> 1.5.0-alt2
- build without ffmpeg

* Wed Jan 13 2021 Sergey V Turchin <zerg@altlinux.org> 1.5.0-alt1
- new version

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt2
- NMU: remove %%ubt from release

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 1.4.3-alt1
- new version

* Thu Aug 10 2017 Sergey V Turchin <zerg@altlinux.org> 1.4.2-alt1
- new version

* Mon Jun 05 2017 Sergey V Turchin <zerg@altlinux.org> 1.2-alt2
- rebuild with ffmpeg

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1
- new version

* Wed May 20 2015 Sergey V Turchin <zerg@altlinux.org> 1.1-alt3
- rebuilt with gcc5

* Wed May 28 2014 Sergey V Turchin <zerg@altlinux.org> 1.1-alt2
- rebuilt with new libav

* Wed Jan 15 2014 Sergey V Turchin <zerg@altlinux.org> 1.1-alt0.M70P.1
- built for M70P

* Wed Jan 15 2014 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- new version

* Thu Sep 26 2013 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- new version
- fix build with new libav; thanks sbloshakov@alt

* Mon May 21 2012 Sergey V Turchin <zerg@altlinux.org> 0.6-alt0.M60P.2
- build for M60P

* Mon May 21 2012 Sergey V Turchin <zerg@altlinux.org> 0.6-alt1
- initial build
