# Conditional build:
# _with_jconv           - adds much more codesets to choice from

Summary:	A bleeding edge branch of Sylpheed, a GTK+ based, lightweight, and fast e-mail client
Summary(pl):	Osobno rozwijana wersja Sylpheed z paroma zmianami/ulepszeniami
Name:		sylpheed-claws
Version:	0.7.8
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://telia.dl.sourceforge.net/sourceforge/sylpheed-claws/sylpheed-%{version}claws.tar.bz2
Source1:	http://prdownloads.sourceforge.net/sylpheed-claws/sylpheed-theme-pak2.tar.bz2 
Source2:	%{name}.desktop
Source3:	sylpheed.png
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib-devel
BuildRequires:	faces-devel
BuildRequires:	gettext-devel
BuildRequires:	gdk-pixbuf-devel >= 0.8
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	gtkhtml-devel >= 0.10.1
BuildRequires:	libtool
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	gpgme-devel
BuildRequires:	pspell-devel >= 12.2-5
%{?_with_jconv:BuildRequires:   libjconv-devel}
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
gettextize --copy --force
aclocal -I ac
%{__autoconf}
autoheader
automake --add-missing --foreign --copy
%configure \
	%{!?_with_jconv:--disable-jconv} \
	--enable-pspell \
	--enable-impib \
	--enable-gdk-pixbuf \
	--enable-threads \
	--enable-ssl \
 	--enable-ipv6 \
	--enable-ldap \
	--enable-gpgme

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Mail,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a themes $RPM_BUILD_ROOT%{_datadir}/sylpheed

gzip -9nf AUTHORS ChangeLog NEWS README* TODO

%find_lang sylpheed

%clean
#rm -rf $RPM_BUILD_ROOT

%files -f sylpheed.lang
%defattr(644,root,root,755)
%doc *.gz
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
%{_applnkdir}/Network/Mail/*
%{_pixmapsdir}/sylpheed.png
