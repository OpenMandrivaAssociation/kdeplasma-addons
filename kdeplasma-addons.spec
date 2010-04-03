%define branch 0
%{?_branch: %{expand: %%global branch 1}}


%if %branch
%define kde_snapshot svn1053190
%endif

Name: kdeplasma-addons
Summary: kdeplasma is a compilation of plasma items ( runners, applets, plasmoids ) for kde4
Version: 4.4.2
Release: %mkrel 2
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
%if %branch
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/kdeplasma-addons-%{version}%kde_snapshot.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/kdeplasma-addons-%{version}.tar.bz2
%endif
Patch1: kdeplasma-addons-4.2.71-lancelot-fix-NewDocument.patch
Patch2: kdeplasma-addons-4.2.71-lancelot-fix-computertab.patch
Patch3: kdeplasma-addons-4.3.73-fix-lancelot-major.patch 
Buildroot: %_tmppath/%name-%version-%release-root
BuildRequires: qt4-devel
BuildRequires: kde4-macros
BuildRequires: X11-devel
BuildRequires: kdebase4-devel >= 1:4.2.98
BuildRequires: kdepimlibs4-devel >= 4.2.98
BuildRequires: kdebase4-workspace-devel >= 2:4.2.98
BuildRequires: qimageblitz-devel 
BuildRequires: boost-devel
BuildRequires: lm_sensors-devel
BuildRequires: qimageblitz-devel
BuildRequires: python-devel
BuildRequires: kdegraphics4-devel
BuildRequires: eigen2
BuildRequires: kdeedu4-devel >= 4.3.73
BuildRequires: qt4-qtdbus
BuildRequires: qalculate-devel
BuildRequires: scim-devel

Provides:  kdeplasma
Provides:  kdeplasma4 = %version
Obsoletes: kdeplasma4 < 4.0.83
Obsoletes: kdeplayground4-plasma
Obsoletes: kdeplayground4-plasma-devel
Obsoletes: extragear-plasma < 4.0.82
Obsoletes: kdeplasmoids4 <= 4.0.98

Suggests: plasma-desktoptheme-default

Suggests: plasma-applet-filewatcher                                                                                           
Suggests: plasma-applet-notes
Suggests: plasma-applet-showdesktop
Suggests: plasma-applet-comic
Suggests: plasma-applet-konqprofiles
Suggests: plasma-applet-rssnow
Suggests: plasma-applet-previewer
Suggests: plasma-applet-bball
Suggests: plasma-applet-incomingmsg
Suggests: plasma-applet-leavenote
Suggests: plasma-applet-life
Suggests: plasma-applet-pastebin
Suggests: plasma-applet-konsoleprofiles
Suggests: plasma-applet-luna
Suggests: plasma-applet-lancelot
Suggests: plasma-applet-microblog
Suggests: plasma-applet-nowplaying
Suggests: plasma-applet-binaryclock
Suggests: plasma-applet-dict
Suggests: plasma-applet-fuzzy-clock
Suggests: plasma-applet-frame
Suggests: plasma-applet-showdashboard
Suggests: plasma-applet-calculator
Suggests: plasma-applet-fifteenpuzzle
Suggests: plasma-applet-kolourpicker
Suggests: plasma-applet-unitconverter
Suggests: plasma-applet-systemloadviewer
Suggests: plasma-applet-weather
Suggests: plasma-applet-bubblemon
Suggests: plasma-applet-weatherstation
Suggests: plasma-applet-news
Suggests: plasma-applet-charselect
Suggests: plasma-applet-eyes
Suggests: plasma-applet-paste
Suggests: plasma-applet-timer
Suggests: plasma-applet-opendesktop
Suggests: plasma-applet-magnifique
Suggests: plasma-applet-mediaplayer
Suggests: plasma-applet-rtm
Suggests: plasma-applet-knowledgebase
Suggests: plasma-applet-blackboard
Suggests: plasma-applet-plasmaboard
Suggests: plasma-applet-qalculate
Suggests: plasma-applet-webslice
Suggests: plasma-applet-spellcheck
Suggests: plasma-applet-kimpanel
Suggests: plasma-runner-converter
Suggests: plasma-runner-contacts
Suggests: plasma-runner-konquerorsessions
Suggests: plasma-runner-katesessions
Suggests: plasma-runner-konsolesessions
Suggests: plasma-runner-browserhistory
Suggests: plasma-runner-spellchecker
Suggests: plasma-runner-audioplayercontrol
Suggests: plasma-runner-mediawiki
Suggests: plasma-runner-kopete

