#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	ExtUtils
%define		pnam	MakeMaker-CPANfile
Summary:	CPANfile support for ExtUtils::MakeMaker
Name:		perl-ExtUtils-MakeMaker-CPANfile
Version:	0.06
Release:	2
License:	GPL+ or Artistic
Group:		Development/Libraries
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8e1a42d67b57ed15e08e25872dd84cac
URL:		http://search.cpan.org/dist/ExtUtils-MakeMaker-CPANfile/
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:	perl(version) >= 0.76
BuildRequires:	perl-Module-CPANfile
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::More) >= 0.88
%endif
Requires:	perl(ExtUtils::MakeMaker) >= 6.17
Requires:	perl(version) >= 0.76
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::MakeMaker::CPANfile loads cpanfile in your distribution and
modifies parameters for WriteMakefile in your Makefile.PL. Just use it
instead of ExtUtils::MakeMaker (which should be loaded internally),
and prepare cpanfile.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist | xargs rm

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README.md
%dir %{perl_vendorlib}/ExtUtils/MakeMaker
%{perl_vendorlib}/ExtUtils/MakeMaker/CPANfile.pm
%{_mandir}/man3/ExtUtils::MakeMaker::CPANfile.3pm*
