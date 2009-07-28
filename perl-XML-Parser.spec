%define	upstream_name	 XML-Parser
%define	upstream_version 2.36

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	A perl module for parsing XML documents
License:	GPL
Group:		Development/Perl
URL:            http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz
Source1:	http://uucode.com/xml/perl/enc.tar.bz2

BuildRequires:	chrpath
BuildRequires:	libexpat-devel >= 2.0.1
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl-devel
BuildRequires:	perl-libwww-perl
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
A perl module for parsing XML documents.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%setup -q -n %{upstream_name}-%{upstream_version} -T -D -a 1

%build
%define Werror_cflags %{nil}
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
chmod +w   %{buildroot}%{perl_vendorarch}/auto/XML/Parser/Expat/Expat.so
chrpath -d %{buildroot}%{perl_vendorarch}/auto/XML/Parser/Expat/Expat.so

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/XML/Parser*
%{perl_vendorarch}/auto/XML/Parser*
