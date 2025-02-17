%define modname	Tie-IxHash
%define modver 1.23

Summary:	%{modname} module for perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	10
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Tie/Tie-IxHash-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
%{modname} module for perl.  This Perl module implements ordered
in-memory associative arrays.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Tie/IxHash.pm
%{_mandir}/man3/*


