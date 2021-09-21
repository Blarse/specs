
%global commit 943005aa9d9d03a68cffb59a8e392ee5f784c832
%global gitversion %(c=%{commit}; echo ${c:0:7})

%define oneadmin_home /var/lib/one
%define oneadmin_uid 9869
%define oneadmin_gid 9869

%add_findreq_skiplist /var/lib/one/*

# from firecracker.spec
%ifarch x86_64 aarch64
%def_with firecracker
%endif

Name: opennebula
Summary: Cloud computing solution for Data Center Virtualization
Version: 5.12.0.4
Release: alt3
License: Apache-2.0
Group: System/Servers
Url: https://opennebula.io

Source0: %name-%version.tar
Source1: lxd-init.sh

BuildRequires(pre): rpm-build-ruby rpm-build-python3 rpm-macros-nodejs
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel libxmlrpc-devel liblzma-devel
BuildRequires: libssl-devel
BuildRequires: libmysqlclient-devel
BuildRequires: postgresql-devel
BuildRequires: libvncserver-devel
BuildRequires: libsqlite3-devel
BuildRequires: libsystemd-devel
BuildRequires: libnsl2-devel
BuildRequires: openssh
BuildRequires: gem(aws-sdk) gem(bundler)
BuildRequires: gem(ipaddress)
BuildRequires: gem(builder)
BuildRequires: gem-nokogiri
BuildRequires: scons
BuildRequires: python3-module-setuptools
BuildRequires: java-1.8.0-openjdk-devel ws-commons-util xmlrpc-common xmlrpc-client
BuildRequires: zlib-devel
BuildRequires: node node-gyp npm node-devel node-sass libsass
BuildRequires: ronn
BuildRequires: groff-base

%ruby_use_gem_dependency faraday_middleware >= 0,faraday_middleware < 2
%ruby_use_gem_dependency faraday >= 0,faraday < 2
%ruby_use_gem_dependency rbvmomi >= 2,rbvmomi < 3
%ruby_use_gem_dependency highline >= 2.0,highline < 3
%ruby_use_gem_dependency i18n >= 1.0,i18n < 2
%ruby_use_gem_dependency activesupport >= 6.0,faraday < 7
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
OpenNebula.org is an open-source project aimed at building the industry
standard open source cloud computing tool to manage the complexity and
heterogeneity of distributed data center infrastructures.

The OpenNebula.org Project is maintained and driven by the community. The
OpenNebula.org community has thousands of users, contributors, and supporters,
who interact through various online email lists, blogs and innovative projects
to support each other.

OpenNebula is free software released under the Apache License.

%package server
Summary: OpenNebula Server and Scheduler
Group: System/Servers
Requires: openssh-server
Requires: genisoimage
Requires: qemu-img
Requires: xmlrpc-c
Requires: nfs-utils
Requires: wget
Requires: curl
Requires: rsync
Requires: iputils
Requires: sqlite3
Requires: %name-common = %EVR
Requires: gem-%name-cli = %EVR
Obsoletes: %name-addon-markets
Obsoletes: %name-ozones
#TODO: Requires http://rubygems.org/gems/net-ldap

%description server
OpenNebula Server and Scheduler daemons.

%package common
Summary: Common OpenNebula package shared by various components
Group: System/Servers
BuildArch: noarch

%description common
Common package shared by various OpenNebula components.

%package -n gem-%name
Summary: OpenNebula Ruby libraries
Group: Development/Ruby
BuildArch: noarch
Provides: %name-ruby = %EVR ruby-%name = %EVR
Obsoletes: %name-ruby < %EVR ruby-%name < %EVR

%description -n gem-%name
OpenNebula Ruby libraries.

%package -n gem-%name-cli
Summary: OpenNebula command line tools
Group: Development/Ruby
BuildArch: noarch
Requires: gem-%name = %EVR
Requires: ruby
Requires: openssl
Requires: openssh-clients

Provides: %name-ruby = %EVR ruby-%name-cli = %EVR %name-tools = %EVR
Obsoletes: %name-ruby < %EVR ruby-%name-cli < %EVR %name-tools < %EVR

%description -n gem-%name-cli
Ruby CLI for OpenNebula.

# curb       => For EC2 and OCCI uploads (OPTIONAL: falls back to multipart)

# Missing gems
# aws-sdk    => EC2 hybrid driver (EPEL)
# mysql      => Required to handle MySQL DB upgrades (EPEL)
# treetop    => OneFlow (EPEL)

# amazon-ec2 => used for ec2 server (expose OpenNebula with an EC2 interface)
# net-ldap   => Ldap authentication
# parse-cron => OneFlow

%package -n python3-module-%name
Summary: Python 3 bindings for OpenNebula Cloud API, OCA
Group: Development/Python3
BuildArch: noarch
Provides: python3-module-pyone = %EVR

%description -n python3-module-%name
Python 3 bindings for OpenNebula Cloud API (OCA).

%package sunstone
Summary: OpenNebula web interface Sunstone
Group: System/Servers
BuildArch: noarch

Requires: %name-common = %EVR
Requires: gem-%name = %EVR
Requires: python3-module-numpy

%description sunstone
Browser based UI for OpenNebula cloud management and usage.

%package gate
Summary: OpenNebula Gate server 
Group: System/Servers
BuildArch: noarch

Requires: %name-common = %EVR
Requires: gem-%name = %EVR

%description gate
Server for information exchange between Virtual Machines and OpenNebula.

%package flow
Summary: OpenNebula Flow server
Group: System/Servers
BuildArch: noarch

Requires: %name-common = %EVR
Requires: gem-%name = %EVR
Requires: %name-sunstone = %EVR

%description flow
Server for multi-VM orchestration.

%package -n docker-machine-opennebula
Summary: OpenNebula driver for Docker Machine
Group: Development/Other

%description -n docker-machine-opennebula
OpenNebula driver for the Docker Machine (note: Docker Machine needs
to be installed separately).

%package java
Summary: Java bindings for OpenNebula Cloud API, OCA
Group: Development/Java
BuildArch: noarch
Requires: ws-commons-util
Requires: xmlrpc-common
Requires: xmlrpc-client

%description java
Java interface to OpenNebula Cloud API.

%package node-kvm
Summary: Services for OpenNebula KVM node
Group: System/Servers
BuildArch: noarch

Conflicts: %name-node-xen
#Requires: ruby ruby-stdlibs
Requires: %name-common = %EVR
Requires: openssh-server
Requires: openssh-clients
Requires: libvirt-kvm libvirt-client polkit
Requires: qemu-kvm
Requires: qemu-img
Requires: nfs-utils
Requires: ipset
Requires: pciutils
Requires: augeas
Requires: rsync

%description node-kvm
Services and configurations for OpenNebula KVM node.

%package node-firecracker
Summary: Services for OpenNebula Firecracker node
Group: System/Servers

Conflicts: %name-node-xen
Requires: %name-common = %EVR
Requires: firecracker
Requires: openssh-server
Requires: openssh-clients
Requires: rsync
Requires: nfs-utils
Requires: ipset
Requires: screen
Requires: bsdtar
Requires: e2fsprogs
Requires: lsof
Requires: qemu-img

%description node-firecracker
Services and configurations for OpenNebula Firecracker node.

# %package node-xen
# Summary: Configures an OpenNebula node providing xen
# Group: System/Servers
# BuildArch: noarch
# Conflicts: %name-node-kvm
# Requires: centos-release-xen
# Requires: ruby
# Requires: openssh-server
# Requires: openssh-clients
# Requires: xen
# Requires: nfs-utils
# Requires: bridge-utils
# Requires: %name-common = %version
#
# %description node-xen
# Configures an OpenNebula node providing xen.

%package node-lxd
Summary: Configures an OpenNebula node providing lxd
Group: System/Servers

#Requires: ruby ruby-stdlibs
Requires: %name-common = %EVR
Requires: %name-node-kvm = %EVR
Requires: libvirt-lxc lxcfs
Requires: kpartx
Requires: lxd3.0 >= 3.0
Conflicts: lxd >= 3.1.0
%ifarch aarch64 ppc64 ppc64le x86_64
Requires: rbd-nbd
%endif
Requires: systemd-settings-disable-kill-user-processes

%description node-lxd
Configures an OpenNebula node providing lxd.

%package provision
Summary: OpenNebula infrastructure provisioning
Group: System/Servers
BuildArch: noarch
Requires: %name-common = %EVR
Requires: %name-server = %EVR

%description provision
OpenNebula provisioning tool

%prep
%setup

ln -sf %nodejs_sitelib/node-gyp src/sunstone/public/node_modules/node-gyp
ln -sf %nodejs_sitelib/node-sass src/sunstone/public/node_modules/node-sass

%build
export PATH="$PATH:$PWD/src/sunstone/public/node_modules/.bin"

pushd src/sunstone/public
npm rebuild

# from ./build.sh
bower -o install
grunt --gruntfile ./Gruntfile.js sass
grunt --gruntfile ./Gruntfile.js requirejs
mv -f dist/main.js dist/main-dist.js
popd

# Compile OpenNebula
scons -j2 \
	mysql=yes \
	postgresql=yes \
	new_xmlrpc=yes \
	sunstone=no \
	systemd=yes \
	rubygems=yes \
	gitversion="%{gitversion}" \
	enterprise=no


%ruby_build \
	--ignore-names=packethost \
	--use=install_gems --alias=opennebula-common --join=lib:bin \
	--use=flow --alias=opennebula-flow --join=lib:bin \
	--srclibdir= --srcconfdir= # --use=opennebula-cli --join=lib:bin

# build man pages
pushd share/man
	./build.sh
popd

pushd src/oca/java
	./build.sh -d
popd


%install
export DESTDIR=%buildroot
./install.sh -p
touch %buildroot%oneadmin_home/sunstone/main.js
rm -f %buildroot%_libexecdir/one/sunstone/public/dist/main.js
ln -r -s %buildroot%oneadmin_home/sunstone/main.js %buildroot%_libexecdir/one/sunstone/public/dist/main.js

%ruby_install

# delete duplicated with gems files
## opennebula
rm -rf %buildroot%_libexecdir/one/ruby/opennebula
rm -f  %buildroot%_libexecdir/one/ruby/ActionManager.rb
rm -f  %buildroot%_libexecdir/one/ruby/CommandManager.rb
rm -f  %buildroot%_libexecdir/one/ruby/DriverExecHelper.rb
rm -f  %buildroot%_libexecdir/one/ruby/OpenNebulaDriver.rb
rm -f  %buildroot%_libexecdir/one/ruby/VirtualMachineDriver.rb
rm -f  %buildroot%_libexecdir/one/ruby/opennebula.rb
rm -f  %buildroot%_libexecdir/one/ruby/vcenter_driver.rb
rm -f  %buildroot%_libexecdir/one/ruby/cloud/CloudClient.rb

## oennebula-cli
rm -rf  %buildroot%_libexecdir/one/ruby/cli

# delete docs
rm -rf %buildroot%_libexecdir/ruby/gems/*/doc
rm -rf %buildroot%_datadir/doc/one

