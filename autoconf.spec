#
# Conditional build:
# _without_emacs - without emacs autoconf-mode

%include	/usr/lib/rpm/macros.perl
Summary:	GNU autoconf - source configuration tools
Summary(de):	Ein GNU-Hilfsmittel f�r Quellencode automatisch konfigurieren
Summary(es):	Una herramienta de GNU para autom�ticamente configurar c�digo de fuente
Summary(fr):	Un outil de GNU pour configurer automatiquement le code source
Summary(it):	Uno strumento di GNU per automaticamente la configurazione del codice sorgente
Summary(pl):	GNU autoconf - narz�dzie do automatycznego konfigurowania �r�de�
Summary(pt_BR):	GNU autoconf - ferramentas de configura��o de fontes
Summary(ru):	GNU autoconf - ���������������� �������� �������
Summary(uk):	GNU autoconf - �������Ʀ������� ��Ȧ���� ����Ԧ�
Name:		autoconf
Version:	2.57
Release:	3
License:	GPL
Group:		Development/Building
# stable releases:
Source0:	ftp://ftp.gnu.org/gnu/autoconf/%{name}-%{version}.tar.bz2
# devel releases:
#Source0:	ftp://alpha.gnu.org/pub/gnu/autoconf/%{name}-%{version}.tar.bz2
Patch0:		%{name}-mawk.patch
Patch1:		%{name}-version.patch
Patch2:		%{name}-info.patch
Patch3:		%{name}-AC_EGREP.patch
URL:		http://www.gnu.org/software/autoconf/
Requires:	diffutils
Requires:	/bin/awk
Requires:	m4
Requires:	mktemp
Conflicts:	gettext < 0.10.38-3
BuildRequires:	m4
BuildRequires:	rpm-perlprov
BuildRequires:	texinfo >= 4.2
%{!?_without_emacs:BuildRequires:	emacs}
BuildConflicts:	m4 = 1.4o
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	autoconf252
Obsoletes:	autoconf253

%define		_libdir		%{_datadir}

%description
GNU's Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to specify
various configuration options.

You should install Autoconf if you are developing software and you'd
like to use it to create shell scripts which will configure your
source code packages. If you are installing Autoconf, you will also
need to install the GNU m4 package.

Note that the Autoconf package is not required for the end user who
may be configuring software with an Autoconf-generated script;
Autoconf is only required for the generation of the scripts, not their
use.

%description -l de
GNU's Autoconf ist eines Hilfsmittels f�r das Konfigurieren des
Quellencodes und der Makefiles. Mit Autoconf k�nnen Programmierer die
beweglichen und konfigurierbaren Pakete erstellen, da der Person, die
das Paket aufbaut, erlaubt wird, verschiedene Konfiguration Optionen
zu spezifizieren.

Sie sollten Autoconf installieren, wenn Sie Software entwickeln und
Sie sie benutzen m�chten, um Shellindexe zu erstellen, die Ihre
Quellencodepakete konfigurieren. Wenn Sie Autoconf installieren,
m�ssen Sie auch das Paket GNU m4 installieren.

Beachten Sie, da� das Paket Autoconf nicht f�r den Endbenutzer
angefordert wird, der Software mit einem Autoconf-festgelegten Index
konfigurieren kann; Autoconf wird nur f�r das Erzeugung der Indexe,
nicht ihr Gebrauch angefordert.

%description -l es
GN�s Autoconf es una herramienta para configurar c�digo y makefiles de
fuente. Usando Autoconf, los programadores pueden crear los conjuntos
portables y configurables, puesto que se permite a la persona que
construye el conjunto especificar varias opciones de la configuraci�n.

Usted debe instalar Autoconf si usted est� desarrollando software
l�gica y usted quisiera utilizarlo para crear los shell scriptes que
configurar�n sus conjuntos del c�digo de fuente. Si usted est�
instalando Autoconf, usted tambi�n necesitar� instalar el conjunto de
GNU m4.

Observe que el conjunto de Autoconf no est� requerido para el
utilizador del extremo que puede configurar software l�gica con una
escritura Autoconf-generada; Autoconf se requiere solamente para la
generaci�n de las escrituras, no su uso.

