
%define		xfce_version	4.10.0
Summary:	Xfce Terminal Emulator
Summary(pl.UTF-8):	Emulator terminala dla Xfce
Name:		xfce4-terminal
Version:	0.6.1
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/xfce4-terminal/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	98613ce500fef2ed62cdbe788084acca
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-user-colors.patch
URL:		http://www.xfce.org/projects/terminal/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.62
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	ncurses-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	vte0-devel >= 0.28.0
BuildRequires:	xfce4-dev-tools >= 4.6.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Obsoletes:	Terminal
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Advanced lightweight Terminal Emulator for the X windowing system.

%description -l pl.UTF-8
Zaawansowany emulator terminala dla systemu X Window.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# already present as ur
%{__sed} -i 's,ur_PK ,,' configure.ac
 
%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README THANKS
%attr(755,root,root) %{_bindir}/xfce4-terminal
%{_datadir}/xfce4/terminal
%{_desktopdir}/%{name}.desktop

%{_mandir}/man1/%{name}*
%lang(ar) %{_mandir}/ar/man1/%{name}*
%lang(ca) %{_mandir}/ca/man1/%{name}*
%lang(da) %{_mandir}/da/man1/%{name}*
%lang(de) %{_mandir}/de/man1/%{name}*
%lang(el) %{_mandir}/el/man1/%{name}*
%lang(es) %{_mandir}/es/man1/%{name}*
%lang(fr) %{_mandir}/fr/man1/%{name}*
%lang(gl) %{_mandir}/gl/man1/%{name}*
%lang(id) %{_mandir}/id/man1/%{name}*
%lang(it) %{_mandir}/it/man1/%{name}*
%lang(ja) %{_mandir}/ja/man1/%{name}*
%lang(ko) %{_mandir}/ko/man1/%{name}*
%lang(lt) %{_mandir}/lt/man1/%{name}*
%lang(pl) %{_mandir}/pl/man1/%{name}*
%lang(pt) %{_mandir}/pt/man1/%{name}*
%lang(pt_BR) %{_mandir}/pt_BR/man1/%{name}*
%lang(ru) %{_mandir}/ru/man1/%{name}*
%lang(sv) %{_mandir}/sv/man1/%{name}*
%lang(tr) %{_mandir}/tr/man1/%{name}*
#%lang(ug) %{_mandir}/ug/man1/%{name}*
%lang(uk) %{_mandir}/uk/man1/%{name}*
%lang(zh_CN) %{_mandir}/zh_CN/man1/%{name}*
