%define		pre	beta1
Summary:	X Terminal Emulator
Summary(pl):	Emulator terminala dla X
Name:		Terminal
Version:	0.2.5.1
Release:	0.%{pre}.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}%{pre}.tar.bz2
# Source0-md5:	9b24c84d07981e9e007253842a92d259
URL:		http://www.os-cillation.com/
BuildRequires:	dbus-glib-devel >= 0.33
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.31
BuildRequires:	libexo-devel >= 0.3.1.6
BuildRequires:	libxfcegui4-devel >= 4.2.0
BuildRequires:	ncurses-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	vte-devel >= 0.11.11
Obsoletes:	xfce4-terminal
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Advanced lightweight Terminal Emulator for the X windowing system.

%description -l pl
Zaawansowany emulator terminala dla systemu X Window.

%prep
%setup -q -n %{name}-%{version}%{pre}

%build
%{__sed} -i 's,Categories.*,Categories=GTK;TerminalEmulator;,' Terminal.desktop.in
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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/TerminalHelp
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}*
%{_iconsdir}/hicolor/*/stock/navigation/*
%{_pixmapsdir}/*

%dir %{_docdir}/%{name}
%{_docdir}/%{name}/C
%{_docdir}/%{name}/*.css
%lang(ja) %{_docdir}/%{name}/ja
%{_mandir}/man1/%{name}*