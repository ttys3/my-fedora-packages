# https://bugzilla.redhat.com/show_bug.cgi?id=1869423
%global __filter_GLIBC_PRIVATE 1
# do not call strip
%global __os_install_post %{nil}
# do not provides/requires for 115 private lib
%global __provides_exclude_from /opt/115pc/(lib/.*|plugins/.*)$
%global __requires_exclude_from /opt/115pc/(lib/.*|plugins/.*)$
%global __requires_exclude ^(libQt5.*|libav.*|libswresample.*)$

Name: 115pc
Version: 2.0.2.9
Release: 1%{?dist}
Summary: 115 PC client for Linux
License: 115 License Agreement
URL: https://pc.115.com/
Source0: https://down.115.com/client/%{name}/lin/%{name}_%{version}.deb
BuildArch: x86_64
BuildRequires: alien

%description
115 PC client for Linux

%prep
# use our own way to extract the files
cp -p %{SOURCE0} .
rm -rf %{name}pc-%{version}
alien -t -g %{name}pc_%{version}.deb
%setup -T -D

%install
mkdir -p %{buildroot}/opt


install -Dm644 usr/share/applications/%{name}.desktop %{buildroot}/usr/share/applications/%{name}.desktop
install -Dm644 ${srcdir}/usr/local/115/res/115.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/%{name}.png
cp -aT usr/local/115 %{buildroot}/opt/%{name}

# hack for Wayland
install -m 755 115.sh %{buildroot}/opt/%{name}/

# do not update via client
echo '#!/bin/bash' > opt/%{name}/update.sh
echo "echo 'only support update via dnf'" >> opt/%{name}/update.sh

# permission tweaks
chmod a+x opt/%{name}/libexec/QtWebEngineProcess

%files
/opt/115pc
/usr/share/applications/%{name}.desktop
/usr/share/icons/hicolor/256x256/apps/%{name}.png

%changelog
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