%description -l fr
GNU's Autoconf est un outil pour configurer le code source et les
fichiers makefile. En utilisant Autoconf, les programmeurs peuvent
cr�er les modules portatifs et configurables, puisqu'on permet � la la
personne �tablissant le module d'indiquer de diverses options de
configuration.

Vous devriez installer Autoconf si vous d�veloppez le logiciel et vous
voudriez l'employer pour cr�er les s�quences type d'interpr�teur de
commandes interactif qui configureront vos modules de code source. Si
vous installez Autoconf, vous devrez �galement installer le module de
GNU m4.

Notez que le module d'Autoconf n'est pas exig� pour l'utilisateur qui
peut configurer le logiciel avec une s�quence type Autoconf-produite;
Autoconf est seulement exig� pour la g�n�ration des s�quences type,
non leur utilisation.

%description -l it
GNU's Autoconf � uno strumento per la configurazione il codice e dei
makefiles sorgente. Usando Autoconf, i programmatori possono creare i
pacchetti portatili e configurabili, poich� alla persona che sviluppa
il pacchetto � permessa specificare le varie opzioni di
configurazione.

Dovreste installare Autoconf se state sviluppando il software e
voleste usarli per creare gli scritti di coperture che configureranno
i vostri pacchetti di codice sorgente. Se state installando Autoconf,
egualmente dovrete installare il pacchetto di GNU m4.

Si noti che il pacchetto di Autoconf non � richiesto per l'
utilizzatore finale che pu� configurare il software con uno scritto
Autoconf-generato; Autoconf � richiesto soltanto per la generazione
degli scritti, il non loro uso.

%description -l pl
GNU autoconf jest narz�dziem wykorzystywanym do automatycznego
konfigurowania kod�w �r�d�owych pakiet�w program�w oraz do generowania
na podstawie automatycznie rozpoznanego �rodowiska plik�w Makefile i
innych zale�nych od zawarto�ci systemu, w kt�rym ma przebiega� proces
kompilacji. Pomaga programi�cie w konfigurowaniu i tworzeniu
oprogramowania daj�cego si� przenie�� na r�ne platformy. Umo�liwia
wyb�r wielu opcji podczas procesu przygotowania do kompilacji.

GNU autoconf nie jest generalnie potrzebny ko�cowemu u�ytkownikowi, a
tylko podczas generowania samych skrypt�w autokonfiguracyjnych.

%description -l pt_BR
GNU "autoconf" � uma ferramenta para configura��o de fontes e
Makefiles. Ele ajuda o programador na cria��o de pacotes port�veis e
configur�veis, permitindo que a pessoa que programa o pacote
especifique v�rias op��es de configura��o. Autoconf � necess�rio
somente para gerar scripts de configura��o.

%description -l ru
GNU autoconf - ���������� ��� ���������������� �������� ������� �
��������� Makefile'��. �������� ������������ ��������� ����������� �
��������������� ������, �������� ����, ��� ��� ������ ��������,
�������� ��������� ����� ������������.

"autoconf" �� �������� ����������� ��� ��������� ������������, ���
���������� ������ ��� ��������� ���������������� ��������.

%description -l uk
GNU autoconf - �� ���������� ��� ����������ϧ ���Ʀ����æ� ��Ȧ����
����Ԧ� �� ������æ� Makefile'��. ��������� ������ͦ��� ����������
��¦��Φ ������, �� ���������� ���Ʀ����æ�. �� ������Ѥ ����, ���
���������� ������� ����� ����Ԧ�, �������� Ҧ�Φ ��æ� ���Ʀ����æ�.

"autoconf" �� � ����Ȧ���� ��� ˦������� �����������, ����
�������������� Ԧ���� ��� ������æ� ���Ʀ����æ���� �����Ԧ�.

%package -n emacs-autoconf-mode-pkg
Summary:	emacs autoconf-mode
Summary(pl):	Tryb autoconf dla emacsa
Group:		Applications/Editors/Emacs
Requires:	emacs

%description -n emacs-autoconf-mode-pkg
Emacs autoconf-mode.

%description -n emacs-autoconf-mode-pkg -l pl
Tryb edycji autoconf dla emacsa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*

%{_infodir}/*.info*
%{_mandir}/man1/*

%{_libdir}/autoconf

%if%{!?_without_emacs:1}%{?_without_emacs:0}
%files -n emacs-autoconf-mode-pkg
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/*.elc
%endif
