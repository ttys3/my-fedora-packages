%global __provides_exclude_from ^%{?name}-.*
%global __requires_exclude ^(.*)$
%global debug_package %{nil}
%global _binaries_in_noarch_packages_terminate_build 0
# Don't generate build_id links to prevent conflicts when installing multiple
# versions of VS Code alongside each other (e.g. `code` and `code-insiders`)
# https://github.com/microsoft/vscode/pull/116105/files
%define _build_id_links none
# do not call strip
%global __os_install_post %{nil}
AutoReqProv: no

Name: jetbrains-runtime
Version: 11.0.16
Release: 1%{?dist}
Summary: JetBrains Runtime
License: GPLv2+
URL: https://www.jetbrains.com/
Source0: https://cache-redirector.jetbrains.com/intellij-jbr/jbr_dcevm-11_0_16-linux-x64-b2043.64.tar.gz

%description
JetBrains Runtime is a Java Runtime Environment developed by JetBrains.

This 11 version is espacially for old software like Charles proxy.

%prep
%setup -q -c
%setup -q -T -D -a 0

%build

%install
# Install the JetBrains Runtime Environment to /opt/jbr
install -d %{buildroot}/opt/jbr
cp -R %{_builddir}/%{name}-%{version}/jbr/* %{buildroot}/opt/jbr/

%files
/opt/jbr/

%changelog
* Thu Feb 17 2023 John Doe <john.doe@chat.openai.com> - 11.0.16
- Initial RPM release
