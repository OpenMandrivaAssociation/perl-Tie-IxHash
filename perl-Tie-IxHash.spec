%define upstream_name    Tie-IxHash
%define upstream_version 1.22

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary: 	%{upstream_name} module for perl
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
%{upstream_name} module for perl.  This Perl module implements ordered
in-memory associative arrays.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
