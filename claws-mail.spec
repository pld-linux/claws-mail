#
# Conditional build:
%bcond_without	compface	# build without compface support
%bcond_without	gpg		# build without GPG support
%bcond_without	ipv6		# build without IPv6 support
%bcond_without	jpilot		# build without JPilot support
%bcond_without	ldap		# build without LDAP support
%bcond_without	tls		# build without gnuTLS support
%bcond_with	valgrind	# Valgrind support for debugging

Summary:	A bleeding edge branch of Sylpheed, a GTK2 based, lightweight, and fast e-mail client
Summary(pl.UTF-8):	Rozwojowa wersja Sylpheed z dużą ilością zmian oraz ulepszeń
Name:		claws-mail
Version:	3.17.8
Release:	2
License:	GPL v3+
Group:		X11/Applications/Mail
#Source0Download: https://www.claws-mail.org/releases.php
Source0:	https://www.claws-mail.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	9a29794503e17921b14a5265425181db
Source1:	%{name}.desktop
Patch0:		%{name}-link.patch
URL:		https://www.claws-mail.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cairo-devel
%{?with_compface:BuildRequires:	compface-devel}
BuildRequires:	curl-devel
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	docbook-utils
# or enchant2-devel >= 2.0.0, but currently 1.4 is preferred
BuildRequires:	enchant-devel >= 1.4.0
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.26
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	glib2-devel >= 1:2.36
%{?with_tls:BuildRequires:	gnutls-devel >= 3.0}
%{?with_gpg:BuildRequires:	gpgme-devel >= 1:1.1.1}
BuildRequires:	gtk+2-devel >= 2:2.24.0
BuildRequires:	gtk-webkit-devel >= 1.10.0
BuildRequires:	gumbo-parser-devel >= 0.10
BuildRequires:	libarchive-devel
BuildRequires:	libcanberra-gtk-devel >= 0.6
BuildRequires:	libetpan-devel >= 1.9.4
BuildRequires:	libgdata-devel >= 0.17.2
BuildRequires:	libical-devel >= 2.0.0
BuildRequires:	libnotify-devel >= 0.4.3
BuildRequires:	librsvg-devel >= 1:2.40.5
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libsoup-gnome-devel >= 2.26
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
#TODO: libunity-devel
BuildRequires:	NetworkManager-devel
BuildRequires:	libytnef-devel
BuildRequires:	nettle-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_jpilot:BuildRequires:	pilot-link-devel}
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.12.0
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pygtk-devel >= 2:2.10.3
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel >= 0.5
BuildRequires:	tar >= 1:1.22
BuildRequires:	texlive-jadetex
BuildRequires:	texlive-latex-marvosym
%{?with_valgrind:BuildRequires:	valgrind-devel >= 2.4.0}
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	dbus-glib >= 0.60
Requires:	enchant >= 1.4.0
Requires:	gdk-pixbuf2 >= 2.26
Requires:	glib2 >= 1:2.36
%{?with_tls:Requires:	gnutls >= 3.0}
Requires:	gtk+2 >= 2:2.24.0
Requires:	libetpan >= 1.9.4
Requires:	librsvg >= 1:2.40.5
%{?with_ldap:Requires:	openldap-libs >= 2.3.0}
Requires:	startup-notification >= 0.5
Provides:	sylpheed-claws
Obsoletes:	claws-mail-plugin-acpi_notifier
Obsoletes:	claws-mail-plugin-address_keeper
Obsoletes:	claws-mail-plugin-att_remover
Obsoletes:	claws-mail-plugin-attachwarner
Obsoletes:	claws-mail-plugin-bogofilter
Obsoletes:	claws-mail-plugin-bsfilter
Obsoletes:	claws-mail-plugin-cachesaver <= 3.7.6-5
Obsoletes:	claws-mail-plugin-clamav
Obsoletes:	claws-mail-plugin-clamd
Obsoletes:	claws-mail-plugin-dillo <= 3.9.0
Obsoletes:	claws-mail-plugin-etpan-privacy
Obsoletes:	claws-mail-plugin-fetchinfo
Obsoletes:	claws-mail-plugin-gtkhtml2_viewer <= 3.9.0
Obsoletes:	claws-mail-plugin-maildir
Obsoletes:	claws-mail-plugin-mailmbox
Obsoletes:	claws-mail-plugin-newmail
Obsoletes:	claws-mail-plugin-spamassassin
Obsoletes:	claws-mail-plugin-synce <= 3.7.6-5
Obsoletes:	claws-mail-plugin-tnef_parse
Obsoletes:	claws-mail-plugin-trayicon <= 3.9.0
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
Requires:	enchant-devel >= 1.4.0
Requires:	glib2-devel >= 1:2.36
%{?with_tls:Requires:	gnutls-devel >= 3.0}
%{?with_gpg:Requires:	gpgme-devel >= 1:1.1.1}
Requires:	gtk+2-devel >= 2:2.24.0
Requires:	libetpan-devel >= 1.9.4
%{?with_ldap:Requires:	openldap-devel >= 2.3.0}
%{?with_jpilot:Requires: pilot-link-devel}
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
Requires:	%{name}-plugin-archive = %{version}-%{release}
Requires:	%{name}-plugin-fancy = %{version}-%{release}
Requires:	%{name}-plugin-gdata = %{version}-%{release}
Requires:	%{name}-plugin-libravatar = %{version}-%{release}
Requires:	%{name}-plugin-litehtml_viewer = %{version}-%{release}
Requires:	%{name}-plugin-notification = %{version}-%{release}
Requires:	%{name}-plugin-pdf_viewer = %{version}-%{release}
Requires:	%{name}-plugin-perl = %{version}-%{release}
%if %{with gpg}
Requires:	%{name}-plugin-pgpinline = %{version}-%{release}
Requires:	%{name}-plugin-pgpmime = %{version}-%{release}
%endif
Requires:	%{name}-plugin-python = %{version}-%{release}
Requires:	%{name}-plugin-rssyl = %{version}-%{release}
%if %{with gpg}
Requires:	%{name}-plugin-smime = %{version}-%{release}
%endif
Requires:	%{name}-plugin-spamreport = %{version}-%{release}
Requires:	%{name}-plugin-vcalendar = %{version}-%{release}
Provides:	sylpheed-claws-extra-plugins
Provides:	sylpheed-claws-plugins = %{version}
Obsoletes:	claws-mail-extra-plugins <= 3.9.0
Obsoletes:	sylpheed-claws-extra-plugins
Obsoletes:	sylpheed-claws-plugin-others
Obsoletes:	sylpheed-claws-plugins

