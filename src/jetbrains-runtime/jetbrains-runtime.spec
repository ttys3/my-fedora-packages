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
mkdir -p %{buildroot}/opt/jbr/
cp -r * %{buildroot}/opt/jbr/

%files
/opt/jbr/

%changelog
* Thu Feb 17 2023 John Doe <john.doe@chat.openai.com> - 11.0.16
- Initial RPM release
