Name:           python-conan
Version:        1.39.0
Release:        1
Summary:        Conan C/C++ package manager
License:        MIT
URL:            https://conan.io
Source:         https://files.pythonhosted.org/packages/source/c/conan/conan-%{version}.tar.gz
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
# SECTION test requirements
#BuildRequires:  %{python_module bottle >= 0.12.8}
#BuildRequires:  %{python_module colorama >= 0.3.3}
#BuildRequires:  %{python_module deprecation >= 2.0}
#BuildRequires:  %{python_module distro >= 1.0.2}
#BuildRequires:  %{python_module fasteners >= 0.14.1}
#BuildRequires:  %{python_module future >= 0.16.0}
#BuildRequires:  %{python_module Jinja2 >= 2.9}
#BuildRequires:  %{python_module node-semver >= 0.6.1}
#BuildRequires:  %{python_module patch-ng >= 1.17.4}
#BuildRequires:  %{python_module pluginbase >= 0.5}
#BuildRequires:  %{python_module pygments >= 2.0}
#BuildRequires:  %{python_module PyJWT >= 1.4.0}
#BuildRequires:  %{python_module python-dateutil >= 2.7.0}
#BuildRequires:  %{python_module PyYAML >= 3.11}
#BuildRequires:  %{python_module requests >= 2.8.1}
#BuildRequires:  %{python_module six >= 1.10.0}
#BuildRequires:  %{python_module tqdm >= 4.28.1}
#BuildRequires:  %{python_module urllib3 < 1.27}
# /SECTION
BuildRequires:  fdupes
Requires:       python-bottle >= 0.12.8
Requires:       python-colorama >= 0.3.3
Requires:       python-deprecation >= 2.0
Requires:       python-distro >= 1.0.2
Requires:       python-fasteners >= 0.14.1
Requires:       python-future >= 0.16.0
Requires:       python-Jinja2 >= 2.9
Requires:       python-node-semver >= 0.6.1
Requires:       python-patch-ng >= 1.17.4
Requires:       python-pluginbase >= 0.5
Requires:       python-pygments >= 2.0
Requires:       python-PyJWT >= 1.4.0
Requires:       python-python-dateutil >= 2.7.0
Requires:       python-PyYAML >= 3.11
Requires:       python-requests >= 2.8.1
Requires:       python-six >= 1.10.0
Requires:       python-tqdm >= 4.28.1
Requires:       python-urllib3 < 1.26
Suggests:       python-nose >= 1.3.7
Suggests:       python-pytest-xdist
Suggests:       python-parameterized >= 0.6.3
Suggests:       python-mock >= 1.3.0
Suggests:       python-WebTest >= 2.0.18
Suggests:       python-bottle
Suggests:       python-pytest >= 4.6.11
Suggests:       python-pytest >= 6.1.1
Suggests:       python-nose >= 1.3.7
Suggests:       python-pytest-xdist
Suggests:       python-parameterized >= 0.6.3
Suggests:       python-mock >= 1.3.0
Suggests:       python-WebTest >= 2.0.18
Suggests:       python-bottle
Suggests:       python-pytest >= 4.6.11
Suggests:       python-pytest >= 6.1.1
BuildArch:      noarch
#python_subpackages

%description
Conan C/C++ package manager

%prep
%setup -q -n conan-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/conan
%python_clone -a %{buildroot}%{_bindir}/conan_server
%python_clone -a %{buildroot}%{_bindir}/conan_build_info
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative conan conan_server conan_build_info

%postun
%python_uninstall_alternative conan

%files
%doc README.rst
%license LICENSE.md
%python_alternative %{_bindir}/conan
%python_alternative %{_bindir}/conan_server
%python_alternative %{_bindir}/conan_build_info
%{python_sitelib}/*
