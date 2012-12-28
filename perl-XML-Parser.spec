%define	modname	XML-Parser
%define	modver	2.41

Summary:	A perl module for parsing XML documents
Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	7
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/XML/%{modname}-%{modver}.tar.gz
Source1:	http://uucode.com/xml/perl/enc.tar.bz2
Patch0:		XML-Parser-2.36-use_filehandle.patch

BuildRequires:	pkgconfig(expat)
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl-devel
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-libwww-perl

%description
A perl module for parsing XML documents.

%prep
%setup -q -n %{modname}-%{modver} -a1
%patch0 -p0 -b .filehandle~

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
make test

%install
%makeinstall_std
install -m644 enc/koi8-r.enc %{buildroot}%{perl_vendorarch}/XML/Parser/Encodings

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/XML/Parser*
%{perl_vendorarch}/auto/XML/Parser*
