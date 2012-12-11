Summary:	Icon theme Rodent for the Xfce Desktop
Name:		xfce4-icon-theme
Version:	4.4.3
Release:	5
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0: 	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	perl(XML::Parser)
Requires:	xfce4-panel >= %{version}
BuildArch:	noarch

%description
Icon theme Rodent for the Xfce Desktop Environment.

Included:
- about 500 icons in SVG format
- all the corresponding copies in PNG format
- almost all icons for a unified Gnome interface (excepted afaict the settings 
  manager, for the time being)
 
%prep 
%setup -q

%build

#(tpg) don't use macro for configure because it fails
./configure --prefix=%{_prefix} --libdir=%{_libdir}

%make

%install
%makeinstall_std

touch %{buildroot}%{_iconsdir}/Rodent/icon-theme.cache

rm -f %{buildroot}%{_libdir}/pkgconfig/xfce4-icon-theme-1.0.pc

%files
%doc README ChangeLog AUTHORS
%dir %{_iconsdir}/Rodent/
%{_iconsdir}/Rodent/48x48
%{_iconsdir}/Rodent/scalable
%{_iconsdir}/Rodent/iconrc*
%{_iconsdir}/Rodent/index.theme
%{_datadir}/xfce4/mime/*
%ghost %{_iconsdir}/Rodent/icon-theme.cache


%changelog
* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.3-4mdv2010.1
+ Revision: 543293
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 4.4.3-3mdv2010.0
+ Revision: 446054
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.3-2mdv2009.1
+ Revision: 349198
- rebuild whole xfce

* Sun Jan 04 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.3-1mdv2009.1
+ Revision: 324496
- update to new version 4.4.3

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 4.4.2-5mdv2009.0
+ Revision: 262359
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 4.4.2-4mdv2009.0
+ Revision: 256870
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 11 2007 Thierry Vignaud <tv@mandriva.org> 4.4.2-2mdv2008.1
+ Revision: 117237
- fix upgrading after renaming (and next time please do a real SVN renaming)

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-1mdv2008.1
+ Revision: 110093
- correct buildrequires
- new version 4.4.2
- new license policy
- do not package COPYING file, add ChangeLog to docs instead
- use upstream name
- use upstream tarball name as a real name

  + Jérôme Soyer <saispo@mandriva.org>
    - New release 4.4.2

* Sat Jun 02 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-3mdv2008.0
+ Revision: 34580
- exclude *.pc file

* Tue May 29 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-2mdv2008.0
+ Revision: 32556
- fix build

* Tue May 29 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-1mdv2008.0
+ Revision: 32503
- don't use macro for configure
- update url
- correct buildrequires
- spec file clean

  + Jérôme Soyer <saispo@mandriva.org>
    - New release 4.4.1

