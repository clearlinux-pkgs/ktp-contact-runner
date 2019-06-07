#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : ktp-contact-runner
Version  : 19.04.2
Release  : 3
URL      : https://download.kde.org/stable/applications/19.04.2/src/ktp-contact-runner-19.04.2.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.2/src/ktp-contact-runner-19.04.2.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.2/src/ktp-contact-runner-19.04.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: ktp-contact-runner-data = %{version}-%{release}
Requires: ktp-contact-runner-lib = %{version}-%{release}
Requires: ktp-contact-runner-license = %{version}-%{release}
Requires: ktp-contact-runner-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : krunner-dev
BuildRequires : ktp-common-internals-dev
BuildRequires : plasma-framework-dev
BuildRequires : telepathy-qt-dev

%description
No detailed description available

%package data
Summary: data components for the ktp-contact-runner package.
Group: Data

%description data
data components for the ktp-contact-runner package.


%package lib
Summary: lib components for the ktp-contact-runner package.
Group: Libraries
Requires: ktp-contact-runner-data = %{version}-%{release}
Requires: ktp-contact-runner-license = %{version}-%{release}

%description lib
lib components for the ktp-contact-runner package.


%package license
Summary: license components for the ktp-contact-runner package.
Group: Default

%description license
license components for the ktp-contact-runner package.


%package locales
Summary: locales components for the ktp-contact-runner package.
Group: Default

%description locales
locales components for the ktp-contact-runner package.


%prep
%setup -q -n ktp-contact-runner-19.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559904234
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1559904234
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ktp-contact-runner
cp COPYING %{buildroot}/usr/share/package-licenses/ktp-contact-runner/COPYING
pushd clr-build
%make_install
popd
%find_lang plasma_runner_ktp_contacts

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/plasma-runner-ktp-contact.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/krunner_ktp_contacts.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ktp-contact-runner/COPYING

%files locales -f plasma_runner_ktp_contacts.lang
%defattr(-,root,root,-)

