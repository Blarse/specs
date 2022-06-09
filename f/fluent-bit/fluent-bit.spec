%def_disable tests

Name: fluent-bit
Version: 1.9.4
Release: alt1
Summary: Fast data collector for Linux
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and MIT
Group: Monitoring
Url: https://github.com/fluent/fluent-bit

Source: https://github.com/fluent/%name/archive/v%version/%name-%version.tar.gz
# Remove -Werror in mbedtls build. Not upstream
Patch: 0001-mbedtls-disable-Werror-in-prod-build.patch
# Fix up some install paths in CMake. Not upstream
Patch1: 0002-CMake-fix-up-install-paths.patch
# Add -fPIC to onigomo build. Not upstream
Patch2: 0003-onigmo-add-fPIC-to-CFLAGS.patch

%if_enabled tests
BuildRequires: ctest
%endif
# libudev-devel BR is needed for systemd input plugin
BuildRequires: libudev-devel
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: flex
BuildRequires: bison
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: postgresql-devel
BuildRequires: zlib-devel
BuildRequires: libgnutls-devel
BuildRequires: libssl-devel
BuildRequires: libsasl2-devel

# Exclude armv7hl temporarily because of failing runtime tests
# https://github.com/fluent/fluent-bit/issues/4395
# ExcludeArch: ppc64le

%description
Fluent Bit is a high performance and multi-platform log forwarder.

%prep
%setup
%patch -p1
%patch1 -p1
#patch2 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DFLB_EXAMPLES=Off \
    -DFLB_OUT_SLACK=Off \
    -DFLB_IN_SYSTEMD=On \
    -DFLB_OUT_TD=Off \
    -DFLB_OUT_ES=Off \
    -DFLB_OUT_KAFKA=On \
    -DFLB_SHARED_LIB=On \
    -DFLB_TESTS_RUNTIME=On \
    -DFLB_TESTS_INTERNAL=Off \
    -DFLB_RELEASE=On \
    -DFLB_DEBUG=Off \
    -DFLB_TLS=On \
    -DFLB_LUAJIT=Off \
    -DFLB_FILTER_LUA=Off \
    -DFLB_HTTP_SERVER=On \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
# We don't ship headers and shared library for plugins (yet)
rm -rvf %buildroot%_includedir

%if_enabled tests
%check
cd %_target_alias
ctest
%endif

%post
%post_service %name.service

%preun
%preun_service %name.service

%files
%doc LICENSE README.md MAINTAINERS.md CODE_OF_CONDUCT.md CONTRIBUTING.md GOLANG_OUTPUT_PLUGIN.md GOVERNANCE.md
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*.conf
%_bindir/%name
%_unitdir/%name.service
%_libdir/lib%name.so

%changelog
* Thu Jun 09 2022 Leontiy Volodin <lvol@altlinux.org> 1.9.4-alt1
- New version.
- Disabled luajit and filter_lua support (ALT #42618).

* Thu Mar 03 2022 Nikolay Burykin <bne@altlinux.org> 1.8.12-alt2
- Add build option -DFLB_OUT_KAFKA=On

* Tue Feb 15 2022 Leontiy Volodin <lvol@altlinux.org> 1.8.12-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
