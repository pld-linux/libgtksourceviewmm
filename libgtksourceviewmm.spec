#
# Conditional build:
%bcond_without	apidocs		# don't generate documentation with doxygen
#
Summary:	A C++ binding of GtkSourceView
Summary(pl.UTF-8):	Wiązania C++ dla GtkSourceView
Name:		libgtksourceviewmm
Version:	0.3.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgtksourceviewmm/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	9f5a6bd4f523a7dc0f6256122e48848d
URL:		http://home.gna.org/gtksourceviewmm/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	gtkmm-devel >= 2.10.8
BuildRequires:	gtksourceview-devel >= 1.8.5
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSourceViewMM is a C++ binding of GtkSourceView, an extension to the
text widget included in GTK+ 2.x adding syntax highlighting and other
features typical for a source file editor.

%description -l pl.UTF-8
GtkSourceViewMM to wiązania C++ dla GtkSourceView - rozszerzenia
tekstowego widgetu będącego częścią GTK+ 2.x, dodającego kolorowanie
składni oraz inne właściwości typowe dla edytora kodu źródłowego.

%package devel
Summary:	Header files for libgtksourceviewmm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgtksourceviewmm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libgtksourceviewmm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgtksourceviewmm.

%package static
Summary:	Static libgtksourceviewmm library
Summary(pl.UTF-8):	Statyczna biblioteka libgtksourceviewmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgtksourceviewmm library.

%description static -l pl.UTF-8
Statyczna biblioteka libgtksourceviewmm.

%package apidocs
Summary:	libgtksourceviewmm API documentation
Summary(pl.UTF-8):	Dokumentacja API libgtksourceviewmm
Group:		Documentation

%description apidocs
libgtksourceviewmm API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgtksourceviewmm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-docs \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with apidocs}
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-1.0
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgtksourceviewmm-1.0.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourceviewmm-1.0.so
%{_libdir}/libgtksourceviewmm-1.0.la
%{_libdir}/gtksourceviewmm-1.0
%{_includedir}/gtksourceviewmm-1.0
%{_pkgconfigdir}/libgtksourceviewmm-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtksourceviewmm-1.0.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc docs/reference/html
%endif
