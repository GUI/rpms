# $Id$
# Authority: dries
# Upstream: Ask Bj&#248;rn Hansen <ask$perl,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-DBI

Summary: Persistent database connections and basic authentication support
Name: perl-Apache-DBI
Version: 0.9901
Release: 2.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-DBI/

Source: http://search.cpan.org/CPAN/authors/id/P/PG/PGOLLUCCI/Apache-DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module is supposed to be used with the Apache server together with
an embedded perl interpreter like mod_perl. It provides support for basic
authentication and authorization as well as support for persistent database
connections via Perl's Database Independent Interface (DBI).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Apache/DBI.pm
%{perl_vendorlib}/Apache/AuthDBI.pm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9901-2.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.9901-2
- Fixed the source url.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.9901-1
- Updated to release 0.9901.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.94-1
- Initial package.
