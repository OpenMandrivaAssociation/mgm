%define name	mgm
%define version	1.1
%define release 4mdk

Name: 	 	%{name}
Summary: 	Moaning Goat Status Meter
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
URL:		http://linuxmafia.com/mgm/
License:	GPL
Group:		Monitoring
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	perl-Tk tk
BuildArch:	noarch

%description
MGM, the Moaning Goat Meter, is the ultimate sixty-ton cast iron lawn
ornament for the desktops of today's hacker set: A gorgeous, highly
configurable load and status meter written entirely in Perl. Serious
pink-flamingo territory.  MGM will not get your whites whiter or your
colors brighter. It will, however, sit there and look spiffy while
sucking down a major honking wad of RAM.

%prep
%setup -q -n %name
chmod 644 `find -type f`
chmod 755 `find -type d`
chmod 755 mgm lib/xpm
rm -fr modules/netbsd
rm -fr modules/solaris

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_datadir/%name
cp -r mgm lib modules $RPM_BUILD_ROOT/%_datadir/%name
mkdir -p $RPM_BUILD_ROOT/%_bindir
echo '#!/bin/bash' > $RPM_BUILD_ROOT/%_bindir/%name
echo 'exec %_datadir/mgm/mgm' >> $RPM_BUILD_ROOT/%_bindir/%name
chmod 755 $RPM_BUILD_ROOT/%_bindir/%name

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="MGM" longtitle="System Monitor" section="Applications/Monitoring"
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %SOURCE2 > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %SOURCE3 > $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc doc/*
%{_bindir}/%name
%{_datadir}/%name
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

