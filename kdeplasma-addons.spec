# workaround bug in rpm unpackaged subdir check
%define _unpackaged_subdirs_terminate_build 0

Name:		kdeplasma-addons
Version:	4.10.1
Release:	1
Summary:	A compilation of plasma items (runners, applets, plasmoids) for KDE4
Group:		Graphical desktop/KDE
License:	GPL
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdeplasma-addons-%{version}.tar.xz
BuildRequires:	kdebase4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	boost-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	marble-devel
BuildRequires:	python-devel
BuildRequires:	qt4-qtdbus
BuildRequires:	pkgconfig(eigen2)
BuildRequires:	pkgconfig(libkexiv2)
BuildRequires:	pkgconfig(libqalculate)
BuildRequires:	pkgconfig(qimageblitz)
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(qoauth)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xtst)

# Possible features to add:
#BuildRequires: pkgconfig(ibus-1.0)
#BuildRequires:	pkgconfig(scim)

Provides:	kdeplasma
Provides:	kdeplasma4 = %{version}

Suggests:	plasma-desktoptheme-default

Suggests:	plasma-applet-filewatcher
Suggests:	plasma-applet-notes
Suggests:	plasma-applet-showdesktop
Suggests:	plasma-applet-comic
Suggests:	plasma-applet-konqprofiles
Suggests:	plasma-applet-rssnow
Suggests:	plasma-applet-previewer
Suggests:	plasma-applet-bball
Suggests:	plasma-applet-incomingmsg
Suggests:	plasma-applet-leavenote
Suggests:	plasma-applet-life
Suggests:	plasma-applet-konsoleprofiles
Suggests:	plasma-applet-luna
Suggests:	plasma-applet-lancelot
Suggests:	plasma-applet-microblog
Suggests:	plasma-applet-nowplaying
Suggests:	plasma-applet-binaryclock
Suggests:	plasma-applet-dict
Suggests:	plasma-applet-fuzzy-clock
Suggests:	plasma-applet-frame
Suggests:	plasma-applet-showdashboard
Suggests:	plasma-applet-calculator
Suggests:	plasma-applet-fifteenpuzzle
Suggests:	plasma-applet-kolourpicker
Suggests:	plasma-applet-unitconverter
Suggests:	plasma-applet-systemloadviewer
Suggests:	plasma-applet-weather
Suggests:	plasma-applet-bubblemon
Suggests:	plasma-applet-weatherstation
Suggests:	plasma-applet-news
Suggests:	plasma-applet-charselect
Suggests:	plasma-applet-eyes
Suggests:	plasma-applet-paste
Suggests:	plasma-applet-timer
Suggests:	plasma-applet-opendesktop
Suggests:	plasma-applet-magnifique
Suggests:	plasma-applet-mediaplayer
Suggests:	plasma-applet-rtm
Suggests:	plasma-applet-knowledgebase
Suggests:	plasma-applet-blackboard
Suggests:	plasma-applet-plasmaboard
Suggests:	plasma-applet-qalculate
Suggests:	plasma-applet-webslice
Suggests:	plasma-applet-spellcheck
Suggests:	plasma-applet-bookmarks
Suggests:	plasma-applet-kimpanel
Suggests:	plasma-applet-icontasks

Suggests:	plasma-runner-charrunner
Suggests:	plasma-runner-converter
Suggests:	plasma-runner-contacts
Suggests:	plasma-runner-datetime
Suggests:	plasma-runner-dictionary
Suggests:	plasma-runner-events
Suggests:	plasma-runner-konquerorsessions
Suggests:	plasma-runner-katesessions
Suggests:	plasma-runner-konsolesessions
Suggests:	plasma-runner-browserhistory
Suggests:	plasma-runner-spellchecker
Suggests:	plasma-runner-audioplayercontrol
Suggests:	plasma-runner-mediawiki
Suggests:	plasma-runner-kopete
Suggests:	plasma-runner-youtube

Suggests:	plasma-wallpaper-pattern
Suggests:	plasma-wallpaper-weather
Suggests:	plasma-wallpaper-virus
Suggests:	plasma-wallpaper-mandelbrot
Suggests:	plasma-wallpaper-marble
Suggests:	plasma-wallpaper-potd

%description
A compilation of plasma items (runners, applets, plasmoids) for KDE4.

%files
%doc COPYING

#-----------------------------------------------------------------------------

%package -n plasma-applet-icontasks
Summary:	Plasma icontasks applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-icontasks
Plasma icontasks applet.

%files -n plasma-applet-icontasks
%{_kde_libdir}/kde4/plasma_applet_icontasks.so
%{_kde_services}/plasma-applet-icontasks.desktop
%{_kde_appsdir}/kdeplasma-addons/mediabuttonsrc
%{_kde_appsdir}/desktoptheme/default/icontasks

#-----------------------------------------------------------------------------

%package -n plasma-applet-filewatcher
Summary:	Monitor applet for files
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-filewatcher
Monitor applet for files.

%files -n plasma-applet-filewatcher
%{_kde_libdir}/kde4/plasma_applet_fileWatcher.so
%{_kde_services}/plasma-fileWatcher-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-bookmarks
Summary:	Bookmark applet for KDE
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Provides:	plasma-applet

%description -n plasma-applet-bookmarks
This applet provides access to KDE's bookmark

%files -n plasma-applet-bookmarks
%{_kde_services}/plasma-applet-bookmarks.desktop
%{_kde_libdir}/kde4/plasma_applet_bookmarks.so

#-----------------------------------------------------------------------------

%package -n plasma-applet-notes
Summary:	Plasma notes applets
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-notes
Plasma notes applets.

%files -n plasma-applet-notes
%{_kde_libdir}/kde4/plasma_applet_notes.so
%{_kde_services}/plasma-notes-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-showdesktop
Summary:	Show desktop contents
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-showdesktop
Show desktop contents.

%files -n plasma-applet-showdesktop
%{_kde_libdir}/kde4/plasma_applet_showdesktop.so
%{_kde_services}/plasma-applet-showdesktop.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-comic
Summary:	Make your day happy with daily desktop comics applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet
Requires:	plasma-dataengine-comic = %{EVRD}

%description -n plasma-applet-comic
Make your day happy with daily desktop comics applet

%files -n plasma-applet-comic
%{_kde_libdir}/kde4/plasma_applet_comic.so
%{_kde_configdir}/comic.knsrc
%{_kde_services}/plasma-packagestructure-comic.desktop
%{_kde_libdir}/kde4/plasma_packagestructure_comic.so
%{_kde_servicetypes}/plasma_comicprovider.desktop
%{_kde_appsdir}/plasma/packages/org.kde.comic

#-----------------------------------------------------------------------------

%package -n plasma-applet-konqprofiles
Summary:	Live konqueror profile viewer
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Requires:	plasma-dataengine-konqprofiles = %{EVRD}
Provides:	plasma-applet

%description -n plasma-applet-konqprofiles
Live konqueror profile viewer.

%files -n plasma-applet-konqprofiles
%{_kde_appsdir}/plasma/plasmoids/konqprofiles
%{_kde_services}/plasma-applet-konqprofiles.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-rssnow
Summary:	Plasma RSS Applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-rssnow
Plasma RSS Applet

