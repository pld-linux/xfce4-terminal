%define		xfce_version	4.14.0
Summary:	Xfce Terminal Emulator
Summary(pl.UTF-8):	Emulator terminala dla Xfce
Name:		xfce4-terminal
Version:	0.8.8
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/xfce4-terminal/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	4295d4d783f6d6dfe92f5bb15d96f6c6
Patch0:		%{name}-desktop.patch
Patch1:		wordseps.patch
URL:		https://docs.xfce.org/apps/terminal/start
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.62
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	ncurses-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	vte-devel
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Obsoletes:	Terminal < 0.6.0
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
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s xfce4-terminal $RPM_BUILD_ROOT%{_bindir}/Terminal

%{__rm} $RPM_BUILD_ROOT%{_datadir}/gnome-control-center/default-apps/xfce4-terminal-default-apps.xml

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README THANKS
%attr(755,root,root) %{_bindir}/xfce4-terminal
%attr(755,root,root) %{_bindir}/Terminal
%{_datadir}/xfce4/terminal
%{_desktopdir}/%{name}.desktop
%{_desktopdir}/%{name}-settings.desktop

%{_mandir}/man1/%{name}*
