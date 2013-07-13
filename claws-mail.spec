#
# Conditional build:
%bcond_without	compface	# build without compface support
%bcond_without	gpg		# build without GPG support
%bcond_without	ipv6		# build without IPv6 support
%bcond_without	jpilot		# build without JPilot support
%bcond_without	ldap		# build without LDAP support
%bcond_without	tls		# build without gnuTLS support
%bcond_with	geolocation

Summary:	A bleeding edge branch of Sylpheed, a GTK2 based, lightweight, and fast e-mail client
Summary(pl.UTF-8):	Rozwojowa wersja Sylpheed z dużą ilością zmian oraz ulepszeń
Name:		claws-mail
Version:	3.9.2
Release:	3
License:	GPL v3+
Group:		X11/Applications/Mail
Source0:	http://downloads.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# Source0-md5:	90de2a265e65fbd9dffdbf428bb0ee28
Source1:	%{name}.desktop
URL:		http://www.claws-mail.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bzip2-devel
%if %{with geolocation}
BuildRequires:	clutter-gtk-devel >= 0.10.0
BuildRequires:	libchamplain-devel >= 0.8.0
%endif
%{?with_compface:BuildRequires:	compface-devel}
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
%{?with_tls:BuildRequires:	gnutls-devel >= 2.6.0}
%{?with_gpg:BuildRequires:	gpgme-devel >= 1:0.4.5}
BuildRequires:	gtk+2-devel >= 2:2.24.0
BuildRequires:	gtk-webkit-devel
BuildRequires:	libarchive-devel
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	libetpan-devel >= 0.57
BuildRequires:	libgdata-devel >= 0.6.4
BuildRequires:	liblockfile-devel
BuildRequires:	libltdl-devel
BuildRequires:	libnotify-devel >= 0.4.3
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libytnef-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%if %{with jpilot}
BuildRequires:	bluez-libs-devel
BuildRequires:	pilot-link-devel
%endif
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel >= 0.5
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	gtk+2 >= 2:2.24.0
Provides:	sylpheed-claws
Obsoletes:	claws-mail-plugin-cachesaver <= 3.7.6-5
Obsoletes:	claws-mail-plugin-clamav
Obsoletes:	claws-mail-plugin-dillo <= 3.9.0
Obsoletes:	claws-mail-plugin-etpan-privacy
Obsoletes:	claws-mail-plugin-gtkhtml2_viewer <= 3.9.0
Obsoletes:	claws-mail-plugin-maildir
Obsoletes:	claws-mail-plugin-pdf_viewer
Obsoletes:	claws-mail-plugin-synce <= 3.7.6-5
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
%if %{with gpg}
Requires:	%{name}-plugin-pgpinline = %{version}-%{release}
Requires:	%{name}-plugin-pgpmime = %{version}-%{release}
%endif
Requires:	%{name}-plugin-acpi_notifier = %{version}-%{release}
Requires:	%{name}-plugin-address_keeper = %{version}-%{release}
Requires:	%{name}-plugin-archive = %{version}-%{release}
Requires:	%{name}-plugin-att_remover = %{version}-%{release}
Requires:	%{name}-plugin-attachwarner = %{version}-%{release}
Requires:	%{name}-plugin-bsfilter = %{version}-%{release}
Requires:	%{name}-plugin-clamd = %{version}-%{release}
Requires:	%{name}-plugin-fancy = %{version}-%{release}
Requires:	%{name}-plugin-fetchinfo = %{version}-%{release}
Requires:	%{name}-plugin-gdata = %{version}-%{release}
Requires:	%{name}-plugin-mailmbox = %{version}-%{release}
Requires:	%{name}-plugin-newmail = %{version}-%{release}
Requires:	%{name}-plugin-notification = %{version}-%{release}
Requires:	%{name}-plugin-perl = %{version}-%{release}
Requires:	%{name}-plugin-rssyl = %{version}-%{release}
Requires:	%{name}-plugin-smime = %{version}-%{release}
Requires:	%{name}-plugin-spamassassin = %{version}-%{release}
Requires:	%{name}-plugin-spamreport = %{version}-%{release}
Requires:	%{name}-plugin-tnef_parse = %{version}-%{release}
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

%package plugin-acpi_notifier
Summary:	acpi_notifier plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka acpi_notifier dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-acpi_notifier
Obsoletes:	sylpheed-claws-plugin-acpi_notifier

%description plugin-acpi_notifier
This plugin enables mail notification via LEDs on some laptops.

%description plugin-acpi_notifier -l pl.UTF-8
Ta wtyczka umożliwia w niektórych laptopach powiadamianie o nowej
poczcie poprzez diody LED.

