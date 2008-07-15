%define with_lancelot 0
%{?_with_lancelot: %{expand: %%global with_lancelot 1}}

Name: kdeplasma-addons
Summary: kdeplasma is a compilation of plasma items ( runners, applets, plasmoids ) for kde4
Version: 4.0.98
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
Release: %mkrel 2
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeplasma-addons-%version.tar.bz2
%if %{with_lancelot}
Patch0:    kdeplasma-addons-4.0.98-enable-lancelot.patch
%endif # with_lancelot
Buildroot: %_tmppath/%name-%version-%release-root
BuildRequires: qt4-devel
BuildRequires: kde4-macros
BuildRequires: X11-devel
BuildRequires: kdebase4-devel >= 4.0.83
BuildRequires: kdepimlibs4-devel >= 4.0.83
BuildRequires: kdebase4-workspace-devel >= 4.0.83
BuildRequires: libzip-devel
BuildRequires: qimageblitz-devel 
BuildRequires: boost-devel
BuildRequires: lm_sensors-devel
BuildRequires: qimageblitz-devel
%if %{with_lancelot}
BuildRequires: kdenetwork4-devel
%endif # with_lancelot
Provides: kdeplasma
Provides: kdeplasma4 = %version
Obsoletes: kdeplasma4 < 4.0.83
Obsoletes: kdeplayground4-plasma
Obsoletes: kdeplayground4-plasma-devel
Obsoletes: extragear-plasma < 4.0.82
Obsoletes: kdeplasmoids4 <= 4.0.98
Requires: plasma-applet-filewatcher
Requires: plasma-applet-notes
Requires: plasma-applet-bluemarble
Requires: plasma-applet-showdesktop
Requires: plasma-applet-comic
Requires: plasma-applet-konqprofiles
Requires: plasma-applet-konsoleprofiles
Requires: plasma-applet-luna
Requires: plasma-applet-twitter
Requires: plasma-applet-nowplaying
Requires: plasma-applet-binaryclock
Requires: plasma-applet-dict
Requires: plasma-applet-fuzzy-clock
Requires: plasma-applet-frame
Requires: plasma-applet-showdashboard
Requires: plasma-applet-calculator
Requires: plasma-applet-fifteenpuzzle
Requires: plasma-applet-kolourpicker
Requires: plasma-dataengine-comic
Requires: plasma-dataengine-twitter
Requires: plasma-desktoptheme-default
Requires: plasma-desktoptheme-heron
Requires: plasma-desktoptheme-aya
Requires: plasma-desktoptheme-slim-glow
Requires: plasma-desktoptheme-silicon
Requires: plasma-desktoptheme-elegance
Requires: plasma-runner-converter
Requires: plasma-runner-contacts

%description
kdeplasma is a compilation of plasma items ( runners, applets, plasmoids ) for kde4.

%files
%doc COPYING

#-----------------------------------------------------------------------------

%package -n plasma-applet-filewatcher
Summary: Monitor applet for files
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-filewatcher
Monitor applet for files.

%files -n plasma-applet-filewatcher
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_fileWatcher.so
%_kde_datadir/kde4/services/plasma-fileWatcher-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-notes
Summary: Plasma notes applets
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-notes
Plasma notes applets.

%files -n plasma-applet-notes
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_notes.so
%_kde_datadir/kde4/services/plasma-notes-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-bluemarble
Summary: OpenGL world planet applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-bluemarble
OpenGL world planet applet.

%files -n plasma-applet-bluemarble
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_bluemarble.so
%_kde_datadir/kde4/services/plasma-applet-bluemarble.desktop
%_kde_appsdir/plasma-bluemarble

#-----------------------------------------------------------------------------

%package -n plasma-applet-showdesktop
Summary: Show desktop contents
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-showdesktop
Show desktop contents.

%files -n plasma-applet-showdesktop
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_showdesktop.so
%_kde_datadir/kde4/services/plasma-applet-showdesktop.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-comic
Summary: Make your day happy with daily desktop comics applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Requires: plasma-dataengine-comic
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-comic
Make your day happy with daily desktop comics applet

%files -n plasma-applet-comic
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_comic.so
%_kde_datadir/kde4/services/plasma-dataengine-comic.desktop
%_kde_appsdir/plasma-comic
%_kde_services/xkcdprovider.desktop
%_kde_services/userfriendlyprovider.desktop
%_kde_services/snoopyprovider.desktop
%_kde_services/dilbertprovider.desktop
%_kde_services/garfieldprovider.desktop
%_kde_services/osnewsprovider.desktop
%_kde_services/phdprovider.desktop
%_kde_servicetypes/plasma_comicprovider.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-konqprofiles
Summary: Live konqueror profile viewer
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-konqprofiles
Live konqueror profile viewer.

