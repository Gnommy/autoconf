Summary:     GNU autoconf - source configuration tools
Summary(pl): GNU autokonf - narz�dzie do automatycznego konfigurowania �r�de�
Name:        autoconf
Version:     2.12
Release:     6
Copyright:   GPL
Group:       Development/Building
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:      autoconf-2.12-race.patch
Requires:    gawk, m4, mktemp
BuildArchitectures: noarch
BuildRoot:   /tmp/%{name}-%{version}-root
Prereq:      /sbin/install-info

%description
GNU's "autoconf" is a tool for source and Makefile configuration. It
assists the programmer in creating portable and configurable packages, by
allowing the person building the package to specify various configuration
options. 

"autoconf" is not required for the end user - it is needed only to
generate the configuration scripts. 

%description -l pl
GNU autoconf jest narz�dziem wykorzystywanym do automatycznego
konfigurowania kod�w �r�d�owych pakiet�w program�w oraz do generowania na
podstawie automatycznie roz[oznanego �rodowiska plik�w Makefile i innch
zale�nych od zawarto�ci systemu w kt�rym ma przebiega� proces kompilacji.
d102 1
przenie�� na r�ne platformy. Umo�liwia wyb�r wielu opcji podczas procesu
przygotowania do kompilacji.

GNU autoconf nie jest generalnie potrzebny dla u�ytkownika ko�cowego, a
tylko podczas generowania samych skrypt�w autokonfiguracyjnych.
 
%prep
%setup -q
%patch0 -p1

%build
./configure --prefix=/usr
make datadir=/usr/lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/info

make prefix=$RPM_BUILD_ROOT/usr datadir=$RPM_BUILD_ROOT/usr/lib install
gzip -9nf $RPM_BUILD_ROOT/usr/info/autoconf.info*

# We don't want to include the standards.info stuff in the package,
# because it comes from binutils...
rm -f $RPM_BUILD_ROOT/usr/info/standards*
cp install-sh $RPM_BUILD_ROOT/usr/lib/autoconf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/autoconf.info.gz /usr/info/dir

%preun
/sbin/install-info --del /usr/info/autoconf.info.gz /usr/info/dir

%files
%defattr(644, root, root, 755)
/usr/info/autoconf.info*
%attr(755, root, root) /usr/bin/*
/usr/lib/autoconf

%changelog
* Mon Sep 21 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.12-5]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- modified pl translation,
- added full %attr description in %files.

* Thu Aug 27 1998 Cristian Gafton <gafton@redhat.com>
- patch for fixing /tmp race conditions

* Fri Jun 12 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [2.12-5]
- added pl transaltion,
- added %defattr support.

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- spec file cleanups
- made a noarch package
- uses autoconf
- uses install-info

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built with glibc- built with glibc
