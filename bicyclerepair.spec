
#
# todo:
# - emacs, idle and vim subpackages
#

# Conditional build:
%bcond_without tests	# disables testing
#
Summary:	Python Refactoring Browser
Name:		bicyclerepair
Version:	0.9
%define beta	BETA4
Release:	0.%{beta}.1
License:	BSD-like
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-%{beta}.tar.gz
# Source0-md5:	635287697aa7f3bb580267e9df203f89
URL:		http://bicyclerepair.sourceforge.net/
BuildRequires:	python-modules >= 2.2.1
BuildRequires:	rpm-pythonprov
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
%setup -q -n %{name}-%{version}-%{beta}

%build
python setup.py build

%{?with_tests:python -O testall.py -v}

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog DESIGN NEWS README*
%doc ide-integration/bike.vim
#%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*
