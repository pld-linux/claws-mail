#
# Conditional build:
%bcond_without	gpg		# build without GPG support
%bcond_without	ssl		# build without SSL support
%bcond_without	ipv6		# build without IPv6 support
%bcond_without	ldap		# build without LDAP support
%bcond_without	faces		# build without compfaces support
%bcond_without	dillo		# build without dillo plugin (html browser)
%bcond_without	clamav		# build without clamav plugin
%bcond_without	spamassassin	# build without spamassassin plugin
%bcond_without	trayicon	# build without trayicon plugin
%bcond_with	mathml		# build with mathml plugin
#
%define		_sname	sylpheed
%define		_iconver	20040206
Summary:	A bleeding edge branch of Sylpheed, a GTK+ based, lightweight, and fast e-mail client
Summary(pl):	Rozwojowa wersja Sylpheed z du¿± ilo¶ci± zmian oraz ulepszeñ
Name:		%{_sname}-claws
Version:	0.9.9
Release:	5
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{_sname}-%{version}claws.tar.bz2
# Source0-md5:	9068192f009fb8240be6e9222ff27999
Source1:	%{name}.desktop
Source2:	http://dl.sourceforge.net/%{name}/%{_sname}-iconset-%{_iconver}.tar.gz
# Source2-md5:	478128ccf00914990f73383692b5cd30
URL:		http://sylpheed-claws.sourceforge.net/
BuildRequires:	aspell-devel >= 0.50
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
%{?with_clamav:BuildRequires:	clamav-devel}
%{?with_faces:BuildRequires:	faces-devel}
BuildRequires:	gdk-pixbuf-devel >= 0.8
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
%{?with_gpg:BuildRequires:	gpgme-devel >= 0.3.10}
%{?with_gpg:BuildRequires:	gpgme-devel < 0.4}
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	imlib-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
# TODO: package gtkmathview: http://helm.cs.unibo.it/mml-widget/ (0.4.3 for gtk1, 0.6.0 for gtk2)
%{?with_mathml:BuildRequires:	gtkmathview >= 0.4.2}
%{?with_mathml:BuildRequires:	gtkmathview < 0.5}
%{?with_ldap:BuildRequires:	openldap-devel}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
BuildRequires:	pkgconfig
%{?with_faces:Requires:	faces}
Obsoletes:	sylpheed
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
Jest to zbiór kilku dodatkowych pluginów powiêkszaj±cych mo¿liwo¶ci Sylpheeda.

%package devel
Summary:	Headers from Sylpheed-Claws
Summary(pl):	Pliki nag³ówkowe programu Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}

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
%setup -q -n %{_sname}-%{version}claws -a1 -a2
mv %{_sname}-iconset-* themes
mv -f themes/README README.themes

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I ac
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_gpg:--enable-gpgme} %{!?with_gpg:--disable-gpgme} \
	%{?with_ldap:--enable-ldap} \
	%{?with_ssl:--enable-openssl} \
	%{?with_ipv6:--enable-ipv6 } \
	%{!?with_faces:--disable-compface} \
	%{?with_dillo:--enable-dillo-viewer-plugin } \
	%{!?with_dillo:--disable-dillo-viewer-plugin } \
	%{?with_clamav:--enable-clamav-plugin } \
	%{!?with_clamav:--disable-clamav-plugin } \
	%{?with_mathml:--enable-mathml-viewer-plugin } \
	%{!?with_mathml:--disable-mathml-viewer-plugin } \
	%{?with_trayicon:--enable-trayicon-plugin } \
	%{!?with_trayicon:--disable-trayicon-plugin } \
	%{?with_spamassassin:--enable-spamassassin-plugin } \
	--enable-aspell \
	--enable-gdk-pixbuf \
	--enable-threads

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -a themes $RPM_BUILD_ROOT%{_datadir}/%{_sname}

install %{_sname}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{_sname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{_sname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%{_mandir}/man1/%{_sname}.1*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{_sname}
%dir %{_datadir}/%{_sname}/manual
%{_datadir}/%{_sname}/manual/en
%lang(de) %{_datadir}/%{_sname}/manual/de
%lang(es) %{_datadir}/%{_sname}/manual/es
%lang(fr) %{_datadir}/%{_sname}/manual/fr
%lang(ja) %{_datadir}/%{_sname}/manual/ja
%dir %{_datadir}/%{_sname}/faq
%{_datadir}/%{_sname}/faq/en
%lang(de) %{_datadir}/%{_sname}/faq/de
%lang(es) %{_datadir}/%{_sname}/faq/es
%lang(fr) %{_datadir}/%{_sname}/faq/fr
%lang(it) %{_datadir}/%{_sname}/faq/it
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{_sname}.png

%files plugins
%defattr(644,root,root,755)
%dir %{_libdir}/%{_sname}
%dir %{_libdir}/%{_sname}/plugins
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/*so

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{_sname}
%{_pkgconfigdir}/*.pc

%files themes
%defattr(644,root,root,755)
%{_datadir}/%{_sname}/themes
