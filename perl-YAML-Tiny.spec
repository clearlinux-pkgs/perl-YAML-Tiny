#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-YAML-Tiny
Version  : 1.73
Release  : 26
URL      : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/YAML-Tiny-1.73.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/YAML-Tiny-1.73.tar.gz
Summary  : 'Read/Write YAML files with as little code as possible'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-YAML-Tiny-license
Requires: perl-YAML-Tiny-man

%description
This archive contains the distribution YAML-Tiny,
version 1.73:
Read/Write YAML files with as little code as possible

%package license
Summary: license components for the perl-YAML-Tiny package.
Group: Default

%description license
license components for the perl-YAML-Tiny package.


%package man
Summary: man components for the perl-YAML-Tiny package.
Group: Default

%description man
man components for the perl-YAML-Tiny package.


%prep
%setup -q -n YAML-Tiny-1.73

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-YAML-Tiny
cp LICENSE %{buildroot}/usr/share/doc/perl-YAML-Tiny/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/YAML/Tiny.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-YAML-Tiny/LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/YAML::Tiny.3
