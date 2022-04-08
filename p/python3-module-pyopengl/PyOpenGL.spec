%define oname OpenGL
%define modulename python3-module-%oname

Name: python3-module-pyopengl
Version: 3.1.6
Release: alt1

Summary: Metapackage including python modules for OpenGL library

Group: Development/Python3
License: see license.txt
Url: http://pyopengl.sourceforge.net

# https://pypi.org/project/PyOpenGL
# https://pypi.org/project/PyOpenGL-accelerate
# https://github.com/mcfletch/pyopengl
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython
BuildRequires: libnumpy-py3-devel

%description
OpenGL bindings for Python including support for GL extensions,
GLU, WGL, GLUT, GLE, and Tk

%package -n %modulename
Summary: A Python module for interfacing with the OpenGL library
Group: Development/Python3
BuildArch: noarch
%add_python3_req_skip OpenGL.GLES3.OES
%add_python3_req_skip OpenGL.raw.DISABLED
%add_python3_req_skip OpenGL.raw.DISABLED._types
%add_python3_req_skip OpenGL.raw.GLSC2
%add_python3_req_skip OpenGL.raw.GLSC2._types

%description -n %modulename
OpenGL bindings for Python including support for GL extensions,
GLU, WGL, GLUT, GLE, and Tk

%package -n %modulename-tk
Summary: %oname Python3 Tk widget
Group: Development/Python3
Requires: %modulename = %EVR
%py3_requires tkinter
BuildArch: noarch

%description -n %modulename-tk
%oname Togl (Tk OpenGL widget) 1.6 support for Python3

%package -n %{modulename}_accelerate
Summary: Acceleration code for PyOpenGL
Group: Development/Python3

%description -n %{modulename}_accelerate
This set of C (Cython) extensions provides acceleration of common
operations for slow points in PyOpenGL 3.x.

%prep
%setup

find tests -type f -name '*.py' -exec \
	sed -i 's|#! %_bindir/env python|#!%_bindir/python3|' '{}' +

%build
%python3_build
pushd accelerate
%python3_build
popd

%install
%python3_install
pushd accelerate
%python3_install
popd

%check
# tests need available video device

%files -n %modulename
%python3_sitelibdir_noarch/%oname
%python3_sitelibdir_noarch/Py%{oname}-*.egg-info
%exclude %python3_sitelibdir_noarch/%oname/Tk

%files -n %modulename-tk
%python3_sitelibdir_noarch/%oname/Tk

%files -n %{modulename}_accelerate
%python3_sitelibdir/%{oname}_accelerate
%python3_sitelibdir/Py%{oname}_accelerate*.egg-info

%changelog
* Wed Mar 30 2022 Grigory Ustinov <grenka@altlinux.org> 3.1.6-alt1
- Build new version.
- Build OpenGL_accelerate from OpenGL git repo.

* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 3.1.5-alt3
- Drop python2 support.

* Thu Jul 22 2021 Stanislav Levin <slev@altlinux.org> 3.1.5-alt2
- Stopped shipping of tests for Python2.

* Tue Jan 14 2020 Fr. Br. George <george@altlinux.ru> 3.1.5-alt1
- Version up

* Sat Apr 20 2019 Anton Midyukov <antohami@altlinux.org> 3.1.1a1-alt2
- Fix build with python-3.7

* Sat Jan 27 2018 Anton Midyukov <antohami@altlinux.org> 3.1.1a1-alt1
- New version 3.1.1a1 (Closes: 34485)
- New subpackages python-module-tk and python3-module-tk

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt2
- Added requirement on 'OpenGL_accelerate'

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1
- Version 3.1.0
- Added module for Python 3

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt1
- Version 3.0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt1.1
- Rebuild with Python-2.7

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1
- Version 3.0.1
- Added tests subpackage

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt3.1
- Rebuilt with python 2.6

* Mon Feb 16 2009 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt3
- new version 3.0.0c1
- build package as noarch

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt2
- new version 3.0.0b8
- remove tests packing (fix bug #18378)

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version (3.0.0)
- cleanup spec, update buildreqs

* Sun Nov 13 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.2.01-alt2
- fix Source tag

* Tue Jul 19 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.2.01-alt1
- first build for ALT Linux Sisyphus
