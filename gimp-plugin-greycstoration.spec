Summary:	GREYCstoration plugin for GIMP
Summary(pl.UTF-8):	Wtyczka GREYCstoration dla GIMP-a
Name:		gimp-plugin-greycstoration
Version:	0.2.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Graphics
Source0:	http://www.haypocalc.com/perso/prog/greycstoration/greycstoration-%{version}.tar.bz2
# Source0-md5:	3ec7b4d5895a54fbc407916c318ef937
URL:		http://www.haypocalc.com/wiki/Gimp_Plugin_GREYCstoration
BuildRequires:	gimp-devel >= 1:2.2.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	pkgconfig
Requires:	gimp >= 1:2.2.0
Requires:	gtk+2 >= 2:2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GREYCstoration is a GIMP plugin using the algorithm written by David
Tschumperle from GREYC laboratory (at Caen in France). Current version
of the plugin only supports the restoration functionality, but the
algorithm can also do great picture resize or good inpainting.

%description -l en.UTF-8
GREYCstoration is a GIMP plugin using the algorithm written by David
Tschumperlé from GREYC laboratory (at Caen in France). Current version
of the plugin only supports the restoration functionality, but the
algorithm can also do great picture resize or good inpainting.

%description -l pl.UTF-8
GREYCstoration to wtyczka GIMP-a używająca algorytmu napisanego przez
Davida Tschumperlé z laboratorium GREYC (w Caen we Francji). Aktualna
wersja wtyczki obsługuje tylko funkcjonalność restaurowania, ale
algorytm można wykorzystać także do przeskalowywania i domalowywania
obrazów.

%prep
%setup -q -n greycstoration-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gimp20-greycstoration

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gimp20-greycstoration.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/gimp/2.0/plug-ins/greycstoration
