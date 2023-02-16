Name:           plantuml-server
Version:        1.2022.7
Release:        1%{?dist}
Summary:        PlantUML Online Server

License:       GPL
URL:           https://github.com/plantuml/plantuml-server

%undefine       _disable_source_fetch
Source0:        https://github.com/plantuml/%{name}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/archlinux/svntogit-community/raw/packages/plantuml-server/trunk/plantuml-server.run
Source2:        https://github.com/archlinux/svntogit-community/raw/packages/plantuml-server/trunk/plantuml-server.conf
Source3:        https://github.com/archlinux/svntogit-community/raw/packages/plantuml-server/trunk/plantuml-server.service

ExclusiveArch:  %{java_arches} noarch
BuildArch:      noarch
BuildRequires:  maven-local
Requires:       java-headless
Suggests:       graphviz
Suggests:       ditaa


%description
PlantUML Server is a web application to generate UML diagrams on-the-fly.

%prep
echo "=============== Extracting sources..."
%setup -n %{name}-%{version}

echo $(pwd)
ls -lh .


%build
echo "=============== building ..."
echo $(pwd)
ls -lh .

mvn package

%install
echo "=============== installing ..."
echo "pwd: $(pwd)"
echo "buildroot: %{buildroot}"
ls -lh .

mkdir -p %{buildroot}/usr/bin/

install -m 755 -D "%{_sourcedir}/%{name}.run" "%{buildroot}/usr/bin/%{name}"
install -m 755 -D "%{_sourcedir}/%{name}.conf" "%{buildroot}/etc/sysconfig/%{name}"
install -m 644 -D "%{_sourcedir}/%{name}.service" "%{buildroot}/usr/lib/systemd/system/%{name}.service"
sed -i 's|/etc/conf.d|/etc/sysconfig|g' "%{buildroot}/usr/lib/systemd/system/%{name}.service"

install -m 644 -D "target/plantuml.war" "%{buildroot}/usr/share/java/%{name}/plantuml.war"
install -m 644 -D "target/dependency/jetty-runner.jar" "%{buildroot}/usr/share/java/%{name}/dependency/jetty-runner.jar"

ls %{buildroot}

%files
/usr/bin/%{name}
/etc/sysconfig/%{name}
/usr/lib/systemd/system/%{name}.service
/usr/share/java/%{name}/plantuml.war
/usr/share/java/%{name}/dependency/jetty-runner.jar

%changelog
* Sat Oct 29 2022 ttyS3
- init port from https://github.com/archlinux/svntogit-community/blob/packages/plantuml-server/trunk/PKGBUILD