# systemd units
install -p -D -m 644 share/pkgs/ALT/opennebula.service %buildroot%_unitdir/opennebula.service
install -p -D -m 644 share/pkgs/ALT/opennebula-ssh-agent.service %buildroot%_unitdir/opennebula-ssh-agent.service
install -p -D -m 644 share/pkgs/ALT/opennebula-ssh-socks-cleaner.service %buildroot%_unitdir/opennebula-ssh-socks-cleaner.service
install -p -D -m 644 share/pkgs/ALT/opennebula-ssh-socks-cleaner.timer %buildroot%_unitdir/opennebula-ssh-socks-cleaner.timer
install -p -D -m 644 share/pkgs/ALT/opennebula-showback.service %buildroot%_unitdir/opennebula-showback.service
install -p -D -m 644 share/pkgs/ALT/opennebula-showback.timer %buildroot%_unitdir/opennebula-showback.timer
install -p -D -m 644 share/pkgs/ALT/opennebula-econe.service %buildroot%_unitdir/opennebula-econe.service
install -p -D -m 644 share/pkgs/ALT/opennebula-flow.service  %buildroot%_unitdir/opennebula-flow.service
install -p -D -m 644 share/pkgs/ALT/opennebula-gate.service  %buildroot%_unitdir/opennebula-gate.service
install -p -D -m 644 share/pkgs/ALT/opennebula-hem.service  %buildroot%_unitdir/opennebula-hem.service
install -p -D -m 644 share/pkgs/ALT/opennebula-novnc.service %buildroot%_unitdir/opennebula-novnc.service
install -p -D -m 644 share/pkgs/ALT/opennebula-scheduler.service %buildroot%_unitdir/opennebula-scheduler.service
install -p -D -m 644 share/pkgs/ALT/opennebula-sunstone.service %buildroot%_unitdir/opennebula-sunstone.service