%files -n plasma-applet-konqprofiles
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_konqprofiles.so
%_kde_datadir/kde4/services/plasma-applet-konqprofiles.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-konsoleprofiles
Summary: Live konsole profile viewer
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-konsoleprofiles
Live konsole profile viewer.

%files -n plasma-applet-konsoleprofiles
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_konsoleprofiles.so
%_kde_datadir/kde4/services/plasma-applet-konsoleprofiles.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-luna
Summary: Lunar calendar
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-luna
Lunar calendar applet.

%files -n plasma-applet-luna
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_luna.so
%_kde_datadir/kde4/services/plasma-applet-luna.desktop

#-----------------------------------------------------------------------------
%if %{with_lancelot}
%package -n plasma-applet-lancelot
Summary: Plasma lancelot applets
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-lancelot
Plasma lancelot applets.

%files -n plasma-applet-lancelot
%defattr(-,root,root)
%_kde_bindir/lancelot
%_kde_bindir/lancelot-test
%_kde_libdir/kde4/plasma_applet_lancelot_launcher.so
%_kde_datadir/kde4/services/plasma-applet-lancelot-launcher.desktop
%_kde_datadir/dbus-1/services/org.kde.lancelot.service
%_kde_iconsdir/hicolor/*/apps/lancelot.png

#-----------------------------------------------------------------------------

%define lancelot_major 0
%define liblancelot %mklibname lancelot %lancelot_major

%package -n %liblancelot
Summary: %name library
Group: System/Libraries

%description -n %liblancelot
%name library.

%post -n %liblancelot -p /sbin/ldconfig
%postun -n %liblancelot -p /sbin/ldconfig

%files -n %liblancelot
%defattr(-,root,root,-)
%_kde_libdir/liblancelot.so.%{lancelot_major}*
%endif #with_lancelot

#-----------------------------------------------------------------------------

%package -n plasma-applet-twitter
Summary: Twitter blog applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Requires: plasma-dataengine-twitter
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-twitter
Twiter blog applet

%files -n plasma-applet-twitter
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_twitter.so
%_kde_datadir/kde4/services/plasma-twitter-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-nowplaying
Summary: SWoong notifier applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-nowplaying
Song notifier applet

%files -n plasma-applet-nowplaying
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_nowplaying.so
%_kde_datadir/kde4/services/plasma-applet-nowplaying.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-binaryclock
Summary: Simplified way to see the hours
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-binaryclock
Simplified way to see the hours.

%files -n plasma-applet-binaryclock
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_binaryclock.so
%_kde_datadir/kde4/services/plasma-applet-binaryclock.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-dict
Summary: Dict applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-dict
A dict applets.

%files -n plasma-applet-dict
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_dict.so
%_kde_datadir/kde4/services/plasma-dict-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-fuzzy-clock
Summary: A lazy way to see the hours
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-fuzzy-clock
A lazy way to see the hours.

%files -n plasma-applet-fuzzy-clock
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_fuzzy_clock.so
%_kde_datadir/kde4/services/plasma-clock-fuzzy.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-frame
Summary: A basic pictures frame to desktop
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-frame
A basic pictures frame to desktop.

%files -n plasma-applet-frame
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_frame.so
%_kde_datadir/kde4/services/plasma-frame-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-showdashboard
Summary: Plasma showdashboard applets
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-showdashboard
Plasma showdashboard applets.

%files -n plasma-applet-showdashboard
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_showdashboard.so
%_kde_datadir/kde4/services/plasma-applet-showdashboard.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-calculator
Summary: Plasma calculator applets
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-calculator
Plasma calculator applets.

%files -n plasma-applet-calculator
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_calculator.so
%_kde_datadir/kde4/services/plasma-applet-calculator.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-fifteenpuzzle
Summary: Plasma fifteenpuzzle applets
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-fifteenpuzzle
Plasma fifteenpuzzle applets.

%files -n plasma-applet-fifteenpuzzle
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_fifteenPuzzle.so
%_kde_datadir/kde4/services/plasma-applet-fifteenPuzzle.desktop
%_kde_iconsdir/*/*/*/fifteenpuzzle.*

#-----------------------------------------------------------------------------

%package -n plasma-applet-kolourpicker
Summary: Basic color picker
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-kolourpicker
Basic color picker.

%files -n plasma-applet-kolourpicker
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_kolourpicker.so
%_kde_datadir/kde4/services/plasma-kolourpicker-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-comic
Summary: Plasma comic dataengines
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-dataengine
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-dataengine-comic
Plasma comic dataengines.

%files -n plasma-dataengine-comic
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_comic*
%_kde_libdir/kde4/plasma_engine_comic.*
%_kde_datadir/kde4/services/plasma-comic-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-twitter
Summary: Plasma twitter dataengines
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-dataengine
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-dataengine-twitter
Plasma twitter dataengines.

%files -n plasma-dataengine-twitter
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_engine_twitter.so
%_kde_datadir/kde4/services/plasma-dataengine-twitter.desktop

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-default
Summary: Plasma default desktopthemes
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-desktoptheme-default
Plasma default desktopthemes.

%files -n plasma-desktoptheme-default
%defattr(-,root,root)
%_kde_appsdir/desktoptheme/default

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-heron
Summary: Plasma heron desktopthemes
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-desktoptheme
Requires: plasma-desktoptheme-default
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-desktoptheme-heron
Plasma heron desktopthemes.

%files -n plasma-desktoptheme-heron
%defattr(-,root,root)
%_kde_appsdir/desktoptheme/heron

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-aya
Summary: Plasma aya desktopthemes
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-desktoptheme
Requires: plasma-desktoptheme-default
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-desktoptheme-aya
Plasma aya desktopthemes.

%files -n plasma-desktoptheme-aya
%defattr(-,root,root)
%_kde_appsdir/desktoptheme/Aya

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-slim-glow
Summary: Plasma slim-glow desktopthemes
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-desktoptheme
Requires: plasma-desktoptheme-default
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-desktoptheme-slim-glow
Plasma slim-glow desktopthemes.

%files -n plasma-desktoptheme-slim-glow
%defattr(-,root,root)
%_kde_appsdir/desktoptheme/slim-glow

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-silicon
Summary: Plasma silicon desktopthemes
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-desktoptheme
Requires: plasma-desktoptheme-default
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-desktoptheme-silicon
Plasma silicon desktopthemes.

%files -n plasma-desktoptheme-silicon
%defattr(-,root,root)
%_kde_appsdir/desktoptheme/Silicon

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-elegance
Summary: Plasma elegance desktopthemes
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-desktoptheme
Requires: plasma-desktoptheme-default
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-desktoptheme-elegance
Plasma elegance desktopthemes.

%files -n plasma-desktoptheme-elegance
%defattr(-,root,root)
%_kde_appsdir/desktoptheme/Elegance

#-----------------------------------------------------------------------------

%package -n plasma-runner-converter
Summary: Plasma converter runners
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-runner-converter
Plasma converter runners.

%files -n plasma-runner-converter
%defattr(-,root,root)
%_kde_datadir/kde4/services/plasma-runner-converter.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-contacts
Summary: Plasma contacts runners
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-runner-contacts
Plasma contacts runners.

%files -n plasma-runner-contacts
%defattr(-,root,root)
%_kde_libdir/kde4/krunner_contacts.so
%_kde_libdir/kde4/krunner_converterrunner.so
%_kde_datadir/kde4/services/plasma-runner-contacts.desktop

#-----------------------------------------------------------------------------

%define plasmacomicprovidercore_major 1
%define libplasmacomicprovidercore %mklibname plasmacomicprovidercore %plasmacomicprovidercore_major

%package -n %libplasmacomicprovidercore
Summary: %name library
Group: System/Libraries

%description -n %libplasmacomicprovidercore
%name library.

%post -n %libplasmacomicprovidercore -p /sbin/ldconfig
%postun -n %libplasmacomicprovidercore -p /sbin/ldconfig

%files -n %libplasmacomicprovidercore
%defattr(-,root,root,-)
%_kde_libdir/libplasmacomicprovidercore.so.%{plasmacomicprovidercore_major}*

#-----------------------------------------------------------------------------

%define plasmaappletdialog_major 4
%define libplasmaappletdialog %mklibname plasmaappletdialog %plasmaappletdialog_major

%package -n %libplasmaappletdialog
Summary: %name library
Group: System/Libraries

%description -n %libplasmaappletdialog
%name library.

%post -n %libplasmaappletdialog -p /sbin/ldconfig
%postun -n %libplasmaappletdialog -p /sbin/ldconfig

%files -n %libplasmaappletdialog
%defattr(-,root,root,-)
%_kde_libdir/libplasmaappletdialog.so.%{plasmaappletdialog_major}*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: %libplasmaappletdialog
Requires: %libplasmacomicprovidercore
Requires: kdelibs4-devel
Obsoletes: extragear-plasma-devel

%description  devel
This package contains header files needed if you wish to build applications
based on %name

%files devel
%defattr(-,root,root)
%{_kde_includedir}/*
%{_kde_libdir}/*.so

#-----------------------------------------------------------------------------

%prep
%setup -q
%if %{with_lancelot}
%patch0 -p0
%endif

%build
%cmake_kde4 
%make

%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

