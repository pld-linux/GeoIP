Summary:	Library to find what country an IP address or hostnames originate from
Summary(pl):	Biblioteka do sprawdzenia z jakiego kraju pochodzi adres IP lub domena
Name:		GeoIP
Version:	1.3.6
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.maxmind.com/download/geoip/api/c/%{name}-%{version}.tar.gz
# Source0-md5:	f5afa496b562a7524b9b33b1d30dbee9
# note: "c" is a filename, do not add '/'
URL:		http://www.maxmind.com/app/c
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GeoIP is a C library that enables the user to find the country that
any IP address or hostname originates from. It uses a file based
database that is accurate as of March 2003. This database simply
contains IP blocks as keys, and countries as values. This database
should be more complete and accurate than using reverse DNS lookups.
Commercial databases and automatic update services are available from
http://www.maxmind.com/.

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
http://www.maxmind.com/.

Ta biblioteka mo¿e byæ u¿ywana do automatycznego wyboru najbli¿szego
geograficznie mirrora, analizy logów serwera WWW w celu okre¶lenia
kraju, z którego pochodz± odwiedzaj±cy, do wykrywania oszustw
dotycz±cych kart kredytowych oraz kontroli eksportu oprogramowania.

%package devel
Summary:	Header files for GeoIP library
Summary(pl):	Pliki nag³ówkowe biblioteki GeoIP
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for GeoIP library.

%description devel -l pl
Pliki nag³ówkowe biblioteki GeoIP.

%package static
Summary:	Static GeoIP library
Summary(pl):	Statyczna biblioteka GeoIP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static GeoIP library.

%description static -l pl
Statyczna biblioteka GeoIP.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/GeoIP.conf
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
