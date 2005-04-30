
#
# todo:
# - emacs, idle and vim subpackages
#

# Conditional build:
%bcond_without tests	# disables testing
#
Summary:	Python Refactoring Browser
Summary(pl):	Przegl±darka do refaktoryzacji kodu w Pythonie
Name:		bicyclerepair
Version:	0.9
Release:	1
License:	BSD-like
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/bicyclerepair/%{name}-%{version}.tar.gz
# Source0-md5:	f825f48384febefacf0717738e909321
URL:		http://bicyclerepair.sourceforge.net/
BuildRequires:	python-modules >= 2.2.1
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bicycle Repair Man is the Python Refactoring Browser, helping
Pythonistas everywhere glide over the gory details of refactoring
their code. Watch him extract jumbled code into well ordered classes.
Gasp, as he renames all occurrences of a method. Thank You, Bicycle
Repair Man!

%description -l pl
Bicycle Repair Man ("Mechanik Rowerowy") to narzêdzie do refaktoryzacji
kodu ¼ród³owego napisanego w jêzyku Python, pozwalaj±ce programistom na
unikniêcie morderczej pracy zwi±zanej z ulepszaniem swojego kodu. 

Patrz, jak brzydki kod przekszta³ca siê w piêkne klasy. Tchu zabraknie Ci
ze zdziwienia, gdy zacznie zmieniaæ wszystkie wyst±pienia metody.
Dziêkujemy Ci, Mechaniku Rowerowy!

%prep
%setup -q

%build
python setup.py build

%{?with_tests:python -O testall.py -v}

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README*
%doc ide-integration/bike.vim
%{py_sitescriptdir}/*
