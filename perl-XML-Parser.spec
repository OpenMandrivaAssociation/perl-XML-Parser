%define	module	XML-Parser
%define	name	perl-%{module}
%define	version 2.36

Name:		%{name}
Version:	%{version}
Release:	%mkrel 2
Summary:	A perl module for parsing XML documents
License:	GPL
Group:		Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.gz
Source1:	http://uucode.com/xml/perl/enc.tar.bz2
BuildRequires:	libexpat-devel >= 2.0.1
BuildRequires:	perl-devel
BuildRequires:	perl-libwww-perl
BuildRequires:	perl-HTML-Parser
BuildRequires:	chrpath
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
A perl module for parsing XML documents.

%prep
%setup -q -n %{module}-%{version}
%setup -q -n %{module}-%{version} -T -D -a 1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
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