%files -n plasma-applet-rssnow
%{_kde_libdir}/kde4/plasma_applet_rssnow.so
%{_kde_appsdir}/desktoptheme/default/rssnow
%{_kde_services}/plasma-applet-rssnow.desktop
%{_kde_appsdir}/rssnow

#-----------------------------------------------------------------------------

%package -n plasma-applet-previewer
Summary:	Previewer Plasma Applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-previewer
Previewer Plasma Applet

%files -n plasma-applet-previewer
%{_kde_libdir}/kde4/plasma_applet_previewer.so
%{_kde_iconsdir}/hicolor/*/apps/previewer.png
%{_kde_services}/ServiceMenus/preview.desktop
%{_kde_services}/plasma-applet-previewer.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-bball
Summary:	bball Plasma Applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-bball
bball Plasma Applet

%files -n plasma-applet-bball
%{_kde_iconsdir}/*/*/*/bball*
%{_kde_services}/plasma-applet-bball.desktop
%{_kde_appsdir}/bball
%{_kde_libdir}/kde4/plasma_applet_bball.so

#-----------------------------------------------------------------------------

%package -n plasma-applet-incomingmsg
Summary:	incomingmsg Plasma Applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-incomingmsg
incomingmsg Plasma Applet

%files -n plasma-applet-incomingmsg
%{_kde_services}/plasma-applet-incomingmsg.desktop
%{_kde_libdir}/kde4/plasma_applet_incomingmsg.so

#-----------------------------------------------------------------------------

%package -n plasma-applet-leavenote
Summary:	Leave A Note
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-leavenote
Leave notes for users while they are away

%files -n plasma-applet-leavenote
%{_kde_libdir}/kde4/plasma_applet_leavenote.so
%{_kde_services}/plasma-applet-leavenote.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-life
Summary:	life Plasma Applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-life
life Plasma Applet

%files -n plasma-applet-life
%{_kde_libdir}/kde4/plasma_applet_life.so
%{_kde_services}/plasma-applet-life.desktop
%{_kde_iconsdir}/hicolor/*/apps/lifegame.*

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-kdeobservatory
Summary:	Engine of the kdeobservatory plasma applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-dataengine

%description -n plasma-dataengine-kdeobservatory
Engine of the kdeobservatory plasma applet

%files -n plasma-dataengine-kdeobservatory
%{_kde_libdir}/kde4/plasma_engine_kdeobservatory.so
%{_kde_appsdir}/plasma/services/kdeobservatory.operations
%{_kde_services}/plasma-engine-kdeobservatory.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-pastebin
Summary:	Pastebin plasma Applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-pastebin
Paste text/images to a remote server

%files -n plasma-applet-pastebin
%{_kde_services}/plasma-applet-pastebin.desktop
%{_kde_libdir}/kde4/plasma_applet_pastebin.so
%{_kde_appsdir}/plasma_pastebin
%{_kde_configdir}/pastebin.knsrc

#-----------------------------------------------------------------------------

%package -n plasma-applet-knowledgebase
Summary:	Widget that can query the knowledgebase of opendesktop.org
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet
Requires:	plasma-dataengine-ocs

%description -n plasma-applet-knowledgebase
Widget that can query the knowledgebase of opendesktop.org

%files -n plasma-applet-knowledgebase
%{_kde_libdir}/kde4/plasma_applet_knowledgebase.so
%{_kde_services}/plasma-applet-knowledgebase.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-blackboard
Summary:	A blackboard plasma applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-blackboard
A blackboard plasma applet

%files -n plasma-applet-blackboard
%{_kde_libdir}/kde4/plasma_applet_blackboard.so
%{_kde_services}/plasma-applet-blackboard.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-plasmaboard
Summary:	A plasmaboard plasma applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-plasmaboard
A virtual, on-screen keyboard

%files -n plasma-applet-plasmaboard
%{_kde_libdir}/kde4/plasma_applet_plasmaboard.so
%{_kde_services}/plasma_applet_plasmaboard.desktop
%{_kde_appsdir}/plasmaboard

#-----------------------------------------------------------------------------

%package -n plasma-applet-konsoleprofiles
Summary:	Live konsole profile viewer
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Requires:	plasma-dataengine-konsoleprofiles = %{EVRD}
Provides:	plasma-applet

%description -n plasma-applet-konsoleprofiles
Live konsole profile viewer.

%files -n plasma-applet-konsoleprofiles
%{_kde_appsdir}/plasma/plasmoids/konsoleprofiles
%{_kde_services}/plasma-applet-konsoleprofiles.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-luna
Summary:	Lunar calendar
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-luna
Lunar calendar applet.

%files -n plasma-applet-luna
%{_kde_libdir}/kde4/plasma_applet_luna.so
%{_kde_services}/plasma-applet-luna.desktop
%{_kde_iconsdir}/hicolor/*/apps/luna.png

#-----------------------------------------------------------------------------

%package -n plasma-applet-lancelot
Summary:	Plasma lancelot applets
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-lancelot
Plasma lancelot applets.

%files -n plasma-applet-lancelot
%{_kde_bindir}/lancelot
%{_kde_libdir}/kde4/plasma_applet_lancelot_part.so
%{_kde_libdir}/kde4/plasma_applet_lancelot_launcher.so
%{_kde_services}/plasma-applet-lancelot-launcher.desktop
%{_kde_iconsdir}/hicolor/*/apps/lancelot*.png
%{_kde_iconsdir}/hicolor/*/apps/plasmaapplet-shelf.png
%{_kde_services}/plasma-applet-lancelot-part.desktop
%{_kde_services}/lancelot.desktop
%{_kde_datadir}/mime/packages/lancelotpart-mime.xml
%{_kde_appsdir}/desktoptheme/*/lancelot
%{_kde_appsdir}/lancelot

#-----------------------------------------------------------------------------

%define lancelot_major 2
%define liblancelot %mklibname lancelot %{lancelot_major}

%package -n %{liblancelot}
Summary:	%{name} library
Group:		System/Libraries
Obsoletes:	%{_lib}lancelot1 < %{EVRD}

%description -n %{liblancelot}
%{name} library.

%files -n %{liblancelot}
%{_kde_libdir}/liblancelot.so.*

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-default
Summary:	Plasma default desktopthemes
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace

%description -n plasma-desktoptheme-default
Plasma default desktopthemes.

%files -n plasma-desktoptheme-default
%{_kde_appsdir}/desktoptheme/default/widgets

#-----------------------------------------------------------------------------

%package -n plasma-applet-microblog
Summary:	Microblog applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet
Requires:	plasma-dataengine-microblog = %{EVRD}
Provides:	plasma-applet-twitter = %{EVRD}

%description -n plasma-applet-microblog
Update and view your microblog status

%files -n plasma-applet-microblog
%{_kde_libdir}/kde4/plasma_applet_microblog.so
%{_kde_services}/plasma-applet-microblog.desktop
%{_kde_appsdir}/plasma/services/tweet.operations

#-----------------------------------------------------------------------------

