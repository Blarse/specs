Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global git_tag 6578a73424849be942308f263eaf47fa897bcd13

Name:           maven-indexer
Version:        6.0.0
Release:        alt1_5jpp11
Summary:        Standard for producing indexes of Maven repositories

License:        ASL 2.0
URL:            http://maven.apache.org/maven-indexer/index.html

Source0:        https://github.com/apache/maven-indexer/archive/%{git_tag}/maven-indexer-%{version}.tar.gz

# Port to latest lucene, sent upstream:
# - https://github.com/apache/maven-indexer/pull/37
Patch0: 0001-MINDEXER-115-Migrate-to-BooleanQuery.Builder.patch
Patch1: 0002-Eliminate-use-of-deprecated-Lucene-API.patch
Patch2: 0003-Changes-needed-to-migrate-to-Lucene-8.patch

# Drop dep on truezip
Patch3:         maven-indexer-truezip.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.lucene:lucene-analyzers-common)
BuildRequires:  mvn(org.apache.lucene:lucene-backward-codecs)
BuildRequires:  mvn(org.apache.lucene:lucene-core) >= 8.0.0
BuildRequires:  mvn(org.apache.lucene:lucene-highlighter)
BuildRequires:  mvn(org.apache.lucene:lucene-queryparser)
BuildRequires:  mvn(org.apache.maven.archetype:archetype-catalog)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)

Requires: lucene >= 8.0.0
Source44: import.info

%description
Apache Maven Indexer (former Sonatype Nexus Indexer) is the defacto
standard for producing indexes of Maven repositories. The Indexes
are produced and consumed by all major tools in the ecosystem.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{git_tag}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3

find -name '*.jar' -delete
find -name '*.zip' -delete
find -name '*.class' -delete

# Tests need porting to a modern jetty
%pom_remove_dep -r org.mortbay.jetty:jetty
%pom_remove_plugin -r :maven-failsafe-plugin

# Remove unnecessary plugins for RPM builds
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :apache-rat-plugin . indexer-core
%pom_remove_plugin :animal-sniffer-maven-plugin

# Avoid bundling Lucene in shaded jar
%pom_remove_plugin :maven-shade-plugin indexer-core

# Make static analysis annotations have provided scope
%pom_xpath_inject "pom:dependency[pom:artifactId='jsr305']" "<scope>provided</scope>" . indexer-core

# Disable CLI module because of how it bundles stuff
%pom_disable_module indexer-cli

# No need to ship examples
%pom_disable_module indexer-examples

# Ensure sisu index is generated
%pom_add_plugin "org.eclipse.sisu:sisu-maven-plugin:0.3.3" . \
"<executions><execution>
  <id>generate-index</id>
  <goals><goal>main-index</goal></goals>
</execution></executions>"

# Drop unneeded optional dep on truezip
%pom_remove_dep -r de.schlichtherle.truezip:
rm indexer-core/src/main/java/org/apache/maven/index/util/zip/TrueZipZipFileHandle.java

%build
# Skip tests because they need porting to modern jetty
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dsource=1.8 -DdetectJavaApiLink=false

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference NOTICE
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference NOTICE

%changelog
* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 6.0.0-alt1_5jpp11
- new version

* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_0.8.gite0570bfjpp8
- build with lucene7

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_0.4.gite0570bfjpp8
- fixed build with new lucene

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_0.1.gite0570bfjpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.1-alt1_9jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.1-alt1_8jpp8
- new version

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_3jpp7
- new version

