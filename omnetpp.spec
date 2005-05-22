
# TODO
# - add soname

Summary:	OMNeT++ - object-oriented discrete event simulation framework
Summary(pl):	OMNeT++ - zorientowane obiektowo ¶rodowisko do symulacji zdarzeñ dyskretnych
Name:		omnetpp
Version:	3.1
Release:	0.4
License:	academic
Group:		Applications/Engineering
Source0:	http://www.omnetpp.org/download/release/%{name}-%{version}-src.tgz
# Source0-md5:	31e81d5111ca417e8a14b2c43b44b8c5
Patch0:		%{name}-makefile.patch
Patch1:		%{name}.patch
Patch2:		%{name}-makemake.patch
URL:		http://www.omnetpp.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	blt-devel
BuildRequires:	tcl-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OMNeT++ is a feature-rich C++-based object-oriented discrete event
simulation framework, primarily targeted at the simulation of
communication networks and other parallel/distributed systems.

%description -l pl
OMNeT++ to bogate w mo¿liwo¶ci, oparte na C++, zorientowane obiektowo
¶rodowisko do symulacji zdarzeñ dyskretnych, g³ównie przeznaczone do
symulacji sieci komunikacyjnych i innych systemów
równoleg³ych/rozproszonych.

%package libs
Summary:	OMNeT++ libraries
Summary(pl):	Biblioteki dostarczane przez OMNeT++
Group:		Libraries
Provides:	libcmdenv.so
Provides:	libenvir.so
Provides:	libnedxml.so
Provides:	libsim_std.so
Provides:	libtkenv.so

%description libs
OMNeT++ libraries

%description libs -l pl
Biblioteki OMNeT++.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.* src/utils
%{__autoconf}
%configure

dir=`pwd`
PATH=$dir/bin:$PATH
export PATH
LD_LIBRARY_PATH=$dir/lib
export LD_LIBRARY_PATH

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/omnetpp/{,platdep},%{_datadir}/omnetpp/bitmaps}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp bin/* $RPM_BUILD_ROOT%{_bindir}
cp -d lib/* $RPM_BUILD_ROOT%{_libdir}
cp include/*.h $RPM_BUILD_ROOT%{_includedir}/omnetpp
cp include/platdep/*.h $RPM_BUILD_ROOT%{_includedir}/omnetpp/platdep
cp -r bitmaps $RPM_BUILD_ROOT%{_datadir}/omnetpp

cp -a samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/api doc/manual doc/nedxml-api doc/parsim-api doc/tictoc-tutorial doc/*.txt doc/README
%doc doc/License doc/*.pdf
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_datadir}/omnetpp
%{_examplesdir}/%{name}-%{version}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.so.*.*
