# ToDo:
#  - pl descirption
#  - split?
Summary:	library to find what country an IP address or hostnames originate from
Summary(pl):	biblioteka do sprawdzenia z jakiego kraju adres IP lub domena pochodzi
Name:		GeoIP
Version:	1.2.0
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://www.maxmind.com/download/geoip/api/c/%{name}-%{version}.tar.gz
Patch0:		%{name}-man-makefile.patch
URL:		http://www.maxmind.com/app/c
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GeoIP is a C library that enables the user to find the country that any IP
address or hostname originates from. It uses a file based database that is
accurate as of March 2003. This database simply contains IP blocks as keys,
and countries as values. This database should be more complete and accurate
than using reverse DNS lookups. Commercial databases and automatic update
services are available from http://www.maxmind.com/

This module can be used to automatically select the geographically closest
mirror, to analyze your web server logs to determine the countries of your
visitors, for credit card fraud detection, and for software export controls.

%prep
%setup -q
%patch0 -p0

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_sysconfdir}/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/*/*
