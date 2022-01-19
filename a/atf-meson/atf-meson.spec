Name: atf-meson
Version: 2.6
Release: alt1

Summary: ARM Trusted Firmware
License: BSD
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

%description
ARM Trusted Firmware provides a reference implementation of secure world
software for ARMv8-A, including Exception Level 3 (EL3) software.
This release provides initial support for the AMLogic AXG, GXBB, GXL and
G12A SoC families.

%prep
%setup

%build
for plat in axg gxbb gxl g12a; do
	make PLAT=$plat bl31
	install -pm0644 -D build/$plat/release/bl31.bin out/$plat/bl31.bin
	make distclean
done

%install
mkdir -p %buildroot%_datadir/atf
cp -a out/* %buildroot%_datadir/atf/

%files
%_datadir/atf/*

%changelog
* Wed Jan 19 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6-alt1
- 2.6 released

* Thu Jun 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5-alt1
- 2.5 released

* Tue Jan 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4-alt1
- 2.4 released

* Thu Jul 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3-alt1
- initial
