%define upstream_name    Tie-IxHash
%define upstream_version 1.22

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    6

Summary: 	%{upstream_name} module for perl
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  perl-devel

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.220.0-4mdv2012.0
+ Revision: 765766
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.220.0-3
+ Revision: 764291
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.220.0-2
+ Revision: 667399
- mass rebuild

* Sun Feb 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.220.0-1mdv2011.0
+ Revision: 512603
- update to 1.22

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.210.0-1mdv2010.0
+ Revision: 405744
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.21-10mdv2009.0
+ Revision: 224401
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.21-9mdv2008.1
+ Revision: 180618
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Oct 11 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-10 09:36:19 (63278)
- bzip sources
- use the check macro

* Sat Oct 07 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-06 07:10:44 (62906)
- Import perl-Tie-IxHash

* Fri Sep 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.21-7mdk
- rebuild

