Summary:	Library to find what country an IP address or hostnames originate from
Summary(pl.UTF-8):	Biblioteka do sprawdzenia z jakiego kraju pochodzi adres IP lub domena
Name:		GeoIP
Version:	1.4.5
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.maxmind.com/download/geoip/api/c/%{name}-%{version}.tar.gz
# Source0-md5:	d95c34cf8ebd48e357b1812db5d75cf1
# note: "c" is a filename, do not add '/'
URL:		http://www.maxmind.com/app/c
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GeoIP is a C library that enables the user to find the country that
any IP address or hostname originates from. It uses a file based
database that is accurate as of March 2003. This database simply
contains IP blocks as keys, and countries as values. This database
should be more complete and accurate than using reverse DNS lookups.
Commercial databases and automatic update services are available from
<http://www.maxmind.com/>.

This library can be used to automatically select the geographically
closest mirror, to analyze your web server logs to determine the
countries of your visitors, for credit card fraud detection, and for
software export controls.

%description -l pl.UTF-8
GeoIP jest biblioteką napisaną w C umożliwiającą użytkownikowi
odnalezienie państwa, z którego pochodzi dany adres IP lub domena.
Używa do tego zapisanej w pliku bazy danych (z marca 2003). W bazie
tej adresy IP są kluczami, a państwa wartościami. Powinna ona być
dokładniejsza niż sprawdzanie odwrotnego DNS. Komercyjne bazy oraz
usługi automatycznych aktualizacji dostępne są na stronie
<http://www.maxmind.com/>.

Ta biblioteka może być używana do automatycznego wyboru najbliższego
geograficznie mirrora, analizy logów serwera WWW w celu określenia
kraju, z którego pochodzą odwiedzający, do wykrywania oszustw
dotyczących kart kredytowych oraz kontroli eksportu oprogramowania.

%package libs
Summary:	GeoIP Library
Summary(pl.UTF-8):	Biblioteka GeoIP
Group:		Libraries
Conflicts:	GeoIP < 1.4.0-2

%description libs
GeoIP library.

%description libs -l pl.UTF-8
Biblioteka GeoIP.

%package devel
Summary:	Header files for GeoIP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GeoIP
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for GeoIP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GeoIP.

%package static
Summary:	Static GeoIP library
Summary(pl.UTF-8):	Statyczna biblioteka GeoIP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GeoIP library.

%description static -l pl.UTF-8
Statyczna biblioteka GeoIP.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/GeoIP.conf.default

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/GeoIP.conf
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
