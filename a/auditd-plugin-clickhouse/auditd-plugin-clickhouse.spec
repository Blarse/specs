%define _unpackaged_files_terminate_build 1

# Recommended versioning scheme for this package:
# 1. If no sources are changed, just increase release.
# 2. If sources are changed, use current date as version in format YYYYMMDD.DBNUM,
#    and increase release for all subsequent versions made on same day.
# 3. DBNUM is incremented for each release with database format is changed:
#    fields are added, removed or their types are changed.

Name:    auditd-plugin-clickhouse
Version: 20221004.1.4
Release: alt1
Summary: Plugin for Auditd daemon for sending data into Clickhouse database
Group:   Monitoring
License: GPLv3+

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: boost-complete
BuildRequires: libclickhouse-cpp-devel
BuildRequires: libaudit-devel
BuildRequires: /usr/bin/ctest libgtest-devel

# audit 3.0 moved to new config location
Requires: audit >= 3.0-alt1

%description
Plugin for Auditd daemon for sending data into Clickhouse database

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

mkdir -pv %buildroot%_localstatedir/auditd-plugin-clickhouse

%check
pushd %_cmake__builddir
ctest
popd

%files
%config(noreplace) %_sysconfdir/audit/auditd-clickhouse-datatypes.json
%config(noreplace) %attr(600,root,root) %_sysconfdir/audit/auditd-clickhouse.conf
%config(noreplace) %_sysconfdir/audit/plugins.d/auditd-plugin-clickhouse.conf
%config(noreplace) %_sysconfdir/logrotate.d/auditd-plugin-clickhouse-logrotate.conf
%_prefix/libexec/auditd-plugin-clickhouse
%attr(700,root,root) %_localstatedir/auditd-plugin-clickhouse

%changelog
* Tue Oct 18 2022 Paul Wolneykien <manowar@altlinux.org> 20221004.1.4-alt1
- Sort array values prior to generate JSON.
- Fixed split value processing: don't skip the first part.
- Don't log reading of each saved record.
- Protect the main loop: skip records on exceptions.
- Throw a custom exception on string decode error.
- Added "istring" type for non-encoded string fields.
- Fixed an inopportune and harmful flush of audit data!
- Check and throw error on incomplete split records.
- Fixed sorting of array values.
- Fixed DB table creation (added the missing "type" field).
- Added database test (should be run manually).

* Thu Oct 06 2022 Paul Wolneykien <manowar@altlinux.org> 20221004.1.3-alt1
- Fixed "none" type handling in table structure and migration code.

* Wed Oct 05 2022 Paul Wolneykien <manowar@altlinux.org> 20221004.1.2-alt1
- Fixed datatypes for unknown fields and automatic migration.
- Added "interp_array" datatype.

* Tue Oct 04 2022 Paul Wolneykien <manowar@altlinux.org> 20221004.1.1-alt1
- Skip "aN_len" fields.
- Add datatype "none" to explicitly skip fields.
- Added a special array type for SYSCALL/EXECVE argument values.
- Added the log file unit-test.
- Accumulate split EXECVE records to produce one complete record.
- Make the "type" field be a selected property field.
- Use encoded strings instead of interpreted for datatype "string".

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 20210217.4.1-alt2
- NMU: spec: adapted to new cmake macros.

* Wed Feb 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 20210217.4.1-alt1
- Updated config file locations for audit-3.0 compatibility.

* Fri Sep 25 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20200911.4.1-alt2
- Updated supported architectures.

* Fri Sep 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20200911.4.1-alt1
- Reintroduced logging unknown fields, controlled by configuration and disabled by default.

* Fri Sep 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20200911.4-alt1
- Disabled logging unknown fields. Monitoring of "unknown_field" column
  might be required to detect new fields.
- Added new fields.
- Implemented experimental automatic migration to new table. It's disabled by default.
- Updated config file permissions.

* Mon Jun 29 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20200207.3-alt2
- Updated supported architectures.

* Fri Feb 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20200207.3-alt1
- Logged and ignored potential exceptions when saving data to temporary storage.

* Thu Jan 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20200130.3-alt1
- Optimized memory consumption.
- Added new field to database.
- Minor logging improvements.

* Mon Jan 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20200127-alt1
- Fixed excessive logging of writes.
- Fixed memory consumption by logging entries if logging is disabled.
- Fixed memory leak in audit data parsing.
- Fixed issue when some data may be not attempted to be written to DB
  when separate writer thread is used.
- Improved performance by reducing data copying.
- Input data buffer size configuration is removed.

* Thu Jan 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20200116-alt1
- New fields added to database table.
- All unknown fields encountered are saved into database.
- Fixed crash when processing NULL strings.
- Fixed warnings for some audit data types.
- Implemented logging.
- Implemented audit data serialization and temporary storing before sending
  to database.

* Tue Dec 17 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20191217-alt1
- Initial build for ALT
