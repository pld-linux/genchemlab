Summary:	General Chemistry Lab Simulator - "GenChemLab"
Summary(pl.UTF-8):	Ogólny symulator labolatorium chemicznego
Name:		genchemlab
Version:	1.0
Release:	3
License:	GPL
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/genchemlab/%{name}-%{version}.tgz
# Source0-md5:	ef364cff3f3e2dba4c62a5d1a0084bae
Patch0:		%{name}-desktop.patch
URL:		http://genchemlab.sourceforge.net/
BuildRequires:	automake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GenChemLab is an OpenGL-based application intended to simulate several
common general chemistry exercises. It is meant to be used to help
students prepare for actual lab experience. It could also be used in
cases where laboratory facilites are not accessible, for instance in
K-12 schools or home schooling.

At present, supported experiments include titration, calorimetry,
freezing point depression, vapor pressure, and spectrophotometry.

%description -l pl.UTF-8
GenChemLab jest bazującą na OpenGL aplikacją przeznaczoną do symulacji
najpopularniejszych ćwiczeń chemicznych. Może być używana do
przygotowania przez studentów doświadczeń w laboratorium, lub w
miejscach gdzie laboratoria nie są publicznie dostępne jak nauka w
szkołach lub domu. Aktualnie są obsługiwane eksperymenty takie jak
miareczkowanie, kalorymetria, zmiana punktu zamrażania, ciśnienie pary
wodnej i spektrometria.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -sf %{_docdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/%{name}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc/*
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/doc
