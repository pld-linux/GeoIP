Summary:	Library to find what country an IP address or hostnames originate from
Summary(pl):	Biblioteka do sprawdzenia z jakiego kraju pochodzi adres IP lub domena
Name:		GeoIP
Version:	1.4.0
Release:	3
License:	GPL v2
Group:		Libraries
Source0:	http://www.maxmind.com/download/geoip/api/c/%{name}-%{version}.tar.gz
# Source0-md5:	da09a3d9a1a91e3d16c0a29e6b056c15
Patch0:		%{name}-link.patch
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

%description -l pl
GeoIP jest bibliotek± napisan± w C umo¿liwiaj±c± u¿ytkownikowi
odnalezienie pañstwa, z którego pochodzi dany adres IP lub domena.
U¿ywa do tego zapisanej w pliku bazy danych (z marca 2003). W bazie
tej adresy IP s± kluczami, a pañstwa warto¶ciami. Powinna ona byæ
dok³adniejsza ni¿ sprawdzanie odwrotnego DNS. Komercyjne bazy oraz
us³ugi automatycznych aktualizacji dostêpne s± na stronie
<http://www.maxmind.com/>.

Ta biblioteka mo¿e byæ u¿ywana do automatycznego wyboru najbli¿szego
geograficznie mirrora, analizy logów serwera WWW w celu okre¶lenia
kraju, z którego pochodz± odwiedzaj±cy, do wykrywania oszustw
dotycz±cych kart kredytowych oraz kontroli eksportu oprogramowania.

%package libs
Summary:	GeoIP Library
Summary(pl):	Biblioteka GeoIP
Group:		Libraries
Conflicts:	GeoIP < 1.4.0-2

%description libs
GeoIP library.

%description libs -l pl
Biblioteka GeoIP.

%package devel
Summary:	Header files for GeoIP library
Summary(pl):	Pliki nag³ówkowe biblioteki GeoIP
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for GeoIP library.

%description devel -l pl
Pliki nag³ówkowe biblioteki GeoIP.

%package static
Summary:	Static GeoIP library
Summary(pl):	Statyczna biblioteka GeoIP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GeoIP library.

%description static -l pl
Statyczna biblioteka GeoIP.

%prep
%setup -q
%patch0 -p1 

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