install -p -D -m 644 share/pkgs/tmpfiles/opennebula.conf %buildroot%_tmpfilesdir/opennebula.conf
install -p -D -m 644 share/pkgs/tmpfiles/opennebula-node.conf %buildroot%_tmpfilesdir/opennebula-node.conf

install -p -D -m 644 share/pkgs/ALT/opennebula-polkit.rules %buildroot%_sysconfdir/polkit-1/rules.d/50-opennebula.rules

# sudoers
mkdir -p %buildroot%_sysconfdir/sudoers.d
install -p -D -m 400 share/pkgs/sudoers/alt/opennebula %buildroot%_sysconfdir/sudoers.d/opennebula
install -p -D -m 400 share/pkgs/sudoers/opennebula-server %buildroot%_sysconfdir/sudoers.d/opennebula-server
install -p -D -m 400 share/pkgs/sudoers/opennebula-node %buildroot%_sysconfdir/sudoers.d/opennebula-node
install -p -D -m 400 share/pkgs/sudoers/opennebula-node-lxd %buildroot%_sysconfdir/sudoers.d/opennebula-node-lxd
%if_with firecracker
install -p -D -m 400 share/pkgs/sudoers/opennebula-node-firecracker %buildroot%_sysconfdir/sudoers.d/opennebula-node-firecracker
%endif

# logrotate
mkdir -p %buildroot%_logrotatedir
install -p -D -m 644 share/pkgs/ALT/opennebula.logrotate %buildroot%_logrotatedir/opennebula

# Shell completion
install -p -D -m 644 share/shell/bash_completion %buildroot%_datadir/bash-completion/completions/one

# Java
install -p -D -m 644 src/oca/java/jar/org.opennebula.client.jar %buildroot%_javadir/org.opennebula.client.jar

# sysctl
install -p -D -m 644 share/etc/sysctl.d/bridge-nf-call.conf %buildroot%_sysconfdir/sysctl.d/bridge-nf-call.conf

# node-lxd
install -p -D -m 755 src/svncterm_server/svncterm_server %buildroot%_bindir/svncterm_server
install -p -D -m 755 src/vmm_mad/remotes/lib/lxd/catfstab %buildroot%_bindir/catfstab
install -p -D -m 644 share/pkgs/ALT/opennebula-lxd.modprobe %buildroot%_sysconfdir/modprobe.d/opennebula-lxd.conf
install -p -D -m 644 share/pkgs/ALT/opennebula-lxd.modules %buildroot%_sysconfdir/modules-load.d/opennebula-lxd.conf
install -p -D -m 755 %SOURCE1 %buildroot%_sysconfdir/firsttime.d/opennebula-lxd-init

