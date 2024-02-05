# thanks to https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=pack-cli

Name: pack
Version: 0.33.0
Release: 1%{?dist}
Summary: CLI for building apps using Cloud Native Buildpacks
License: Apache-2.0 license
URL: https://github.com/buildpacks/pack

# https://github.com/buildpacks/pack/releases/download/v0.33.0/pack-v0.33.0-linux.tgz
Source0: https://github.com/buildpacks/pack/releases/download/v0.33.0/%{name}-v%{version}-linux.tgz

BuildArch: x86_64

# do not call strip
%global __os_install_post %{nil}

%description
Cloud Native Buildpacks makes building container images as easy as running “pack build.” 
However, you will eventually want to customize that out-of-the-box experience. 
This talk explores the many buildpacks extension points that enable custom workflows. 
For application developers, we introduce inline buildpacks and build time environment variables. 
For platform operators, we present image extension with Dockerfiles, 
and how to control the level of customization available in order to adhere to security requirements.

%prep
# http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html
%setup -c -D -n %{name}-%{version}

ls -lhp

%install
mkdir -p %{buildroot}/usr/local/bin/

ls -lhp

install -Dm755 %{name} %{buildroot}/usr/local/bin/%{name}

%files
/usr/local/bin/%{name}

%changelog
* Mon Feb 05 2024 ttyS3 <ttys3.rust@gmail.com> 0.33.0-1
- new package built with tito




