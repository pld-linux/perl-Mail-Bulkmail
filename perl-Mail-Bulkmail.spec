#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Mail
%define		pnam	Bulkmail
Summary:	Mail::Bulkmail - platform independent mailing list module
Summary(pl.UTF-8):	Mail::Bulkmail - niezależny od platformy moduł do list mailowych
Name:		perl-Mail-Bulkmail
Version:	3.12
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8c1275e9655bbe2ba177f9b33e2b694e
URL:		http://search.cpan.org/dist/Mail-Bulkmail/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail::Bulkmail gives a fairly complete set of tools for managing
mass-mailing lists. I initially wrote it because the tools I was using
at the time were just too damn slow for mailing out to thousands of
recipients. I keep working on it because it's reasonably popular and I
enjoy it.

In a nutshell, it allows you to rapidly transmit a message to a
mailing list by zipping out the information to them via an SMTP relay
(your own, of course). Subclasses provide the ability to use mail
merges, dynamic messages, and anything else you can think of.

%description -l pl.UTF-8
Mail::Bulkmail dostarcza w miarę kompletny zestaw narzędzi do
zarządzania listami wysyłki masowej. Zostały początkowo napisane
ponieważ narzędzia używane przez autora były zbyt wolne przy
rozsyłaniu do tysięcy adresatów. Pracuje nad tym modułem nadal,
ponieważ stał się dosyć popularny.

W skrócie ten pakiet pozwala szybko wysłać wiadomość na listę
wysyłkową poprzez wysłanie informacji do adresatów poprzez przekaźnik
SMTP (oczywiście własny). Podklasy pozwalają na używanie listów
łączonych, wiadomości dynamicznych i innych rzeczy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes *.txt sample.*
%{perl_vendorlib}/Mail/Bulkmail.pm
%dir %{perl_vendorlib}/Mail/Bulkmail
%{perl_vendorlib}/Mail/Bulkmail/*.pm
%{_mandir}/man3/*
