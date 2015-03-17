Summary:	Icon theme Rodent for the Xfce Desktop
Name:		rodent-icon-theme
Version:	5.0
Release:	4
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://sourceforge.net/projects/xffm/files/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	perl(XML::Parser)
BuildArch:	noarch
Obsoletes:	xfce4-icon-theme <= 4.4.3-6
Provides:	xfce4-icon-theme = 4.4.3-7

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
%{_iconsdir}/Rodent/scalable
%{_iconsdir}/Rodent/index.theme
%ghost %{_iconsdir}/Rodent/icon-theme.cache