%package -n plasma-applet-nowplaying
Summary:	SWoong notifier applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-nowplaying
Song notifier applet

%files -n plasma-applet-nowplaying
%{_kde_appsdir}/plasma/plasmoids/nowplaying
%{_kde_services}/plasma-applet-nowplaying.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-binaryclock
Summary:	Simplified way to see the hours
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-binaryclock
Simplified way to see the hours.

%files -n plasma-applet-binaryclock
%{_kde_libdir}/kde4/plasma_applet_binaryclock.so
%{_kde_services}/plasma-applet-binaryclock.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-dict
Summary:	Dict applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-dict
A dict applets.

%files -n plasma-applet-dict
%{_kde_libdir}/kde4/plasma_applet_dict.so
%{_kde_services}/plasma-dict-default.desktop
%{_kde_iconsdir}/hicolor/scalable/apps/accessories-dict*

#-----------------------------------------------------------------------------

%package -n plasma-applet-fuzzy-clock
Summary:	A lazy way to see the hours
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-fuzzy-clock
A lazy way to see the hours.

%files -n plasma-applet-fuzzy-clock
%{_kde_libdir}/kde4/plasma_applet_fuzzy_clock.so
%{_kde_services}/plasma-clock-fuzzy.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-frame
Summary:	A basic pictures frame to desktop
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-frame
A basic pictures frame to desktop.

%files -n plasma-applet-frame
%{_kde_libdir}/kde4/plasma_applet_frame.so
%{_kde_services}/plasma-frame-default.desktop
%{_kde_appsdir}/plasma-applet-frame

#-----------------------------------------------------------------------------

%package -n plasma-applet-showdashboard
Summary:	Plasma showdashboard applets
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-showdashboard
Plasma showdashboard applets.

%files -n plasma-applet-showdashboard
%{_kde_libdir}/kde4/plasma_applet_showdashboard.so
%{_kde_services}/plasma-applet-showdashboard.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-calculator
Summary:	Plasma calculator applets
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-calculator
Plasma calculator applets.

%files -n plasma-applet-calculator
%{_kde_appsdir}/plasma/plasmoids/calculator
%{_kde_services}/plasma-applet-calculator.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-fifteenpuzzle
Summary:	Plasma fifteenpuzzle applets
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-fifteenpuzzle
Plasma fifteenpuzzle applets.

%files -n plasma-applet-fifteenpuzzle
%{_kde_libdir}/kde4/plasma_applet_fifteenPuzzle.so
%{_kde_services}/plasma-applet-fifteenPuzzle.desktop
%{_kde_appsdir}/desktoptheme/default/fifteenPuzzle
%{_kde_iconsdir}/*/*/*/fifteenpuzzle.*

#-----------------------------------------------------------------------------

%package -n plasma-applet-kolourpicker
Summary:	Basic color picker
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-kolourpicker
Basic color picker.

%files -n plasma-applet-kolourpicker
%{_kde_libdir}/kde4/plasma_applet_kolourpicker.so
%{_kde_services}/plasma-kolourpicker-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-unitconverter
Summary:	Unit Converter
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-unitconverter
Unit Converter.

%files -n plasma-applet-unitconverter
%{_kde_libdir}/kde4/plasma_applet_unitconverter.so
%{_kde_services}/plasma-applet-unitconverter.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-systemloadviewer
Summary:	System Load Viewer
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-systemloadviewer
System Load Viewer.

%files -n plasma-applet-systemloadviewer
%{_kde_libdir}/kde4/plasma-applet_systemloadviewer.so
%{_kde_services}/plasma-applet-systemloadviewer.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-weather
Summary:	Weather Forecast
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-weather
Weather Forecast.

%files -n plasma-applet-weather
%{_kde_libdir}/kde4/plasma_applet_weather.so
%{_kde_services}/plasma-applet-weather.desktop
%{_kde_appsdir}/desktoptheme/default/weather/wind-arrows.svgz

#-----------------------------------------------------------------------------

%package -n plasma-applet-bubblemon
Summary:	Monitor your system
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-bubblemon
A pretty bubble that monitors your system.

%files -n plasma-applet-bubblemon
%{_kde_libdir}/kde4/plasma_applet_bubblemon.so
%{_kde_services}/plasma-applet-bubblemon.desktop
%{_kde_appsdir}/desktoptheme/default/bubblemon/bubble.svg

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-comic
Summary:	Plasma comic dataengines
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-dataengine
Conflicts:	plasma-applet-comic < 4.9.80

%description -n plasma-dataengine-comic
Plasma comic dataengines.

%files -n plasma-dataengine-comic
%{_kde_libdir}/kde4/plasma_comic*
%{_kde_libdir}/kde4/plasma_engine_comic.*
%{_kde_services}/plasma-comic-default.desktop
%{_kde_services}/plasma-dataengine-comic.desktop

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-microblog
Summary:	Plasma micrbolog dataengines
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-dataengine
Provides:	plasma-dataengine-twitter = %{EVRD}

%description -n plasma-dataengine-microblog
Plasma microblog dataengines.

%files -n plasma-dataengine-microblog
%{_kde_libdir}/kde4/plasma_engine_microblog.so
%{_kde_services}/plasma-dataengine-microblog.desktop

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-rtm
Summary:	An engine to work with Remember the Milk
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-dataengine
Provides:	plasma-dataengine-rememberthemilk = %{EVRD}
Provides:	plasma-dataengine-rtm = %{EVRD}

%description -n plasma-dataengine-rtm
An engine to work with Remember the Milk.

%files -n plasma-dataengine-rtm
%{_kde_libdir}/kde4/plasma_engine_rtm.so
%{_kde_services}/plasma-engine-rtm.desktop
%{_kde_appsdir}/plasma/services/rtmauth.operations
%{_kde_appsdir}/plasma/services/rtmtask.operations
%{_kde_appsdir}/plasma/services/rtmtasks.operations

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-ocs
Summary:	Open Collaboration Services
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-dataengine
Provides:	plasma-dataengine-ocs = %{EVRD}

%description -n plasma-dataengine-ocs
Open Collaboration Services.

%files -n plasma-dataengine-ocs
%{_kde_libdir}/kde4/plasma_engine_ocs.so
%{_kde_services}/plasma-dataengine-ocs.desktop

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-potd
Summary:	Picture of the Day
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-dataengine
Provides:	plasma-dataengine-potd = %{EVRD}

%description -n plasma-dataengine-potd
Data Engine for getting various online Pictures of The Day.

%files -n plasma-dataengine-potd
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

%package -n plasma-dataengine-konqprofiles
Summary:	List and launch Konqueror profiles
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-dataengine

%description -n plasma-dataengine-konqprofiles
Data Engine to list and launch Konqueror profiles.

%files -n plasma-dataengine-konqprofiles
%{_kde_libdir}/kde4/plasma_engine_konqprofiles.so
%{_kde_services}/plasma-dataengine-konqprofiles.desktop
%{_kde_appsdir}/plasma/services/org.kde.plasma.dataengine.konqprofiles.operations

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-konsoleprofiles
Summary:	List and launch Konsole profiles
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-dataengine

