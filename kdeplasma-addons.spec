# FIXME split into several packages
%define major 5
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

%define libweather_major 1
%define libweather %mklibname plasmaweather %{libweather_major}

Name: kdeplasma-addons
Version: 6.5.1
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/kdeplasma-addons/-/archive/%{gitbranch}/kdeplasma-addons-%{gitbranchd}.tar.bz2#/kdeplasma-addons-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/kdeplasma-addons-%{version}.tar.xz
%endif
Summary: KDE 6 Plasma Add-Ons
URL: https://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Svg)
BuildRequires: cmake(Plasma) >= 5.90.0
BuildRequires: cmake(PlasmaQuick)
BuildRequires: cmake(KF6Runner)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6Holidays)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(Plasma5Support)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6UnitConversion)
BuildRequires: cmake(KF6Auth)
#BuildRequires: cmake(LibTaskManager)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WebEngineCore)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6WebEngineQuick)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xft)
BuildRequires: cmake(KF6NetworkManagerQt)
Obsoletes: %{libweather} < %{EVRD}
# Renamed after 6.0 2025-05-03
%rename plasma6-kdeplasma-addons
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE 6 Plasma Add-Ons.

%install -a
# (tpg) not needed
rm -rf	%{buildroot}%{_libdir}/libplasmapotdprovidercore.so \
	%{buildroot}%{_includedir} \
	%{buildroot}%{_libdir}/cmake/PlasmaPotdProvider \
	%{buildroot}%{_datadir}/kdevappwizard/templates/plasmapotdprovider.tar.bz2

%files -f %{name}.lang
%{_libdir}/libplasmapotdprovidercore.so*
%{_datadir}/qlogging-categories6/kdeplasma-addons.categories
%{_datadir}/knsrcfiles/comic.knsrc
%{_qtdir}/plugins/plasma/applets/*.so
%{_qtdir}/plugins/potd
%{_qtdir}/plugins/plasmacalendarplugins/astronomicalevents.so
%{_qtdir}/plugins/plasmacalendarplugins/astronomicalevents
%{_qtdir}/qml/org/kde/plasma/private/notes
%{_qtdir}/qml/org/kde/plasma/private/dict
%{_datadir}/icons/hicolor/scalable/apps/accessories-dictionary.svgz
%{_datadir}/plasma/plasmoids/org.kde.plasma_applet_dict
%{_datadir}/plasma/plasmoids/org.kde.plasma.calculator
%{_datadir}/plasma/plasmoids/org.kde.plasma.fuzzyclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.konsoleprofiles
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickerdash
%{_datadir}/plasma/plasmoids/org.kde.plasma.notes
%{_datadir}/plasma/plasmoids/org.kde.plasma.webbrowser
%{_datadir}/plasma/plasmoids/org.kde.plasma.fifteenpuzzle
%{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker
%{_datadir}/plasma/plasmoids/org.kde.plasma.diskquota
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe
%{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher
%{_datadir}/plasma/plasmoids/org.kde.plasma.grouping
%{_datadir}/plasma/desktoptheme/default/widgets/timer.svgz
%{_datadir}/plasma/desktoptheme/default/weather/wind-arrows.svgz
%{_datadir}/plasma/wallpapers/org.kde.haenau
%{_datadir}/plasma/wallpapers/org.kde.hunyango
%{_datadir}/plasma/wallpapers/org.kde.potd
%{_datadir}/kwin/effects/cube
%{_datadir}/kwin/tabbox
%{_datadir}/icons/hicolor/scalable/apps/fifteenpuzzle.svgz
%{_qtdir}/qml/org/kde/plasma/private/colorpicker
%{_qtdir}/qml/org/kde/plasma/private/diskquota
%{_qtdir}/qml/org/kde/plasma/private/fifteenpuzzle
%{_qtdir}/qml/org/kde/plasma/private/mediaframe
%{_qtdir}/qml/org/kde/plasmacalendar
%{_qtdir}/plugins/kf6/krunner/unitconverter.so
%{_qtdir}/plugins/kf6/krunner/krunner_charrunner.so
%{_qtdir}/plugins/kf6/krunner/krunner_dictionary.so
%{_qtdir}/plugins/kf6/krunner/krunner_katesessions.so
%{_qtdir}/plugins/kf6/krunner/krunner_konsoleprofiles.so
%{_qtdir}/plugins/kf6/krunner/krunner_spellcheck.so
%{_qtdir}/plugins/kf6/krunner/org.kde.datetime.so
%{_qtdir}/plugins/kf6/krunner/kcms/kcm_krunner_charrunner.so
%{_qtdir}/plugins/kf6/krunner/kcms/kcm_krunner_dictionary.so
%{_qtdir}/plugins/kf6/krunner/kcms/kcm_krunner_spellcheck.so
%{_qtdir}/plugins/kwin/effects/configs/kwin_cube_config.so
%{_qtdir}/qml/org/kde/plasma/wallpapers/potd
%{_qtdir}/plugins/plasmacalendarplugins/alternatecalendar.so
%{_qtdir}/plugins/plasmacalendarplugins/alternatecalendar
%{_qtdir}/qml/org/kde/plasma/private/profiles
%{_datadir}/plasma/plasmoids/org.kde.plasma.addons.katesessions
%{_qtdir}/plugins/kf6/packagestructure/plasma_comic.so
%{_datadir}/knotifications6/plasma_applet_timer.notifyrc
%{_libdir}/libexec/kf6/kauth/kameleonhelper
%{_qtdir}/plugins/kf6/kded/kameleon.so
%{_qtdir}/qml/org/kde/plasma/private/alternatecalendarconfig
%{_datadir}/dbus-1/system-services/org.kde.kameleonhelper.service
%{_datadir}/dbus-1/system.d/org.kde.kameleonhelper.conf
%{_datadir}/polkit-1/actions/org.kde.kameleonhelper.policy
%{_qtdir}/plugins/kf6/krunner/krunner_colors.so
%{_datadir}/qlogging-categories6/kdeplasma-addons.renamecategories
%{_libdir}/libplasmaweatherdata.so*
%{_libdir}/libplasmaweatherion.so*
%{_qtdir}/plugins/plasma/weather_ions
%{_datadir}/plasma/weather/noaa_station_list.xml
