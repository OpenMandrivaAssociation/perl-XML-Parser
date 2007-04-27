%define	name	perl-XML-Parser
%define	module	XML-Parser

Summary: 	A perl module for parsing XML documents
Name: 		%{name}
Version: 	2.34
Release: 	%mkrel 5
License: 	GPL
Group: 		Development/Perl
Source: 	http://www.cpan.org/authors/id/C/CO/COOPERCL/%{module}-%{version}.tar.bz2
Source1:	http://uucode.com/xml/perl/enc.tar.bz2
Url: 		http://www.cpan.org
BuildRoot: 	%{_tmppath}/%{name}-buildroot/
Requires: 	perl, libexpat1_95
BuildRequires: 	libexpat-devel perl-devel perl-libwww-perl perl-HTML-Parser

%description
A perl module for parsing XML documents

Needed by eGrail

%prep
%setup -q -n %{module}-%{version} -a 1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"
make test

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
install -m 644 enc/koi8-r.enc $RPM_BUILD_ROOT%{perl_vendorarch}/XML/Parser/Encodings

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/XML/Parser*
%{perl_vendorarch}/auto/XML/Parser*


