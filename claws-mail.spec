#
# Conditional build:
# _without_jconv        - without jconv support
# _without_gpg          - without gpg support
# _without_ssl          - without ssl support
# _without_ipv6         - without ipv6 support
# _without_ldap         - without ldap support
# _without_faces        - without compfaces support
# _without_dillo	- without dillo plugin (html browser)
# _without_clamav	- without clamav plugin
# _with_mathml		- with mathml plugin
# _without_trayicon	- without trayicon plugin
# _without_spamassassin - without spamassassin plugin
#

%define		_sname	sylpheed
%define		_iconver	20030712
Summary:	A bleeding edge branch of Sylpheed, a GTK+ based, lightweight, and fast e-mail client
Summary(pl):	Rozwojowa wersja Sylpheed z du¿± ilo¶ci± zmian oraz ulepszeñ
Name:		%{_sname}-claws
Version:	0.9.6
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{_sname}-%{version}claws.tar.bz2
# Source0-md5:	a4a7e7c9a6c1b17f688a782e8c06ae4b
Source1:	%{name}.desktop
Source2:	http://dl.sourceforge.net/%{name}/%{_sname}-iconset-%{_iconver}.tar.gz
# Source2-md5:	7da918c0ebe89cd6c9f8b65bc3e18377
URL:		http://sylpheed-claws.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_clamav:BuildRequires:	clamav-devel}
%{!?_without_faces:BuildRequires:	faces-devel}
BuildRequires:	gdk-pixbuf-devel >= 0.8
BuildRequires:	gettext-devel
%{!?_without_gpg:BuildRequires:	gpgme-devel < 0.4}
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	imlib-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
%{!?_without_ldap:BuildRequires:	openldap-devel}
%{!?_without_ssl:BuildRequires:	openssl-devel >= 0.9.7c}
BuildRequires:	aspell-devel >= 0.50
%{!?_without_jconv:BuildRequires:	libjconv-devel}
%{!?_without_faces:Requires:	faces}
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
Requires:	%{name} = %{version}
%{!?_without_dillo:Requires:	dillo}

%description plugins
This is collection of some usefull plugins for Sylpheed-claws.

%description plugins -l pl
Jest to zbiór kilku dodatkowych pluginów powiêkszaj±cych mo¿liwo¶ci Sylpheeda.

%package devel
Summary:	Headers from Sylpheed-Claws
Summary(pl):	Pliki nag³ówkowe programu Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}

%description devel
Sylpheed-Claws development package.

%description devel -l pl
Pliki nag³ówkowe programu Sylpheed-Claws.

%package themes
Summary:	Themes for Sylpheed-Claws
Summary(pl):	Motywy dla programu Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}

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
	%{!?_without_jconv:--enable-jconv} %{?_without_jconv:--disable-jconv} \
	%{!?_without_gpg:--enable-gpgme} %{?_without_gpg:--disable-gpgme} \
	%{!?_without_ldap:--enable-ldap} \
	%{!?_without_ssl:--enable-openssl} \
	%{!?_without_ipv6:--enable-ipv6 } \
	%{?_without_faces:--disable-compfaces } \
	%{!?_without_dillo:--enable-dillo-viewer-plugin } \
	%{?_without_dillo:--disable-dillo-viewer-plugin } \
	%{!?_without_clamav:--enable-clamav-plugin } \
	%{?_without_clamav:--disable-clamav-plugin } \
	%{?_with_mathml:--enable-mathml-viewer-plugin } \
	%{!?_with_mathml:--disable-mathml-viewer-plugin } \
	%{!?_without_trayicon:--enable-trayicon-plugin } \
	%{?_without_trayicon:--disable-trayicon-plugin } \
	%{!?_without_spamassassin:--enable-spamassassin-plugin } \
	--enable-aspell \
	--enable-gdk-pixbuf \
	--enable-threads

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Mail,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
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
%{_applnkdir}/Network/Mail/%{name}.desktop
%{_pixmapsdir}/%{_sname}.png

%files plugins
%defattr(644,root,root,755)
%dir %{_libdir}/%{_sname}
%dir %{_libdir}/%{_sname}/plugins
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/*so

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{_sname}

%files themes
%defattr(644,root,root,755)
%{_datadir}/%{_sname}/themes
