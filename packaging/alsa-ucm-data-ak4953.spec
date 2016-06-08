Name:       alsa-ucm-data-ak4953
Summary:    ALSA UCM data pkg for AK4953 codec
Version:    0.0.1
Release:    1
License:    LGPL-2.1+
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz

%description
ALSA UCM data for ak4953

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/alsa/ucm
cp -a ak4953 %{buildroot}/usr/share/alsa/ucm
mkdir -p %{buildroot}/usr/share/license
cp -a LICENSE.LGPL-2.1+ %{buildroot}/usr/share/license/%{name}

%post

%files
%manifest alsa-ucm-conf-ak4953.manifest
/usr/share/alsa/ucm/ak4953/*
/usr/share/license/alsa-ucm-data-ak4953
