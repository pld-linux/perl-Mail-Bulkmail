%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	Bulkmail
Summary:	%{pdir}::%{pnam} perl module
Summary(pl):	Modu³ perla %{pdir}::%{pnam}
Name:		perl-%{pdir}-%{pnam}
Version:	3.09
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{pdir}::%{pnam} is a platform independent mailing list module.

%description -l pl
%{pdir}::%{pnam} to prosty, niezale¿ny od platformy modu³ do list
mailowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes *.txt sample.*
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%dir %{perl_sitelib}/%{pdir}/%{pnam}
%{perl_sitelib}/%{pdir}/%{pnam}/*.pm
%{_mandir}/man3/*
