Summary:	OMNeT++ - object-oriented discrete event simulation framework
Name:		omnetpp
Version:	3.1
Release:	0.2
License:	academic
Group:		Applications/Engineering
Source0:	http://www.omnetpp.org/download/release/%{name}-%{version}-src.tgz
# Source0-md5:	31e81d5111ca417e8a14b2c43b44b8c5
Patch0:		%{name}-makefile.patch
Patch1:		%{name}.patch
URL:		http://www.omnetpp.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	blt-devel
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OMNeT++ is a feature-rich C++-based object-oriented discrete event
simulation framework, primarily targeted at the simulation of
communication networks and other parallel/distributed systems.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub src/utils
cp -f /usr/share/automake/config.guess src/utils

%{__autoconf}
%configure

dir=`pwd`
PATH=$PATH:$dir/bin
export PATH
LD_LIBRARY_PATH=$dir/lib
export LD_LIBRARY_PATH

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_libdir},%{_includedir}/omnetpp/{,platdep},%{_datadir}/omnetpp/bitmaps}
install -d $RPM_BUILD_ROOT/%{_examplesdir}/%{name}-%{version}

cp bin/* $RPM_BUILD_ROOT/%{_bindir}
cp -d lib/* $RPM_BUILD_ROOT/%{_libdir}
cp include/*.h $RPM_BUILD_ROOT/%{_includedir}/omnetpp
cp include/platdep/*.h $RPM_BUILD_ROOT/%{_includedir}/omnetpp/platdep
cp -r bitmaps $RPM_BUILD_ROOT/%{_datadir}/omnetpp/

cp -a samples/* $RPM_BUILD_ROOT/%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/api doc/manual doc/nedxml-api doc/parsim-api doc/tictoc-tutorial doc/*.txt doc/README
%doc doc/License doc/*.pdf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*
%{_datadir}/omnetpp
%{_examplesdir}/%{name}-%{version}
