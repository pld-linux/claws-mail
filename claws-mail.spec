# Conditional build:
# _without_jconv           - without jconv support

Summary:	A bleeding edge branch of Sylpheed, a GTK+ based, lightweight, and fast e-mail client
Summary(pl):	Rozwojowa wersja Sylpheed z du¿± ilo¶ci± zmian oraz ulepszeñ
Name:		sylpheed-claws
Version:	0.8.3
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://telia.dl.sourceforge.net/sourceforge/sylpheed-claws/sylpheed-%{version}claws.tar.gz
Source1:	http://prdownloads.sourceforge.net/sylpheed-claws/sylpheed-theme-pak2.tar.bz2 
Source2:	%{name}.desktop
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	faces-devel
BuildRequires:	gdk-pixbuf-devel >= 0.8
BuildRequires:	gettext-devel
BuildRequires:	gpgme-devel
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	imlib-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	aspell-devel >= 0.50
%{!?_without_jconv:BuildRequires:   libjconv-devel}
Requires:	faces
Obsoletes:	sylpheed
URL:		http://sylpheed-claws.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This program is an X based fast e-mail client which has features same
as orginal Sylpheed but with new/improved features. Some of new stuff
is really cool and useable.

%description -l pl
Szybki klient poczty o mo¿liwo¶ciach takich jak oryginalny Sylpheed
ale z nowymi/poprawionymi funkcjami. Niektóre dodatki s± naprawdê
¶wietne i u¿yteczne.

%prep
%setup -q -n sylpheed-%{version}claws
mkdir themes
cd themes
tar -jxf %{SOURCE1}
mv -f README ../README.themes
cd ..

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I ac
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?_without_jconv:--enable-jconv} \
	--enable-gpgme \
	--enable-ldap \
	--enable-ssl \
	--enable-ipv6 \
	--enable-aspell \
	--enable-gdk-pixbuf \
	--enable-threads

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
cp -a themes $RPM_BUILD_ROOT%{_datadir}/sylpheed

%find_lang sylpheed

%clean
rm -rf $RPM_BUILD_ROOT

%files -f sylpheed.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%{_mandir}/man1/sylpheed.1.gz
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
%{_datadir}/sylpheed/themes
%{_applnkdir}/Network/Mail/%{name}.desktop
%{_pixmapsdir}/sylpheed.png
