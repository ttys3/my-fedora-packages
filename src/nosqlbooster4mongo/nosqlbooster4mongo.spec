# thanks to https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=nosqlbooster-mongodb

Name: nosqlbooster4mongo
Version: 9.1.6
Release: 1%{?dist}
Summary: a cross-platform IDE for MongoDB Server
License: NoSQLBooster EULA
URL: https://nosqlbooster.com

# https://s3.nosqlbooster.com/download/releasesv9/nosqlbooster4mongo-9.1.6.tar.gz
Source0: https://s3.nosqlbooster.com/download/releasesv9/%{name}-%{version}.tar.gz

Source1: nosqlbooster4mongo.desktop

Source2: nosqlbooster4mongo.png

Source3: AppRun

BuildArch: x86_64

Requires: GConf2
Requires: libnotify

# https://bugzilla.redhat.com/show_bug.cgi?id=1869423
%global __filter_GLIBC_PRIVATE 1
# do not call strip
%global __os_install_post %{nil}

# do not provides/requires for all libs
%global __provides_exclude_from /opt/%{name}/(.*\.so|swiftshader/.*|resources/.*|locales/.*)$
%global __requires_exclude_from /opt/%{name}/.*$
%define __requires_exclude ^lib.*$

# Don't generate build_id links to prevent conflicts when installing multiple
# versions of VS Code alongside each other (e.g. `code` and `code-insiders`)
# https://github.com/microsoft/vscode/pull/116105/files
%define _build_id_links none

%description
NoSQLBooster is a cross-platform IDE for MongoDB Server, which provides a build-in MongoDB script debugger,
SQL query, server monitoring tools, chaining fluent query, query code generator, task scheduling, ES2020 support,
and advanced IntelliSense experience.

%prep
# http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html
%setup -c -D -n %{name}-%{version}

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
* Wed Feb 26 2025 ttyS3 <ttys3.rust@gmail.com> 9.1.6-1
- fix(build): use dynamic fedora release version in build scripts
  (ttys3.rust@gmail.com)

* Wed May 29 2024 ttyS3 <ttys3.rust@gmail.com> 8.1.9-1
- chore: change build script to f40 (ttys3.rust@gmail.com)
- fix: fix nosqlbooster4mongo.spec download url domain (ttys3.rust@gmail.com)
- fix: fix nosqlbooster4mongo sources (ttys3.rust@gmail.com)

* Sat Oct 28 2023 ttyS3 <ttys3.rust@gmail.com> 8.1.1-1
- chore: update build.sh to use f39 release param (ttys3.rust@gmail.com)


