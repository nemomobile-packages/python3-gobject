%define upstream_name pygobject
%define source_subtree %{upstream_name}-%{version}
%define python_version python3

Name:		%{python_version}-gobject
Version:	3.12.1
Release:	1
Summary:	Python 3 bindings for GObject Introspection

Group:		System Environment/Libraries
License:	MIT
URL:		http://ftp.gnome.org/pub/GNOME/sources/pygobject/3.12/
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	%{python_version}-devel
BuildRequires:	pkgconfig(glib-2.0) >= 2.38.0
BuildRequires:	pkgconfig(py3cairo)
Requires:	%{python_version}-base

%description
%{summary}.

%package devel
Summary:        Python 3 bindings for GObject Introspection (development headers)
Requires:       %{name} = %{version}

%description devel
%{summary}.

%prep
%setup -q

%build
cd %{source_subtree}
# Make sure it builds against the right Python version
%configure PYTHON=%{python_version}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd %{source_subtree}
make install DESTDIR=$RPM_BUILD_ROOT

# Remove .la files
find $RPM_BUILD_ROOT -name '*.la' -exec rm {} +

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/%{python_version}.*/site-packages/gi
%{_libdir}/%{python_version}.*/site-packages/pygtkcompat
%{_libdir}/%{python_version}.*/site-packages/%{upstream_name}-%{version}-*.egg-info

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{upstream_name}-3.0/%{upstream_name}.h
%{_libdir}/pkgconfig/%{upstream_name}-3.0.pc
