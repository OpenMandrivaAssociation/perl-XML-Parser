%define	upstream_name	 XML-Parser
%define	upstream_version 2.41

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A perl module for parsing XML documents
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz
Source1:	http://uucode.com/xml/perl/enc.tar.bz2
Patch0:		XML-Parser-2.36-use_filehandle.patch

BuildRequires:	chrpath
BuildRequires:	libexpat-devel >= 2.0.1
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl-devel >= 2:5.14
BuildRequires:	perl-List-MoreUtils >= 0.320.0-3
BuildRequires:	perl-libwww-perl

%description
A perl module for parsing XML documents.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%setup -q -n %{upstream_name}-%{upstream_version} -T -D -a 1
%patch0 -p0 -b .filehandle

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.410.0-5
+ Revision: 765848
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.410.0-4
+ Revision: 764372
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 2.410.0-3
+ Revision: 763117
- rebuild

* Fri Jan 20 2012 Bernhard Rosenkraenzer <bero@bero.eu> 2.410.0-2
+ Revision: 762875
- Build for perl 5.14.x
- Fix some whitespace inconsistency in spec file

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.410.0-1
+ Revision: 684830
- update to new version 2.41

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.400.0-2
+ Revision: 667453
- mass rebuild

* Fri Nov 12 2010 J茅r么me Quelin <jquelin@mandriva.org> 2.400.0-1mdv2011.0
+ Revision: 596736
- update to

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.360.0-5mdv2011.0
+ Revision: 564596
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.360.0-4mdv2011.0
+ Revision: 555291
- rebuild

  + J茅r么me Quelin <jquelin@mandriva.org>
    - rebuild for 5.12

* Mon Oct 12 2009 J茅r么me Quelin <jquelin@mandriva.org> 2.360.0-2mdv2010.1
+ Revision: 456933
- bump mkrel
- fix upstream bug 1939, which also impacts MDK::Common

* Tue Jul 28 2009 J茅r么me Quelin <jquelin@mandriva.org> 2.360.0-1mdv2010.0
+ Revision: 401474
- rebuild using %%perl_convert_version

* Sun Mar 22 2009 Funda Wang <fwang@mandriva.org> 2.36-5mdv2009.1
+ Revision: 360239
- disable format checking

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.36-4mdv2009.0
+ Revision: 224638
- rebuild

* Mon Jan 14 2008 G枚tz Waschk <waschk@mandriva.org> 2.36-3mdv2008.1
+ Revision: 151346
- rebuild for new perl

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 2.36-2mdv2008.1
+ Revision: 151315
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.36-1mdv2008.1
+ Revision: 110875
- new version

* Mon Nov 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.35-1mdv2008.1
+ Revision: 110246
- new version

* Thu Jun 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.34-6mdv2008.0
+ Revision: 36890
- rebuild for expat
- nuke rpath
- spec file clean

* Fri Apr 27 2007 Pixel <pixel@mandriva.com> 2.34-5mdv2008.0
+ Revision: 18624
- rebuild


* Fri Feb 03 2006 Pixel <pixel@mandriva.com> 2.34-4mdk
- rebuild

* Mon Nov 15 2004 G鰐z Waschk <waschk@linux-mandrake.com> 2.34-3mdk
- rebuild for new perl

* Tue Apr 06 2004 Pixel <pixel@mandrakesoft.com> 2.34-2mdk
- rebuild

* Thu Aug 21 2003 Fran鏾is Pons <fpons@mandrakesoft.com> 2.34-1mdk
- 2.34.

* Thu Aug 14 2003 Per 貀vind Karlsen <peroyvind@linux-mandrake.com> 2.31-8mdk
- rebuild for new perl
- drop Prefix tag
- drop Distribution tag
- don't use PREFIX
- use %%make macro
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.31-7mdk
- rebuild for new auto{prov,req}

