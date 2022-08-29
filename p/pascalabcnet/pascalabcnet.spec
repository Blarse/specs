Name:    pascalabcnet
Version: 3.8.3.3159
Release: alt1

Summary: PascalABC.NET programming language  
License: LGPL-3.0
Group:   Development/Other
Url:     http://pascalabc.net/
# VCS: https://github.com/pascalabcnet/pascalabcnet

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

ExcludeArch: ppc64le

BuildRequires(pre): rpm-build-mono
BuildRequires: mono-devel
BuildRequires: mono-locale-extras

Requires: mono-devel
Requires: mono-locale-extras

%filter_from_requires /mono(\(PresentationCore\|PresentationFramework\))/d

%description
PascalABC.NET is a Pascal programming language that implements classic Pascal,
most Delphi language features, as well as a number of their own extensions. It
is implemented on the .NET Framework platform and contains all the modern
language features: classes, operator overloading, interfaces, exception
handling, generic classes and routines, garbage collection, lambda expressions,
parallel programming tools.

%prep
%setup
# Use xbuild insead of msbuild
subst 's/msbuild/xbuild/;/^if/,$d' _RebuildReleaseAndRunTests.sh
# Remove proprietary part
rm -rf bin/PT4
# Remove all binaries
find . -name \*.exe -delete
# TODO remove bundled libraries
#find . -name \*.dll -delete

%build
# Build compiler
sh -x _RebuildReleaseAndRunTests.sh
# Build Linux graphical library GraphABCLinux
mono bin/pabcnetcclear.exe ./bin/Lib/GraphABCLinux.pas
# Build IDE
#MONO_IOMAP=case xbuild /p:Configuration=release PascalABCNET.sln

%install
mkdir -p %buildroot%_libexecdir/%name
cp -a bin/* %buildroot%_libexecdir/%name
mkdir -p %buildroot%_bindir
# Executable wrappers
cat > %buildroot%_bindir/pabcnetc << ENDF
#!/bin/bash
export MONO_IOMAP=all
mono %_libexecdir/pascalabcnet/pabcnetc.exe \$@
ENDF
chmod +x %buildroot%_bindir/pabcnetc
cat > %buildroot%_bindir/pabcnetcclear << ENDF
#!/bin/bash
export MONO_IOMAP=all
mono %_libexecdir/pascalabcnet/pabcnetcclear.exe \$@
ENDF
chmod +x %buildroot%_bindir/pabcnetcclear

%files
%doc README.md InstallerSamples
%_bindir/*
%_libexecdir/%name

%changelog
* Mon Aug 29 2022 Andrey Cherepanov <cas@altlinux.org> 3.8.3.3159-alt1
- New version.
- Built graphical library GraphABCLinux.
- Moved binaries and libraries to %_libexecdir/%name.
- Packaged examples.

* Thu Nov 25 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.0.2964-alt2
- Requires mono-devel for compilation.

* Sat Aug 21 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.0.2964-alt1
- New version.
- Runtime requires mono-locale-extras.
- Patches were applied by upstream.

* Sat Aug 07 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.0.2951-alt3
- Do not use black background to compiler banner (#211).
- Remove tests run during build process.

* Fri Aug 06 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.0.2951-alt2
- Use rpm-build-mono.

* Fri Aug 06 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.0.2951-alt1
- Initial build in Sisyphus.
