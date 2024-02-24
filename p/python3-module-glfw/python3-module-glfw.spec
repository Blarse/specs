%define pypi_name glfw

Name:    python3-module-%pypi_name
Version: 2.7.0
Release: alt1

Summary: Python bindings for GLFW
License: MIT
Group:   Development/Python3
URL:     https://github.com/FlorianRhiem/pyGLFW

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
BuildRequires: libglfw3-devel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
This module provides Python bindings for GLFW (on GitHub: glfw/glfw). It is a
ctypes wrapper which keeps very close to the original GLFW API.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Feb 24 2024 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- New version.

* Thu Jan 25 2024 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1
- New version.

* Sat Dec 16 2023 Andrey Cherepanov <cas@altlinux.org> 2.6.4-alt1
- New version.

* Tue Nov 21 2023 Andrey Cherepanov <cas@altlinux.org> 2.6.3-alt1
- New version.

* Sat Jul 01 2023 Andrey Cherepanov <cas@altlinux.org> 2.6.2-alt1
- New version.

* Mon Jun 26 2023 Andrey Cherepanov <cas@altlinux.org> 2.6.1-alt1
- New version.

* Sat Jun 24 2023 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- New version.

* Mon Apr 03 2023 Andrey Cherepanov <cas@altlinux.org> 2.5.9-alt1
- new version 2.5.9

* Thu Mar 16 2023 Andrey Cherepanov <cas@altlinux.org> 2.5.7-alt1
- New version.

* Wed Feb 08 2023 Andrey Cherepanov <cas@altlinux.org> 2.5.6-alt1
- New version.

* Mon Jan 09 2023 Andrey Cherepanov <cas@altlinux.org> 2.5.5-alt1
- Initial build for Sisyphus
