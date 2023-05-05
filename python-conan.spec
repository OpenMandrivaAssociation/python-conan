Summary:        Conan C/C++ package manager
Name:           python-conan
Version:        2.0.4
Release:        1
License:        MIT
URL:            https://conan.io
Source:         https://pypi.io/packages/source/c/conan/conan-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

BuildArch:      noarch

%description
Conan is a dependency and package manager for C and C++ languages.

It is free and open-source, works in all platforms ( Windows, Linux,
OSX, FreeBSD, Solaris, etc.), and can be used to develop for all targets
including embedded, mobile (iOS, Android), and bare metal. It also
integrates with all build systems like CMake, Visual Studio (MSBuild),
Makefiles, SCons, etc., including proprietary ones.

It is specifically designed and optimized for accelerating the development
and Continuous Integration of C and C++ projects. With full binary
management, it can create and reuse any number of different binaries (for
different configurations like architectures, compiler versions, etc.) for
any number of different versions of a package, using exactly the same
process in all platforms. As it is decentralized, it is easy to run your
own server to host your own packages and binaries privately, without
needing to share them.

%files 
%license LICENSE.md
%doc README.md
%{_bindir}/conan
%{python_sitelib}/conan/
%{python_sitelib}/conan-*.*info/
%{python_sitelib}/conans/

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n conan-%{version}

# relax version in requirements
sed -e 's/, .*//g' -i conans/requirements.txt

%build
%py_build

%install
%py_install

