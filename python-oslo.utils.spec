#
# Conditional build:
%bcond_with	doc	# do build doc (missing deps)
%bcond_with	tests	# do perform "make test" (missing deps)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Oslo Utility library
Name:		python-oslo.utils
Version:	3.36.3
Release:	2
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/o/oslo.utils/oslo.utils-%{version}.tar.gz
# Source0-md5:	f4d23e51547a37b2e54bb1623e6d2534
URL:		https://pypi.python.org/pypi/oslo.utils
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%endif
BuildRequires:	sed >= 4.0
Requires:	python-debtcollector >= 1.2.0
Requires:	python-funcsigs >= 0.4
Requires:	python-iso8601 >= 0.1.11
Requires:	python-monotonic >= 0.6
Requires:	python-netaddr >= 0.7.13
Requires:	python-netifaces >= 0.10.4
Requires:	python-oslo.i18n >= 2.1.0
Requires:	python-pbr >= 2.0.0
Requires:	python-pyparsing >= 2.1.0
Requires:	python-pytz >= 2013.6
Requires:	python-six >= 1.9.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The oslo.utils library provides support for common utility type
functions, such as encoding, exception handling, string manipulation,
and time handling.

%description -l pl.UTF-8

%package -n python3-oslo.utils
Summary:	Oslo Utility library
Group:		Libraries/Python
Requires:	python3-debtcollector >= 1.2.0
Requires:	python3-iso8601 >= 0.1.11
Requires:	python3-monotonic >= 0.6
Requires:	python3-netaddr >= 0.7.13
Requires:	python3-netifaces >= 0.10.4
Requires:	python3-oslo.i18n >= 2.1.0
Requires:	python3-pbr >= 2.0.0
Requires:	python3-pyparsing >= 2.1.0
Requires:	python3-pytz >= 2013.6
Requires:	python3-six >= 1.9.0

%description -n python3-oslo.utils
The oslo.utils library provides support for common utility type
functions, such as encoding, exception handling, string manipulation,
and time handling.

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
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

# when files are installed in other way that standard 'setup.py
# they need to be (re-)compiled
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install

# python dependency generator does not support conditionals
# remove python2-only dependencies here
sed -i -e"/python_version=='2./,+1 d" $RPM_BUILD_ROOT%{py3_sitescriptdir}/oslo.utils-%{version}-py*.egg-info/requires.txt
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
%doc doc/_build/html/*
%endif
