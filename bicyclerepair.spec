
#
# todo:
# - emacs, idle and vim subpackages
#


%include	/usr/lib/rpm/macros.python

%define beta BETA3

Summary:	Python Refactoring Browser
Name:		bicyclerepair
Version:	0.9
Release:	0.%{beta}.1
License:	unknown
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-%{beta}.tar.gz
# Source0-md5:	c8c22c2a8133a72aaf30b3d105fe7499
URL:		http://bicyclerepair.sourceforge.net/
BuildRequires:	python-modules >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bicycle Repair Man is the Python Refactoring Browser, helping Pythonistas
everywhere glide over the gory details of refactoring their code. Watch him
extract jumbled code into well ordered classes. Gasp, as he renames all
occurrences of a method. Thank You, Bicycle Repair Man!

%prep
%setup -q -n %{name}-%{version}-%{beta}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog DESIGN NEWS README*
%doc ide-integration/bike.vim
#%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*
