# $Id$
# Authority: dag
# Upstream: Andy Lester <andy$petdance,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Timer

Summary: Rudimentary profiling for Template Toolkit
Name: perl-Template-Timer
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Timer/

Source: http://www.cpan.org/modules/by-module/Template/Template-Timer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Rudimentary profiling for Template Toolkit.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Template::Timer.3pm*
%dir %{perl_vendorlib}/Template/
#%{perl_vendorlib}/Template/Timer/
%{perl_vendorlib}/Template/Timer.pm

%changelog
* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 1.00-1
- Updated to version 1.00.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
