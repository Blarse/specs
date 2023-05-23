%define alterator_libexecdir %_prefix/libexec/alterator

Name: alterator-manager
Version: 0.1.4
Release: alt1

Summary: Modular tool for system configuration via D-Bus
License: GPL-2
Group: System/Configuration/Other

BuildRequires: cmake gcc
BuildRequires: libgio-devel libsystemd-devel libpolkit-devel

Source: %name-%version.tar

%description
Modular tool for system configuration via D-Bus.

%package devel
Summary: Headers for developing alterator-manager modules
Group: Development/Other
Requires: libgio-devel

%description devel
Headers for developing alterator-manager modules.


%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std
mkdir -p %buildroot%alterator_libexecdir
mkdir -p %buildroot%_datadir/alterator/backends

%files
%_sbindir/%name
%_datadir/dbus-1/system.d/ru.basealt.alterator_manager.conf
%_unitdir/alterator-manager.service
%dir %alterator_libexecdir
%dir %_datadir/alterator/backends
%doc docs/*

%files devel
%_includedir/alterator

%changelog
* Mon May 22 2023 Ivan Savin <svn17@altlinux.org> 0.1.4-alt1
- Add checking of user rights to execute methods using polkit.
- Data from alterator-manager is now transferred not in a GHashTable,
  but in a structure ManagerData.
- Add check for the correctness of the interface name in a backend file.
- Add check for the correctness of the node name in a backend file.
- Add automatic addition of prefix 'ru.basealt.alterator.' to the interface
  name from a file.
- Update docs/README-ru.md.

* Fri Apr 21 2023 Ivan Savin <svn17@altlinux.org> 0.1.3-alt1
- Add thread_limit option to manager section in backend file.
- Update doc/README-ru.md.

* Tue Apr 11 2023 Ivan Savin <svn17@altlinux.org> 0.1.2-alt1
- Add the get_signals method to the ru.basealt.alterator.manager interface that
  returns a list of signal names (stdout/stderr). The arguments to this method
  are the interface name and the method name.

* Tue Apr 04 2023 Ivan Savin <svn17@altlinux.org> 0.1.1-alt2
- Add readme file (RU).

* Thu Mar 09 2023 Ivan Savin <svn17@altlinux.org> 0.1.1-alt1
- Add a default interface called manager into root.
- The manager contains a method get_objects that returns object paths by
  interface name.

* Thu Feb 16 2023 Ivan Savin <svn17@altlinux.org> 0.1.0-alt1
- All backend files are now loaded in the manager, and modules receive a
  pointer to a table with data that contains information about D-Bus objects
  and handlers. One file describes one interface for one module.
- g_dbus_connection_register_object replaced by
  g_dbus_connection_register_subtree.
- The interaction between the manager and modules has changed: the module now
  returns not xml, but an instance of GDBusInterfaceInfo (it writes a pointer
  to this instance to the table with data received from the manager, a
  pointer to the vtable is also written there).

* Sat Oct 22 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.0.3-alt1
- Improve errors treatment.
- Rename source files from plugin to modules in common style.
- Add support loading backends prototype with interfaces from
  alterator_manager_interface in modules.

* Thu Oct 13 2022 Ivan Savin <svn17@altlinux.org> 0.0.2-alt1
- Add devel.

* Fri Aug 19 2022 Ivan Savin <svn17@altlinux.org> 0.0.1-alt1
- Initial commit.

