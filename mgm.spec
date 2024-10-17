Summary:	Moaning Goat Status Meter
Name:		mgm
Version:	1.1
Release:	11
License:	GPLv2+
Group:		Monitoring
Url:		https://linuxmafia.com/mgm/
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}48.png
Source2:	%{name}32.png
Source3:	%{name}16.png
Patch0:		mgm-1.1-fix-abs-path.patch
Requires:	perl-Tk
Requires:	tk
BuildArch:	noarch

%description
MGM, the Moaning Goat Meter, is the ultimate sixty-ton cast iron lawn
ornament for the desktops of today's hacker set: A gorgeous, highly
configurable load and status meter written entirely in Perl. Serious
pink-flamingo territory.  MGM will not get your whites whiter or your
colors brighter. It will, however, sit there and look spiffy while
sucking down a major honking wad of RAM.

%files
%doc doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}
%patch0 -p0
chmod 644 `find -type f`
chmod 755 `find -type d`
chmod 755 mgm lib/xpm
rm -fr modules/netbsd
rm -fr modules/solaris

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r mgm lib modules %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
echo '#!/bin/bash' > %{buildroot}%{_bindir}/%{name}
echo 'exec %{_datadir}/mgm/mgm' >> %{buildroot}%{_bindir}/%{name}
chmod 755 %{buildroot}%{_bindir}/%{name}

#menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=MGM
Comment=System Monitor
Categories=System;Monitor;
EOF

#icons
mkdir -p %{buildroot}%{_liconsdir}
cat %{SOURCE1} > %{buildroot}%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}
cat %{SOURCE2} > %{buildroot}%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}%{_miconsdir}
cat %{SOURCE3} > %{buildroot}%{_miconsdir}/%{name}.png


