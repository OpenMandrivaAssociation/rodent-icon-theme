Summary:	Icon theme Rodent for the Xfce Desktop
Name:		xfce4-icon-theme
Version: 	4.4.3
Release:	%mkrel 5
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0: 	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= %{version}
BuildRequires:	perl(XML::Parser)
Requires:	xfce4-panel >= %{version}
BuildArch:	noarch
Obsoletes:	xfce-icon-theme < 4.4.3
Provides:	xfce-icon-theme
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
rm -rf %{buildroot}
%makeinstall_std

touch %{buildroot}%{_iconsdir}/Rodent/icon-theme.cache

%clean
rm -rf %{buildroot}

%post
%update_icon_cache Rodent

%postun
%clean_icon_cache Rodent

%files
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%dir %{_iconsdir}/Rodent/
%{_iconsdir}/Rodent/*/
%{_datadir}/xfce4/mime/*
%exclude %{_libdir}/pkgconfig/xfce4-icon-theme-1.0.pc
%ghost %{_iconsdir}/Rodent/icon-theme.cache
