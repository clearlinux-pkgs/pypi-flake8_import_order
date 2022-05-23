#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-flake8_import_order
Version  : 0.18.1
Release  : 29
URL      : https://files.pythonhosted.org/packages/81/47/5f2cea0164e77dd40726d83b4c865c2a701f60b73cb6af7b539cd42aafb4/flake8-import-order-0.18.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/81/47/5f2cea0164e77dd40726d83b4c865c2a701f60b73cb6af7b539cd42aafb4/flake8-import-order-0.18.1.tar.gz
Summary  : Flake8 and pylama plugin that checks the ordering of import statements.
Group    : Development/Tools
License  : LGPL-3.0
Requires: pypi-flake8_import_order-license = %{version}-%{release}
Requires: pypi-flake8_import_order-python = %{version}-%{release}
Requires: pypi-flake8_import_order-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pycodestyle)
BuildRequires : pypi(setuptools)

%description
===================
        
        |Build Status|

%package license
Summary: license components for the pypi-flake8_import_order package.
Group: Default

%description license
license components for the pypi-flake8_import_order package.


%package python
Summary: python components for the pypi-flake8_import_order package.
Group: Default
Requires: pypi-flake8_import_order-python3 = %{version}-%{release}

%description python
python components for the pypi-flake8_import_order package.


%package python3
Summary: python3 components for the pypi-flake8_import_order package.
Group: Default
Requires: python3-core
Provides: pypi(flake8_import_order)
Requires: pypi(pycodestyle)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-flake8_import_order package.


%prep
%setup -q -n flake8-import-order-0.18.1
cd %{_builddir}/flake8-import-order-0.18.1
pushd ..
cp -a flake8-import-order-0.18.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653331205
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-flake8_import_order
cp %{_builddir}/flake8-import-order-0.18.1/COPYING %{buildroot}/usr/share/package-licenses/pypi-flake8_import_order/f45ee1c765646813b442ca58de72e20a64a7ddba
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-flake8_import_order/f45ee1c765646813b442ca58de72e20a64a7ddba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
