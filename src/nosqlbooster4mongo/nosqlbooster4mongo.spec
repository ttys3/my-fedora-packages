# thanks to https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=nosqlbooster-mongodb

Name: nosqlbooster4mongo
Version: 8.0.2
Release: 1%{?dist}
Summary: a cross-platform IDE for MongoDB Server
License: NoSQLBooster EULA
URL: https://nosqlbooster.com

Source0: https://s3.mongobooster.com/download/releasesv8/%{name}-%{version}.tar.gz

Source1: nosqlbooster4mongo.desktop

Source2: nosqlbooster4mongo.png

BuildArch: noarch

Requires: GConf2
Requires: libnotify

# https://bugzilla.redhat.com/show_bug.cgi?id=1869423
%global __filter_GLIBC_PRIVATE 1
# do not call strip
%global __os_install_post %{nil}

%description
NoSQLBooster is a cross-platform IDE for MongoDB Server, which provides a build-in MongoDB script debugger, 
SQL query, server monitoring tools, chaining fluent query, query code generator, task scheduling, ES2020 support, 
and advanced IntelliSense experience.

%prep
# http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html
%setup -D -n %{name}-%{version}

ls -lhp

%install
mkdir -p %{buildroot}/opt

ls -lhp

install -Dm644 %{_sourcedir}/%{name}.desktop %{buildroot}/usr/share/applications/%{name}.desktop

install -Dm644 %{_sourcedir}/%{name}.png %{buildroot}/usr/share/icons/hicolor/512x512/apps/%{name}.png

cp -aT %{name}-%{version} %{buildroot}/opt/%{name}

install -Dm755 %{_sourcedir}/AppRun %{buildroot}/opt/%{name}/AppRun

# permission tweaks
find "%{buildroot}/opt/%{name}" -type d -exec chmod 755 {} +

%files
/opt/%{name}
/usr/share/applications/%{name}.desktop
/usr/share/icons/hicolor/512x512/apps/%{name}.png

%changelog

