#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	Bulkmail
Summary:	%{pdir}::%{pnam} Perl module
Summary(pl):	Modu³ Perla %{pdir}::%{pnam}
Name:		perl-%{pdir}-%{pnam}
Version:	3.12
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8c1275e9655bbe2ba177f9b33e2b694e
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes *.txt sample.*
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%dir %{perl_vendorlib}/%{pdir}/%{pnam}
%{perl_vendorlib}/%{pdir}/%{pnam}/*.pm
%{_mandir}/man3/*
