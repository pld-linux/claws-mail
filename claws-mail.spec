#
# Conditional build:
# _without_jconv           - without jconv support
#
Summary:	A bleeding edge branch of Sylpheed, a GTK+ based, lightweight, and fast e-mail client
Summary(pl):	Rozwojowa wersja Sylpheed z du¿± ilo¶ci± zmian oraz ulepszeñ
Name:		sylpheed-claws
Version:	0.8.8
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://telia.dl.sourceforge.net/sourceforge/sylpheed-claws/sylpheed-%{version}claws.tar.bz2
Source1:	http://prdownloads.sourceforge.net/sylpheed-claws/sylpheed-0.8.7claws-iconset.tar.gz
Source2:	%{name}.desktop
Patch0:		%{name}-po.patch
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


%description
This program is an X based fast e-mail client which has features same
as orginal Sylpheed but with new/improved features. Some of new stuff
is really cool and useable.

%description -l pl
Szybki klient poczty o mo¿liwo¶ciach takich jak oryginalny Sylpheed
ale z nowymi/poprawionymi funkcjami. Niektóre dodatki s± naprawdê
¶wietne i u¿yteczne.

%prep
%setup -q -n sylpheed-%{version}claws -a1
%patch0 -p1
mv sylpheed*claws-iconset themes
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
	%{!?_without_jconv:--enable-jconv} \
	--enable-gpgme \
	--enable-ldap \
	--enable-openssl \
	--enable-ipv6 \
	--enable-aspell \
	--enable-gdk-pixbuf \
	--enable-threads

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Mail,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
cp -a themes $RPM_BUILD_ROOT%{_datadir}/sylpheed

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
%{_datadir}/sylpheed/themes
%{_applnkdir}/Network/Mail/%{name}.desktop
%{_pixmapsdir}/sylpheed.png