# node-firecracker
%if_with firecracker
#install -p -D -m 755 src/svncterm_server/svncterm_server %buildroot%_bindir/svncterm_server
install -p -D -m 755 src/vmm_mad/remotes/lib/firecracker/one-clean-firecracker-domain %buildroot%_sbindir/one-clean-firecracker-domain
install -p -D -m 755 src/vmm_mad/remotes/lib/firecracker/one-prepare-firecracker-domain %buildroot%_sbindir/one-prepare-firecracker-domain
%endif

# cleanup
rm -f %buildroot%_datadir/one/Gemfile
rm -f %buildroot%_datadir/one/install_gems
rm -rf %buildroot%_libexecdir/install_gems
rm -rf %buildroot%_libexecdir/one/ruby/vendors
rm -f %buildroot%_sbindir/install-firecracker

# fix placement
mv %buildroot%_libexecdir/flow %buildroot%_datadir/flow

# Python
pushd src/oca/python
PYTHON=%__python3 make install3 ROOT=%buildroot
popd

%pre common
groupadd -r -f -g %oneadmin_gid oneadmin 2>/dev/null ||:
useradd -r -M -g oneadmin -G disk,wheel -c 'Opennebula Daemon User' \
        -s /bin/bash -d %oneadmin_home \
	-u %oneadmin_uid -g %oneadmin_gid \
	oneadmin 2>/dev/null ||:

%post common
if [ $1 = 1 ]; then
    # install ~oneadmin/.ssh/config if not present on a fresh install only
    if [ ! -e "%oneadmin_home/.ssh/config" ]; then
        if [ ! -d "%oneadmin_home/.ssh" ]; then
            mkdir -p %oneadmin_home/.ssh
            chmod 0700 %oneadmin_home/.ssh
            chown oneadmin:oneadmin %oneadmin_home/.ssh
        fi
        cp %_datadir/one/ssh/config %oneadmin_home/.ssh/config
        chmod 0600 %oneadmin_home/.ssh/config
        chown oneadmin:oneadmin %oneadmin_home/.ssh/config
    fi
fi
systemd-tmpfiles --create %_tmpfilesdir/opennebula.conf || :

%pre server
if [ $1 = 1 ]; then
    if [ ! -e %oneadmin_home/.one/one_auth ]; then
        PASSWORD=$(echo $RANDOM$(date '+%s')|md5sum|cut -d' ' -f1)
        mkdir -p %oneadmin_home/.one
	chmod 700 %oneadmin_home/.one
        echo oneadmin:$PASSWORD > %oneadmin_home/.one/one_auth
        chown -R oneadmin:oneadmin %oneadmin_home/.one
	chmod 600 %oneadmin_home/.one/one_auth
    fi

    if [ ! -f %oneadmin_home/.ssh/id_rsa ]; then
        su -c "ssh-keygen -N '' -t rsa -f %oneadmin_home/.ssh/id_rsa" -l oneadmin
	if [ ! -f "%oneadmin_home/.ssh/authorized_keys" ]; then
	    cp -p %oneadmin_home/.ssh/id_rsa.pub %oneadmin_home/.ssh/authorized_keys
	    chmod 600 %oneadmin_home/.ssh/authorized_keys
	fi
    fi
fi

%post server
%post_service %name
%post_service %name-scheduler
%post_service %name-hem
%post_service %name-ssh-agent

%preun server
%preun_service %name
%preun_service %name-scheduler
%preun_service %name-hem
%preun_service %name-ssh-agent

# %post node-xen
# if [ $1 = 1 ]; then
#     /usr/bin/grub-bootxen.sh
# fi

%post sunstone
%post_service %name-sunstone
%post_service %name-novnc

%preun sunstone
%preun_service %name-sunstone
%preun_service %name-novnc

%pre node-kvm
usermod -a -G vmusers oneadmin  2>/dev/null ||:

#Modify /etc/libvirt/qemu.conf to set oneadmin user as running user for libvirt daemon
#Otherwise, you might get some errors like :
#   could not open disk image /var/lib/one/datastores/0/0/disk.0: Permission denied
%post node-kvm
if [ $1 = 1 ]; then
    # Install
    if [ -e /etc/libvirt/qemu.conf ]; then
        cp /etc/libvirt/qemu.conf /etc/libvirt/qemu.conf.orig

        echo 'user  = "oneadmin"'    >  /etc/libvirt/qemu.conf
        echo 'group = "oneadmin"'    >> /etc/libvirt/qemu.conf
        echo 'dynamic_ownership = 0' >> /etc/libvirt/qemu.conf
    fi
elif [ $1 = 2 ]; then
    # Upgrade
    PID=$(cat /tmp/one-monitord-client.pid 2> /dev/null)
    [ -n "$PID" ] && kill $PID 2> /dev/null || :
fi

%pre node-lxd
usermod -a -G lxd oneadmin  2>/dev/null ||:

