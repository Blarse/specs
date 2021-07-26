%define _unpackaged_files_terminate_build 1

%define soname 3

Name: biosig
Version: 2.3.1
Release: alt1
Summary: Reading and writing routines for different biosignal data formats
Group: Sciences/Medicine
License: GPL-3.0+
Url: http://biosig.sourceforge.net

Source: %name-%version.tar

Patch1: %name-alt-return-type.patch
Patch2: %name-alt-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel libnumpy-py3-devel
BuildRequires: gcc-c++
BuildRequires: libalsa-devel
BuildRequires: libb64-devel
BuildRequires: libsuitesparse-devel
BuildRequires: libdcmtk-devel
BuildRequires: zlib-devel
BuildRequires: tinyxml-devel

Requires: lib%name%soname = %EVR

%description
BioSig is an open source software library for biomedical signal processing,
featuring for example the analysis of biosignals such as
the electroencephalogram (EEG), electrocorticogram (ECoG),
electrocardiogram (ECG), electrooculogram (EOG), electromyogram (EMG),
respiration, and so on. Major application areas are: Neuroinformatics,
brain-computer interfaces, neurophysiology, psychology,
cardiovascular systems and sleep research. The aim of the BioSig project
is to foster research in biomedical signal processing by
providing open source software tools for many different applications.
Generally, many concerns have to be addressed in this scientific field.
BioSig handles this by providing solutions for data acquisition,
artifact processing, quality control, feature extraction, classification,
modeling, data visualization, and so on.

Everything in this project is freely available under the GNU General Public License.

%package -n lib%name%soname
Summary: Reading and writing routines for different biosignal data formats
Group: System/Libraries

%description -n lib%name%soname
BioSig is an open source software library for biomedical signal processing,
featuring for example the analysis of biosignals such as
the electroencephalogram (EEG), electrocorticogram (ECoG),
electrocardiogram (ECG), electrooculogram (EOG), electromyogram (EMG),
respiration, and so on. Major application areas are: Neuroinformatics,
brain-computer interfaces, neurophysiology, psychology,
cardiovascular systems and sleep research. The aim of the BioSig project
is to foster research in biomedical signal processing by
providing open source software tools for many different applications.
Generally, many concerns have to be addressed in this scientific field.
BioSig handles this by providing solutions for data acquisition,
artifact processing, quality control, feature extraction, classification,
modeling, data visualization, and so on.

Everything in this project is freely available under the GNU General Public License.

%package devel
Summary: Reading and writing routines for different biosignal data formats
Group: Development/C++
Requires: %name = %EVR
Requires: lib%name%soname = %EVR

%description devel
BioSig is an open source software library for biomedical signal processing,
featuring for example the analysis of biosignals such as
the electroencephalogram (EEG), electrocorticogram (ECoG),
electrocardiogram (ECG), electrooculogram (EOG), electromyogram (EMG),
respiration, and so on. Major application areas are: Neuroinformatics,
brain-computer interfaces, neurophysiology, psychology,
cardiovascular systems and sleep research. The aim of the BioSig project
is to foster research in biomedical signal processing by
providing open source software tools for many different applications.
Generally, many concerns have to be addressed in this scientific field.
BioSig handles this by providing solutions for data acquisition,
artifact processing, quality control, feature extraction, classification,
modeling, data visualization, and so on.

Everything in this project is freely available under the GNU General Public License.

%package -n python3-module-%name
Summary: Reading and writing routines for different biosignal data formats
Group: Development/Python3
Requires: lib%name%soname = %EVR

%description -n python3-module-%name
BioSig is an open source software library for biomedical signal processing,
featuring for example the analysis of biosignals such as
the electroencephalogram (EEG), electrocorticogram (ECoG),
electrocardiogram (ECG), electrooculogram (EOG), electromyogram (EMG),
respiration, and so on. Major application areas are: Neuroinformatics,
brain-computer interfaces, neurophysiology, psychology,
cardiovascular systems and sleep research. The aim of the BioSig project
is to foster research in biomedical signal processing by
providing open source software tools for many different applications.
Generally, many concerns have to be addressed in this scientific field.
BioSig handles this by providing solutions for data acquisition,
artifact processing, quality control, feature extraction, classification,
modeling, data visualization, and so on.

Everything in this project is freely available under the GNU General Public License.

%prep
%setup
%patch1 -p2
%patch2 -p2

# sigviewer isn't built here. don't install it's manpage either
rm -f biosig4c++/doc/sigviewer.1

# same
rm -f biosig4c++/doc/mexSLOAD.1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*.1*

%files -n lib%name%soname
%doc COPYING
%doc README CITATION
%_libdir/*.so.%{soname}

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/%name

%files -n python3-module-%name
%python3_sitelibdir/%{name}*.so
%python3_sitelibdir/Biosig-%version-py%{_python3_version}.egg-info

%changelog
* Mon Jul 26 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.1-alt1
- Initial build for ALT.
