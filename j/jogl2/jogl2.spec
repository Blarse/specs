%add_findreq_skiplist %_libdir/jogl2/libnativewindow_awt.so
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: java-1.8.0-openjdk-devel
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:    jogl2
Version: 2.3.2
Release: alt8_9jpp8
%global src_name jogl-v%{version}
Summary: Java bindings for the OpenGL API

# For a breakdown of the licensing, see LICENSE.txt 
License: BSD and MIT and Apache-2.0 and Apache-1.1 
URL: http://jogamp.org/
Source0: http://jogamp.org/deployment/v%{version}/archive/Sources/%{src_name}.tar.xz
Source1: %{name}-pom.xml

Patch2: %{name}-0002-deactivate-debug-printf.patch
Patch3: %{name}-0003-delete-not-supported-API.patch
Patch4: %{name}-0004-disable-some-tests.patch
Patch5: %{name}-add-secarchs.patch
Patch6: %{name}-mesa-profile-detection.patch
Patch7: jogl2-disable-build-native-broadcom.patch

BuildRequires: gcc
BuildRequires: jpackage-utils
BuildRequires: gluegen2-devel = %{version}
BuildRequires: eclipse-swt
BuildRequires: libXt-devel
BuildRequires: libXrender-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: maven-local

Requires: jpackage-utils
Requires: gluegen2 = %{version}
Source44: import.info

%description
The JOGL project hosts the development version of the Java Binding for
the OpenGL API (JSR-231), and is designed to provide hardware-supported 3D
graphics to applications written in Java. JOGL provides full access to the
APIs in the OpenGL 2.0 specification as well as nearly all vendor extensions,
and integrates with the AWT and Swing widget sets. It is part of a suite of
open-source technologies initiated by the Game Technology Group at
Sun Microsystems.

%package doc
Group: Development/Java
Summary:        User manual for jogl2
BuildArch:      noarch

%description doc
User manual for jogl2.

%prep
%setup -n %{src_name}

%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p2

# Remove bundled dependencies
find -name "*.jar" -type f -exec rm {} \;
find -name "*.apk" -type f -exec rm {} \;
rm -fr make/lib

# Restore the gluegen2 source code from gluegen2-devel
rm -fr ../gluegen
cp -rdf %{_datadir}/gluegen2 ../gluegen

# Fix file-not-utf8
for file in README.txt; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

# git executable should not be used, use true (to avoid checkout) instead
sed -i 's/executable="git"/executable="true"/' make/build-common.xml

# install in _javadir
%mvn_file org.jogamp.jogl:jogl %{name}
%mvn_alias org.jogamp.jogl:jogl "org.jogamp.jogl:jogl-all"

%build
# zerg's girar armh hack:
(while true; do date; sleep 7m; done) &
# end armh hack, kill it when girar will be fixed
cd make

# As we never cross-compile this package, the SDK root is always /
export TARGET_PLATFORM_ROOT=/

export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
xargs -t ant <<EOF
 -verbose
 -Dc.compiler.debug=true
 -Djavacdebug=true
 -Djavac.memorymax=512m
 -Dcommon.gluegen.build.done=true
 
 -Dantlr.jar=%{_javadir}/antlr.jar 
 -Djunit.jar=%{_javadir}/junit.jar 
 -Dant.jar=%{_javadir}/ant.jar 
 -Dant-junit.jar=%{_javadir}/ant/ant-junit.jar 
 -Dgluegen.jar=%{_javadir}/gluegen2.jar 
 -Dgluegen-rt.jar=%{_jnidir}/gluegen2-rt.jar 
 -Dswt.jar=%{_jnidir}/swt.jar 

 -Djava.excludes.all='com/jogamp/newt/util/applet*/**/*.java com/jogamp/audio/**/*.java jogamp/opengl/gl2/fixme/**/*.java com/jogamp/opengl/test/**/*.java'

 -Djavadoc.link=%{_javadocdir}/java 
 -Dgluegen.link=%{_javadocdir}/gluegen2 
 
 build.nativewindow build.jogl build.newt one.dir javadoc.public
EOF

cd ..
export JAVA_HOME=/usr/lib/jvm/java
%mvn_artifact %{SOURCE1} build/jar/jogl-all.jar

%install
%mvn_install 
mkdir -p %{buildroot}%{_javadir}/%{name} \
    %{buildroot}%{_libdir}/%{name} \
    %{buildroot}%{_javadir}

ln -s ../../..%{_jnidir}/%{name}.jar %{buildroot}%{_libdir}/%{name}/
install -t %{buildroot}%{_libdir}/%{name}/ build/lib/*.so


# Make the doc package
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -rdf doc/* %{buildroot}%{_docdir}/%{name}
cp -t %{buildroot}%{_docdir}/%{name}/ README.txt LICENSE.txt CHANGELOG.txt

%files -f .mfiles
%doc README.txt LICENSE.txt CHANGELOG.txt
%{_libdir}/%{name}

%files doc
%{_docdir}/%{name}

%changelog
* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 2.3.2-alt8_9jpp8
- xmvn4 support

* Mon Jun 06 2022 Igor Vlasenko <viy@altlinux.org> 2.3.2-alt7_9jpp8
- migrated to %%mvn_artifact
- jogl2.jar moved to _jnidir

* Fri May 27 2022 Igor Vlasenko <viy@altlinux.org> 2.3.2-alt6_9jpp8
- fixed build with new libs.req

* Sat Nov 27 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt5_9jpp8
- use patch for new Mesa from Mageia (ALT #41445)
- fix license names according to SPDX
- fix file conflicts between jogl2 and jogl2-doc

* Sat Dec 12 2020 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt4_9jpp8
- use zerg@'s hack for armh

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt3_9jpp8
- fixed build with new java

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_9jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_6jpp8
- java update

* Sun Oct 29 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_5jpp8
- restored arch libs (closes: #34087)

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_3jpp8
- new jpp release

* Mon Jan 23 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt2_2jpp8
- package libraries for scilab (ALT #33025)

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_2jpp8
- new version

* Fri Oct 14 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1_4jpp8
- replaced with fc imported package

* Sun Nov 16 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version

* Thu Jul 24 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt11.2
- NMU: fixed BR: junit-junit4 no more

* Sun Apr 21 2013 Andrey Cherepanov <cas@altlinux.org> 2.0-alt11.1
- Initial build in Sisyphus (thanks Fedora maintainers)
- Disable Broadcom native support
