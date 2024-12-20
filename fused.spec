Name:          fused
Version:       1.0.0
Release:       1%{?relval}%{?dist}
Summary:       DAOS File System in Userspace Library

License:       LGPLv2+
URL:           https://github.com/daos-stack/fused
Source0:       https://github.com/daos-stack/%{name}/releases/download/%{shortcommit0}/%{name}-%{version}.tar.gz

Requires:      which
Conflicts:     filesystem < 3
BuildRequires: libselinux-devel
BuildRequires: meson, gcc-c++, gcc

%description
This package builds on FUSE but implements a completely custom file
system intended for use with the DAOS file system.

%package devel
Summary:   DAOS File System in Userspace based on (FUSE) v3 libraries and headers
Group:     System Environment/Libraries
License:   LGPLv2+
Conflicts: filesystem < 3
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description devel
Provides a user space library and headers for DAOS specific FUSE filesystem

%global debug_package %{nil}

%prep
%autosetup

%build
%meson --strip -Ddisable-mtab=True -Dutils=False --default-library shared
%meson_build

%install
export MESON_INSTALL_DESTDIR_PREFIX=%{buildroot}/usr %meson_install
find %{buildroot} .
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/libfused.so.*

%files devel
%{_libdir}/libfused.so
%{_includedir}/fused/
%{_libdir}/pkgconfig

%changelog
* Mon Feb 12 2024 Jeff Olivier <jeffolivier@google.com> - 1.0.0-1.0
- Initial packaging for fused, a DAOS file system adaptation of libfused