%description -n plasma-dataengine-konsoleprofiles
Data Engine to list and launch Konsole profiles.

%files -n plasma-dataengine-konsoleprofiles
%{_kde_libdir}/kde4/plasma_engine_konsoleprofiles.so
%{_kde_services}/plasma-dataengine-konsoleprofiles.desktop
%{_kde_appsdir}/plasma/services/org.kde.plasma.dataengine.konsoleprofiles.operations

#-----------------------------------------------------------------------------

%package -n plasma-runner-converter
Summary:	Plasma converter runners
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-converter
Plasma converter runners.

%files -n plasma-runner-converter
%{_kde_services}/plasma-runner-converter.desktop
%{_kde_libdir}/kde4/krunner_converter.so

#-----------------------------------------------------------------------------

%package -n plasma-runner-charrunner
Summary:	Plasma charrunner runners
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-charrunner
Plasma charrunner runners.

%files -n plasma-runner-charrunner
%{_kde_libdir}/kde4/kcm_krunner_charrunner.so
%{_kde_libdir}/kde4/krunner_charrunner.so
%{_kde_services}/CharRunner_config.desktop
%{_kde_services}/CharacterRunner.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-datetime
Summary:	Plasma charrunner runners
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-datetime
Plasma datetime runners.

%files -n plasma-runner-datetime
%{_kde_libdir}/kde4/plasma_runner_datetime.so
%{_kde_services}/plasma-runner-datetime.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-dictionary
Summary:	Plasma charrunner runners
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-dictionary
Plasma datetime runners.

%files -n plasma-runner-dictionary
%{_kde_libdir}/kde4/kcm_krunner_dictionary.so
%{_kde_libdir}/kde4/krunner_dictionary.so
%{_kde_services}/plasma-runner-dictionary.desktop
%{_kde_services}/plasma-runner-dictionary_config.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-contacts
Summary:	Plasma contacts runners
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-contacts
Plasma contacts runners.

%files -n plasma-runner-contacts
%{_kde_libdir}/kde4/krunner_contacts.so
%{_kde_services}/plasma-runner-contacts.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-events
Summary:	Plasma events runners
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-events
Plasma events runners.

%files -n plasma-runner-events
%{_kde_libdir}/kde4/plasma_runner_events.so
%{_kde_libdir}/kde4/kcm_plasma_runner_events.so
%{_kde_services}/plasma-runner-events_config.desktop
%{_kde_services}/plasma-runner-events.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-weatherstation
Summary:	Plasma applet weatherstation
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-weatherstation
Plasma applet weatherstation

%files -n plasma-applet-weatherstation
%{_kde_libdir}/kde4/plasma_applet_weatherstation.so
%{_kde_appsdir}/desktoptheme/default/weatherstation
%{_kde_services}/plasma-applet-weatherstation.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-news
Summary:	Plasma applet news
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-news
Plasma applet news

%files -n plasma-applet-news
%{_kde_services}/plasma-applet-news.desktop
%{_kde_libdir}/kde4/plasma_applet_news.so
%{_kde_appsdir}/desktoptheme/default/stylesheets/news.css

#-----------------------------------------------------------------------------

%package -n plasma-applet-charselect
Summary:	Plasma applet charselect
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-charselect
Plasma applet charselect

%files -n plasma-applet-charselect
%{_kde_services}/plasma-applet-charselect.desktop
%{_kde_libdir}/kde4/plasma_applet_charselect.so

#-----------------------------------------------------------------------------

%package -n plasma-applet-eyes
Summary:	Plasma applet paste
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-eyes
Plasma applet eyes

%files -n plasma-applet-eyes
%{_kde_libdir}/kde4/plasma_applet_eyes.so
%{_kde_services}/plasma-applet-eyes.desktop
%{_kde_iconsdir}/hicolor/*/apps/eyes.*

#-----------------------------------------------------------------------------

%package -n plasma-applet-paste
Summary:	Plasma applet paste
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-paste
Plasma applet paste

%files -n plasma-applet-paste
%{_kde_libdir}/kde4/plasma_applet_paste.so
%{_kde_services}/plasma-applet-paste.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-timer
Summary:	Plasma applet timer
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-timer
Plasma applet timer

%files -n plasma-applet-timer
%{_kde_libdir}/kde4/plasma_applet_timer.so
%{_kde_services}/plasma-applet-timer.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-opendesktop
Summary:	Communicate using the Social Desktop
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Requires:	plasma-dataengine-ocs
Provides:	plasma-applet

%description -n plasma-applet-opendesktop
Communicate using the Social Desktop.

%files -n plasma-applet-opendesktop
%{_kde_libdir}/kde4/plasma_applet_opendesktop.so
%{_kde_services}/plasma-applet-opendesktop.desktop
%{_kde_services}/plasma-applet-opendesktop-activities.desktop
%{_kde_libdir}/kde4/plasma_applet_opendesktop_activities.so
%{_kde_appsdir}/plasma-applet-opendesktop-activities/plasma-applet-opendesktop-activities.notifyrc
%{_kde_appsdir}/plasma/services/ocsPerson.operations
%{_kde_appsdir}/plasma-applet-opendesktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-magnifique
Summary:	A magnification glass for Plasma canvas
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-magnifique
A magnification glass for Plasma canvas.

%files -n plasma-applet-magnifique
%{_kde_libdir}/kde4/plasma_applet_magnifique.so
%{_kde_services}/plasma-applet-magnifique.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-qalculate
Summary:	A Qalculate plasma applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-qalculate
A Qalculate plasma applet

%files -n plasma-applet-qalculate
%{_kde_libdir}/kde4/plasma_applet_qalculate.so
%{_kde_services}/plasma-applet-qalculate.desktop
%{_kde_iconsdir}/hicolor/*/apps/qalculate-applet.png

#-----------------------------------------------------------------------------

%package -n plasma-applet-mediaplayer
Summary:	Widget that can play video and sound
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-mediaplayer
Widget that can play video and sound.

%files -n plasma-applet-mediaplayer
%{_kde_libdir}/kde4/plasma_applet_mediaplayer.so
%{_kde_services}/plasma-applet-mediaplayer.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-spellcheck
Summary:	Fast spell checking applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-spellcheck
Fast spell checking applet

%files -n plasma-applet-spellcheck
%{_kde_libdir}/kde4/plasma_applet_spellcheck.so
%{_kde_services}/plasma-applet-spellcheck.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-webslice
Summary:	Applet that show a part of a webpage
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-webslice
Applet that show a part of a webpage

%files -n plasma-applet-webslice
%{_kde_services}/plasma-applet-webslice.desktop
%{_kde_libdir}/kde4/plasma_applet_webslice.so

#-----------------------------------------------------------------------------

%package -n plasma-applet-rtm
Summary:	Remember The Milk Todo list applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet
Provides:	plasma-applet-rememberthemilk = %{EVRD}
Requires:	plasma-dataengine-rtm = %{EVRD}

%description -n plasma-applet-rtm
Remember The Milk Todo list applet.

