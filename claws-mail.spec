# Conditional build:
# _with_jconv		- adds much more codesets to choice from

Summary:	A bleeding edge branch of Sylpheed, a GTK+ based, lightweight, and fast e-mail client
Summary(pl):	Osobno rozwijana wersja Sylpheed z paroma zmianami/ulepszeniami.
Name:		sylpheed-claws
Version:	0.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(cs):	X11/Aplikace/S�ov�
Group(da):	X11/Programmer/Netv�rks
Group(de):	X11/Applikationen/Netzwerkwesen
Group(es):	X11/Aplicaciones/Red
Group(fr):	X11/Applications/R�seau
Group(it):	X11/Applicazioni/Rete
Group(no):	X11/Applikasjoner/Nettverks
Group(pl):	X11/Aplikacje/Sieciowe
Group(pt_BR):	X11/Aplica��es/Rede
Group(pt):	X11/Aplica��es/Rede
Group(ru):	X11/����������/�������
Group(sv):	X11/Till�mpningar/N�tverk
Source0:	http://prdownloads.sourceforge.net/sylpheed-claws/sylpheed-%{version}claws.tar.gz
Source1:	%{name}.desktop
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib-devel
BuildRequires:	faces-devel
BuildRequires:	gettext-devel
BuildRequires:	gdk-pixbuf-devel >= 0.8
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	gtkhtml-devel >= 0.10.1
%{?_with_jconv:BuildRequires:	libjconv-devel}
BuildRequires:	libtool
BuildRequires:	openssl-devel
Requires:	faces
Conflicts:	sylpheed
URL:		http://sylpheed-claws.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This program is an X based fast e-mail client which has features 
same as orginal Sylpheed but with new/improved features.
%description -l pl
Szybki klient poczty o mo�liwo�ciach takich jak
oryginalny Sylpheed ale z nowymi/poprawionymi funkcjami.

%prep
%setup -q -n sylpheed-0.7.1claws

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force 
aclocal -I ac
autoconf
autoheader
automake --add-missing --foreign --copy
%configure \
	%{!?_with_jconv:--disable-jconv} \
	--enable-impib \
	--enable-gdk-pixbuf \
	--enable-threads \
	--enable-ssl \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang sylpheed

%clean
rm -rf $RPM_BUILD_ROOT

%files -f sylpheed.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/sylpheed
%dir %{_datadir}/sylpheed/manual
%{_datadir}/sylpheed/manual/en
%lang(ja) %{_datadir}/sylpheed/manual/ja
%{_applnkdir}/Network/Mail/*
