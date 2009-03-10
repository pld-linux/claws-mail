#
# Conditional build:
%bcond_without	compface	# build without compface support
%bcond_without	gpg		# build without GPG support
%bcond_without	ipv6		# build without IPv6 support
%bcond_without	jpilot		# build without JPilot support
%bcond_without	ldap		# build without LDAP support
%bcond_without	tls		# build without gnuTLS support
#
Summary:	A bleeding edge branch of Sylpheed, a GTK2 based, lightweight, and fast e-mail client
Summary(pl.UTF-8):	Rozwojowa wersja Sylpheed z dużą ilością zmian oraz ulepszeń
Name:		claws-mail
Version:	3.7.1
Release:	1
License:	GPL v3
Group:		X11/Applications/Mail
Source0:	http://dl.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# Source0-md5:	8351ba15b04c1388d772ba52e41a8643
Source1:	%{name}.desktop
URL:		http://www.claws-mail.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bzip2-devel
%{?with_compface:BuildRequires:	compface-devel}
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
%{?with_tls:BuildRequires:	gnutls-devel >= 2.6.0}
%{?with_gpg:BuildRequires:	gpgme-devel >= 1:0.4.5}
BuildRequires:	gtk+2-devel >= 2:2.12.8
BuildRequires:	libetpan-devel >= 0.57
BuildRequires:	liblockfile-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%{?with_jpilot:BuildRequires:	pilot-link-devel}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	startup-notification-devel >= 0.5
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	gtk+2 >= 2:2.12.8
Provides:	sylpheed-claws
Obsoletes:	claws-mail-plugin-clamav
Obsoletes:	claws-mail-plugin-etpan-privacy
Obsoletes:	claws-mail-plugin-maildir
Obsoletes:	claws-mail-plugin-pdf_viewer
Obsoletes:	sylpheed-claws
Obsoletes:	sylpheed-claws-plugin-clamav
Obsoletes:	sylpheed-gtk2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is an X based fast e-mail client which has features same
as orginal Sylpheed but with new/improved features. Some of new stuff
is really cool and useable.

%description -l pl.UTF-8
Szybki klient poczty o możliwościach takich jak oryginalny Sylpheed
ale z nowymi/poprawionymi funkcjami. Niektóre dodatki są naprawdę
świetne i użyteczne.

%package devel
Summary:	Headers from Claws-Mail
Summary(pl.UTF-8):	Pliki nagłówkowe programu Claws-Mail
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnutls-devel >= 2.6.0
Requires:	gpgme-devel >= 1:0.4.5
Requires:	libetpan-devel >= 0.54
Provides:	sylpheed-claws-devel
Obsoletes:	sylpheed-claws-devel

%description devel
Claws-Mail development package.

%description devel -l pl.UTF-8
Pliki nagłówkowe programu Claws-Mail.

%package plugins
Summary:	Special plugins for Claws-Mail (metapackage)
Summary(pl.UTF-8):	Dodatkowe wtyczki dla Claws-Mail (metapakiet)
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugin-bogofilter = %{version}-%{release}
Requires:	%{name}-plugin-dillo = %{version}-%{release}
%if %{with gpg}
Requires:	%{name}-plugin-pgpinline = %{version}-%{release}
Requires:	%{name}-plugin-pgpmime = %{version}-%{release}
%endif
Requires:	%{name}-plugin-smime = %{version}-%{release}
Requires:	%{name}-plugin-spamassassin = %{version}-%{release}
Requires:	%{name}-plugin-trayicon = %{version}-%{release}
Provides:	sylpheed-claws-plugins = %{version}
Obsoletes:	sylpheed-claws-plugins

%description plugins
This is collection of some usefull plugins for Claws-Mail
(metapackage).

%description plugins -l pl.UTF-8
Jest to zbiór kilku dodatkowych wtyczek powiększających możliwości
Claws-Mail (metapakiet).

%package plugin-bogofilter
Summary:	Bogofilter plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka bogofilter dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	bogofilter
Provides:	sylpheed-claws-plugin-bogofilter
Obsoletes:	sylpheed-claws-plugin-bogofilter

%description plugin-bogofilter
This plugin enables the scanning of incoming mail received from a POP,
IMAP or LOCAL account using Bogofilter. It can optionally delete mail
identified as spam or save it to a designated folder.

%description plugin-bogofilter -l pl.UTF-8
Wtyczka pozwalająca na skanowanie bogofilterem poczty przychodzącej
jak i już znajdującej się w lokalnych skrzynkach. Opcjonalnie może
usuwać listy oznaczone jako spam lub zapisywać je w dedykowanym
folderze.

%package plugin-dillo
Summary:	dillo plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka dillo dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	dillo
Provides:	sylpheed-claws-plugin-dillo
Obsoletes:	sylpheed-claws-plugin-dillo
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-dillo
This plugin enables the viewing of html messages using the Dillo web
browser.

