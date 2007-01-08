#
# Conditional build:
%bcond_without	clamav		# build without clamav plugin
%bcond_without	compface	# build without compface support
%bcond_without	gnomeprint	# build without gnomeprint support
%bcond_without	gpg		# build without GPG support
%bcond_without	ipv6		# build without IPv6 support
%bcond_without	jpilot		# build without JPilot support
%bcond_without	ldap		# build without LDAP support
%bcond_without	ssl		# build without SSL support
#
Summary:	A bleeding edge branch of Sylpheed, a GTK2 based, lightweight, and fast e-mail client
Summary(pl):	Rozwojowa wersja Sylpheed z du¿± ilo¶ci± zmian oraz ulepszeñ
Name:		claws-mail
Version:	2.7.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# Source0-md5:	3f99b79fce9d7e15ec6874582231b41e
Source1:	%{name}.desktop
URL:		http://www.claws-mail.net/
BuildRequires:	aspell-devel >= 2:0.50
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bzip2-devel
%{?with_clamav:BuildRequires:	clamav-devel}
%{?with_compface:BuildRequires:	compface-devel}
BuildRequires:	gdk-pixbuf-devel >= 0.8
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
%{?with_gpg:BuildRequires:	gpgme-devel >= 1:0.4.5}
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	imlib-devel >= 1.9
BuildRequires:	libetpan-devel >= 0.48
%{?with_gnomeprint:BuildRequires:	libgnomeprintui-devel}
BuildRequires:	libltdl-devel
BuildRequires:	libtool
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
%{?with_jpilot:BuildRequires:	pilot-link-devel}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	startup-notification-devel >= 0.5
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Provides:	sylpheed-claws
Obsoletes:	sylpheed
Obsoletes:	sylpheed-claws
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

%package devel
Summary:	Headers from Claws-Mail
Summary(pl):	Pliki nag³ówkowe programu Claws-Mail
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	gpgme-devel >= 1:0.4.5
Requires:	libetpan-devel >= 0.48
Requires:	openssl-devel >= 0.9.7d
Provides:	sylpheed-claws-devel
Obsoletes:	sylpheed-claws-devel

%description devel
Claws-Mail development package.

%description devel -l pl
Pliki nag³ówkowe programu Claws-Mail.

%package plugins
Summary:	Special plugins for Claws-Mail (metapackage)
Summary(pl):	Dodatkowe wtyczki dla Claws-Mail (metapakiet)
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugin-bogofilter = %{version}-%{release}
%{?with_clamav:Requires:	%{name}-plugin-clamav = %{version}-%{release}}
Requires:	%{name}-plugin-dillo = %{version}-%{release}
%if %{with gpg}
Requires:	%{name}-plugin-pgpinline = %{version}-%{release}
Requires:	%{name}-plugin-pgpmime = %{version}-%{release}
%endif
Requires:	%{name}-plugin-spamassassin = %{version}-%{release}
Requires:	%{name}-plugin-trayicon = %{version}-%{release}
Provides:	sylpheed-claws-plugins = %{version}
Obsoletes:	sylpheed-claws-plugins

%description plugins
This is collection of some usefull plugins for Claws-Mail
(metapackage).

%description plugins -l pl
Jest to zbiór kilku dodatkowych wtyczek powiêkszaj±cych mo¿liwo¶ci
Claws-Mail (metapakiet).

%package plugin-bogofilter
Summary:	Bogofilter plugin for Claws-Mail
Summary(pl):	Wtyczka bogofilter dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	bogofilter
Provides:	sylpheed-claws-plugin-bogofilter
Obsoletes:	sylpheed-claws-plugin-bogofilter

%description plugin-bogofilter
This plugin enables the scanning of incoming mail received from a POP,
IMAP or LOCAL account using Bogofilter. It can optionally delete mail
identified as spam or save it to a designated folder.

%description plugin-bogofilter -l pl
Wtyczka pozwalaj±ca na skanowanie bogofilterem poczty przychodz±cej
jak i ju¿ znajduj±cej siê w lokalnych skrzynkach. Opcjonalnie mo¿e
usuwaæ listy oznaczone jako spam lub zapisywaæ je w dedykowanym
folderze.

%package plugin-clamav
Summary:	clamav plugin for Claws-Mail
Summary(pl):	Wtyczka clamav dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-clamav
Obsoletes:	sylpheed-claws-plugin-clamav
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-clamav
This plugin enables the scanning of message attachments in mail
received from a POP, IMAP, or LOCAL account using Clam AntiVirus. It
can optionally delete the mail or save it to a designated folder.

%description plugin-clamav -l pl
Ta wtyczka pozwala na lokalne skanowanie za³±czników z poczty
otrzymanej przez POP, IMAP lub znajduj±cej siê w lokalnych skrzynkach.
Opcjonalnie mo¿e usuwaæ lub zapisywaæ zainfekowane listy w
przeznaczonym do tego folderze.

%package plugin-dillo
Summary:	dillo plugin for Claws-Mail
Summary(pl):	Wtyczka dillo dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	dillo
Provides:	sylpheed-claws-plugin-dillo
Obsoletes:	sylpheed-claws-plugin-dillo
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-dillo
This plugin enables the viewing of html messages using the Dillo web
browser.

%description plugin-dillo -l pl
Wtyczka pozwalaj±ca na przegl±danie listów pisanych w HTML przy pomocy
przegl±darki Dillo.

%package plugin-pgpcore
Summary:	PGP/Core plugin for Claws-Mail
Summary(pl):	Wtyczka PGP/Core dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-pgpcore
Obsoletes:	sylpheed-claws-plugin-pgpcore
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-pgpcore
This plugin handles core PGP functions.

