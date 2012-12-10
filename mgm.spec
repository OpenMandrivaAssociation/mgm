%define name	mgm
%define version	1.1
%define release %mkrel 9

Name: 	 	%{name}
Summary: 	Moaning Goat Status Meter
Version: 	%{version}
Release: 	%{release}
Source:		%{name}-%{version}.tar.bz2
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
URL:		http://linuxmafia.com/mgm/
License:	GPLv2
Patch0:		mgm-1.1-fix-abs-path.patch
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
%patch0 -p0
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
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=MGM
Comment=System Monitor
Categories=System;Monitor;
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

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc doc/*
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png



%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-9mdv2011.0
+ Revision: 612864
- the mass rebuild of 2010.1 packages

* Wed Feb 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.1-8mdv2010.1
+ Revision: 510509
- fix license
- add a patch from gentoo

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1-7mdv2010.0
+ Revision: 430024
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.1-6mdv2009.0
+ Revision: 252385
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 1.1-4mdv2008.1
+ Revision: 133910
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import mgm


* Fri Jan 27 2006 Austin Acton <austin@mandriva.org> 1.1-4mdk
- fix URL (Adam Williamson)

* Fri Jan 27 2006 Austin Acton <austin@mandriva.org> 1.1-3mdk
- fix location

* Fri Apr 2 2004 Austin Acton <austin@mandrake.org> 1.1-2mdk
- stale rebuild

* Sun Feb 9 2003 Austin Acton <aacton@yorku.ca> 1.1-1mdk
- initial package