%description plugin-dillo -l pl.UTF-8
Wtyczka pozwalająca na przeglądanie listów pisanych w HTML przy pomocy
przeglądarki Dillo.

%package plugin-pgpcore
Summary:	PGP/Core plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka PGP/Core dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-pgpcore
Obsoletes:	sylpheed-claws-plugin-pgpcore
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-pgpcore
This plugin handles core PGP functions.

%description plugin-pgpcore -l pl.UTF-8
Wtyczka obsługująca podstawowe funkcje PGP.

%package plugin-pgpinline
Summary:	PGP/Inline plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka PGP/Inline dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name}-plugin-pgpcore = %{version}-%{release}
Provides:	sylpheed-claws-plugin-pgpinline
Obsoletes:	sylpheed-claws-plugin-pgpinline
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-pgpinline
This plugin handles PGP/Inline signed and/or encrypted mails. It can
decrypt mails, verify signatures or sign and encrypt your own mails.

%description plugin-pgpinline -l pl.UTF-8
Wtyczka obsługująca listy podpisane lub szyfrowane PGP/Inline. Potrafi
rozszyfrowywać, sprawdzać podpisy a także szyfrować i podpisywać
własne listy.

%package plugin-pgpmime
Summary:	PGP/MIME plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka PGP/MIME dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name}-plugin-pgpcore = %{version}-%{release}
Provides:	sylpheed-claws-plugin-pgpmime
Obsoletes:	sylpheed-claws-plugin-pgpmime
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-pgpmime
This plugin handles PGP/MIME signed and/or encrypted mails. It can
decrypt mails, verify signatures or sign and encrypt your own mails.

%description plugin-pgpmime -l pl.UTF-8
Wtyczka obsługująca listy podpisane lub szyfrowane PGP/MIME. Potrafi
rozszyfrowywać, sprawdzać podpisy a także szyfrować i podpisywać
własne listy.

%package plugin-smime
Summary:	S/MIME plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka S/MIME dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugin-pgpcore = %{version}-%{release}
Provides:	sylpheed-claws-plugin-smime
Obsoletes:	sylpheed-claws-plugin-smime

%description plugin-smime
This plugin handles S/MIME signed and/or encrypted mails. You can
decrypt mails, verify signatures or sign and encrypt your own mails.

%description plugin-smime -l pl.UTF-8
Wtyczka obsługująca listy podpisane lub szyfrowane S/MIME. Potrafi
rozszyfrowywać, sprawdzać podpisy a także szyfrować i podpisywać
własne listy.

%package plugin-spamassassin
Summary:	spamassassin plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka spamassassin dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-spamassassin
Obsoletes:	sylpheed-claws-plugin-spamassassin
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-spamassassin
This plugin enables the scanning of incoming mail received from a POP,
IMAP, or LOCAL account using SpamAssassin. It can optionally delete
mail identified as spam or save it to a designated folder, and also
can be used to train a local Spamassassin or a remote one.

%description plugin-spamassassin -l pl.UTF-8
Wtyczka pozwalająca na skanowanie SpamAssassinem poczty przychodzącej
jak i już znajdującej się w lokalnych skrzynkach. Opcjonalnie może
usuwać listy oznaczone jako spam lub zapisywać je w dedykowanym
folderze. Może też byż używana do "uczenia" lokalnego lub zdalnego
demona SpamAssassin.

%package plugin-trayicon
Summary:	trayicon plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka trayicon dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-trayicon
Obsoletes:	sylpheed-claws-plugin-trayicon
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-trayicon
This plugin places an icon in the system tray that indicates whether
you have any new mail. A tooltip also shows the current new, unread
and total number of messages, and a contextual menu allows the most
common operations.

%description plugin-trayicon -l pl.UTF-8
Wtyczka umieszczająca w tacce systemowej ikonę informującą o nadejściu
nowej poczty. Ikona wyświetla dane na temat wiadomości (ilość nowych,
nieprzeczytanych i wszystkich) a jej menu pozwala wykonywać
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
	--%{?with_compface:en}%{!?with_compface:dis}able-compface \
	--%{?with_gpg:en}%{!?with_gpg:dis}able-pgpcore-plugin \
	--%{?with_gpg:en}%{!?with_gpg:dis}able-pgpmime-plugin \
	--%{?with_gpg:en}%{!?with_gpg:dis}able-pgpinline-plugin \
	--%{?with_ipv6:en}%{!?with_ipv6:dis}able-ipv6 \
	--%{?with_jpilot:en}%{!?with_jpilot:dis}able-jpilot \
	--%{?with_ldap:en}%{!?with_ldap:dis}able-ldap \
	--%{?with_tls:en}%{!?with_tls:dis}able-gnutls \
	--enable-bogofilter-plugin \
	--enable-dillo-viewer-plugin \
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

%files plugin-smime
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/smime.so

%files plugin-spamassassin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/spamassassin.so

%files plugin-trayicon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/trayicon.so
