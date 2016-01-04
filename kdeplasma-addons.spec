# FIXME split into several packages
%define major 5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: kdeplasma-addons
Version: 5.5.2
Release: 2
Source0: http://download.kde.org/plasma/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: KDE 5 Plasma Add-Ons
URL: http://kde.org/
License: GPL
Group: System/Libraries
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
BuildRequires: pkgconfig(scim)
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xft)

%description
KDE 5 Plasma Add-Ons.

%libpackage plasmacomicprovidercore 1

%prep
%setup -qn
%apply_patches

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang konqprofiles
%find_lang konsoleprofiles
%find_lang lancelot
%find_lang liblancelot-datamodels
%find_lang libplasma_groupingcontainment
%find_lang libplasmaweather
for i in CharSelectApplet org.kde.plasma.activitypager binaryclock bookmarks bubblemon org.kde.plasma.colorpicker org.kde.plasma.diskquota fileWatcher frame groupingpanel incomingmsg knowledgebase leavenote life luna magnifique microblog news org.kde.kimpanel org.kde.plasma.calculator org.kde.plasma.comic org.kde.plasma.fuzzyclock org.kde.plasma.notes org.kde.plasma.quickshare org.kde.plasma.systemloadviewer org.kde.plasma.timer org.kde.plasma.showdesktop org.kde.plasma.fifteenpuzzle plasmaboard previewer qalculate qstardict org.kde.plasma.quicklaunch rssnow spellcheck unitconverter org.kde.plasma.userswitcher weather weatherstation webslice; do
	%find_lang plasma_applet_$i
done
%find_lang plasma_packagestructure_comic
for i in CharacterRunner audioplayercontrol browserhistory contacts converterrunner datetime events katesessions konquerorsessions konsolesessions kopete krunner_dictionary mediawiki spellcheckrunner translator youtube; do
	%find_lang plasma_runner_$i
done
cat *.lang >all.lang

%files -f all.lang
%{_sysconfdir}/xdg/comic.knsrc
%{_libdir}/qt5/plugins/kcm_krunner_dictionary.so
%{_libdir}/qt5/plugins/krunner_converter.so
%{_libdir}/qt5/plugins/krunner_dictionary.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_kimpanel.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_comic.so
%{_libdir}/qt5/plugins/krunner_datetime.so
%{_libdir}/qt5/plugins/kcm_krunner_spellcheck.so
%{_libdir}/qt5/plugins/krunner_spellcheck.so
%{_libdir}/qt5/plugins/plasma_comic_krossprovider.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_comic.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_comic.so
%{_libdir}/libexec/kimpanel-ibus-panel
%{_libdir}/libexec/kimpanel-scim-panel
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_konsoleprofiles.so
%{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel
%{_libdir}/qt5/qml/org/kde/plasma/private/notes
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.calculator.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.fuzzyclock.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kimpanel.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.notes.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.systemloadviewer.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.timer.desktop
%{_datadir}/kservices5/plasma-dataengine-kimpanel.desktop
%{_datadir}/kservices5/plasma-dataengine-konsoleprofiles.desktop
%{_datadir}/kservices5/plasma-runner-converter.desktop
%{_datadir}/kservices5/plasma-runner-dictionary.desktop
%{_datadir}/kservices5/plasma-runner-dictionary_config.desktop
%{_datadir}/kservices5/plasma-wallpaper-org.kde.haenau.desktop
%{_datadir}/kservices5/plasma-wallpaper-org.kde.hunyango.desktop
%{_datadir}/kservices5/plasma-runner-spellchecker*.desktop
%{_datadir}/kservices5/plasma-runner-datetime.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.comic.desktop
%{_datadir}/kservices5/plasma-dataengine-comic.desktop
%{_datadir}/kservicetypes5/plasma_comicprovider.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.calculator
%{_datadir}/plasma/plasmoids/org.kde.plasma.fuzzyclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel
%{_datadir}/plasma/plasmoids/org.kde.plasma.comic
%{_datadir}/plasma/plasmoids/org.kde.plasma.konsoleprofiles
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickerdash
%{_datadir}/plasma/services/kimpanel.operations
%{_datadir}/plasma/plasmoids/org.kde.plasma.notes
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemloadviewer
%{_datadir}/plasma/plasmoids/org.kde.plasma.timer
%{_datadir}/plasma/desktoptheme/default/widgets/timer.svgz
%{_datadir}/plasma/desktoptheme/default/icons/quota.svg
%{_datadir}/plasma/services/org.kde.plasma.dataengine.konsoleprofiles.operations
%{_datadir}/plasma/wallpapers/org.kde.haenau
%{_datadir}/plasma/wallpapers/org.kde.hunyango
%{_datadir}/plasma/plasmoids/org.kde.plasma.webbrowser
%{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.fifteenpuzzle
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager
%{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker
%{_datadir}/plasma/plasmoids/org.kde.plasma.diskquota
%{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch
%{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher
%{_datadir}/kwin/tabbox
%{_datadir}/kwin/desktoptabbox
%{_datadir}/kservices5/plasma-runner-audioplayercontrol.desktop
%{_datadir}/kservices5/plasma-runner-audioplayercontrol_config.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.fifteenpuzzle.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.showdesktop.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.webbrowser.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.konsoleprofiles.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kickerdash.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.activitypager.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.colorpicker.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.diskquota.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicklaunch.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.userswitcher.desktop
%{_datadir}/kservices5/kwin/kwin4_desktop_switcher_previews.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_big_icons.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_compact.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_informative.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_present_windows.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_small_icons.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_text.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_thumbnails.desktop
%{_datadir}/icons/hicolor/scalable/apps/fifteenpuzzle.svgz
%{_libdir}/qt5/qml/org/kde/plasma/private/activitypager
%{_libdir}/qt5/qml/org/kde/plasma/private/colorpicker
%{_libdir}/qt5/qml/org/kde/plasma/private/diskquota
%{_libdir}/qt5/qml/org/kde/plasma/private/quicklaunch
%{_libdir}/qt5/qml/org/kde/plasma/private/showdesktop
%{_libdir}/qt5/qml/org/kde/plasma/private/fifteenpuzzle
%{_libdir}/qt5/qml/org/kde/plasma/private/timer
%{_libdir}/qt5/plugins/kcm_krunner_audioplayercontrol.so
%{_libdir}/qt5/plugins/krunner_audioplayercontrol.so
