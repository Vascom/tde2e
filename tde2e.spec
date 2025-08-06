# This package contains only static libraries.
%global debug_package %{nil}

# The upstream doesn't tag versions, so snapshot have to be used.
%global commit bb474a201baa798784d696d2d9d762a9d2807f96

Name: tde2e
Version: 1.8.51
Release: %autorelease

License: BSL-1.0
URL: https://github.com/tdlib/td
Summary: Cross-platform library for building Telegram clients
Source0: %{url}/archive/%{commit}/tdlib-%{version}.tar.gz

BuildRequires: abseil-cpp-devel
BuildRequires: google-crc32c-devel
BuildRequires: gperftools-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: ninja-build

%description
TDE2E is a cross-platform library for building Telegram clients.

%package devel
Summary: Development files for %{name}
Provides:   %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:  tdlib-devel

%description devel
%{summary}.

%prep
%autosetup -n td-%{commit} -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DBUILD_TESTING:BOOL=OFF \
    -DTD_ENABLE_JNI:BOOL=OFF \
    -DTD_ENABLE_DOTNET:BOOL=OFF \
    -DTD_WITH_ABSEIL:BOOL=ON \
    -DTD_E2E_ONLY:BOOL=ON \
    -DTDE2E_ENABLE_INSTALL:BOOL=ON \
    -DTDE2E_INSTALL_INCLUDES:BOOL=ON
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE_1_0.txt
%doc README.md
%{_includedir}/td/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/td*.pc
%{_libdir}/libtd*.a

%changelog
%autochangelog