%files -n plasma-applet-rtm
%{_kde_libdir}/kde4/plasma_applet_rtm.so
%{_kde_services}/plasma-applet-rememberthemilk.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-konquerorsessions
Summary:	Plasma runner places
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-konquerorsessions
Plasma runner konquerorsessions.

%files -n plasma-runner-konquerorsessions
%{_kde_services}/konquerorsessions.desktop
%{_kde_libdir}/kde4/krunner_konquerorsessions.so

#-----------------------------------------------------------------------------

%package -n plasma-runner-katesessions
Summary:	Plasma runner katesessions
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-katesessions
Plasma runner katesessions.

%files -n plasma-runner-katesessions
%{_kde_services}/katesessions.desktop
%{_kde_libdir}/kde4/krunner_katesessions.so

#-----------------------------------------------------------------------------

%package -n plasma-runner-konsolesessions
Summary:	Plasma runner konsolesessions
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-konsolesessions
Plasma runner konsolesessions.

%files -n plasma-runner-konsolesessions
%{_kde_services}/konsolesessions.desktop
%{_kde_libdir}/kde4/krunner_konsolesessions.so

#-----------------------------------------------------------------------------

%package -n plasma-runner-browserhistory
Summary:	Plasma runner browserhistory
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-browserhistory
Plasma runner browserhistory.

%files -n plasma-runner-browserhistory
%{_kde_libdir}/kde4/krunner_browserhistory.so
%{_kde_services}/browserhistory.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-spellchecker
Summary:	Plasma runner spellchecker
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-spellchecker
Plasma runner spellchecker.

%files -n plasma-runner-spellchecker
%{_kde_services}/plasma-runner-spellchecker.desktop
%{_kde_services}/plasma-runner-spellchecker_config.desktop
%{_kde_libdir}/kde4/krunner_spellcheckrunner.so
%{_kde_libdir}/kde4/kcm_krunner_spellcheck.so

#-----------------------------------------------------------------------------

%package -n plasma-runner-audioplayercontrol
Summary:	Plasma runner audioplayercontrol
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-audioplayercontrol
Plasma runner audioplayercontrol.

%files -n plasma-runner-audioplayercontrol
%{_kde_libdir}/kde4/kcm_krunner_audioplayercontrol.so
%{_kde_libdir}/kde4/krunner_audioplayercontrol.so
%{_kde_services}/plasma-runner-audioplayercontrol.desktop
%{_kde_services}/plasma-runner-audioplayercontrol_config.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-kopete
Summary:	Plasma runner kopete
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-kopete
Plasma runner kopete.

%files -n plasma-runner-kopete
%{_kde_libdir}/kde4/krunner_kopete.so
%{_kde_services}/plasma-runner-kopete.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-mediawiki
Summary:	Plasma runner mediawiki (matches MediaWiki queries)
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-mediawiki
Plasma runner mediawiki (matches MediaWiki queries).

%files -n plasma-runner-mediawiki
%{_kde_libdir}/kde4/krunner_mediawiki.so
%{_kde_services}/plasma-runner-techbase.desktop
%{_kde_services}/plasma-runner-wikipedia.desktop
%{_kde_services}/plasma-runner-wikitravel.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-youtube
Summary:	Plasma runner youtube (matches YouTube queries)
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner
Conflicts:	kipi-plugins-youtube < 2.0.2-2

%description -n plasma-runner-youtube
Plasma runner youtube (matches YouTube queries).

