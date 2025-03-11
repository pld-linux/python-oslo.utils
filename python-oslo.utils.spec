#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (missing deps)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Oslo Utility library
Summary(pl.UTF-8):	Biblioteka narzędziowa Oslo
Name:		python-oslo.utils
# keep 3.x here for python2 support
Version:	3.42.1
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/o/oslo.utils/oslo.utils-%{version}.tar.gz
# Source0-md5:	bc6550abc4199f01c74261b9d641de36
URL:		https://pypi.org/project/oslo.utils/
%if %{with python2}
BuildRequires:	python-pbr >= 3.0.0
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-debtcollector >= 1.2.0
BuildRequires:	python-ddt >= 1.0.1
BuildRequires:	python-eventlet >= 0.18.4
BuildRequires:	python-fixtures >= 3.0.0
BuildRequires:	python-funcsigs >= 1.0.0
BuildRequires:	python-iso8601 >= 0.1.11
BuildRequires:	python-mock >= 2.0.0
BuildRequires:	python-oslo.i18n >= 3.15.3
BuildRequires:	python-monotonic >= 0.6
BuildRequires:	python-netaddr >= 0.7.18
BuildRequires:	python-netifaces >= 0.10.4
BuildRequires:	python-oslo.config >= 5.2.0
BuildRequires:	python-oslotest >= 3.2.0
BuildRequires:	python-pyparsing >= 2.1.0
BuildRequires:	python-pytz >= 2013.6
BuildRequires:	python-six >= 1.10.0
BuildRequires:	python-stestr >= 2.0.0
BuildRequires:	python-testscenarios >= 0.4
BuildRequires:	python-testtools >= 2.2.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 3.0.0
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-debtcollector >= 1.2.0
BuildRequires:	python3-ddt >= 1.0.1
BuildRequires:	python3-eventlet >= 0.18.4
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-iso8601 >= 0.1.11
BuildRequires:	python3-oslo.i18n >= 3.15.3
BuildRequires:	python3-netaddr >= 0.7.18
BuildRequires:	python3-netifaces >= 0.10.4
BuildRequires:	python3-oslo.config >= 5.2.0
BuildRequires:	python3-oslotest >= 3.2.0
BuildRequires:	python3-pyparsing >= 2.1.0
BuildRequires:	python3-pytz >= 2013.6
BuildRequires:	python3-six >= 1.10.0
BuildRequires:	python3-stestr >= 2.0.0
BuildRequires:	python3-testscenarios >= 0.4
BuildRequires:	python3-testtools >= 2.2.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
%if %{with doc}
BuildRequires:	python-openstackdocstheme >= 1.18.1
BuildRequires:	python-reno >= 2.5.0
BuildRequires:	sphinx-pdg-2 >= 1.8.0
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The oslo.utils library provides support for common utility type
functions, such as encoding, exception handling, string manipulation,
and time handling.

%description -l pl.UTF-8
Biblioteka oslo.utils udostępnia wspólne funkcje narzędziowe, takie
jak kodowanie, obsługa wyjątków, operacje na łańcuchach znaków czy
obsługa czasu.

%package -n python3-oslo.utils
Summary:	Oslo Utility library
Summary(pl.UTF-8):	Biblioteka narzędziowa Oslo
Group:		Libraries/Python

%description -n python3-oslo.utils
The oslo.utils library provides support for common utility type
functions, such as encoding, exception handling, string manipulation,
and time handling.

%description -n python3-oslo.utils -l pl.UTF-8
Biblioteka oslo.utils udostępnia wspólne funkcje narzędziowe, takie
jak kodowanie, obsługa wyjątków, operacje na łańcuchach znaków czy
obsługa czasu.

%package apidocs
Summary:	API documentation for Python oslo.utils module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona oslo.utils
Group:		Documentation

%description apidocs
API documentation for Pythona oslo.utils module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona oslo.utils.

%prep
%setup -q -n oslo.utils-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
sphinx-build-2 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/oslo_utils/tests
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/oslo_utils/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/oslo_utils
%{py_sitescriptdir}/oslo.utils-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-oslo.utils
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/oslo_utils
%{py3_sitescriptdir}/oslo.utils-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,contributor,install,reference,user,*.html,*.js}
%endif
