Summary:	General Chemistry Lab Simulator - "GenChemLab"
Summary(pl):	Ogólny symulator labolatorium chemicznego
Name:		genchemlab
Version:	1.0
Release:	1
Source0:	http://dl.sourceforge.net/genchemlab/%{name}-%{version}.tgz
# Source0-md5:	ef364cff3f3e2dba4c62a5d1a0084bae
URL:		http://genchemlab.sourceforge.net/
License:	GPL
Group:		X11/Applications/Science
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

%description -l pl
GenChemLab jest bazuj±c± na OpenGL aplikacj± przeznaczon± do symulacji
najpopularniejszych æwiczeñ chemicznych. Mo¿e byæ u¿ywana do
przygotowania przez studentów do¶wiadczeñ w labolatorium, lub w
miejscach gdzie labolatoria nie s± publicznie dostêpne jak nauka w
szko³ach lub domu. Aktualnie s± obs³ugiwane eksperymenty takie jak
miareczkowanie, kalorymetria, zmiana punktu zamra¿ania, ci¶nienie pary
wodnej i spektrometria.

%prep
%setup -q

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