%package plugin-address_keeper
Summary:	address_keeper plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka address_keeper dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-address_keeper
Obsoletes:	sylpheed-claws-plugin-address_keeper

%description plugin-address_keeper
Keeps all recipient addresses in an addressbook folder.

%description plugin-address_keeper -l pl.UTF-8
Trzyma wszystkie adresy w dedykowanym folderze.

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

%package plugin-att_remover
Summary:	att_remover plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka att_remover dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-att_remover
Obsoletes:	sylpheed-claws-plugin-att_remover

%description plugin-att_remover
This plugin lets you remove attachments from emails.

%description plugin-att_remover -l pl.UTF-8
Ta wtyczka pozwala usuwać załączniki z poczty.

%package plugin-attachwarner
Summary:	attachwarner plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka attachwarner dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description plugin-attachwarner
This plugin warns when the user composes a message mentioning an
attachment in the message body, but without attaching any files to the
message.

%description plugin-attachwarner -l pl.UTF-8
Ta wtyczka ostrzega, kiedy użytkownik piszący wiadomość wspomina w
treści o załączniku, ale nie załącza żadnego pliku do wiadomości.

%package plugin-clamd
Summary:	clamd plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka clamd dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	clamav

%description plugin-clamd
Scan all messages that are received from an IMAP, LOCAL or POP account
using clamd (Clam AV).

%description plugin-clamd -l pl.UTF-8
Sprawdza wszystkie wiadomości odebrane poprzez IMAP, LOCAL lub POP
przy użyciu clamd (Clam AV).

%package plugin-bsfilter
Summary:	bsfilter plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka bsfilter dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description plugin-bsfilter
Check all messages that are received from an IMAP, LOCAL or POP
account for spam using Bsfilter.

%description plugin-bsfilter -l pl.UTF-8
Ta wtyczka sprawdza wszystkie wiadomości odebrane przez IMAP, lokalnie
bądź POP pod kątem występowania spamu przy użyciu bsfilter.

%package plugin-fancy
Summary:	fancy plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka fancy dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description plugin-fancy
Renders HTML e-mail using the WebKit library.

%description plugin-fancy -l pl.UTF-8
Ta wtyczka przetwarza wiadomości w formacie HTML przy użyciu
biblioteki WebKit.

%package plugin-fetchinfo
Summary:	fetchinfo plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka fetchinfo dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-fetchinfo
Obsoletes:	sylpheed-claws-plugin-fetchinfo

%description plugin-fetchinfo
This plugin inserts headers containing some download information:
UIDL, Claws-Mail, account name, POP server, user ID and retrieval
time.

%description plugin-fetchinfo -l pl.UTF-8
Ta wtyczka wstawia nagłówki zawierające informacje o ściąganiu: UIDL,
Claws-Mail, nazwę konta, serwer POP, identyfikator użytkownika i czas
pobrania.

%package plugin-gdata
Summary:	gdata plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka gdata dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description plugin-gdata
gdata plugin for Claws-Mail.

%description plugin-gdata -l pl.UTF-8
Wtyczka gdata dla Claws-Mail.

%package plugin-geolocation
Summary:	geolocation plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka geolocation dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description plugin-geolocation
This plugin provides GeoLocation functionality.

%description plugin-geolocation -l pl.UTF-8
Wtyczka dostarcza funkcje geolokacji.

%package plugin-mailmbox
Summary:	mailMBOX plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka mailMBOX dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-mailmbox
Obsoletes:	sylpheed-claws-plugin-mailmbox

%description plugin-mailmbox
This plugin handles mailboxes in mbox format.

%description plugin-mailmbox -l pl.UTF-8
Ta wtyczka obsługuje skrzynki w formacie mbox.

%package plugin-newmail
Summary:	newmail plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka newmail dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
Provides:	sylpheed-claws-plugin-newmail
Obsoletes:	sylpheed-claws-plugin-newmail

%description plugin-newmail
This plugin writes a msg header summary to a log file, (Default:
~/Mail/NewLog), on arrival of new mail after sorting.

%description plugin-newmail -l pl.UTF-8
Ta wtyczka zapisuje podsumowanie nagłówków wiadomości do pliku loga
(domyślnie ~/Mail/NewLog) w czasie dostarczania nowej poczty, po
sortowaniu.

%package plugin-notification
Summary:	notification plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka notification dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
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

%description plugin-pdf_viewer
This plugin enables the viewing of PDF and PostScript attachments.

