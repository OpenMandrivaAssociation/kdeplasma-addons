# FIXME split into several packages
%define major 5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

%define libweather_major 1
%define libweather %mklibname plasmaweather %{libweather_major}

Name: kdeplasma-addons
Version: 5.14.1
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: KDE 5 Plasma Add-Ons
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5DNSSD)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5Runner)
BuildRequires: cmake(KF5Kross)
BuildRequires: cmake(KF5KrossUi)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5Holidays)
BuildRequires: cmake(KF5Purpose)
BuildRequires: cmake(LibTaskManager)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5WebEngine)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xft)
%rename kdeplasma-addons5
Provides: kdeplasma
Provides: kdeplasma4 = %{version}
Obsoletes: plasma-desktoptheme-default < 4.14.3-4
Obsoletes: plasma-applet-bball < 4.14.3-4
Obsoletes: plasma-applet-binaryclock < 4.14.3-4
Obsoletes: plasma-applet-blackboard < 4.14.3-4
Obsoletes: plasma-applet-bookmarks < 4.14.3-4
Obsoletes: plasma-applet-bubblemon < 4.14.3-4
Obsoletes: plasma-applet-calculator < 4.14.3-4
Obsoletes: plasma-applet-charselect < 4.14.3-4
Obsoletes: plasma-applet-comic < 4.14.3-4
Obsoletes: plasma-applet-dict < 4.14.3-4
Obsoletes: plasma-applet-eyes < 4.14.3-4
Obsoletes: plasma-applet-fifteenpuzzle < 4.14.3-4
Obsoletes: plasma-applet-filewatcher < 4.14.3-4
Obsoletes: plasma-applet-frame < 4.14.3-4
Obsoletes: plasma-applet-fuzzy-clock < 4.14.3-4
Obsoletes: plasma-applet-icontasks < 4.14.3-4
Obsoletes: plasma-applet-incomingmsg < 4.14.3-4
Obsoletes: plasma-applet-kimpanel < 4.14.3-4
Obsoletes: plasma-applet-kolourpicker < 4.14.3-4
Obsoletes: plasma-applet-konqprofiles < 4.14.3-4
Obsoletes: plasma-applet-konsoleprofiles < 4.14.3-4
Obsoletes: plasma-applet-knowledgebase < 4.14.3-4
Obsoletes: plasma-applet-lancelot < 4.14.3-4
Obsoletes: plasma-applet-leavenote < 4.14.3-4
Obsoletes: plasma-applet-life < 4.14.3-4
Obsoletes: plasma-applet-luna < 4.14.3-4
Obsoletes: plasma-applet-magnifique < 4.14.3-4
Obsoletes: plasma-applet-mediaplayer < 4.14.3-4
Obsoletes: plasma-applet-microblog < 4.14.3-4
Obsoletes: plasma-applet-news < 4.14.3-4
Obsoletes: plasma-applet-notes < 4.14.3-4
Obsoletes: plasma-applet-nowplaying < 4.14.3-4
Obsoletes: plasma-applet-opendesktop < 4.14.3-4
Obsoletes: plasma-applet-paste < 4.14.3-4
Obsoletes: plasma-applet-plasmaboard < 4.14.3-4
Obsoletes: plasma-applet-previewer < 4.14.3-4
Obsoletes: plasma-applet-qalculate < 4.14.3-4
Obsoletes: plasma-applet-rssnow < 4.14.3-4
Obsoletes: plasma-applet-rtm < 4.14.3-4
Obsoletes: plasma-applet-showdashboard < 4.14.3-4
Obsoletes: plasma-applet-showdesktop < 4.14.3-4
Obsoletes: plasma-applet-spellcheck < 4.14.3-4
Obsoletes: plasma-applet-systemloadviewer < 4.14.3-4
Obsoletes: plasma-applet-timer < 4.14.3-4
Obsoletes: plasma-applet-unitconverter < 4.14.3-4
Obsoletes: plasma-applet-weather < 4.14.3-4
Obsoletes: plasma-applet-weatherstation < 4.14.3-4
Obsoletes: plasma-applet-webslice < 4.14.3-4
Obsoletes: plasma-runner-audioplayercontrol < 4.14.3-4
Obsoletes: plasma-runner-browserhistory < 4.14.3-4
Obsoletes: plasma-runner-charrunner < 4.14.3-4
Obsoletes: plasma-runner-contacts < 4.14.3-4
Obsoletes: plasma-runner-converter < 4.14.3-4
Obsoletes: plasma-runner-datetime < 4.14.3-4
Obsoletes: plasma-runner-dictionary < 4.14.3-4
Obsoletes: plasma-runner-events < 4.14.3-4
Obsoletes: plasma-runner-katesessions < 4.14.3-4
Obsoletes: plasma-runner-konquerorsessions < 4.14.3-4
Obsoletes: plasma-runner-konsolesessions < 4.14.3-4
Obsoletes: plasma-runner-kopete < 4.14.3-4
Obsoletes: plasma-runner-mediawiki < 4.14.3-4
Obsoletes: plasma-runner-spellchecker < 4.14.3-4
Obsoletes: plasma-runner-translator < 4.14.3-4
Obsoletes: plasma-runner-youtube < 4.14.3-4
Obsoletes: plasma-wallpaper-mandelbrot < 4.14.3-4
Obsoletes: plasma-wallpaper-marble < 4.14.3-4
Obsoletes: plasma-wallpaper-pattern < 4.14.3-4
Obsoletes: plasma-wallpaper-potd < 4.14.3-4
Obsoletes: plasma-wallpaper-qml < 4.14.3-4
Obsoletes: plasma-wallpaper-virus < 4.14.3-4
Obsoletes: plasma-wallpaper-weather < 4.14.3-4
Obsoletes: %{libweather} < %{EVRD}
# (tpg) fix bug https://issues.openmandriva.org/show_bug.cgi?id=1616
Requires: qt5-qtwebengine

