%define name	syncekonnector
%define version 0.3.2
%define release	%mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	MIT
Summary: 	KDE IO connector to access to Windows modile
Group: 		Graphical desktop/KDE
URL:    	http://synce.sourceforge.net/synce/kde
Source: 	http://ovh.dl.sourceforge.net/sourceforge/synce/%name-%version.tar.bz2
Patch0:     synce-konnector-cpp.patch

BuildRequires:	libsynce-devel
BuildRequires:	kdebase-devel qt3-devel
BuildRequires:  kdepim-devel
BuildRequires:  librra-devel
BuildRequires:  synce-kde-devel
Requires: 	synce >= 0.9.0

%description
SynCE-KDE is part of the SynCE project:
  http://synce.sourceforge.net/

KDE IO connector to access to Windows modile.

%prep
%setup -q
%patch0 -p0 -b .cpp-fix

%build
%configure2_5x 

%make

%install
rm -fr %buildroot
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%_libdir/*
%_datadir/doc/HTML/en/syncekonnector/common
%_datadir/doc/HTML/en/syncekonnector/index.cache.bz2
%_datadir/doc/HTML/en/syncekonnector/index.docbook
%dir %_datadir/services/kresources/konnector
%_datadir/services/kresources/konnector/syncedevicekonnector.desktop
%_datadir/services/kresources/konnector/syncelocalkonnector.desktop
%_datadir/services/rakikabcsync.desktop
%_datadir/services/rakikcalsync.desktop
%_datadir/services/rakiktasksync.desktop