%description plugin-pdf_viewer -l pl.UTF-8
Ta wtyczka umożliwia wyświetlanie załączników w formacie PDF i
PostScript.

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

%package plugin-spamreport
Summary:	SpamReport plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka SpamReport dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description plugin-spamreport
This plugin allows you to upload spams to various spam reporting
places, like http://www.signal-spam.fr/ .

%package plugin-tnef_parse
Summary:	TNEF Parse plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka TNEF Parse dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description plugin-tnef_parse
This plugin enables reading application/ms-tnef attachments.

%description plugin-tnef_parse -l pl.UTF-8
Ta wtyczka pozwala czytać załączniki typu application/ms-tnef.

%package plugin-vcalendar
Summary:	vCalendar plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka vCalendar dla Claws-Mail
Group:		X11/Applications/Mail
Requires:	%{name} = %{version}-%{release}
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

%{__rm} po/stamp-po

# id_ID -> id and pt_PT -> pt hacks
mv -f po/{id_ID,id}.po
mv -f po/{pt_PT,pt}.po
%{__sed} -i -e 's,pt_PT,pt,g;s,id_ID,id,g' src/codeconv.c
%{__sed} -i -e 's,pt_PT,pt,g;s,id_ID,id,g' configure.ac

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--%{?with_compface:en}%{!?with_compface:dis}able-compface \
	--%{?with_ipv6:en}%{!?with_ipv6:dis}able-ipv6 \
	--%{?with_jpilot:en}%{!?with_jpilot:dis}able-jpilot \
	--%{?with_ldap:en}%{!?with_ldap:dis}able-ldap \
	--%{?with_tls:en}%{!?with_tls:dis}able-gnutls \
	--enable-acpi_notifier-plugin \
	--enable-address_keeper-plugin \
	--enable-archive-plugin \
	--enable-att_remover-plugin \
	--enable-attachwarner-plugin \
	--enable-bogofilter-plugin \
	--enable-bsfilter-plugin \
	--enable-clamd-plugin \
	--enable-fancy-plugin \
	--enable-fetchinfo-plugin \
	--enable-gdata-plugin \
	--%{?with_geolocation:en}%{!?with_geolocation:dis}able-geolocation-plugin \
	--enable-mailmbox-plugin \
	--enable-newmail-plugin \
	--enable-notification-plugin \
	--enable-pdf_viewer-plugin \
	--enable-perl-plugin \
	--enable-python-plugin \
	--%{?with_gpg:en}%{!?with_gpg:dis}able-pgpcore-plugin \
	--%{?with_gpg:en}%{!?with_gpg:dis}able-pgpmime-plugin \
	--%{?with_gpg:en}%{!?with_gpg:dis}able-pgpinline-plugin \
	--enable-rssyl-plugin \
	--enable-smime-plugin \
	--enable-spamassassin-plugin \
	--enable-spam_report-plugin \
	--enable-tnef_parse-plugin \
	--enable-vcalendar-plugin \
	--enable-libetpan \
	--enable-pthread \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name}/themes,%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.{deps,la}
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}/RELEASE_NOTES
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}/manual/{de,en,es,fr,pl}/*.{pdf,ps,html,txt}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README* RELEASE_NOTES TODO
%{_mandir}/man1/%{name}.1*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_docdir}/%{name}
%dir %{_datadir}/%{name}/themes
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%{_iconsdir}/hicolor/128x128/apps/%{name}.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files plugins
%defattr(644,root,root,755)

%files plugin-bogofilter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/bogofilter.so

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

%files plugin-acpi_notifier
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/acpi_notifier.so

%files plugin-address_keeper
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/address_keeper.so

%files plugin-archive
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/archive.so

%files plugin-att_remover
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/att_remover.so

%files plugin-attachwarner
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/attachwarner.so

%files plugin-bsfilter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/bsfilter.so

%files plugin-clamd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/clamd.so

%files plugin-fancy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/fancy.so

%files plugin-fetchinfo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/fetchinfo.so

%files plugin-gdata
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/gdata.so

%if %{with geolocation}
%files plugin-geolocation
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/geolocation.so
%endif

%files plugin-mailmbox
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/mailmbox.so

%files plugin-newmail
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/newmail.so

%files plugin-notification
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/notification.so

%files plugin-perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/perl.so

%files plugin-pdf_viewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/pdf_viewer.so

%files plugin-python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/python.so

%files plugin-rssyl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/rssyl.so

%files plugin-spamreport
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/spamreport.so

%files plugin-tnef_parse
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/tnef_parse.so

%files plugin-vcalendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/vcalendar.so
