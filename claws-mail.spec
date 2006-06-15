#
# Conditional build:
%bcond_without  clamav          # build without clamav plugin
%bcond_without  compface        # build without compface support
%bcond_without  dillo           # build without dillo plugin (html browser)
%bcond_without  gnomeprint      # build without gnomeprint support
%bcond_without	gpg		# build without GPG support
%bcond_without  ipv6            # build without IPv6 support
%bcond_without  ldap            # build without LDAP support
%bcond_with     mathml          # build with mathml plugin
%bcond_without	spamassassin	# build without spamassassin plugin
%bcond_without  ssl             # build without SSL support
%bcond_without	trayicon	# build without trayicon plugin
#
%define		_iconver	20040929
Summary:	A bleeding edge branch of Sylpheed, a GTK2 based, lightweight, and fast e-mail client
Summary(pl):	Rozwojowa wersja Sylpheed z du¿± ilo¶ci± zmian oraz ulepszeñ
Name:		sylpheed-claws
Version:	2.3.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# Source0-md5:	a59b1f1736e89918c648794c94120a8e
Source1:	%{name}.desktop
Source2:	http://dl.sourceforge.net/sylpheed-claws/sylpheed-iconset-%{_iconver}.tar.gz
# Source2-md5:	d72cf03bf3d13cf9e2785eaca3807707
URL:		http://sylpheed-claws.sourceforge.net/
BuildRequires:	aspell-devel >= 2:0.50
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bzip2-devel
%{?with_clamav:BuildRequires:	clamav-devel}
%{?with_compface:BuildRequires:	compface-devel}
BuildRequires:	gdk-pixbuf-devel >= 0.8
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
%{?with_gnomeprint:BuildRequires:	libgnomeprintui-devel}
%{?with_gpg:BuildRequires:	gpgme-devel >= 1:0.4.5}
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRequires:	imlib-devel >= 1.9
BuildRequires:	libetpan-devel >= 0.45
BuildRequires:	libltdl-devel
BuildRequires:	libtool
# TODO: package gtkmathview: http://helm.cs.unibo.it/mml-widget/ (0.4.3 for gtk1, 0.6.0 for gtk2)
%{?with_mathml:BuildRequires:	gtkmathview >= 0.4.2}
%{?with_mathml:BuildRequires:	gtkmathview < 0.5}
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
BuildRequires:	pkgconfig
%{?with_faces:Requires:	faces}
Obsoletes:	sylpheed
Obsoletes:	sylpheed-gtk2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is an X based fast e-mail client which has features same
as orginal Sylpheed but with new/improved features. Some of new stuff
is really cool and useable.

%description -l pl
Szybki klient poczty o mo¿liwo¶ciach takich jak oryginalny Sylpheed
ale z nowymi/poprawionymi funkcjami. Niektóre dodatki s± naprawdê
¶wietne i u¿yteczne.

%package plugins
Summary:	Special plugins for Sylpheed-Claws
Summary(pl):	Dodatkowe pluginy dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
%{?with_dillo:Requires:	dillo}

%description plugins
This is collection of some usefull plugins for Sylpheed-claws.

%description plugins -l pl
Jest to zbiór kilku dodatkowych pluginów powiêkszaj±cych mo¿liwo¶ci
Sylpheeda.

%package devel
Summary:	Headers from Sylpheed-Claws
Summary(pl):	Pliki nag³ówkowe programu Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	gpgme-devel >= 1:0.4.5
Requires:	libetpan-devel >= 0.45
Requires:	openssl-devel >= 0.9.7d

%description devel
Sylpheed-Claws development package.

%description devel -l pl
Pliki nag³ówkowe programu Sylpheed-Claws.

%package themes
Summary:	Themes for Sylpheed-Claws
Summary(pl):	Motywy dla programu Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description themes
Sylpheed-Claws themes package.

%description themes -l pl
Motywy dla programu Sylpheed-Claws.

%prep
%setup -q -a2
mv sylpheed-iconset-* themes
mv -f themes/README README.themes

rm -f po/stamp-po

%build
#%%{__libtoolize}
#%%{__gettextize}
#%%{__aclocal} -I m4
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
%configure \
	--%{?with_clamav:en}%{!?with_clamav:dis}able-clamav-plugin \
	--%{?with_compface:en}%{!?with_compface:dis}able-compface \
	--%{?with_dillo:en}%{!?with_dillo:dis}able-dillo-viewer-plugin \
	--%{?with_gnomeprint:en}%{!?with_gnomeprint:dis}able-gnomeprint \
	--%{?with_gpg:en}%{!?with_gpg:dis}able-pgpmime-plugin \
	--%{?with_ipv6:en}%{!?with_ipv6:dis}able-ipv6 \
	--%{?with_ldap:en}%{!?with_ldap:dis}able-ldap \
	--%{?with_mathml:en}%{!?with_mathml:dis}able-mathml-viewer-plugin \
	--%{?with_spamassassin:en}%{!?with_spamassassin:dis}able-spamassassin-plugin \
	--%{?with_ssl:en}%{!?with_ssl:dis}able-openssl \
	--%{?with_trayicon:en}%{!?with_trayicon:dis}able-trayicon-plugin \
	--enable-aspell \
	--enable-gdk-pixbuf \
	--enable-pthread \
	--disable-static \
	--enable-libetpan \
	--with-config-dir=.sylpheed

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -a themes $RPM_BUILD_ROOT%{_datadir}/%{name}

install %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%{_mandir}/man1/%{name}.1*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/manual
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_datadir}/%{name}/manual/en
%lang(fr) %{_datadir}/%{name}/manual/fr
%lang(pl) %{_datadir}/%{name}/manual/pl
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

%files plugins
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files themes
%defattr(644,root,root,755)
%{_datadir}/%{name}/themes
