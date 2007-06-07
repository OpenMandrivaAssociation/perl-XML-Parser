%define	name	perl-XML-Parser
%define	module	XML-Parser

Summary:	A perl module for parsing XML documents
Name:		%{name}
Version:	2.34
Release:	%mkrel 6
License:	GPL
Group:		Development/Perl
Source:		http://www.cpan.org/authors/id/C/CO/COOPERCL/%{module}-%{version}.tar.bz2
Source1:	http://uucode.com/xml/perl/enc.tar.bz2
Url: 		http://www.cpan.org
Requires:	perl
BuildRequires:	libexpat-devel >= 2.0.1
BuildRequires:	perl-devel
BuildRequires:	perl-libwww-perl
BuildRequires:	perl-HTML-Parser
BuildRequires:	chrpath
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A perl module for parsing XML documents.

%prep
%setup -q -n %{module}-%{version} -a 1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"
make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std
install -m 644 enc/koi8-r.enc %{buildroot}%{perl_vendorarch}/XML/Parser/Encodings
chrpath -d %{buildroot}%{perl_vendorarch}/auto/XML/Parser/Expat/Expat.so

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/XML/Parser*
%{perl_vendorarch}/auto/XML/Parser*
