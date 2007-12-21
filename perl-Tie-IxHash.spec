%define module  Tie-IxHash
%define	pdir	Tie

Summary: 	%{module} module for perl
Name: 		perl-%{module}
Version: 	1.21
Release: 	%mkrel 8
License: 	GPL or Artistic
Group: 		Development/Perl
URL:            http://search.cpan.org/search?dist=%{module}
Source0: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{module}-%{version}.tar.bz2
Requires: 	perl
BuildRequires:	perl-devel
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-buildroot

%description
%{module} module for perl.  This Perl module implements ordered
in-memory associative arrays.

%prep

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tie/IxHash.pm
%{_mandir}/*/*


