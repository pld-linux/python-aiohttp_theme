#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	aiohttp documentation theme
Summary(pl.UTF-8):	Motyw dokumentacji aiohttp
Name:		python-aiohttp_theme
Version:	0.1.6
Release:	5
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/aiohttp-theme/
Source0:	https://files.pythonhosted.org/packages/source/a/aiohttp-theme/aiohttp-theme-%{version}.tar.gz
# Source0-md5:	163f576bae3da0d308c6d3f9f6ce2fc6
URL:		https://pypi.org/project/aiohttp-theme/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aiohttp documentation theme, based on Alabaster.

%description -l pl.UTF-8
Motyw dokumentacji aiohttp, oparty na motywie Alabaster.

%package -n python3-aiohttp_theme
Summary:	aiohttp documentation theme
Summary(pl.UTF-8):	Motyw dokumentacji aiohttp
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-aiohttp_theme
aiohttp documentation theme, based on Alabaster.

%description -n python3-aiohttp_theme -l pl.UTF-8
Motyw dokumentacji aiohttp, oparty na motywie Alabaster.

%prep
%setup -q -n aiohttp-theme-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/aiohttp_theme
%{py_sitescriptdir}/aiohttp_theme-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-aiohttp_theme
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/aiohttp_theme
%{py3_sitescriptdir}/aiohttp_theme-%{version}-py*.egg-info
%endif
