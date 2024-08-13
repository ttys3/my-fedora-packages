%undefine _debugsource_packages
%global _version 0.5.0

Name:           quickjs
Version:        %{_version}
Release:        2
Summary:        A small and embeddable Javascript engine
License:        BSD
URL:            https://github.com/quickjs-ng/quickjs
Source0:	    https://github.com/quickjs-ng/quickjs/archive/refs/tags/v%{_version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake
BuildRequires: sed

%package devel
Summary:	Development files for package %{name}
Requires:	%{name}

%description
QuickJS supports the ES2020 specification 1 including modules, asynchronous
generators, proxies and BigInt. It supports mathematical extensions such as
big decimal float float numbers (BigDecimal), big binary floating point numbers
(BigFloat), and operator overloading.

%description devel
Header files and Libraries for package %{name}.

%prep
%setup -q -n quickjs-%{_version}

%build
# ref https://docs.fedoraproject.org/en-US/packaging-guidelines/CMake/
%cmake -DBUILD_SHARED_LIBS=OFF -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/quickjs -DCMAKE_INSTALL_LIBDIR=/usr/lib64
%cmake_build

%install
%cmake_install

%files
%doc LICENSE doc/*
%{_bindir}/*

%files devel
%exclude /usr/share/doc/quickjs/examples/*
%{_includedir}/*
%{_libdir}/*

%changelog
* Tue Jan 17 2023 Zephyr Lykos <fedora@mochaa.ws> - 2021.03.27-2
- Fix qjsc library path
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2021.03.27-1
- Rebuilt for Fedora
