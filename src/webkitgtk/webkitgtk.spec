## NOTE: Lots of files in various subdirectories have the same name (such as
## "LICENSE") so this short macro allows us to distinguish them by using their
## directory names (from the source tree) as prefixes for the files.
%global add_to_license_files() \
        mkdir -p _license_files ; \
        cp -p %1 _license_files/$(echo '%1' | sed -e 's!/!.!g')

# No libmanette in RHEL
%if !0%{?rhel}
%global with_gamepad 1
%endif

# Build documentation by default (use `rpmbuild --without docs` to override it).
# This is used by Coverity. Coverity injects custom compiler warnings, but
# any warning during WebKit docs build is fatal!
%bcond_without docs

Name:           webkitgtk
Version:        2.38.5
Release:        %autorelease
Summary:        GTK web content engine library

License:        LGPLv2
URL:            https://www.webkitgtk.org/
Source0:        https://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz
Source1:        https://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz.asc
# Use the keys from https://webkitgtk.org/verifying.html
# $ gpg --import aperez.key carlosgc.key
# $ gpg --export --export-options export-minimal D7FCF61CF9A2DEAB31D81BD3F3D322D0EC4582C3 5AA3BC334FD7E3369E7C77B291C559DBE4C9123B > webkitgtk-keys.gpg
Source2:        webkitgtk-keys.gpg

Patch0:         PasteboardGtk.cpp.patch

BuildRequires:  bison
BuildRequires:  bubblewrap
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  git
BuildRequires:  gnupg2
BuildRequires:  gperf
BuildRequires:  hyphen-devel
BuildRequires:  libatomic
BuildRequires:  ninja-build
BuildRequires:  perl(English)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::PP)
BuildRequires:  python3
BuildRequires:  ruby
BuildRequires:  rubygems
BuildRequires:  rubygem-json
BuildRequires:  xdg-dbus-proxy

BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwoff2dec)
BuildRequires:  pkgconfig(libxslt)
%if 0%{?with_gamepad}
BuildRequires:  pkgconfig(manette-0.2)
%endif
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wpe-1.0)
BuildRequires:  pkgconfig(wpebackend-fdo-1.0)
BuildRequires:  pkgconfig(xt)

# Filter out provides for private libraries
%global __provides_exclude_from ^(%{_libdir}/webkit2gtk-5\\.0/.*\\.so)$

%description
WebKitGTK is the port of the WebKit web rendering engine to the
GTK platform.

%package -n     webkit2gtk5.0
Summary:        WebKitGTK for GTK 4
Requires:       javascriptcoregtk5.0%{?_isa} = %{version}-%{release}
Requires:       bubblewrap
Requires:       xdg-dbus-proxy
Recommends:     geoclue2
Recommends:     gstreamer1-plugins-bad-free
Recommends:     gstreamer1-plugins-good
Recommends:     xdg-desktop-portal-gtk
Provides:       bundled(angle)
Provides:       bundled(pdfjs)
Provides:       bundled(xdgmime)

%description -n webkit2gtk5.0
WebKitGTK is the port of the WebKit web rendering engine to the
GTK platform. This package contains WebKitGTK for GTK 4.

%package -n     webkit2gtk5.0-devel
Summary:        Development files for webkit2gtk5.0
Requires:       webkit2gtk5.0%{?_isa} = %{version}-%{release}
Requires:       javascriptcoregtk5.0%{?_isa} = %{version}-%{release}
Requires:       javascriptcoregtk5.0-devel%{?_isa} = %{version}-%{release}

%description -n webkit2gtk5.0-devel
The webkit2gtk5.0-devel package contains libraries, build data, and header
files for developing applications that use webkit2gtk5.0.

%if %{with docs}
%package -n     webkit2gtk5.0-doc
Summary:        Documentation files for webkit2gtk5.0
BuildArch:      noarch
Requires:       webkit2gtk5.0 = %{version}-%{release}

%description -n webkit2gtk5.0-doc
This package contains developer documentation for webkit2gtk5.0.

%endif

%package -n     javascriptcoregtk5.0
Summary:        JavaScript engine from webkit2gtk5.0

%description -n javascriptcoregtk5.0
This package contains JavaScript engine from webkit2gtk5.0.

%package -n     javascriptcoregtk5.0-devel
Summary:        Development files for JavaScript engine from webkit2gtk5.0
Requires:       javascriptcoregtk5.0%{?_isa} = %{version}-%{release}

%description -n javascriptcoregtk5.0-devel
The javascriptcoregtk5.0-devel package contains libraries, build data, and header
files for developing applications that use JavaScript engine from webkit2gtk-5.0.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n webkitgtk-%{version}

%build