Suggests: plasma-wallpaper-pattern
Suggests: plasma-wallpaper-weather
Suggests: plasma-wallpaper-virus
Suggests: plasma-wallpaper-mandelbrot
Suggests: plasma-wallpaper-marble

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
%_kde_services/plasma-fileWatcher-default.desktop

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
%_kde_services/plasma-notes-default.desktop

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
%_kde_services/plasma-applet-showdesktop.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-comic
Summary: Make your day happy with daily desktop comics applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Requires: plasma-dataengine-comic = %version
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-comic
Make your day happy with daily desktop comics applet

%files -n plasma-applet-comic
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_comic.so
%_kde_services/plasma-dataengine-comic.desktop
%_kde_configdir/comic.knsrc
%_kde_services/plasma-packagestructure-comic.desktop
%_kde_libdir/kde4/plasma_packagestructure_comic.so
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
%_kde_services/plasma-applet-konqprofiles.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-rssnow
Summary: Plasma RSS Applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-rssnow
Plasma RSS Applet

%files -n plasma-applet-rssnow
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_rssnow.so
%_kde_appsdir/desktoptheme/default/rssnow
%_kde_services/plasma-applet-rssnow.desktop
%_kde_appsdir/rssnow

#-----------------------------------------------------------------------------

%package -n plasma-applet-previewer
Summary: Previewer Plasma Applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-previewer
Previewer Plasma Applet

