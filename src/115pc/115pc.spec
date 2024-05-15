# thanks to https://github.com/liuhangbin/115/blob/main/115.spec
# thanks to https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=115pc

Name: 115pc
Version: 2.0.10.2
Release: 1%{?dist}
Summary: 115 PC client for Linux
License: 115 License Agreement
URL: https://pc.115.com/

# https://down.115.com/client/115pc/lin/115_v2.0.10.2.deb
Source0: https://down.115.com/client/%{name}/lin/115_v%{version}.deb
Source1: 115.sh

BuildArch: x86_64
BuildRequires: alien

# https://bugzilla.redhat.com/show_bug.cgi?id=1869423
%global __filter_GLIBC_PRIVATE 1
# do not call strip
%global __os_install_post %{nil}
# do not provides/requires for 115 private lib
%global __provides_exclude_from /opt/%{name}/(lib/.*|plugins/.*)$
%global __requires_exclude_from /opt/%{name}/(lib/.*|plugins/.*)$
%global __requires_exclude ^(libQt5.*|libav.*|libswresample.*)$

%description
115 PC client for Linux

%prep
# use our own way to extract the files
cp -p %{SOURCE0} .
rm -rf %{name}-%{version}

# https://manpages.debian.org/unstable/alien/alien.1p.en.html
alien -v -t -g 115_v%{version}.deb

ls -lhp
# 115-2.0.8.5

mv 115-%{version} %{name}-%{version}

%setup -T -D -n %{name}-%{version}

%install
mkdir -p %{buildroot}/opt

ls -lhp

install -Dm644 usr/share/applications/115.desktop %{buildroot}/usr/share/applications/%{name}.desktop

sed -i 's|/usr/local/115|/opt/%{name}|g' %{buildroot}/usr/share/applications/%{name}.desktop

#install -Dm644 usr/local/115/res/115.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/%{name}.png

cp -aT usr/local/115 %{buildroot}/opt/%{name}

# hack for Wayland
install -m 755 %{_sourcedir}/115.sh %{buildroot}/opt/%{name}/

# do not update via client
echo '#!/bin/bash' > %{buildroot}/opt/%{name}/update.sh
echo "echo 'only support update via dnf'" >> %{buildroot}/opt/%{name}/update.sh

# permission tweaks
chmod a+x %{buildroot}/opt/%{name}/libexec/QtWebEngineProcess

%files
/opt/%{name}
/usr/share/applications/%{name}.desktop

%changelog
* Thu May 16 2024 ttyS3 <ttys3.rust@gmail.com> 2.0.10.2-1
- chore: change build script to f40 (ttys3.rust@gmail.com)
- chore: fix warning (ttys3.rust@gmail.com)
- chore: add build.sh for 115pc (ttys3.rust@gmail.com)

* Tue Mar 19 2024 ttyS3 <ttys3.rust@gmail.com> 2.0.9.3-1
-

* Sat Mar 02 2024 ttyS3 <ttys3.rust@gmail.com>
-

* Thu Feb 22 2024 ttyS3 <ttys3.rust@gmail.com>
- update to https://down.115.com/client/115pc/lin/115pc_2.0.7.9.deb

* Sat Oct 28 2023 ttyS3 <ttys3.rust@gmail.com> 2.0.6.6-1
-

* Sun Dec 25 2022 Hangbin Liu <liuhangbin@gmail.com> - 2.0.2.9-1
- Update to 2.0.2.9

* Mon Oct 10 2022 Hangbin Liu <liuhangbin@gmail.com> - 2.0.1.7-1
- Update to 2.0.1.7

* Tue Sep 6 2022 Hangbin Liu <liuhangbin@gmail.com> - 2.0.0.19-1
- Update to 2.0.0.19

* Tue Jul 19 2022 Hangbin Liu <liuhangbin@gmail.com> - 1.0.8.9-1
- Update to 1.0.8.9

* Wed Jun 15 2022 Hangbin Liu <liuhangbin@gmail.com> - 1.0.7.7-1
- Update to 1.0.7.7

* Thu May 12 2022 Hangbin Liu <liuhangbin@gmail.com> - 1.0.6.7-2
- Do not update via client by default

* Thu May 12 2022 Hangbin Liu <liuhangbin@gmail.com> - 1.0.6.7-1
- Update to 1.0.6.7

* Wed Apr 27 2022 Hangbin Liu <liuhangbin@gmail.com> - 1.0.5.18-1
- Update to 1.0.5.18

* Mon Mar 7 2022 Hangbin Liu <liuhangbin@gmail.com> - 1.0.1-6
- Update to 1.0.1-6

* Mon Mar 7 2022 Hangbin Liu <liuhangbin@gmail.com> - 1.0.0-16
- Initial build