%post node-lxd
if [ $1 = 1 ]; then
    if ! grep -qs '^root:' /etc/subuid \
       && ! grep -qs '^root:' /etc/subgid \
       && ! grep -qs '^lxd:' /etc/subuid \
       && ! grep -qs '^lxd:' /etc/subuid
   then
       [ -f /etc/subuid ] || touch /etc/subuid
       [ -f /etc/subgid ] || touch /etc/subgid
       echo root:100000:65536 >> /etc/subuid
       echo root:100000:65536 >> /etc/subgid
       echo lxd:100000:65536 >> /etc/subuid
       echo lxd:100000:65536 >> /etc/subgid
   fi
fi

%post node-firecracker
if [ $1 = 1 ]; then
    # Changes ownership of chroot folder
    mkdir -p /srv/jailer/firecracker
    chown oneadmin:oneadmin /srv/jailer/firecracker
    chmod 750 /srv/jailer/firecracker
fi

if [ $1 = 2 ]; then
    # Upgrade
    PID=$(cat /tmp/one-monitord-client.pid 2> /dev/null)
    [ -n "$PID" ] && kill $PID 2> /dev/null || :
fi

#%post ruby
#cat <<EOF
#Please remember to execute %_datadir/one/install_gems to install all the
#required gems.
#EOF

%files common
%doc LICENSE NOTICE README.md

%config(noreplace) %_sysconfdir/sudoers.d/opennebula
%config(noreplace) %_sysconfdir/logrotate.d/opennebula

%_tmpfilesdir/opennebula.conf
%_tmpfilesdir/opennebula-node.conf
%dir %_libexecdir/one
%dir %_datadir/one
%_datadir/one/ssh
%dir %attr(0750, root, oneadmin) %_sysconfdir/one
%dir %attr(0770, root, oneadmin) %_logdir/one
%dir %attr(0750, oneadmin, oneadmin) %oneadmin_home

%files node-kvm
%config(noreplace) %_sysconfdir/polkit-1/rules.d/50-opennebula.rules
%config(noreplace) %_sysconfdir/sysctl.d/bridge-nf-call.conf
#%config %_sysconfdir/cron.d/opennebula-node
%config(noreplace) %_sysconfdir/sudoers.d/opennebula-node

%files node-lxd
%doc README.opennebula-lxd
%_bindir/svncterm_server
%_bindir/catfstab
%config(noreplace) %_sysconfdir/modprobe.d/opennebula-lxd.conf
%config(noreplace) %_sysconfdir/modules-load.d/opennebula-lxd.conf
%config(noreplace) %_sysconfdir/sudoers.d/opennebula-node-lxd
%_sysconfdir/firsttime.d/opennebula-lxd-init

%if_with firecracker
%files node-firecracker
%config %_sysconfdir/sysctl.d/bridge-nf-call.conf
#%config %_sysconfdir/cron.d/opennebula-node
%_sbindir/one-clean-firecracker-domain
%_sbindir/one-prepare-firecracker-domain
%_bindir/svncterm_server
%config(noreplace) %_sysconfdir/sudoers.d/opennebula-node-firecracker
%endif

# %files node-xen

%files java
%_javadir/org.opennebula.client.jar

%files -n gem-%name
%ruby_gemspecdir/%name-%version.gemspec
%ruby_gemslibdir/%name-%version

#%ruby_sitelibdir/opennebula.rb
#%ruby_sitelibdir/opennebula
#%ruby_sitelibdir/vcenter_driver.rb
#%ruby_sitelibdir/VirtualMachineDriver.rb
#%ruby_sitelibdir/OpenNebulaDriver.rb
#%ruby_sitelibdir/CommandManager.rb
#%ruby_sitelibdir/ActionManager.rb
#%ruby_sitelibdir/DriverExecHelper.rb
#%ruby_sitelibdir/cloud/CloudClient.rb

%_libexecdir/one/ruby/scripts_common.rb
%_libexecdir/one/ruby/vcenter_driver
%_libexecdir/one/ruby/nsx_driver.rb
%_libexecdir/one/ruby/nsx_driver

#%ruby_gemspecdir/opennebula*
#%exclude %ruby_gemspecdir/opennebula-cli*