%description
KDE 5 Plasma Add-Ons.

%libpackage plasmacomicprovidercore 1
%libpackage plasmapotdprovidercore 1

%prep
%autosetup -p1

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# (tpg) not needed
rm -rf	%{buildroot}%{_libdir}/libplasmapotdprovidercore.so \
	%{buildroot}%{_includedir} \
	%{buildroot}%{_libdir}/cmake/PlasmaPotdProvider

%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_sysconfdir}/xdg/comic.knsrc
%{_libdir}/qt5/plugins/*.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_comic.so
%{_libdir}/qt5/plugins/plasma/applets/*.so
%{_libdir}/qt5/plugins/plasma/dataengine/*.so
%{_libdir}/qt5/plugins/potd
%{_libdir}/qt5/plugins/plasmacalendarplugins/astronomicalevents.so
%{_libdir}/qt5/plugins/plasmacalendarplugins/astronomicalevents
%{_libdir}/qt5/qml/org/kde/plasma/private/notes
%{_libdir}/qt5/qml/org/kde/plasma/private/dict
%{_datadir}/icons/hicolor/scalable/apps/accessories-dictionary.svgz
%{_datadir}/metainfo/*.xml
%{_datadir}/kdevappwizard/templates/plasmapotdprovider.tar.bz2
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservicetypes5/plasma_comicprovider.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma_applet_dict
%{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.calculator
%{_datadir}/plasma/plasmoids/org.kde.plasma.fuzzyclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.comic
%{_datadir}/plasma/plasmoids/org.kde.plasma.konsoleprofiles
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickerdash
%{_datadir}/plasma/plasmoids/org.kde.plasma.notes
%{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemloadviewer
%{_datadir}/plasma/plasmoids/org.kde.plasma.timer
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardindicator
%{_datadir}/plasma/plasmoids/org.kde.plasma.webbrowser
%{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.fifteenpuzzle
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager
%{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker
%{_datadir}/plasma/plasmoids/org.kde.plasma.diskquota
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather
%{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch
%{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher
%{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare
%{_datadir}/plasma/plasmoids/org.kde.plasma.grouping
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping
%{_datadir}/plasma/desktoptheme/default/widgets/timer.svgz
%{_datadir}/plasma/desktoptheme/default/icons/quota.svg
%{_datadir}/plasma/desktoptheme/default/weather/wind-arrows.svgz
%{_datadir}/plasma/services/org.kde.plasma.dataengine.konsoleprofiles.operations
%{_datadir}/plasma/wallpapers/org.kde.haenau
%{_datadir}/plasma/wallpapers/org.kde.hunyango
%{_datadir}/plasma/wallpapers/org.kde.potd
%{_datadir}/kwin/tabbox
%{_datadir}/kwin/desktoptabbox
%{_datadir}/kservices5/kwin/kwin4_desktop_switcher_previews.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_big_icons.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_compact.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_informative.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_present_windows.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_small_icons.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_text.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_thumbnails.desktop
%{_datadir}/icons/hicolor/scalable/apps/fifteenpuzzle.svgz
%{_libdir}/qt5/qml/org/kde/plasma/private/colorpicker
%{_libdir}/qt5/qml/org/kde/plasma/private/diskquota
%{_libdir}/qt5/qml/org/kde/plasma/private/quicklaunch
%{_libdir}/qt5/qml/org/kde/plasma/private/showdesktop
%{_libdir}/qt5/qml/org/kde/plasma/private/fifteenpuzzle
%{_libdir}/qt5/qml/org/kde/plasma/private/timer
%{_libdir}/qt5/qml/org/kde/plasma/private/mediaframe/libmediaframeplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/mediaframe/qmldir
%{_libdir}/qt5/qml/org/kde/plasma/private/weather/libweatherplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/weather/qmldir
%{_libdir}/qt5/qml/org/kde/plasma/private/purpose/qmldir
%{_libdir}/qt5/qml/org/kde/plasma/private/purpose/libpurposeplugin.so
%{_libdir}/qt5/qml/org/kde/plasmacalendar