%files -n plasma-applet-previewer
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_previewer.so
%_kde_iconsdir/hicolor/*/apps/previewer.png
%_kde_services/ServiceMenus/preview.desktop
%_kde_services/plasma-applet-previewer.desktop


#-----------------------------------------------------------------------------

%package -n plasma-applet-bball
Summary: bball Plasma Applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-bball
bball Plasma Applet

%files -n plasma-applet-bball
%defattr(-,root,root)
%_kde_iconsdir/*/*/*/bball*
%_kde_services/plasma-applet-bball.desktop
%_kde_appsdir/bball
%_kde_libdir/kde4/plasma_applet_bball.so

#-----------------------------------------------------------------------------

%package -n plasma-applet-incomingmsg
Summary: incomingmsg Plasma Applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-incomingmsg
incomingmsg Plasma Applet

%files -n plasma-applet-incomingmsg
%defattr(-,root,root)
%_kde_services/plasma-applet-incomingmsg.desktop
%_kde_libdir/kde4/plasma_applet_incomingmsg.so

#-----------------------------------------------------------------------------

%package -n plasma-applet-leavenote
Summary: leavenote Plasma Applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-leavenote
leavenote Plasma Applet

%files -n plasma-applet-leavenote
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_leavenote.so
%_kde_services/plasma-applet-leavenote.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-life
Summary: life Plasma Applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-life
life Plasma Applet

%files -n plasma-applet-life
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_life.so
%_kde_services/plasma-applet-life.desktop

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-pastebin
Summary:  Engine of the pastebin plasma applet
Group:    Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-dataengine
Requires: plasma-dataengine-pastebin = %version-%release

%description -n plasma-dataengine-pastebin
Engine of the pastebin plasma applet

%files -n plasma-dataengine-pastebin
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_engine_pastebin.so
%_kde_services/plasma-engine-pastebin.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-pastebin
Summary: Pastebin plasma Applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Requires: plasma-dataengine-pastebin
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-pastebin
plasma-applet-pastebin

%files -n plasma-applet-pastebin
%defattr(-,root,root)
%_kde_services/plasma-applet-pastebin.desktop
%_kde_libdir/kde4/plasma_applet_pastebin.so
%_kde_appsdir/plasma/services/pastebin.operations
%_kde_appsdir/plasma_pastebin


#-----------------------------------------------------------------------------

%package -n plasma-applet-knowledgebase
Summary: Widget that can query the knowledgebase of opendesktop.org
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-knowledgebase
Widget that can query the knowledgebase of opendesktop.org

%files -n plasma-applet-knowledgebase
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_knowledgebase.so
%_kde_services/plasma-applet-knowledgebase.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-blackboard
Summary: A blackboard plasma applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-blackboard
A blackboard plasma applet

%files -n plasma-applet-blackboard
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_blackboard.so
%_kde_services/plasma-applet-blackboard.desktop


#-----------------------------------------------------------------------------

%package -n plasma-applet-plasmaboard
Summary: A plasmaboard plasma applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-plasmaboard
A plasmaboard plasma applet

%files -n plasma-applet-plasmaboard
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_plasmaboard.so
%_kde_services/plasma_applet_plasmaboard.desktop

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
%_kde_services/plasma-applet-konsoleprofiles.desktop

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
%_kde_services/plasma-applet-luna.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-lancelot
Summary: Plasma lancelot applets
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82
Conflicts: plasma-desktoptheme-elegance < 4.1.85-2
Conflicts: plasma-desktoptheme-slim-glow < 4.1.85-2
Conflicts: plasma-desktoptheme-silicon < 4.1.85-2
Conflicts: plasma-desktoptheme-aya < 4.1.85-2
Conflicts: plasma-desktoptheme-heron < 4.1.85-2

%description -n plasma-applet-lancelot
Plasma lancelot applets.

%files -n plasma-applet-lancelot
%defattr(-,root,root)
%_kde_bindir/lancelot
%_kde_libdir/kde4/plasma_applet_lancelot_part.so
%_kde_libdir/kde4/plasma_applet_lancelot_launcher.so
%_kde_services/plasma-applet-lancelot-launcher.desktop
%_kde_datadir/dbus-1/services/org.kde.lancelot.service
%_kde_iconsdir/hicolor/*/apps/lancelot*.png
%_kde_services/plasma-applet-lancelot-part.desktop
%_kde_datadir/mime/packages/lancelotpart-mime.xml
%_kde_appsdir/desktoptheme/default/lancelot
%_kde_appsdir/desktoptheme/oxygen/lancelot
%_kde_appsdir/desktoptheme/Elegance
%_kde_appsdir/desktoptheme/Silicon
%_kde_appsdir/desktoptheme/slim-glow
%_kde_appsdir/desktoptheme/Aya
%_kde_appsdir/desktoptheme/heron
%_kde_appsdir/lancelot

#-----------------------------------------------------------------------------

%define lancelot_major 1
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
%_kde_appsdir/desktoptheme/default/widgets                                    
                                                                              
#-----------------------------------------------------------------------------

%package -n plasma-applet-microblog
Summary: Microblog applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Requires: plasma-dataengine-microblog = %version
Conflicts: extragear-plasma < 4.0.82
Provides: plasma-applet-twitter = %version-%release
Obsoletes: plasma-applet-twitter < 4.2.70

%description -n plasma-applet-microblog
Microblog applet

%files -n plasma-applet-microblog
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_microblog.so
%_kde_services/plasma-applet-microblog.desktop
%_kde_appsdir/plasma/services/tweet.operations

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
%_kde_services/plasma-applet-nowplaying.desktop

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
%_kde_services/plasma-applet-binaryclock.desktop

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
%_kde_services/plasma-dict-default.desktop
%_kde_iconsdir/hicolor/scalable/apps/accessories-dict*

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
%_kde_services/plasma-clock-fuzzy.desktop

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
%_kde_services/plasma-frame-default.desktop
%_kde_appsdir/plasma-applet-frame

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
%_kde_services/plasma-applet-showdashboard.desktop

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
%_kde_services/plasma-applet-calculator.desktop

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
%_kde_services/plasma-applet-fifteenPuzzle.desktop
%_kde_appsdir/desktoptheme/default/fifteenPuzzle
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
%_kde_services/plasma-kolourpicker-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-unitconverter
Summary: Unit Converter
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet

%description -n plasma-applet-unitconverter
Unit Converter.

%files -n plasma-applet-unitconverter
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_unitconverter.so
%_kde_services/plasma-applet-unitconverter.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-systemloadviewer
Summary: System Load Viewer
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet

%description -n plasma-applet-systemloadviewer
System Load Viewer.

%files -n plasma-applet-systemloadviewer
%defattr(-,root,root)
%_kde_libdir/kde4/plasma-applet_systemloadviewer.so
%_kde_services/plasma-applet-systemloadviewer.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-weather
Summary: Weather Forecast
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet

%description -n plasma-applet-weather
Weather Forecast.

%files -n plasma-applet-weather
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_weather.so
%_kde_services/plasma-applet-weather.desktop
%_kde_appsdir/desktoptheme/default/weather/wind-arrows.svgz

#-----------------------------------------------------------------------------

%package -n plasma-applet-bubblemon
Summary: Monitor your system
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet

%description -n plasma-applet-bubblemon
A pretty bubble that monitors your system.

%files -n plasma-applet-bubblemon
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_bubblemon.so
%_kde_services/plasma-applet-bubblemon.desktop
%_kde_appsdir/desktoptheme/default/bubblemon/bubble.svg

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
%_kde_services/plasma-comic-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-microblog
Summary: Plasma micrbolog dataengines
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-dataengine
Provides: plasma-dataengine-twitter = %name-%version
Obsoletes: plasma-dataengine-twitter < 4.2.70

%description -n plasma-dataengine-microblog
Plasma microblog dataengines.

%files -n plasma-dataengine-microblog
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_engine_microblog.so
%_kde_services/plasma-dataengine-microblog.desktop

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-rtm
Summary: An engine to work with Remember the Milk
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-dataengine
Provides: plasma-dataengine-rememberthemilk = %{version}-%{release}
Requires: plasma-dataengine-rtm = %version-%release

%description -n plasma-dataengine-rtm
An engine to work with Remember the Milk.

%files -n plasma-dataengine-rtm
%defattr(-,root,root)
%{_kde_libdir}/kde4/plasma_engine_rtm.so
%{_kde_services}/plasma-engine-rtm.desktop
%{_kde_appsdir}/plasma/services/rtmauth.operations
%{_kde_appsdir}/plasma/services/rtmtask.operations
%{_kde_appsdir}/plasma/services/rtmtasks.operations

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-ocs
Summary: Open Collaboration Services
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-dataengine
Requires: plasma-dataengine-ocs = %version-%release

%description -n plasma-dataengine-ocs
Open Collaboration Services.

%files -n plasma-dataengine-ocs
%defattr(-,root,root)
%{_kde_libdir}/kde4/plasma_engine_ocs.so
%{_kde_services}/plasma-dataengine-ocs.desktop

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-potd
Summary: Picture of the Day
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-dataengine
Requires: plasma-dataengine-potd = %version-%release

%description -n plasma-dataengine-potd
Data Engine for getting various online Pictures of The Day.

%files -n plasma-dataengine-potd
%defattr(-,root,root)
%{_kde_libdir}/kde4/plasma_potd_apodprovider.so
%{_kde_libdir}/kde4/plasma_potd_epodprovider.so
%{_kde_libdir}/kde4/plasma_potd_flickrprovider.so
%{_kde_libdir}/kde4/plasma_potd_oseiprovider.so
%{_kde_libdir}/kde4/plasma_potd_wcpotdprovider.so
%{_kde_libdir}/kde4/plasma_engine_potd.so
%{_kde_services}/plasma-dataengine-potd.desktop
%{_kde_services}/apodprovider.desktop
%{_kde_services}/epodprovider.desktop
%{_kde_services}/flickrprovider.desktop
%{_kde_services}/oseiprovider.desktop
%{_kde_services}/wcpotdprovider.desktop
%{_kde_servicetypes}/plasma_potdprovider.desktop

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
%_kde_services/plasma-runner-converter.desktop
%_kde_libdir/kde4/krunner_converter.so

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
%_kde_services/plasma-runner-contacts.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-weatherstation
Summary: Plasma applet weatherstation
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-weatherstation
Plasma applet weatherstation