%description plugins
This is collection of some usefull plugins for Claws-Mail
(metapackage).

%description plugins -l pl.UTF-8
Jest to zbiór kilku dodatkowych wtyczek powiększających możliwości
Claws-Mail (metapakiet).

%package plugin-archive
Summary:	archive plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka archive dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description plugin-archive
This plugin lets you archive IMAP, LOCAL and POP accounts as well as
calendar accounts.

%description plugin-archive -l pl.UTF-8
Ta wtyczka pozwala archiwizować konta IMAP, LOCAL i POP jak również
kalendarze.

%package plugin-fancy
Summary:	fancy plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka fancy dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	gtk-webkit >= 1.10.0
Requires:	libsoup-gnome >= 2.26

%description plugin-fancy
Renders HTML e-mail using the WebKit library.

%description plugin-fancy -l pl.UTF-8
Ta wtyczka przetwarza wiadomości w formacie HTML przy użyciu
biblioteki WebKit.

%package plugin-gdata
Summary:	gdata plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka gdata dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	libgdata >= 0.17.2

%description plugin-gdata
gdata plugin for Claws-Mail.

%description plugin-gdata -l pl.UTF-8
Wtyczka gdata dla Claws-Mail.

%package plugin-libravatar
Summary:	Avatar fetching plugin
Summary(pl.UTF-8):	Wtyczka pobierająca avatary
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description plugin-libravatar
Avatar fetching plugin.

