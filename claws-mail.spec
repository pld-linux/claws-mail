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
Summary:	A bleeding edge branch of Sylpheed, a GTK+ based, lightweight, and fast e-mail client
Summary(pl):	Rozwojowa wersja Sylpheed z du¿± ilo¶ci± zmian oraz ulepszeñ
Name:		sylpheed-claws
Version:	0.9.5
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/sylpheed-claws/sylpheed-%{version}claws.tar.bz2
# Source0-md5:	66d72383222e4deb47300889d24f1044
Source1:	%{name}.desktop
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
%{!?_without_ssl:BuildRequires:	openssl-devel >= 0.9.7}
BuildRequires:	aspell-devel >= 0.50
%{!?_without_jconv:BuildRequires:	libjconv-devel}
%{!?_without_faces:Requires:	faces}
%{!?_without_dillo:Requires:	dillo}
Obsoletes:	sylpheed
URL:		http://sylpheed-claws.sourceforge.net/
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

%description plugins
This is collection of some usefull plugins for Sylpheed-claws.

%description plugins -l pl
Jest to zbiór kilku dodatkowych pluginów powiêkszaj±cych mo¿liwo¶ci Sylpheeda.

%prep
%setup -q -n sylpheed-%{version}claws -a1
#mv sylpheed*claws-iconset themes
#mv -f themes/README README.themes

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
#cp -a themes $RPM_BUILD_ROOT%{_datadir}/sylpheed

install sylpheed.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang sylpheed

%clean
rm -rf $RPM_BUILD_ROOT

%files -f sylpheed.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%{_mandir}/man1/sylpheed.1*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/sylpheed
%dir %{_datadir}/sylpheed/manual
%{_datadir}/sylpheed/manual/en
%lang(de) %{_datadir}/sylpheed/manual/de
%lang(es) %{_datadir}/sylpheed/manual/es
%lang(fr) %{_datadir}/sylpheed/manual/fr
%lang(ja) %{_datadir}/sylpheed/manual/ja
%dir %{_datadir}/sylpheed/faq
%{_datadir}/sylpheed/faq/en
%lang(de) %{_datadir}/sylpheed/faq/de
%lang(es) %{_datadir}/sylpheed/faq/es
%lang(fr) %{_datadir}/sylpheed/faq/fr
%lang(it) %{_datadir}/sylpheed/faq/it
#%{_datadir}/sylpheed/themes
%{_applnkdir}/Network/Mail/%{name}.desktop
%{_pixmapsdir}/sylpheed.png

%files plugins
%defattr(644,root,root,755)
%dir %{_libdir}/sylpheed
%dir %{_libdir}/sylpheed/plugins
%{_libdir}/sylpheed/plugins/*so