%files -n plasma-applet-weatherstation
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_weatherstation.so
%_kde_appsdir/desktoptheme/default/weatherstation
%_kde_services/plasma-applet-weatherstation.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-news
Summary: Plasma applet news
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner
Conflicts: extragear-plasma < 4.0.82
Conflicts: plasma-applet-twitter < 4.3.0

%description -n plasma-applet-news
Plasma applet news

%files -n plasma-applet-news
%defattr(-,root,root)
%_kde_services/plasma-applet-news.desktop
%_kde_libdir/kde4/plasma_applet_news.so
%_kde_appsdir/desktoptheme/default/stylesheets/news.css

#-----------------------------------------------------------------------------

%package -n plasma-applet-charselect
Summary: Plasma applet charselect
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-charselect
Plasma applet charselect

%files -n plasma-applet-charselect
%defattr(-,root,root)
%_kde_services/plasma-applet-charselect.desktop
%_kde_libdir/kde4/plasma_applet_charselect.so

#-----------------------------------------------------------------------------

%package -n plasma-applet-eyes
Summary: Plasma applet paste
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-eyes
Plasma applet eyes

%files -n plasma-applet-eyes
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_eyes.so                                                                                       
%_kde_services/plasma-applet-eyes.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-paste
Summary: Plasma applet paste
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-paste
Plasma applet paste

%files -n plasma-applet-paste
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_paste.so                                                                                      
%_kde_services/plasma-applet-paste.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-timer
Summary: Plasma applet timer
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-timer
Plasma applet timer

%files -n plasma-applet-timer
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_timer.so
%_kde_services/plasma-applet-timer.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-opendesktop
Summary: Communicate using the Social Desktop
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet

%description -n plasma-applet-opendesktop
Communicate using the Social Desktop.

%files -n plasma-applet-opendesktop
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_opendesktop.so
%_kde_services/plasma-applet-opendesktop.desktop
%_kde_libdir/kde4/plasma_applet_opendesktop_activities.so
%_kde_appsdir/plasma-applet-opendesktop-activities/plasma-applet-opendesktop-activities.notifyrc
%_kde_appsdir/plasma/services/ocsPerson.operations
%_kde_datadir/kde4/services/plasma-applet-opendesktop-activities.desktop
%_kde_appsdir/plasma-applet-opendesktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-magnifique
Summary: A magnification glass for Plasma canvas
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet

%description -n plasma-applet-magnifique
A magnification glass for Plasma canvas.

%files -n plasma-applet-magnifique
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_magnifique.so
%_kde_services/plasma-applet-magnifique.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-qalculate
Summary: A Qalculate plasma applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet

%description -n plasma-applet-qalculate
A Qalculate plasma applet