%description plugin-libravatar -l pl.UTF-8
Wtyczka pobierająca avatary.

%package plugin-litehtml_viewer
Summary:	Light HTML viewer plugin for Claws Mail
Summary(pl.UTF-8):	Wtyczka z lekką przeglądarką HTML dla Claws Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	gumbo-parser >= 0.10

%description plugin-litehtml_viewer
Viewer plugin for HTML emails, using the litehtml library
(<http://www.litehtml.com/>).

%description plugin-litehtml_viewer -l pl.UTF-8
Wtyczka z przeglądarką do wiadomości HTML, wykorzystująca bibliotekę
litehtml (<http://www.litehtml.com/>).

%package plugin-notification
Summary:	notification plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka notification dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	libcanberra-gtk >= 0.6
Requires:	libnotify >= 0.4.3
Provides:	sylpheed-claws-plugin-notification
Obsoletes:	sylpheed-claws-plugin-notification

%description plugin-notification
This plugin provides various ways to notify the user of new and unread
email.

%description plugin-notification -l pl.UTF-8
Ta wtyczka udostępnia różne sposoby informowania użytkownika o nowej i
nieprzeczytanej poczcie.

%package plugin-perl
Summary:	perl plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka perl dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-perl
Obsoletes:	sylpheed-claws-plugin-perl

%description plugin-perl
This plugin is intended to extend the filtering possibilities of
Claws-Mail. It provides a Perl interface to Claws-Mail filtering
mechanism, allowing the use of full Perl power in email filters.

%description plugin-perl -l pl.UTF-8
Ta wtyczka ma na celu rozszerzenie możliwości filtrowania
Sylpheeda-Claws. Udostępnia perlowy interfejs do mechanizmów
filtrowania Sylpheeda-Claws, pozwalając na użycie pełnej mocy Perla w
filtrach wiadomości.

%package plugin-pdf_viewer
Summary:	pdf_viewer plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka pdf_viewer dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	ghostscript
Requires:	poppler-glib >= 0.12.0

%description plugin-pdf_viewer
This plugin enables the viewing of PDF and PostScript attachments.

%description plugin-pdf_viewer -l pl.UTF-8
Ta wtyczka umożliwia wyświetlanie załączników w formacie PDF i
PostScript.

%package plugin-pgpcore
Summary:	PGP/Core plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka PGP/Core dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	gpgme >= 1:1.1.1
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

%package plugin-python
Summary:	python plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka python dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description plugin-python
This plugin provides Python integration features.

%description plugin-python -l pl.UTF-8
Wtyczka do pythona.

%package plugin-rssyl
Summary:	RSSyl plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka RSSyl dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-rssyl
Obsoletes:	sylpheed-claws-plugin-rssyl

%description plugin-rssyl
This plugin allows you to read your favorite newsfeeds in Claws-Mail.
RSS 1.0, 2.0 and Atom feeds are currently supported.

%description plugin-rssyl -l pl.UTF-8
Ta wtyczka pozwala na czytanie ulubionych nowinek w Sylpheedzie-Claws.
Aktualnie obsługiwane są formaty RSS 1.0, 2.0 i Atom.

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

%package plugin-spamreport
Summary:	SpamReport plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka SpamReport dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description plugin-spamreport
This plugin allows you to upload spams to various spam reporting
places, like <http://www.signal-spam.fr/>.

%description plugin-spamreport -l pl.UTF-8
Ta wtyczka pozwala przesyłać spam do różnych miejsc raportowania,
takich jak <http://www.signal-spam.fr/>.

%package plugin-vcalendar
Summary:	vCalendar plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka vCalendar dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	libical >= 2.0.0
Provides:	sylpheed-claws-plugin-vcalendar
Obsoletes:	sylpheed-claws-plugin-vcalendar

%description plugin-vcalendar
This plugin enables vCalendar message handling like that produced by
Evolution or Outlook and handles webCal subscriptions.

%description plugin-vcalendar -l pl.UTF-8
Ta wtyczka pozwala na obsługę wiadomości vCalendar, takich jak te
tworzone przez Evolution czy Outlooka, a także obsługuje subskrypcje
webCal.

%prep
%setup -q
%patch0 -p1

%{__rm} po/stamp-po

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-compface%{!?with_compface:=no} \
	--enable-gnutls%{!?with_tls:=no} \
	--enable-ipv6%{!?with_ipv6:=no} \
	--enable-jpilot%{!?with_jpilot:=no} \
	--enable-ldap%{!?with_ldap:=no} \
	--enable-libetpan \
	--enable-pgpcore-plugin%{!?with_gpg:=no} \
	--enable-pgpinline-plugin%{!?with_gpg:=no} \
	--enable-pgpmime-plugin%{!?with_gpg:=no} \
	--enable-smime-plugin%{!?with_gpg:=no} \
	--enable-valgrind%{!?with_valgrind:=no} \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name}/themes,%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.{deps,la}
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/el_GR
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}/RELEASE_NOTES
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}/manual/{en,es,fr}/*.{pdf,ps,html,txt}

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{id_ID,id}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{pt_PT,pt}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README RELEASE_NOTES TODO
%attr(755,root,root) %{_bindir}/claws-mail
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/themes
%dir %{_docdir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
# no (big) external deps
%attr(755,root,root) %{_libdir}/%{name}/plugins/acpi_notifier.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/address_keeper.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/att_remover.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/attachwarner.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/bogofilter.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/bsfilter.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/clamd.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/dillo.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/fetchinfo.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/mailmbox.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/managesieve.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/newmail.so
# R: zlib
%attr(755,root,root) %{_libdir}/%{name}/plugins/spamassassin.so
# R: libytnef
%attr(755,root,root) %{_libdir}/%{name}/plugins/tnef_parse.so
%{_desktopdir}/claws-mail.desktop
%{_pixmapsdir}/claws-mail.png
%{_iconsdir}/hicolor/48x48/apps/claws-mail.png
%{_iconsdir}/hicolor/64x64/apps/claws-mail.png
%{_iconsdir}/hicolor/128x128/apps/claws-mail.png
%{_mandir}/man1/claws-mail.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/claws-mail
%{_pkgconfigdir}/claws-mail.pc

%files plugins
%defattr(644,root,root,755)

# R: libarchive
%files plugin-archive
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/archive.so

# R: curl gtk-webkit libsoup libsoup-gnome
%files plugin-fancy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/fancy.so

# R: libgdata
%files plugin-gdata
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/gdata.so

# R: curl-libs
%files plugin-libravatar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libravatar.so

# R: cairo curl fontconfig gumbo-parser
%files plugin-litehtml_viewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/litehtml_viewer.so

# R: libcanberra-gtk libnotify [libunity]
%files plugin-notification
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/notification.so

# R: perl-base
%files plugin-perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/perl.so

# R: poppler-glib
%files plugin-pdf_viewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/pdf_viewer.so

%if %{with gpg}
# R: gpgme
%files plugin-pgpcore
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/pgpcore.so

# R: gpgme
%files plugin-pgpinline
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/pgpinline.so

# R: gpgme
%files plugin-pgpmime
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/pgpmime.so
%endif

# R: python-libs
%files plugin-python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/python.so

# R: curl expat
%files plugin-rssyl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/rssyl.so

%if %{with gpg}
# R: gpgme
%files plugin-smime
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/smime.so
%endif

# R: curl
%files plugin-spamreport
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/spamreport.so

# R: curl libical perl-base
%files plugin-vcalendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/vcalendar.so
