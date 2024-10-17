%{?_javapackages_macros:%_javapackages_macros}
%global tag 684bc0559758cdf71cc68d6710ceee840c9c1bbc

Name:           feclipse-maven-plugin
Version:        0.0.4
Release:        0.1.git684bc0.0%{?dist}
Summary:        Eclipse repo2runnable Maven Mojo


License:        ASL 2.0
URL:            https://maven.apache.org
Source0:        https://git.fedorahosted.org/cgit/feclipse-maven-plugin.git/snapshot/feclipse-maven-plugin-%{tag}.tar.gz
BuildArch:      noarch

BuildRequires: mvn(org.eclipse.tycho:tycho-p2-facade) >= 0.19.0
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.eclipse.tycho.extras:tycho-p2-extras-plugin)
BuildRequires: maven-local
Requires: mvn(org.eclipse.tycho:tycho-p2-facade)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(junit:junit)
Requires: mvn(org.eclipse.tycho.extras:tycho-p2-extras-plugin)
Requires: eclipse-platform

%description
A Maven plugin that transform Eclipse P2 repository into a runnable form,
so the repository can be put into dropins folder.

%package javadoc

Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n feclipse-maven-plugin-%{tag}

%build
cd installer
%mvn_build

%install
cd installer
%mvn_install


%files -f installer/.mfiles
%dir %{_javadir}/%{name}

%files javadoc -f installer/.mfiles-javadoc


%changelog
* Wed Oct 30 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.0.4-0.1.git684bc0
- Update to tycho 0.19.0 API.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-0.3.gitfb5939
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.0.3-0.2.gitfb5939
- Remote content.jar and artifacts.jar after the build.

* Tue Jul 16 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.0.3-0.1.git85c3ca
- Update to latest snapshot.

* Thu May 9 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.0.2-1
- Update to latest upstream.

* Thu May 2 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.0.1-2
- Properly upload sources.

* Wed May 1 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.0.1-1
- Initial import (RHBZ 958431)
