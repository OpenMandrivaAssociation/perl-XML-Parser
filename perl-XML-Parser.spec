%define	modname	XML-Parser
%define	modver	2.44

%ifarch %{aarch64}
# FIXME as of clang 9.0 20190709, building with LTO results in
# Can't find 'boot_XML__Parser__Expat' symbol in /home/bero/temp/abf/perl-XML-Parser/BUILD/XML-Parser-2.44/blib/arch/auto/XML/Parser/Expat/Expat.so
# when running "use XML::Parser;"
%global _disable_lto 1
%endif

Summary:	A perl module for parsing XML documents
Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/XML::Parser
Source0:	http://www.cpan.org/modules/by-module/XML/%{modname}-%{modver}.tar.gz
Source1:	http://uucode.com/xml/perl/enc.tar.bz2
Patch0:		XML-Parser-2.36-use_filehandle.patch
BuildRequires:	perl-devel
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(HTML::Parser)
BuildRequires:	pkgconfig(expat)
# For tests
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)

%description
A perl module for parsing XML documents.

%prep
%setup -qn %{modname}-%{modver} -a1
%patch0 -p0 -b .filehandle~

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
make test || :

%install
%makeinstall_std
install -m644 enc/koi8-r.enc %{buildroot}%{perl_vendorarch}/XML/Parser/Encodings

%files
%doc README Changes
%{perl_vendorarch}/XML/Parser*
%{perl_vendorarch}/auto/XML/Parser*
%{_mandir}/man3/*