# disable build debuginfo packages
# or --rpmbuild-options for tito ?
# ref https://docs.fedoraproject.org/en-US/packaging-guidelines/Debuginfo/#_useless_or_incomplete_debuginfo_packages_due_to_other_reasons
%global debug_package %{nil}

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkit2gtk-5.0
%cmake \
  -GNinja \
  -DPORT=GTK \
  -DCMAKE_BUILD_TYPE=Release \
  -DUSE_GTK4=ON \
  -DENABLE_WEBDRIVER=OFF \
%if %{without docs}
  -DENABLE_DOCUMENTATION=OFF \
%endif
%if !0%{?with_gamepad}
  -DENABLE_GAMEPAD=OFF \
%endif
%if 0%{?rhel}
%ifarch aarch64
  -DENABLE_JIT=OFF \
  -DUSE_SYSTEM_MALLOC=ON \
%endif
%endif
  %{nil}

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkit2gtk-5.0
export NINJA_STATUS=" ?????? [1/1][%f/%t %es] "
%cmake_build %limit_build -m 3072

%install
%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkit2gtk-5.0
%cmake_install

%find_lang WebKit2GTK-5.0

# Finally, copy over and rename various files for %%license inclusion
%add_to_license_files Source/JavaScriptCore/COPYING.LIB
%add_to_license_files Source/ThirdParty/ANGLE/LICENSE
%add_to_license_files Source/ThirdParty/ANGLE/src/common/third_party/smhasher/LICENSE
%add_to_license_files Source/ThirdParty/ANGLE/src/third_party/libXNVCtrl/LICENSE
%add_to_license_files Source/WebCore/LICENSE-APPLE
%add_to_license_files Source/WebCore/LICENSE-LGPL-2
%add_to_license_files Source/WebCore/LICENSE-LGPL-2.1
%add_to_license_files Source/WebInspectorUI/UserInterface/External/CodeMirror/LICENSE
%add_to_license_files Source/WebInspectorUI/UserInterface/External/Esprima/LICENSE
%add_to_license_files Source/WebInspectorUI/UserInterface/External/three.js/LICENSE
%add_to_license_files Source/WTF/icu/LICENSE
%add_to_license_files Source/WTF/wtf/dtoa/COPYING
%add_to_license_files Source/WTF/wtf/dtoa/LICENSE

%files -n webkit2gtk5.0 -f WebKit2GTK-5.0.lang
%license _license_files/*ThirdParty*
%license _license_files/*WebCore*
%license _license_files/*WebInspectorUI*
%license _license_files/*WTF*
%{_libdir}/libwebkit2gtk-5.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/WebKit2-5.0.typelib
%{_libdir}/girepository-1.0/WebKit2WebExtension-5.0.typelib
%{_libdir}/webkit2gtk-5.0/
%{_libexecdir}/webkit2gtk-5.0/
%exclude %{_libexecdir}/webkit2gtk-5.0/MiniBrowser
%exclude %{_libexecdir}/webkit2gtk-5.0/jsc
# drop /usr/bin/WebKitWebDriver to avoid conflict with webkit2gtk4.1 provided one
#%{_bindir}/WebKitWebDriver

%files -n webkit2gtk5.0-devel
%{_libexecdir}/webkit2gtk-5.0/MiniBrowser
%{_includedir}/webkitgtk-5.0/
%exclude %{_includedir}/webkitgtk-5.0/JavaScriptCore
%exclude %{_includedir}/webkitgtk-5.0/jsc
%{_libdir}/libwebkit2gtk-5.0.so
%{_libdir}/pkgconfig/webkit2gtk-5.0.pc
%{_libdir}/pkgconfig/webkit2gtk-web-extension-5.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/WebKit2-5.0.gir
%{_datadir}/gir-1.0/WebKit2WebExtension-5.0.gir

%files -n javascriptcoregtk5.0
%license _license_files/*JavaScriptCore*
%{_libdir}/libjavascriptcoregtk-5.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/JavaScriptCore-5.0.typelib

%files -n javascriptcoregtk5.0-devel
%{_libexecdir}/webkit2gtk-5.0/jsc
%dir %{_includedir}/webkitgtk-5.0
%{_includedir}/webkitgtk-5.0/JavaScriptCore/
%{_includedir}/webkitgtk-5.0/jsc/
%{_libdir}/libjavascriptcoregtk-5.0.so
%{_libdir}/pkgconfig/javascriptcoregtk-5.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/JavaScriptCore-5.0.gir

%if %{with docs}
%files -n webkit2gtk5.0-doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/javascriptcoregtk-5.0/
%{_datadir}/gtk-doc/html/webkit2gtk-5.0/
%{_datadir}/gtk-doc/html/webkit2gtk-web-extension-5.0/

%endif

%changelog
* Tue Feb 14 2023 ttyS3 2.38.4-1
- add PasteboardGtk patch, fixup paste image bug
%autochangelog
