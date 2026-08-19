%define	modname	XML-Parser

%ifarch %{aarch64}
# FIXME as of clang 9.0 20190709, building with LTO results in
# Can't find 'boot_XML__Parser__Expat' symbol in /home/bero/temp/abf/perl-XML-Parser/BUILD/XML-Parser-2.44/blib/arch/auto/XML/Parser/Expat/Expat.so
# when running "use XML::Parser;"
#global _disable_lto 1
%endif

Summary:	A perl module for parsing XML documents
Name:		perl-%{modname}
Version:	2.59
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/XML::Parser
Source0:	https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{modname}-%{version}.tar.gz
Source1:	http://uucode.com/xml/perl/enc.tar.bz2
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(HTML::Parser)
BuildRequires:	pkgconfig(expat)
# For tests
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-File-ShareDir-Install

%description
A perl module for parsing XML documents.

%prep
%autosetup -n %{modname}-%{version} -a1 -p1

%build
%if %{cross_compiling}
# Host perl + ExtUtils::MakeMaker. Devel::CheckLib uses Config{cc} and
# cannot compile target headers; MakeMaker then injects host libpth
# (-L/usr/lib64, a linker script on x86_64).
export CC="%{__cc}"
export EXPATLIBPATH=%{_prefix}/%{_target_platform}%{_libdir}
export EXPATINCPATH=%{_prefix}/%{_target_platform}%{_includedir}
sed -i 's/check_lib(/1 || check_lib(/' Makefile.PL
perl Makefile.PL INSTALLDIRS=vendor \
	EXPATLIBPATH="$EXPATLIBPATH" \
	EXPATINCPATH="$EXPATINCPATH" \
	INC="-I$EXPATINCPATH" \
	LIBS="-L$EXPATLIBPATH -lexpat" \
	LDDLFLAGS="-shared -L$EXPATLIBPATH"
[ -f Makefile ] || exit 1
find . -name Makefile | xargs -r sed -i \
	-e "s|-L/usr/lib64|-L$EXPATLIBPATH|g" \
	-e "s|-L/usr/local/lib||g"
%else
perl Makefile.PL INSTALLDIRS=vendor
%endif
%make_build CC="%{__cc}" LD="%{__cc}" OPTIMIZE="%{optflags}"

%check
make test || :

%install
%make_install
install -m644 enc/koi8-r.enc %{buildroot}%{perl_vendorarch}/XML/Parser/Encodings

%files
%doc Changes
%{perl_vendorarch}/XML/Parser*
%{perl_vendorarch}/auto/XML/Parser*
%{perl_vendorarch}/auto/share/dist/XML-Parser/
%{_mandir}/man3/*