%files -n python3-module-%name
%python3_sitelibdir_noarch/*

%files sunstone
%_libexecdir/one/sunstone
%_libexecdir/one/ruby/OpenNebulaVNC.rb
%_libexecdir/one/ruby/OpenNebulaAddons.rb
%_libexecdir/one/ruby/cloud/econe
%_libexecdir/one/ruby/cloud/CloudAuth.rb
%_libexecdir/one/ruby/cloud/CloudServer.rb
%_libexecdir/one/ruby/cloud/CloudAuth

%_bindir/sunstone-server
%_bindir/novnc-server
%_bindir/econe-server
%_bindir/econe-allocate-address
%_bindir/econe-associate-address
%_bindir/econe-attach-volume
%_bindir/econe-create-keypair
%_bindir/econe-create-volume
%_bindir/econe-delete-keypair
%_bindir/econe-delete-volume
%_bindir/econe-describe-addresses
%_bindir/econe-describe-images
%_bindir/econe-describe-instances
%_bindir/econe-describe-keypairs
%_bindir/econe-describe-volumes
%_bindir/econe-detach-volume
%_bindir/econe-disassociate-address
%_bindir/econe-reboot-instances
%_bindir/econe-register
%_bindir/econe-release-address
%_bindir/econe-run-instances
%_bindir/econe-start-instances
%_bindir/econe-stop-instances
%_bindir/econe-terminate-instances
%_bindir/econe-upload

%_unitdir/opennebula-sunstone.service
%_unitdir/opennebula-econe.service
%_unitdir/opennebula-novnc.service

%_datadir/one/websockify

%_man1dir/econe*


%dir %attr(0770, root, oneadmin) %oneadmin_home/sunstone
%attr(0770, root, oneadmin) %oneadmin_home/sunstone/main.js

%defattr(0640, root, oneadmin, 0750)
%config(noreplace) %_sysconfdir/one/sunstone-server.conf
%config(noreplace) %_sysconfdir/one/sunstone-logos.yaml
%config(noreplace) %_sysconfdir/one/ec2query_templates/*
%config(noreplace) %_sysconfdir/one/econe.conf
%config(noreplace) %_sysconfdir/one/sunstone-views.yaml
%config(noreplace) %_sysconfdir/one/sunstone-views/*
%config(noreplace) %_sysconfdir/one/ec2_driver.conf
%config %_sysconfdir/one/ec2_driver.default

%files gate
%config(noreplace) %attr(0640, root, oneadmin) %_sysconfdir/one/onegate-server.conf
%_libexecdir/one/onegate
%_bindir/onegate-server
%_unitdir/opennebula-gate.service

%files flow
%config(noreplace) %attr(0640, root, oneadmin) %_sysconfdir/one/oneflow-server.conf
%_libexecdir/one/oneflow
%_bindir/oneflow-server
%_unitdir/opennebula-flow.service
%_datadir/flow

%files provision
%_bindir/oneprovision
%config(noreplace) %_sysconfdir/one/cli/oneprovision.yaml
#%_libexecdir/one/ruby/cli/one_helper/oneprovision_helper.rb
%_libexecdir/one/oneprovision
%_datadir/one/oneprovision
%_man1dir/oneprovision.1*


%files server
%config(noreplace) %_sysconfdir/sudoers.d/opennebula-server
%_unitdir/opennebula.service
%_unitdir/opennebula-scheduler.service
%_unitdir/opennebula-hem.service
%_unitdir/opennebula-ssh-agent.service
%_unitdir/opennebula-ssh-socks-cleaner.service
%_unitdir/opennebula-ssh-socks-cleaner.timer
%_unitdir/opennebula-showback.service
%_unitdir/opennebula-showback.timer

%_bindir/mm_sched

%_bindir/one
%_bindir/oned
%_bindir/onedb
%_bindir/onehem-server
%_bindir/onehook

%_datadir/one/examples
%_datadir/one/esx-fw-vnc
%_datadir/one/follower_cleanup
%_datadir/one/start-scripts
%_datadir/one/schemas
%_datadir/one/context

%_libexecdir/one/mads
%_libexecdir/one/onehem
%_libexecdir/one/ruby/az_driver.rb
%_libexecdir/one/ruby/ec2_driver.rb
%_libexecdir/one/ruby/onedb
%_libexecdir/one/ruby/one_vnm.rb
%_libexecdir/one/ruby/opennebula_driver.rb
%_libexecdir/one/ruby/ssh_stream.rb
%_libexecdir/one/ruby/packet_driver.rb
%_libexecdir/one/ruby/PublicCloudDriver.rb
%_libexecdir/one/sh
%_datadir/one/conf

#%ruby_gemspecdir/opennebula-server/Gemfile

%_man1dir/onedb.1.*

%dir %attr(0750, oneadmin, oneadmin) %oneadmin_home/datastores
%dir %attr(0750, oneadmin, oneadmin) %oneadmin_home/remotes

%attr(-, oneadmin, oneadmin) %oneadmin_home/datastores/*
%attr(-, oneadmin, oneadmin) %oneadmin_home/vms
%config(noreplace) %attr(-, oneadmin, oneadmin) %oneadmin_home/remotes/*

%defattr(0640, root, oneadmin, 0750)
%config(noreplace) %_sysconfdir/one/defaultrc
%config(noreplace) %_sysconfdir/one/tmrc
%config(noreplace) %_sysconfdir/one/hm/*
%config(noreplace) %_sysconfdir/one/oned.conf
%config(noreplace) %_sysconfdir/one/sched.conf
%config(noreplace) %_sysconfdir/one/monitord.conf
%config(noreplace) %_sysconfdir/one/onehem-server.conf
%config(noreplace) %_sysconfdir/one/vmm_exec/*
%config(noreplace) %_sysconfdir/one/az_driver.conf
%config %_sysconfdir/one/az_driver.default
%config %_sysconfdir/one/vcenter_driver.default
%config(noreplace) %_sysconfdir/one/auth/server_x509_auth.conf
%config(noreplace) %_sysconfdir/one/auth/ldap_auth.conf
%config(noreplace) %_sysconfdir/one/auth/x509_auth.conf

%files -n gem-%name-cli
%dir %_sysconfdir/one/cli
%ruby_gemspecdir/%name-cli-%version.gemspec
%ruby_gemslibdir/%name-cli-%version
%config(noreplace) %_sysconfdir/one/cli/*
%exclude %_sysconfdir/one/cli/oneprovision.yaml
%_datadir/bash-completion/completions/one

%_bindir/oneacct
%_bindir/oneacl
%_bindir/onecluster
%_bindir/onedatastore
%_bindir/onegroup
%_bindir/onehost
%_bindir/oneimage
%_bindir/onemarket
%_bindir/onemarketapp
%_bindir/onetemplate
%_bindir/oneuser
%_bindir/onevdc
%_bindir/onevm
%_bindir/onevmgroup
%_bindir/onevnet
%_bindir/onevntemplate
%_bindir/onevrouter
%_bindir/onezone
%_bindir/onevcenter
%_bindir/onesecgroup
%_bindir/oneshowback

%_bindir/oneflow
%_bindir/oneflow-template

#%_libexecdir/one/ruby/cli
#%exclude %_libexecdir/one/ruby/cli/one_helper/oneprovision_helper.rb
#%ruby_gemspecdir/opennebula-cli*
#%ruby_sitelibdir/cli_helper.rb
#%ruby_sitelibdir/one_helper.rb
#%ruby_sitelibdir/command_parser.rb
#%ruby_sitelibdir/one_helper

%_datadir/one/onetoken.sh

%_man1dir/one*
%exclude %_man1dir/onedb.1.*
%exclude %_man1dir/oneprovision.1*

%changelog
* Tue Sep 21 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.12.0.4-alt3
- FTBFS: yet another gem deps

* Tue Sep 14 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.12.0.4-alt2
- FTBFS: gem deps

* Thu Jul 08 2021 Pavel Skrylev <majioa@altlinux.org> 5.12.0.4-alt1.1
- * ruby macros, and call to ruby build

* Tue Jun 22 2021 Alexey Shabalin <shaba@altlinux.org> 5.12.0.4-alt1
- 5.12.0.4
- drop support sysV init scripts

* Wed May 26 2021 Mikhail Gordeev <obirvalger@altlinux.org> 5.10.5-alt8
- node-lxd: setup lxd in post and firsttime.d
- add requires to python3-module-numpy to improve vnc speed

* Mon May 17 2021 Mikhail Gordeev <obirvalger@altlinux.org> 5.10.5-alt7
- fix regexp matching file output for qcow images

* Thu May 13 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.10.5-alt6
- lxd: increase the image size to store all additional packages
- node-lxd: disable killing of vnc server

* Wed Apr 14 2021 Alexey Shabalin <shaba@altlinux.org> 5.10.5-alt5
- adduser oneadmin with static UID and GID = 9869
  (for compat with shared cluster FS like NFS or GlusterFS
  and compat with upstream packages)

* Fri Jul 24 2020 Alexey Shabalin <shaba@altlinux.org> 5.10.5-alt4
- adopt check enable support-tab in yaml files patch for 5.10

* Wed Jun 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 5.10.5-alt3
- revert ac0a19b24a35cd22b2428ed83e845a4b5bd474a8 (not build for 32-bit arm)

* Thu Jun 18 2020 Alexey Shabalin <shaba@altlinux.org> 5.10.5-alt2
- backport patches from upstream/one-5.10 branch
- fixed requires on lxd3.0 (lxd-4 not supported)
- add requires lxcfs to node-lxd package

* Mon May 11 2020 Alexey Shabalin <shaba@altlinux.org> 5.10.5-alt1
- 5.10.5
- add requires libvirt-client and polkit to opennebula-node-kvm package

* Fri Apr 10 2020 Alexey Shabalin <shaba@altlinux.org> 5.10.4-alt3
- update sudoers config for allow use LXD
- update Requires for node-lxd package

* Wed Apr 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 5.10.4-alt2
- add ALT to linuxcontainers market

* Wed Apr 08 2020 Alexey Shabalin <shaba@altlinux.org> 5.10.4-alt1
- 5.10.4

* Thu Apr 02 2020 Pavel Skrylev <majioa@altlinux.org> 5.10.3-alt1.1
- ! spec according to move the lib64/ to lib/

* Tue Mar 10 2020 Alexey Shabalin <shaba@altlinux.org> 5.10.3-alt1
- 5.10.3

* Mon Feb 17 2020 Alexey Shabalin <shaba@altlinux.org> 5.10.2-alt1
- 5.10.2

* Mon Jan 27 2020 Alexey Shabalin <shaba@altlinux.org> 5.10.1-alt1
- 5.10.1
- use system node-gyp and node-sass for build

* Wed Nov 27 2019 Alexey Shabalin <shaba@altlinux.org> 5.10.0-alt1
- 5.10.0

* Thu Sep 26 2019 Alexey Shabalin <shaba@altlinux.org> 5.8.5-alt1
- 5.8.5

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 5.8.4-alt3.2
- spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 5.8.4-alt3.1
- spec to fix dependency gem version

* Wed Jul 31 2019 Alexey Shabalin <shaba@altlinux.org> 5.8.4-alt3
- revert "remove support tab"
- check enable support-tab in yaml files

* Fri Jul 26 2019 Andrew A. Vasilyev <andy@altlinux.org> 5.8.4-alt2
- remove support tab

* Wed Jul 24 2019 Alexey Shabalin <shaba@altlinux.org> 5.8.4-alt1
- 5.8.4
- update requires

* Fri Jul 19 2019 Andrew A. Vasilyev <andy@altlinux.org> 5.8.3-alt4
- run python3 for novnc websockify script
- fix datastore scripts file mode

* Mon Jul 15 2019 Andrew A. Vasilyev <andy@altlinux.org> 5.8.3-alt3
- add moosefs support

* Tue Jul 09 2019 Andrew A. Vasilyev <andy@altlinux.org> 5.8.3-alt2
- add lizardfs support

* Thu Jul 04 2019 Alexey Shabalin <shaba@altlinux.org> 5.8.3-alt1
- 5.8.3

* Thu Jun 13 2019 Alexey Shabalin <shaba@altlinux.org> 5.8.2-alt2
- Fixed execute onedb (fixed ALT#36832)

* Mon May 27 2019 Alexey Shabalin <shaba@altlinux.org> 5.8.2-alt1
- 5.8.2

* Tue Apr 09 2019 Alexey Shabalin <shaba@altlinux.org> 5.8.1-alt2
- 5.8.1 release
- fix provides and obsoletes
- add opennebula-node-lxd package

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 5.8.1-alt1
- Use Ruby Policy 2.0

* Mon Mar 11 2019 Alexey Shabalin <shaba@altlinux.org> 5.8.0-alt1
- 5.8.0

* Thu Mar 07 2019 Pavel Skrylev <majioa@altlinux.org> 5.6.2-alt6
- Remove unnecessary dependency.

* Thu Jan 24 2019 Alexey Shabalin <shaba@altlinux.org> 5.6.2-alt5
- use new ruby rpm macros for build

* Mon Jan 14 2019 Mikhail Gordeev <obirvalger@altlinux.org> 5.6.2-alt4
- Add ruby-nokogiri to BuildRequires for building man pages
- Move man files to appropriate packages

* Fri Dec 14 2018 Alexey Shabalin <shaba@altlinux.org> 5.6.2-alt3
- move scripts_common.rb to ruby package for allow install sunstone without server package
- build with system node headers from node-devel package

* Wed Nov 14 2018 Alexey Shabalin <shaba@altlinux.org> 5.6.2-alt2
- update Requires

* Fri Nov 09 2018 Alexey Shabalin <shaba@altlinux.org> 5.6.2-alt1
- 5.6.2

* Tue Oct 09 2018 Alexey Shabalin <shaba@altlinux.org> 5.6.1-alt2
- rebuild with node-8.12.0

* Mon Sep 24 2018 Alexey Shabalin <shaba@altlinux.org> 5.6.1-alt1
- 5.6.1

* Tue Jun 26 2018 Alexey Shabalin <shaba@altlinux.ru> 5.4.15-alt2.S1
- backport patches from upstream/one-5.4 branch

* Tue Jun 19 2018 Alexey Shabalin <shaba@altlinux.ru> 5.4.15-alt1
- 5.4.15

* Sat Jun 09 2018 Alexey Shabalin <shaba@altlinux.ru> 5.4.13-alt1
- 5.4.13
- build man pages
- add Restart=on-failure for services

* Sat May 12 2018 Alexey Shabalin <shaba@altlinux.ru> 5.4.12-alt1
- 5.4.12

* Tue Apr 03 2018 Alexey Shabalin <shaba@altlinux.ru> 5.4.10-alt1
- 5.4.10

* Wed Feb 28 2018 Alexey Shabalin <shaba@altlinux.ru> 5.4.8-alt1
- 5.4.8

* Sat Feb 17 2018 Alexey Shabalin <shaba@altlinux.ru> 5.4.7-alt1
- 5.4.7
- rename ALT logo altlinux -> alt

* Sat Jan 27 2018 Alexey Shabalin <shaba@altlinux.ru> 5.4.6-alt1
- 5.4.6

* Thu Dec 14 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.5-alt1
- 5.4.5
- fix install ALTLinux logo
- update Requires: libvirt-qemu to libvirt-kvm in node-kvm package

* Tue Dec 05 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.4-alt1
- 5.4.4

* Wed Nov 08 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.3-alt1
- 5.4.3

* Wed Oct 11 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.2-alt1
- 5.4.2

* Tue Sep 19 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.1-alt1
- 5.4.1

* Wed Sep 13 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.0-alt5
- update to one-5.4 branch

* Fri Sep 08 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.0-alt4
- add user oneadmin to wheel group for allow run sudo

* Tue Sep 05 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.0-alt3
- fix run sunstone (add nodejs and bower modules to source)

* Tue Sep 05 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.0-alt2
- update to one-5.4 branch
- fix post scripts
- rename package client to tools

* Wed Aug 30 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.0-alt1
- Initial build (based on upstream spec)