%files -n plasma-runner-youtube
%{_kde_libdir}/kde4/krunner_youtube.so
%{_kde_services}/plasma-runner-youtube.desktop
%{_kde_iconsdir}/hicolor/*/actions/youtube.*

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-pattern
Summary:	Pattern wallpaper
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-wallpaper

%description -n plasma-wallpaper-pattern
Pattern wallpaper.

%files -n plasma-wallpaper-pattern
%{_kde_libdir}/kde4/plasma_wallpaper_pattern.so
%{_kde_services}/plasma-wallpaper-pattern.desktop
%{_kde_appsdir}/plasma_wallpaper_pattern

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-weather
Summary:	Weather wallpaper
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-wallpaper

%description -n plasma-wallpaper-weather
Weather wallpaper.

%files -n plasma-wallpaper-weather
%{_kde_libdir}/kde4/plasma_wallpaper_weather.so
%{_kde_services}/plasma-wallpaper-weather.desktop
%{_kde_configdir}/plasmaweather.knsrc

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-virus
Summary:	Virus wallpaper
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-wallpaper

%description -n plasma-wallpaper-virus
Virus wallpaper.

%files -n plasma-wallpaper-virus
%{_kde_libdir}/kde4/plasma_wallpaper_virus.so
%{_kde_services}/plasma-wallpaper-virus.desktop
%{_kde_configdir}/virus_wallpaper.knsrc

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-marble
Summary:	Marble wallpaper
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Requires:	marble-common
Provides:	plasma-wallpaper

%description -n plasma-wallpaper-marble
Marble wallpaper.

%files -n plasma-wallpaper-marble
%{_kde_libdir}/kde4/plasma_wallpaper_marble.so
%{_kde_services}/plasma-wallpaper-marble.desktop

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-mandelbrot
Summary:	Mandelbrot wallpaper
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-wallpaper

%description -n plasma-wallpaper-mandelbrot
Mandelbrot wallpaper.

%files -n plasma-wallpaper-mandelbrot
%{_kde_libdir}/kde4/plasma_wallpaper_mandelbrot.so
%{_kde_services}/plasma-wallpaper-mandelbrot.desktop

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-qml
Summary:	Animated Wallpaper
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-wallpaper

%description -n plasma-wallpaper-qml
Animated QML Wallpaper.

%files -n plasma-wallpaper-qml
%{_kde_libdir}/kde4/plasma_wallpaper_qml.so
%{_kde_appsdir}/plasma/packages/org.kde.lcdweather/
%{_kde_appsdir}/plasma/packages/org.kde.weather/
%{_kde_appsdir}/plasma/wallpapers/org.kde.animals/
%{_kde_appsdir}/plasma/wallpapers/org.kde.haenau/
%{_kde_appsdir}/plasma/wallpapers/org.kde.hunyango/
%{_kde_services}/plasma-wallpaper-qml.desktop 

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-potd
Summary:	Potd wallpaper
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-wallpaper

%description -n plasma-wallpaper-potd
Potd wallpaper.

%files -n plasma-wallpaper-potd
%{_kde_libdir}/kde4/plasma_wallpaper_potd.so
%{_kde_services}/plasma-wallpaper-potd.desktop


#-----------------------------------------------------------------------------

%define plasmacomicprovidercore_major 1
%define libplasmacomicprovidercore %mklibname plasmacomicprovidercore %{plasmacomicprovidercore_major}

%package -n %{libplasmacomicprovidercore}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libplasmacomicprovidercore}
%{name} library.

%files -n %{libplasmacomicprovidercore}
%{_kde_libdir}/libplasmacomicprovidercore.so.%{plasmacomicprovidercore_major}*

#-----------------------------------------------------------------------------

%define plasmaweather_major 4
%define libplasmaweather %mklibname plasmaweather %{plasmaweather_major}

%package -n %{libplasmaweather}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libplasmaweather}
%{name} library.

%files -n %{libplasmaweather}
%{_kde_libdir}/libplasmaweather.so.%{plasmaweather_major}*

#-----------------------------------------------------------------------------

%define rtm_major 4
%define librtm %mklibname rtm %{rtm_major}

%package -n %{librtm}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{librtm}
%{name} library.

%files -n %{librtm}
%{_kde_libdir}/librtm.so.%{rtm_major}*

#-----------------------------------------------------------------------------

%define plasmapotdprovidercore_major 1
%define libplasmapotdprovidercore %mklibname plasmapotdprovidercore %{plasmapotdprovidercore_major}

%package -n %{libplasmapotdprovidercore}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libplasmapotdprovidercore}
%{name} library.

%files -n %{libplasmapotdprovidercore}
%{_kde_libdir}/libplasmapotdprovidercore.so.%{plasmapotdprovidercore_major}*

#-----------------------------------------------------------------------------

%define lancelot_datamodels_major 1
%define liblancelot_datamodels %mklibname lancelot-datamodels %{lancelot_datamodels_major}

%package -n %{liblancelot_datamodels}
Summary:	%{name} library
Group:		System/Libraries
Obsoletes:	%{_lib}lancelot-datamodels0 < %{EVRD}

%description -n %{liblancelot_datamodels}
%{name} library.

%files -n %{liblancelot_datamodels}
%{_kde_libdir}/liblancelot-datamodels.so.%{lancelot_datamodels_major}*

#-----------------------------------------------------------------------------

%define plasma_containments_grouping_major 4
%define libplasma_containments_grouping %mklibname plasmacontainmentsgrouping %{plasma_containments_grouping_major}

%package -n %{libplasma_containments_grouping}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libplasma_containments_grouping}
%{name} library.

%files -n %{libplasma_containments_grouping}
%{_kde_libdir}/libplasma_groupingcontainment.so.%{plasma_containments_grouping_major}*

#------------------------------------------------------------------------------

%package -n plasma-applet-kimpanel
Summary:	KDE Input method panel (applet)
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet
Requires:	plasma-dataengine-kimpanel

%description -n plasma-applet-kimpanel
KDE Input method panel (applet)

%files -n plasma-applet-kimpanel
%{_kde_libdir}/kde4/plasma_applet_kimpanel.so
%{_kde_datadir}/config.kcfg/kimpanelconfig.kcfg
%{_kde_services}/plasma-applet-kimpanel.desktop

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-kimpanel
Summary:	Engine of the kimpanel plasma applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-dataengine

%description -n plasma-dataengine-kimpanel
Engine of the kimpanel plasma applet.

%files -n plasma-dataengine-kimpanel
%{_kde_libdir}/kde4/plasma_engine_kimpanel.so
%{_kde_appsdir}/plasma/services/kimpanel.operations
%{_kde_services}/plasma-dataengine-kimpanel.desktop

#-----------------------------------------------------------------------------

%package -n plasma-containments-grouping
Summary:	Containments that do widget grouping and gridding
Group:		Graphical desktop/KDE

%description -n plasma-containments-grouping
This little project will provide the user the ability to layout his
applets in a more advanced way: He will be able to group them inside
special QGraphicsWidgets called Groups, in a way that depends on the
specific group.

%files -n plasma-containments-grouping
%{_kde_libdir}/kde4/plasma_containment_groupingdesktop.so
%{_kde_libdir}/kde4/plasma_containment_groupingpanel.so
%{_kde_libdir}/kde4/plasma_containment_griddesktop.so
%{_kde_services}/plasma-containment-griddesktop.desktop
%{_kde_services}/plasma-containment-groupingdesktop.desktop
%{_kde_services}/plasma-containment-groupingpanel.desktop

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libplasmacomicprovidercore} = %{EVRD}
Requires:	%{libplasmaweather} = %{EVRD}
Requires:	%{librtm} = %{EVRD}
Requires:	%{libplasmapotdprovidercore} = %{EVRD}
Requires:	%{liblancelot} = %{EVRD}
Requires:	plasma-applet-kimpanel = %{EVRD}
Requires:	kdelibs4-devel

%description devel
This package contains header files needed if you wish to build applications
based on %{name}

%files devel
%{_kde_libdir}/*.so
%{_kde_includedir}/lancelot
%{_kde_includedir}/KDE/Lancelot
%{_kde_includedir}/lancelot-datamodels
%{_kde_appsdir}/cmake/modules/FindLancelot-Datamodels.cmake
%{_kde_appsdir}/cmake/modules/FindLancelot.cmake

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0
- Move some files from plasma-applet-comic to plasma-dataengine-comic
- New subpackage plasma-runner-dictionary
- New subpackage plasma-wallpaper-qml
- Update files
- Add pkgconfig(xtst) to BuildRequires

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1
- Disable l10n-ru patch

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0
- plasma-runner-duckduckgo and plasma-runner-bing are removed in upstream 4.9

* Wed Jul 18 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.97-1
- New version 4.8.97
- Make better usage of KDE4 path macros
- Update some summaries and descriptions

* Sat Jun 30 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- Update to 4.8.95
- Adjust Requires, Conflicts, Obsoletes, BuildRequires
- Update l10n patch
- Add pkgconfig(qoauth) and pkgconfig(QJson) to BuildRequires
- Update file lists as now some plasmoids are QML stuff
- New subpackages:
    - plasma-runner-duckduckgo
    - plasma-runner-youtube
    - plasma-runner-bing
    - plasma-dataengine-konsoleprofiles
    - plasma-dataengine-konqprofiles

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.3-1
- update to 4.8.3

* Mon Apr 16 2012 Mikhail Kompaniets <mkompan@mezon.ru> 4.8.2-2
- Russian localization for .desktop files

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.1-1
- update to 4.8.1

* Sun Feb 26 2012 Andrey Bondrov <abondrov@mandriva.org> 4.8.0-2
+ Revision: 780809
- Add pkgconfig(xi) to BuildRequires
- Add libkexiv2-devel to BR, fix some descriptions, update spec aesthetics

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758052
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 744533
- New upstream tarball

* Fri Dec 16 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.90-2
+ Revision: 743072
- Rebuild because of BS failure
- Workaround a rpm5 bug
- New version

* Tue Dec 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-1
+ Revision: 738182
- Fix file list
- Fix file lists ( patch from olivier lahaye )
- New upstream tarball 4.7.80

* Thu Nov 17 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.41-1
+ Revision: 731365
- New version 4.7.41
- Remove branch switch

* Mon Jun 13 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.6.4-1
+ Revision: 684417
- New version 4.6.4

* Fri May 13 2011 Funda Wang <fwang@mandriva.org> 4.6.3-1
+ Revision: 674039
- new version 4.6.3

* Tue Apr 05 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.6.2-1
+ Revision: 650780
- Remove mkrel
- New version 4.6.2

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 4.6.1-1
+ Revision: 643922
- move scim detection into backend subdir, as kimpanel itself has nothing
  todo with scim, only scim backend need to be enabled or disabled.
- scim is in contrib now, so disabling scim backend

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New version 4.6.1

* Mon Feb 07 2011 John Balcaen <mikala@mandriva.org> 4.6.0-2
+ Revision: 636674
- Drop Requires for plasma-dataengine-pastebin for plasma-applet-pastebin package
- Update some descriptions/summary

* Mon Jan 31 2011 Funda Wang <fwang@mandriva.org> 4.6.0-1
+ Revision: 634511
- update provides

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New version KDE 4.6 Final

* Sun Jan 09 2011 Funda Wang <fwang@mandriva.org> 4.5.95-1mdv2011.0
+ Revision: 630687
- drop kdeobservatory, it needs qwt
- update file list

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New version KDE 4.6 RC2

* Thu Dec 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.5.90-1mdv2011.0
+ Revision: 624109
- New upstream tarball

* Sun Dec 12 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.5.85-1mdv2011.0
+ Revision: 620593
- Fix file list
- New upstream tarball

* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 4.5.80-1mdv2011.0
+ Revision: 601666
- new version 4.5.80 (aka 4.6 beta1)

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599288
- update file list
- new snapshot 4.5.77

* Thu Nov 04 2010 Funda Wang <fwang@mandriva.org> 4.5.74-1mdv2011.0
+ Revision: 593217
- fix file list
- new snapshot 4.5.74

* Mon Oct 11 2010 Funda Wang <fwang@mandriva.org> 4.5.71-1mdv2011.0
+ Revision: 584909
- new snapshot

* Thu Sep 16 2010 Funda Wang <fwang@mandriva.org> 4.5.68-1mdv2011.0
+ Revision: 579002
- update file list
- new snapshot 4.5.68

* Tue Sep 07 2010 John Balcaen <mikala@mandriva.org> 4.5.67-1mdv2011.0
+ Revision: 576633
- Add plasma-containments-grouping & his library

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - LOL
    - Fix file list
    - New version 4.5.67

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.5.0-1mdv2011.0
+ Revision: 566583
- New upstream tarball
- Update to version 4.5.0

* Thu Jul 29 2010 Funda Wang <fwang@mandriva.org> 4.4.95-1mdv2011.0
+ Revision: 562958
- new version 4.4.95

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - KDE 4.5 RC3

* Wed Jun 16 2010 Ahmad Samir <ahmadsamir@mandriva.org> 4.4.3-4mdv2010.1
+ Revision: 548181
- add patch to fix audioplayercontrol icon fixes (mdv #59762)

* Sun May 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.4.3-3mdv2010.1
+ Revision: 544118
- Fix Requires

* Thu May 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.4.3-2mdv2010.1
+ Revision: 542880
- Bump release to psuh funda changes

  + Funda Wang <fwang@mandriva.org>
    - add back kdebase4-workspace requirement
    - suggests backend for kimpanel
    - split out impanel's scim backend for future addition of ibus and fcitx backend
    - drop kdebase-workspace requirement of kimpanel, it is not required in fact

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.4.3-1mdv2010.1
+ Revision: 542131
- Update to version 4.4.3

  + Funda Wang <fwang@mandriva.org>
    - add missing requries for actural lib files

* Sun Apr 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.4.2-2mdv2010.1
+ Revision: 531018
- New subpackage plasma-applet-kimpanel

* Sun Mar 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.4.2-1mdv2010.1
+ Revision: 528337
- Update to version 4.4.2

* Tue Mar 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.4.1-2mdv2010.1
+ Revision: 513424
- Update to version 4.4.1

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.4.0-2mdv2010.1
+ Revision: 502637
- Update to version 4.4.0

* Mon Feb 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.3.98-2mdv2010.1
+ Revision: 502211
- Fix requires on subpackages

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.3.98-1mdv2010.1
+ Revision: 498957
- Update to version 4.3.98 aka "kde 4.4 RC3"
- Fix Requires (Bug #57274)

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.3.95-1mdv2010.1
+ Revision: 496132
- Update to kde 4.4 Rc2

* Sun Jan 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.3.90-1mdv2010.1
+ Revision: 488571
- Update to kde 4.4 rc1

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.3.85-1mdv2010.1
+ Revision: 480777
- Update to kde 4.4 beta2
- Update to kde 4.4 beta2

  + John Balcaen <mikala@mandriva.org>
    - Remove a Requires for plasma-applet-qalculate

* Fri Dec 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.3.80-2mdv2010.1
+ Revision: 473435
- Fix file list
- Update to kde 4.4 Beta 1
  New packages:
        - plasma-applet-webslice
        - plasma-applet-spellcheck
        - plasma-runner-audioplayercontrol
        - plasma-runner-mediawiki
        - plasma-runner-kopete

* Sat Nov 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.3.77-1mdv2010.1
+ Revision: 470836
- Remove merged patch
- Update to kde 4.3.77

* Fri Nov 20 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.3.75-1mdv2010.1
+ Revision: 467598
- Update to kde 4.3.75
  Remove merged patch

* Fri Nov 13 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.3.73-1mdv2010.1
+ Revision: 465803
- Add qalculate-devel as buildrequires for the qalculate applet
- Update to 4.3.73
  Some news packages :
                      - plasma-applet-knowledgebase
                      - plasma-applet-blackboard
                      - plasma-applet-plasmaboard
                      - plasma-applet-qalculate
                      - plasma-dataengine-pastebin
- Add patch to fix the build of contact-runner
- Add patch to fix the build of plasma-weather
- Fix major of liblancelot

* Thu Oct 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.3.2-3mdv2010.0
+ Revision: 457502
- Add fixes for RTM
- Fix conflicts

* Sat Oct 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.3.2-2mdv2010.0
+ Revision: 456516
- Add marble-common as requires

* Tue Oct 06 2009 Helio Chissini de Castro <helio@mandriva.com> 4.3.2-1mdv2010.0
+ Revision: 454830
- New upstream release 4.3.2.

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 4.3.1-2mdv2010.0
+ Revision: 423223
- New upstream release 4.3.1.

* Tue Aug 04 2009 Helio Chissini de Castro <helio@mandriva.com> 4.3.0-2mdv2010.0
+ Revision: 409540
- New upstream release 4.3.0.
- Update to KDE 4.3 RC3

* Sun Jul 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.2.96-1mdv2010.0
+ Revision: 394959
- Update to Rc2

* Sat Jun 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.2.95-1mdv2010.0
+ Revision: 389596
- Update to kde 4.3 Rc1
  Remove plasma-applet-bluemarble

* Fri Jun 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.2.90-1mdv2010.0
+ Revision: 382948
- Update to beta2

* Fri May 29 2009 Funda Wang <fwang@mandriva.org> 4.2.88-2mdv2010.0
+ Revision: 381039
- correct file list for previewer

* Fri May 29 2009 Funda Wang <fwang@mandriva.org> 4.2.88-1mdv2010.0
+ Revision: 380825
- fix file list
- New version 4.2.88

* Tue May 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.2.87-4mdv2010.0
+ Revision: 379780
- Enable marble wallpaper
  Clean specfile

  + Funda Wang <fwang@mandriva.org>
    - fix summary and requires

* Mon May 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.2.87-3mdv2010.0
+ Revision: 379518
- Add eigen2 as Buildrequires
- Adapt kdesdk to new layout

* Sat May 23 2009 Funda Wang <fwang@mandriva.org> 4.2.87-1mdv2010.0
+ Revision: 378897
- New version 4.2.87

* Mon May 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.2.85-2mdv2010.0
+ Revision: 374803
- New upstream tarball for beta1

* Sat May 09 2009 Funda Wang <fwang@mandriva.org> 4.2.85-1mdv2010.0
+ Revision: 373689
- fix ocs soversion
- add more plasmoids

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Update to kde 4.2.85

* Tue May 05 2009 Funda Wang <fwang@mandriva.org> 4.2.71-0.svn961800.1mdv2010.0
+ Revision: 372079
- drop patch from trunk
- correct requires
- New version 4.2.71
- qt.patch, lancelot-cpuUsage.patch, lancelot-sortbyname.patch merged upstream
- rediff lancelot-fix-NewDocument.patch, lancelot-fix-computertab.patch
- twitter applet has been renamed to microblog

  + Helio Chissini de Castro <helio@mandriva.com>
    - Raise release to rebuild

* Fri Mar 27 2009 Helio Chissini de Castro <helio@mandriva.com> 4.2.2-1mdv2009.1
+ Revision: 361716
- Update with 4.2.2 try#1 packages

* Sat Mar 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.2.1-3mdv2009.1
+ Revision: 360080
- Fix Bbal applet

* Wed Mar 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.2.1-2mdv2009.1
+ Revision: 348180
- Add back patches lost on kde 4.2.1 migration

* Sat Feb 28 2009 Helio Chissini de Castro <helio@mandriva.com> 4.2.1-1mdv2009.1
+ Revision: 346138
- KDE 4.2.1 try#1 upstream release

* Wed Feb 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.2.0-6mdv2009.1
+ Revision: 342421
- Fix CPU Usage for lancelot

* Tue Feb 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.2.0-5mdv2009.1
+ Revision: 341503
- Fix lancelot with qt45

* Mon Feb 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.2.0-4mdv2009.1
+ Revision: 340890
- Rebuild against qt4.5

* Mon Feb 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.2.0-3mdv2009.1
+ Revision: 338633
- Update list of Suggests

* Sun Feb 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.2.0-2mdv2009.1
+ Revision: 338532
- Convert Requires into suggests

* Wed Jan 28 2009 Helio Chissini de Castro <helio@mandriva.com> 4.2.0-1mdv2009.1
+ Revision: 334706
- Update with official 4.2.0 upstream tarball

* Thu Jan 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.96-3mdv2009.1
+ Revision: 330047
- Fix more conflicts on lancelot
- Fix conflicts

* Fri Jan 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.96-1mdv2009.1
+ Revision: 327598
- Remove old requires
- Remove desktopthemes, they are in kdeartwork now

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.96

* Fri Dec 12 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.85-1mdv2009.1
+ Revision: 313712
- Update with Beta 1 - 4.1.85

* Thu Dec 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.82-1mdv2009.1
+ Revision: 313430
- Update to kde 4.1.82

* Mon Dec 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.81-1mdv2009.1
+ Revision: 308705
- Update to kde 4.1.81

* Sun Nov 23 2008 Funda Wang <fwang@mandriva.org> 4.1.80-1mdv2009.1
+ Revision: 305977
- kdenetwork and kdepim is not needed
- add kdegraphcis for kexiv

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove merged patch

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.80

* Sat Nov 15 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.73-1mdv2009.1
+ Revision: 303410
- Update to kde 4.1.73
- Sort entries by name in lancelot (Bug #45537)
  Add drakconf and rpmdrake in Computer tab in Lancelot (Bug #45538)
  Fix use of OO.o desktop files on non 32bit arch (Bug #45539)

* Sat Oct 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.71-1mdv2009.1
+ Revision: 297067
- New version 4.1.71 ( several  new applets packages)

* Wed Oct 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.70-1mdv2009.1
+ Revision: 296339
- Update to kde 4.1.70
  Fix File List

* Thu Sep 25 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.2-1mdv2009.0
+ Revision: 288280
- KDE 4.1.2 arriving.

* Wed Sep 10 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.1-5mdv2009.0
+ Revision: 283626
- Fix lancelot patch with upstream commit 859364
- Fix patch headers

* Fri Sep 05 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.1-3mdv2009.0
+ Revision: 281714
- Sync with plasma branch

* Tue Sep 02 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.1-2mdv2009.0
+ Revision: 278764
- Update with latest lancelot from branch

* Sun Aug 31 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.1-1mdv2009.0
+ Revision: 277843
- Disable lancelot util maintainer fix new filelist
- Upgrade to forthcoming 4.1.1 packages

* Mon Aug 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.0-4mdv2009.0
+ Revision: 276015
- Add python-devel as BuildRequire
- Bump release
- Use lancelot from branch
- Fix Requires of lancelot ( to enable only for 2009.1 )

* Mon Aug 04 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.0-2mdv2009.0
+ Revision: 263228
- Update with current branch 4.1 patches

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add kdepim4-devel as BR for lancelot
    - Removed merged part of the patch

* Sun Jul 27 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.0-1mdv2009.0
+ Revision: 250454
- Bluemarble plasmoid have been disabled on upstream commit 834159
- Fix Lib SOVERSION  ( need review before upstream commit )
- Add patch0 to enable lancelot ( not activated by default )

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.0

* Thu Jul 10 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.98-2mdv2009.0
+ Revision: 233198
- Update with Release Candidate 1 - 4.0.98
- Update for rc since we're already changed the package naming
- And we rename package again !!

* Mon Jul 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.85-1mdv2009.0
+ Revision: 232546
- New version kde 4.0.85

* Wed Jul 02 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.84-2mdv2009.0
+ Revision: 230800
- Update with current svn to fix some applets causing random kconfig crashes. The crash ususlly happens on the applet registration on plasma startup, leading to wrong assumption to where is crashing. .85 rc1 will be arrives on next week, so we're avoid put svn numbering on tarball

* Fri Jun 27 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.84-1mdv2009.0
+ Revision: 229419
- Update with new snapshot tarballs 4.0.84

  + Anssi Hannula <anssi@mandriva.org>
    - ensure major correctness

* Tue Jun 24 2008 Anssi Hannula <anssi@mandriva.org> 4.0.83-2mdv2009.0
+ Revision: 228616
- drop duplicate buildrequires

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix conflicts for a better upgrade ( patch from colin )

  + Helio Chissini de Castro <helio@mandriva.com>
    - kdeplasmoids back with provides to kdeplasma4 and updated for 4.0.83 release
    - Not until 4.2, i'm a little bit forwad :-(

* Wed Jun 18 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.82-3mdv2009.0
+ Revision: 225412
- Rebuild to fix task-kde4 issue

* Mon Jun 16 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.82-2mdv2009.0
+ Revision: 220466
- Enabled kdeplasma metapackage
- Added proper obsoletes

* Thu Jun 12 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.82-1mdv2009.0
+ Revision: 218615
- Fixed buildrequires and obsoletes
- Fullfill some descriptions
- import kdeplasma4