%description plugin-pgpcore -l pl
Wtyczka obs³uguj±ca podstawowe funkcje PGP.

%package plugin-pgpinline
Summary:	PGP/Inline plugin for Claws-Mail
Summary(pl):	Wtyczka PGP/Inline dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	%{name}-plugin-pgpcore = %{version}-%{release}
Provides:	sylpheed-claws-plugin-pgpinline
Obsoletes:	sylpheed-claws-plugin-pgpinline
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-pgpinline
This plugin handles PGP/Inline signed and/or encrypted mails. It can
decrypt mails, verify signatures or sign and encrypt your own mails.

%description plugin-pgpinline -l pl
Wtyczka obs³uguj±ca listy podpisane lub szyfrowane PGP/Inline. Potrafi
rozszyfrowywaæ, sprawdzaæ podpisy a tak¿e szyfrowaæ i podpisywaæ
w³asne listy.

%package plugin-pgpmime
Summary:	PGP/MIME plugin for Claws-Mail
Summary(pl):	Wtyczka PGP/MIME dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	%{name}-plugin-pgpcore = %{version}-%{release}
Provides:	sylpheed-claws-plugin-pgpmime
Obsoletes:	sylpheed-claws-plugin-pgpmime
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-pgpmime
This plugin handles PGP/MIME signed and/or encrypted mails. It can
decrypt mails, verify signatures or sign and encrypt your own mails.

%description plugin-pgpmime -l pl
Wtyczka obs³uguj±ca listy podpisane lub szyfrowane PGP/MIME. Potrafi
rozszyfrowywaæ, sprawdzaæ podpisy a tak¿e szyfrowaæ i podpisywaæ
w³asne listy.

%package plugin-spamassassin
Summary:	spamassassin plugin for Claws-Mail
Summary(pl):	Wtyczka spamassassin dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-spamassassin
Obsoletes:	sylpheed-claws-plugin-spamassassin
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-spamassassin
This plugin enables the scanning of incoming mail received from a POP,
IMAP, or LOCAL account using SpamAssassin. It can optionally delete
mail identified as spam or save it to a designated folder, and also
can be used to train a local Spamassassin or a remote one.

%description plugin-spamassassin -l pl
Wtyczka pozwalaj±ca na skanowanie SpamAssassinem poczty przychodz±cej
jak i ju¿ znajduj±cej siê w lokalnych skrzynkach. Opcjonalnie mo¿e
usuwaæ listy oznaczone jako spam lub zapisywaæ je w dedykowanym
folderze. Mo¿e te¿ by¿ u¿ywana do "uczenia" lokalnego lub zdalnego
demona SpamAssassin.

%package plugin-trayicon
Summary:	trayicon plugin for Claws-Mail
Summary(pl):	Wtyczka trayicon dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-trayicon
Obsoletes:	sylpheed-claws-plugin-trayicon
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-trayicon
This plugin places an icon in the system tray that indicates whether
you have any new mail. A tooltip also shows the current new, unread
and total number of messages, and a contextual menu allows the most
common operations.

%description plugin-trayicon -l pl
Wtyczka umieszczaj±ca w tacce systemowej ikonê informuj±c± o nadej¶ciu
nowej poczty. Ikona wy¶wietla dane na temat wiadomo¶ci (ilo¶æ nowych,
nieprzeczytanych i wszystkich) a jej menu pozwala wykonywaæ
najpopularniejsze operacje.

%prep
%setup -q

rm -f po/stamp-po

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--%{?with_clamav:en}%{!?with_clamav:dis}able-clamav-plugin \
	--%{?with_compface:en}%{!?with_compface:dis}able-compface \
	--%{?with_gnomeprint:en}%{!?with_gnomeprint:dis}able-gnomeprint \
	--%{?with_gpg:en}%{!?with_gpg:dis}able-pgpcore-plugin \
	--%{?with_gpg:en}%{!?with_gpg:dis}able-pgpmime-plugin \
	--%{?with_gpg:en}%{!?with_gpg:dis}able-pgpinline-plugin \
	--%{?with_ipv6:en}%{!?with_ipv6:dis}able-ipv6 \
	--%{?with_jpilot:en}%{!?with_jpilot:dis}able-jpilot \
	--%{?with_ldap:en}%{!?with_ldap:dis}able-ldap \
	--%{?with_ssl:en}%{!?with_ssl:dis}able-openssl \
	--enable-aspell \
	--enable-bogofilter \
	--enable-dillo-viewer-plugin \
	--enable-gdk-pixbuf \
	--enable-libetpan \
	--enable-pthread \
	--enable-spamassassin-plugin \
	--enable-trayicon-plugin \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name}/themes,%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.{deps,la}
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/RELEASE_NOTES
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/manual/{en,es,fr,pl}/*.{pdf,ps,html}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* RELEASE_NOTES TODO
%{_mandir}/man1/%{name}.1*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/manual
%dir %{_datadir}/%{name}/themes
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_docdir}/%{name}/manual/en
%lang(es) %{_docdir}/%{name}/manual/es
%lang(fr) %{_docdir}/%{name}/manual/fr
%lang(pl) %{_docdir}/%{name}/manual/pl
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files plugins
%defattr(644,root,root,755)

%files plugin-bogofilter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/bogofilter.so

%if %{with clamav}
%files plugin-clamav
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/clamav_plugin.so
%endif

%files plugin-dillo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/dillo_viewer.so

%if %{with gpg}
%files plugin-pgpcore
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/pgpcore.so

%files plugin-pgpinline
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/pgpinline.so

%files plugin-pgpmime
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/pgpmime.so
%endif

%files plugin-spamassassin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/spamassassin.so

%files plugin-trayicon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/trayicon.so
