%define		xfce_version	4.18.0
Summary:	Xfce Terminal Emulator
Summary(pl.UTF-8):	Emulator terminala dla Xfce
Name:		xfce4-terminal
Version:	1.1.5
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/apps/xfce4-terminal/1.1/%{name}-%{version}.tar.xz
# Source0-md5:	d779b64ead82330b6bbc7d500f542490
Patch0:		%{name}-desktop.patch
Patch1:		wordseps.patch
URL:		https://docs.xfce.org/apps/terminal/start
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.62
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-doc
BuildRequires:	gtk-layer-shell-devel >= 0.7.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libutempter-devel
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	meson >= 0.54.0
BuildRequires:	ncurses-devel
BuildRequires:	ninja
BuildRequires:	pcre2-8-devel >= 10.00
BuildRequires:	pcre2-common-devel >= 10.00
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	vte-devel >= 0.51.3
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xfconf-devel >= 4.16.0
BuildRequires:	xorg-lib-libX11-devel >= 1.6.7
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
%patch -P0 -p1
%patch -P1 -p1

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

ln -s xfce4-terminal $RPM_BUILD_ROOT%{_bindir}/Terminal

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{fa_IR,hye,ie,ur_PK}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS HACKING NEWS THANKS
%attr(755,root,root) %{_bindir}/xfce4-terminal
%attr(755,root,root) %{_bindir}/Terminal
%{_datadir}/xfce4/terminal
%{_desktopdir}/%{name}.desktop
%{_desktopdir}/%{name}-settings.desktop
%{_iconsdir}/hicolor/*/apps/org.xfce.terminal*
%{_mandir}/man1/%{name}*
