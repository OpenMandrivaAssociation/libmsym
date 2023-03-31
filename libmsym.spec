%define major 0
%define libname %mklibname msym %{major}
%define devname %mklibname -d msym

Name:		libmsym
Version:	0.2.3
Release:	3
License:	MIT
Source0:	https://github.com/mcodev31/libmsym/archive/v%{version}.tar.gz
Patch0:		libmsym-0.2.3-lib64.patch
Group:		System/Libraries
Summary:	Molecular Point Group Symmetry library
BuildRequires:	cmake
BuildRequires:	ninja

%description
Molecular Point Group Symmetry library

%package -n %{libname}
Summary:	Molecular Point Group Symmetry library
Group:		System/Libraries

%description -n %{libname}
Molecular Point Group Symmetry library

%package -n %{devname}
Summary:	Development files for the Molecular Point Group Symmetry library
Group:		Development/C++ and C
Requires:	%{libname} = %{EVRD}
Provides:	msym-devel = %{EVRD}

%description -n %{devname}
Development files for the Molecular Point Group Symmetry library

%prep
%autosetup -p1
%cmake -G Ninja -DINSTALL_LIB_DIR=%{_lib}

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libmsym.so.%{major}*

%files -n %{devname}
%{_includedir}/libmsym
%{_libdir}/libmsym.so
%{_prefix}/lib/cmake/libmsym