%files -n plasma-applet-qalculate
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_qalculate.so
%_kde_datadir/kde4/services/plasma-applet-qalculate.desktop
%_kde_iconsdir/oxygen/*/apps/qalculate-applet.png

#-----------------------------------------------------------------------------

%package -n plasma-applet-mediaplayer
Summary: Widget that can play video and sound
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet

%description -n plasma-applet-mediaplayer
Widget that can play video and sound.

%files -n plasma-applet-mediaplayer
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_mediaplayer.so
%_kde_services/plasma-applet-mediaplayer.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-spellcheck
Summary:  Fast spell checking applet
Group:    Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet

%description -n plasma-applet-spellcheck
Fast spell checking applet

%files -n plasma-applet-spellcheck
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_spellcheck.so
%_kde_services/plasma-applet-spellcheck.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-webslice
Summary:  Applet that show a part of a webpage
Group:    Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet

%description -n plasma-applet-webslice
Applet that show a part of a webpage

%files -n plasma-applet-webslice
%defattr(-,root,root)
%_kde_services/plasma-applet-webslice.desktop
%_kde_libdir/kde4/plasma_applet_webslice.so

#-----------------------------------------------------------------------------

%package -n plasma-applet-rtm
Summary: Remember The Milk Todo list applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Provides: plasma-applet-rememberthemilk = %{version}-%{release}
Requires: plasma-dataengine-rtm = %{version}

%description -n plasma-applet-rtm
Remember The Milk Todo list applet.

%files -n plasma-applet-rtm
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_rtm.so
%_kde_services/plasma-applet-rememberthemilk.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-kimpanel
Summary: KDE Input method panel (applet) 
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet

%description -n plasma-applet-kimpanel
KDE Input method panel (applet)

%files -n plasma-applet-kimpanel
%defattr(-,root,root)
%_kde_bindir/kimpanel
%_kde_libdir/kde4/plasma_applet_kimpanel.so
%_kde_libdir/libkimpanelruntime.so.0
%_kde_libdir/scim-1.0/scim-panel-dbus
%_kde_datadir/config.kcfg/kimpanelconfig.kcfg
%_kde_datadir/dbus-1/interfaces/org.kde.impanel.xml
%_kde_services/plasma-applet-kimpanel.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-konquerorsessions
Summary: Plasma applet places
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-runner-konquerorsessions
Plasma runner konquerorsessions

%files -n plasma-runner-konquerorsessions
%defattr(-,root,root)
%_kde_services/konquerorsessions.desktop
%_kde_libdir/kde4/krunner_konquerorsessions.so

#-----------------------------------------------------------------------------

%package -n plasma-runner-katesessions
Summary: Plasma katesessions runner
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-runner-katesessions
Plasma runner katesessions

%files -n plasma-runner-katesessions
%defattr(-,root,root)
%_kde_services/katesessions.desktop
%_kde_libdir/kde4/krunner_katesessions.so


#-----------------------------------------------------------------------------

%package -n plasma-runner-konsolesessions
Summary: Plasma runner konsolesessions
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-runner-konsolesessions
Plasma runner konsolesessions

%files -n plasma-runner-konsolesessions
%defattr(-,root,root)
%_kde_services/konsolesessions.desktop
%_kde_libdir/kde4/krunner_konsolesessions.so

#-----------------------------------------------------------------------------

%package -n plasma-runner-browserhistory
Summary: Plasma runner browserhistory
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-runner-browserhistory
Plasma runner konsolesessions

%files -n plasma-runner-browserhistory
%defattr(-,root,root)
%_kde_libdir/kde4/krunner_browserhistory.so
%_kde_services/browserhistory.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-spellchecker
Summary: Plasma runner spellchecker
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-runner-spellchecker
Plasma runner konsolesessions

%files -n plasma-runner-spellchecker
%defattr(-,root,root)
%_kde_services/plasma-runner-spellchecker.desktop
%_kde_services/plasma-runner-spellchecker_config.desktop
%_kde_libdir/kde4/krunner_spellcheckrunner.so
%_kde_libdir/kde4/kcm_krunner_spellcheck.so

#-----------------------------------------------------------------------------

%package -n plasma-runner-audioplayercontrol
Summary: Plasma runner audioplayercontrol
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner

%description -n plasma-runner-audioplayercontrol
Plasma runner audioplayercontrol

%files -n plasma-runner-audioplayercontrol
%defattr(-,root,root)
%_kde_libdir/kde4/kcm_krunner_audioplayercontrol.so
%_kde_libdir/kde4/krunner_audioplayercontrol.so
%_kde_datadir/kde4/services/plasma-runner-audioplayercontrol.desktop
%_kde_datadir/kde4/services/plasma-runner-audioplayercontrol_config.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-kopete
Summary: Plasma runner kopete
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner

%description -n plasma-runner-kopete
Plasma runner kopete

%files -n plasma-runner-kopete
%defattr(-,root,root)
%_kde_libdir/kde4/krunner_kopete.so
%_kde_datadir/kde4/services/plasma-runner-kopete.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-mediawiki
Summary: Plasma runner mediawiki
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner

%description -n plasma-runner-mediawiki
Plasma runner mediawiki

%files -n plasma-runner-mediawiki
%defattr(-,root,root)
%_kde_libdir/kde4/krunner_mediawiki.so
%_kde_datadir/kde4/services/plasma-runner-techbase.desktop
%_kde_datadir/kde4/services/plasma-runner-wikipedia.desktop
%_kde_datadir/kde4/services/plasma-runner-wikitravel.desktop

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-pattern
Summary: Pattern wallpaper
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-wallpaper

%description -n plasma-wallpaper-pattern
Pattern wallpaper.

%files -n plasma-wallpaper-pattern
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_wallpaper_pattern.so
%_kde_services/plasma-wallpaper-pattern.desktop
%_kde_appsdir/plasma_wallpaper_pattern

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-weather
Summary: Weather wallpaper
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-wallpaper

%description -n plasma-wallpaper-weather
Weather wallpaper.

%files -n plasma-wallpaper-weather
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_wallpaper_weather.so
%_kde_services/plasma-wallpaper-weather.desktop
%_kde_datadir/config/plasmaweather.knsrc

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-virus
Summary: Virus wallpaper
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-wallpaper

%description -n plasma-wallpaper-virus
Virus wallpaper.

%files -n plasma-wallpaper-virus
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_wallpaper_virus.so
%_kde_services/plasma-wallpaper-virus.desktop
%_kde_configdir/virus_wallpaper.knsrc

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-marble
Summary: Marble wallpaper
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Requires: marble-common
Provides: plasma-wallpaper

%description -n plasma-wallpaper-marble
+Marble wallpaper.

%files -n plasma-wallpaper-marble
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_wallpaper_marble.so
%_kde_services/plasma-wallpaper-marble.desktop

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-mandelbrot
Summary: Mandelbrot wallpaper
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-wallpaper

%description -n plasma-wallpaper-mandelbrot
Mandelbrot wallpaper.

%files -n plasma-wallpaper-mandelbrot
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_wallpaper_mandelbrot.so
%_kde_services/plasma-wallpaper-mandelbrot.desktop

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

%define plasmaweather_major 4
%define libplasmaweather %mklibname plasmaweather %plasmaweather_major

%package -n %libplasmaweather
Summary: %name library
Group: System/Libraries

%description -n %libplasmaweather
%name library.

%post -n %libplasmaweather -p /sbin/ldconfig
%postun -n %libplasmaweather -p /sbin/ldconfig

%files -n %libplasmaweather
%defattr(-,root,root,-)
%_kde_libdir/libplasmaweather.so.%{plasmaweather_major}*

#-----------------------------------------------------------------------------

%define rtm_major 4
%define librtm %mklibname rtm %rtm_major

%package -n %librtm
Summary: %name library
Group: System/Libraries

%description -n %librtm
%name library.

%post -n %librtm -p /sbin/ldconfig
%postun -n %librtm -p /sbin/ldconfig

%files -n %librtm
%defattr(-,root,root,-)
%_kde_libdir/librtm.so.%{rtm_major}*

#-----------------------------------------------------------------------------

%define plasmapotdprovidercore_major 1
%define libplasmapotdprovidercore %mklibname plasmapotdprovidercore %plasmapotdprovidercore_major

%package -n %libplasmapotdprovidercore
Summary: %name library
Group: System/Libraries

%description -n %libplasmapotdprovidercore
%name library.

%post -n %libplasmapotdprovidercore -p /sbin/ldconfig
%postun -n %libplasmapotdprovidercore -p /sbin/ldconfig

%files -n %libplasmapotdprovidercore
%defattr(-,root,root,-)
%_kde_libdir/libplasmapotdprovidercore.so.%{plasmapotdprovidercore_major}*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: %libplasmacomicprovidercore = %version
Requires: %libplasmaweather = %version
Requires: %librtm = %version
Requires: %libplasmapotdprovidercore = %version
Requires: kdelibs4-devel
Obsoletes: extragear-plasma-devel

%description  devel
This package contains header files needed if you wish to build applications
based on %name

%files devel
%defattr(-,root,root)
%{_kde_libdir}/*.so
%_kde_includedir/lancelot

#-----------------------------------------------------------------------------

%prep
%if %branch
%setup -qn %name-%{version}%kde_snapshot
%else
%setup -qn %name-%{version}
%endif
%patch1 -p0
%patch2 -p0
%patch3 -p0

%build
%cmake_kde4 
%make

%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

