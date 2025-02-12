%global import_path github.com/minio/minio
%global commit b5984027386ec1e55c504d27f42ef40a189cdb55
%global shortcommit %(c=%{commit}; echo ${c:0:12})
%global tag RELEASE.2024-05-10T01-41-38Z
%define version 2024.05.10

%global _unpackaged_files_terminate_build 1

Name: minio
Version: %version
Release: alt1
Summary: Cloud Storage Server
Group: System/Servers
License: AGPL-3.0
Url: https://www.min.io/

Source: %name-%version.tar
Source2: %name.config
Source3: %name.sysconfig
Source4: %name.service

Patch: %name-%version.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.21

%description
MinIO is an object storage server released under Apache License v2.0.
It is compatible with Amazon S3 cloud storage service. It is best
suited for storing unstructured data such as photos, videos, log
files, backups and container / VM images. Size of an object can
range from a few KBs to a maximum of 5TiB.

%prep
%setup -q
%patch -p1


%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export TAG=%tag
export VERSION=${TAG#RELEASE.}
export COMMIT=%commit
export SCOMMIT=%shortcommit
export YEAR=2024
export prefix=%import_path/cmd

# setup flags like 'go run buildscripts/gen-ldflags.go' would do
export LDFLAGS="-X $prefix.Version=$VERSION -X $prefix.ReleaseTag=$TAG -X $prefix.CommitID=$COMMIT -X $prefix.ShortCommitID=$SCOMMIT  -X .$prefix.CopyrightYear=$YEAR"
export TAGS="kqueue"

sed -e "s|DEVELOPMENT.GOGET|$VERSION|g" -i cmd/build-constants.go

%golang_prepare
pushd $BUILDDIR/src/%import_path
%gobuild -tags kqueue -trimpath -o %name .
#CGO_ENABLED=0 %golang_build .
popd

%install
export BUILDDIR="$PWD/.gopath"
mkdir -p -- \
        %buildroot%_bindir \
        %buildroot%_unitdir \
        %buildroot%_sysconfdir/%name \
        %buildroot%_sharedstatedir/%name \
        %buildroot%_logdir/%name

cd .gopath/src/%import_path
install -p -m 755 %name %buildroot%_bindir/%name
install -D -p -m 0644 %SOURCE2 %buildroot%_sysconfdir/%name/config.json
install -D -p -m 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -D -p -m 0644 %SOURCE4 %buildroot%_unitdir/%name.service

%pre
groupadd -r -f _%name
useradd -r -g _%name -c "Minio" -d %_sharedstatedir/%name -s /dev/null -n _%name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md
%_bindir/minio
%dir %attr(750,root,_%name) %_sysconfdir/%name
%config(noreplace) %attr(640,_%name,_%name) %_sysconfdir/%name/config.json
%config(noreplace) %attr(640,root,_%name) %_sysconfdir/sysconfig/%name
%dir %attr(750,_%name,_%name) %_sharedstatedir/%name
%dir %attr(750,_%name,_%name) %_logdir/%name
%_unitdir/%name.service

%changelog
* Fri May 17 2024 Alexey Shabalin <shaba@altlinux.org> 2024.05.10-alt1
- Update to RELEASE.2024-05-10T01-41-38Z

* Sun Mar 03 2024 Alexey Shabalin <shaba@altlinux.org> 2024.02.26-alt1
- Update to RELEASE.2024-02-26T09-33-48Z

* Mon Oct 23 2023 Alexey Shabalin <shaba@altlinux.org> 2023.10.16-alt1
- Update to RELEASE.2023-10-16T04-13-43Z

* Fri Oct 06 2023 Alexey Shabalin <shaba@altlinux.org> 2023.09.30-alt1
- Update to RELEASE.2023-09-30T07-02-29Z

* Mon Jul 31 2023 Alexey Shabalin <shaba@altlinux.org> 2023.07.21-alt1
- Update to RELEASE.2023-07-21T21-12-44Z

* Sat May 27 2023 Alexey Shabalin <shaba@altlinux.org> 2023.05.18-alt1
- Update to RELEASE.2023-05-18T00-05-36Z

* Mon Mar 27 2023 Alexey Shabalin <shaba@altlinux.org> 2023.03.24-alt1
- Update to RELEASE.2023-03-24T21-41-23Z
  (FIxes: CVE-2023-25812, CVE-2023-27589, CVE-2023-28432, CVE-2023-28433, CVE-2023-28434)

* Wed Dec 21 2022 Alexey Shabalin <shaba@altlinux.org> 2022.12.07-alt1
- Update to RELEASE.2022-12-07T00-56-37Z
  (Fixes: CVE-2022-24842 CVE-2022-31028 CVE-2022-35919)

* Thu Feb 03 2022 Alexey Shabalin <shaba@altlinux.org> 2022.02.01-alt1
- Update to RELEASE.2022-02-01T18-00-14Z (Fixes: CVE-2021-43858)

* Thu Nov 11 2021 Alexey Shabalin <shaba@altlinux.org> 2021.11.09-alt1
- Update to RELEASE.2021-11-09T03-21-45Z (Fixes: CVE-2021-41137)

* Fri Jun 25 2021 Alexey Shabalin <shaba@altlinux.org> 2021.06.17-alt1
- Update to RELEASE.2021-06-17T00-10-46Z

* Sat Mar 27 2021 Alexey Shabalin <shaba@altlinux.org> 2021.03.26-alt1
- Update to RELEASE.2021-03-26T00-00-41Z (Fixes: CVE-2021-21362, CVE-2021-21390)

* Mon Feb 08 2021 Alexey Shabalin <shaba@altlinux.org> 2021.02.07-alt1
- Update to RELEASE.2021-02-07T01-31-02Z (Fixes: CVE-2021-21287)

* Sun Oct 25 2020 Alexey Shabalin <shaba@altlinux.org> 2020.10.18-alt1
- Update to RELEASE.2020-10-18T21-54-12Z

* Mon Aug 17 2020 Alexey Shabalin <shaba@altlinux.org> 2020.08.16-alt1
- Update to RELEASE.2020-08-16T18-39-38Z

* Sun Jun 28 2020 Alexey Shabalin <shaba@altlinux.org> 2020.06.22-alt1
- Update to RELEASE.2020-06-22T03-12-50Z

* Fri May 29 2020 Alexey Shabalin <shaba@altlinux.org> 2020.05.28-alt1
- Update to RELEASE.2020-05-28T23-29-21Z

* Wed Apr 29 2020 Alexey Shabalin <shaba@altlinux.org> 2020.04.28-alt1
- Update to RELEASE.2020-04-28T23-56-56Z (Fixes: CVE-2020-11012)

* Tue Apr 28 2020 Alexey Shabalin <shaba@altlinux.org> 2020.04.23-alt1
- Initial build.
