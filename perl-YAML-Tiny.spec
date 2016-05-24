#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-YAML-Tiny
Version  : 1.69
Release  : 16
URL      : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/YAML-Tiny-1.69.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/YAML-Tiny-1.69.tar.gz
Summary  : 'Read/Write YAML files with as little code as possible'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-YAML-Tiny-doc

%description
This archive contains the distribution YAML-Tiny,
version 1.69:
Read/Write YAML files with as little code as possible

%package doc
Summary: doc components for the perl-YAML-Tiny package.
Group: Documentation

%description doc
doc components for the perl-YAML-Tiny package.


%prep
%setup -q -n YAML-Tiny-1.69

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/site_perl/5.24.0/YAML/Tiny.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
