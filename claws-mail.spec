# TODO:
# - pl description for new subpackages
#
# Conditional build:
%bcond_without  clamav          # build without clamav plugin
%bcond_without  compface        # build without compface support
%bcond_without  dillo           # build without dillo plugin (html browser)
%bcond_without  gnomeprint      # build without gnomeprint support
%bcond_without	gpg		# build without GPG support
%bcond_without  ipv6            # build without IPv6 support
%bcond_without	jpilot		# build without JPilot support
%bcond_without  ldap            # build without LDAP support
%bcond_without	spamassassin	# build without spamassassin plugin
%bcond_without  ssl             # build without SSL support
%bcond_without	trayicon	# build without trayicon plugin
#
Summary:	A bleeding edge branch of Sylpheed, a GTK2 based, lightweight, and fast e-mail client
Summary(pl):	Rozwojowa wersja Sylpheed z du¿± ilo¶ci± zmian oraz ulepszeñ
Name:		sylpheed-claws
Version:	2.3.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# Source0-md5:	08e8fe1f3466d146b499d128f1445ba6
Source1:	%{name}.desktop
URL:		http://www.sylpheed-claws.net/
BuildRequires:	aspell-devel >= 2:0.50
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bzip2-devel
%{?with_clamav:BuildRequires:	clamav-devel}
%{?with_compface:BuildRequires:	compface-devel}
BuildRequires:	gdk-pixbuf-devel >= 0.8
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
%{?with_gpg:BuildRequires:	gpgme-devel >= 1:0.4.5}
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	imlib-devel >= 1.9
BuildRequires:	libetpan-devel >= 0.45
%{?with_gnomeprint:BuildRequires:	libgnomeprintui-devel}
BuildRequires:	libltdl-devel
BuildRequires:	libtool
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
%{?with_jpilot:BuildRequires:	pilot-link-devel}
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel >= 0.5
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

%package plugins
Summary:	Special plugins for Sylpheed-Claws (metapackage)
Summary(pl):	Dodatkowe pluginy dla Sylpheed-Claws (metapakiet)
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
%{?with_clamav:Requires: %{name}-plugin-clamav = %{version}-%{release}}
%{?with_dillo:Requires:	%{name}-plugin-dillo = %{version}-%{release}}
%if %{with gpg}
Requires:	%{name}-plugin-pgpinline = %{version}-%{release}
Requires:	%{name}-plugin-pgpmime = %{version}-%{release}
%endif
%{?with_spamassassin:Requires: %{name}-plugin-spamassassin = %{version}-%{release}}
%{?with_trayicon:Requires: %{name}-plugin-trayicon = %{version}-%{release}}

%description plugins
This is collection of some usefull plugins for Sylpheed-Claws
(metapackage).

%description plugins -l pl
Jest to zbiór kilku dodatkowych pluginów powiêkszaj±cych mo¿liwo¶ci
Sylpheed-Claws (metapakiet).

%package plugin-clamav
Summary:	clamav plugin for Sylpheed-Claws
Summary(pl):	Wtyczka clamav dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-clamav
This plugin enables the scanning of message attachments in mail
received from a POP, IMAP, or LOCAL account using Clam AntiVirus. It
can optionally delete the mail or save it to a designated folder.

%package plugin-dillo
Summary:	dillo plugin for Sylpheed-Claws
Summary(pl):	Wtyczka dillo dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	dillo
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-dillo
This plugin enables the viewing of html messages using the Dillo web
browser.

%package plugin-pgpcore
Summary:	PGP/Core plugin for Sylpheed-Claws
Summary(pl):	Wtyczka PGP/Core dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-pgpcore
This plugin handles core PGP functions.

%package plugin-pgpinline
Summary:	PGP/Inline plugin for Sylpheed-Claws
Summary(pl):	Wtyczka PGP/Inline dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	%{name}-plugin-pgpcore = %{version}-%{release}
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-pgpinline
This plugin handles PGP/Inline signed and/or encrypted mails. It can
decrypt mails, verify signatures or sign and encrypt your own mails.

%package plugin-pgpmime
Summary:	PGP/MIME plugin for Sylpheed-Claws
Summary(pl):	Wtyczka PGP/MIME dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	%{name}-plugin-pgpcore = %{version}-%{release}
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-pgpmime
This plugin handles PGP/MIME signed and/or encrypted mails. It can
decrypt mails, verify signatures or sign and encrypt your own mails.

%package plugin-spamassassin
Summary:	spamassassin plugin for Sylpheed-Claws
Summary(pl):	Wtyczka spamassassin dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-spamassassin
This plugin enables the scanning of incoming mail received from a POP,
IMAP, or LOCAL account using SpamAssassin. It can optionally delete
mail identified as spam or save it to a designated folder, and also
can be used to train a local Spamassassin or a remote one.

%package plugin-trayicon
Summary:	trayicon plugin for Sylpheed-Claws
Summary(pl):	Wtyczka trayicon dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Conflicts:	sylpheed-claws-plugins <= 2.3.0-1

%description plugin-trayicon
This plugin places an icon in the system tray that indicates whether
you have any new mail. A tooltip also shows the current new, unread
and total number of messages, and a contextual menu allows the most
common operations.

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
	--%{?with_dillo:en}%{!?with_dillo:dis}able-dillo-viewer-plugin \
	--%{?with_gnomeprint:en}%{!?with_gnomeprint:dis}able-gnomeprint \
	--%{?with_gpg:en}%{!?with_gpg:dis}able-pgpcore-plugin \
	--%{?with_gpg:en}%{!?with_gpg:dis}able-pgpmime-plugin \
	--%{?with_gpg:en}%{!?with_gpg:dis}able-pgpinline-plugin \
	--%{?with_ipv6:en}%{!?with_ipv6:dis}able-ipv6 \
	--%{?with_jpilot:en}%{!?with_jpilot:dis}able-jpilot \
	--%{?with_ldap:en}%{!?with_ldap:dis}able-ldap \
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
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name}/themes,%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.{deps,la}

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
%dir %{_datadir}/%{name}/themes
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_datadir}/%{name}/manual/en
%lang(fr) %{_datadir}/%{name}/manual/fr
%lang(pl) %{_datadir}/%{name}/manual/pl
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files plugins
%defattr(644,root,root,755)

%if %{with clamav}
%files plugin-clamav
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/clamav_plugin.so
%endif

%if %{with dillo}
%files plugin-dillo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/dillo_viewer.so
%endif

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

%if %{with spamassassin}
%files plugin-spamassassin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/spamassassin.so
%endif

%if %{with trayicon}
%files plugin-trayicon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/trayicon.so
%endif
