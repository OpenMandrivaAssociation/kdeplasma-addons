Name: kdeplasma-addons
Summary: kdeplasma is a compilation of plasma items ( runners, applets, plasmoids ) for kde4
Version: 4.2.1
Release: %mkrel 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeplasma-addons-%version.tar.bz2
Patch0:    kdeplasma-addons-4.2.0-fix-qt45.patch
Buildroot: %_tmppath/%name-%version-%release-root
BuildRequires: qt4-devel
BuildRequires: kde4-macros
BuildRequires: X11-devel
BuildRequires: kdebase4-devel >= 4.0.83
BuildRequires: kdepimlibs4-devel >= 4.0.83
BuildRequires: kdebase4-workspace-devel >= 4.0.83
#BuildRequires: libzip-devel
BuildRequires: qimageblitz-devel 
BuildRequires: boost-devel
BuildRequires: lm_sensors-devel
BuildRequires: qimageblitz-devel
BuildRequires: python-devel
BuildRequires: kdegraphics4-devel
Provides: kdeplasma
Provides: kdeplasma4 = %version
Obsoletes: kdeplasma4 < 4.0.83
Obsoletes: kdeplayground4-plasma
Obsoletes: kdeplayground4-plasma-devel
Obsoletes: extragear-plasma < 4.0.82
Obsoletes: kdeplasmoids4 <= 4.0.98

Suggests: plasma-applet-filewatcher                                                                                           
Suggests: plasma-applet-notes
Suggests: plasma-applet-bluemarble
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
Suggests: plasma-desktoptheme-default
Suggests: plasma-applet-twitter
Suggests: plasma-applet-nowplaying
Suggests: plasma-applet-binaryclock
Suggests: plasma-applet-dict
Suggests: plasma-applet-fuzzy-clock
Suggests: plasma-applet-frame
Suggests: plasma-applet-showdashboard
Suggests: plasma-applet-calculator
Suggests: plasma-applet-fifteenpuzzle
Suggests: plasma-applet-kolourpicker
Suggests: plasma-dataengine-comic
Suggests: plasma-dataengine-twitter
Suggests: plasma-runner-converter
Suggests: plasma-runner-contacts
Suggests: plasma-applet-weatherstation
Suggests: plasma-applet-news
Suggests: plasma-applet-charselect
Suggests: plasma-applet-eyes
Suggests: plasma-applet-paste
Suggests: plasma-applet-timer
Suggests: plasma-runner-konquerorsessions
Suggests: plasma-runner-katesessions
Suggests: plasma-runner-konsolesessions
Suggests: plasma-runner-browserhistory
Suggests: plasma-runner-spellchecker

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
%_kde_datadir/config/comic.knsrc
%_kde_datadir/kde4/services/plasma-packagestructure-comic.desktop
%_kde_libdir/kde4/plasma_packagestructure_comic.so
%_kde_datadir/kde4/servicetypes/plasma_comicprovider.desktop

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
%_kde_datadir/kde4/services/plasma-applet-rssnow.desktop
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
%_kde_iconsdir/hicolor/*/apps/*.png
%_kde_datadir/kde4/services/ServiceMenus/preview.desktop
%_kde_datadir/kde4/services/plasma-applet-previewer.desktop


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
%_kde_iconsdir/oxygen/scalable/apps/bball.svgz
%_kde_datadir/kde4/services/plasma-applet-bball.desktop
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
%_kde_datadir/kde4/services/plasma-applet-incomingmsg.desktop
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
%_kde_datadir/kde4/services/plasma-applet-leavenote.desktop

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
%_kde_datadir/kde4/services/plasma-applet-life.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-pastebin
Summary: Pastebin plasma Applet
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-pastebin
plasma-applet-pastebin

%files -n plasma-applet-pastebin
%defattr(-,root,root)
%_kde_datadir/kde4/services/plasma-applet-pastebin.desktop
%_kde_libdir/kde4/plasma_applet_pastebin.so

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
%_kde_datadir/kde4/services/plasma-applet-lancelot-launcher.desktop
%_kde_datadir/dbus-1/services/org.kde.lancelot.service
%_kde_iconsdir/hicolor/*/apps/lancelot*.png
%_kde_datadir/kde4/services/plasma-applet-lancelot-part.desktop
%_kde_datadir/mime/packages/lancelotpart-mime.xml
%_kde_appsdir/desktoptheme/default/lancelot
%_kde_appsdir/desktoptheme/Elegance
%_kde_appsdir/desktoptheme/Silicon
%_kde_appsdir/desktoptheme/slim-glow
%_kde_appsdir/desktoptheme/Aya
%_kde_appsdir/desktoptheme/heron

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
%_kde_appsdir/desktoptheme/default/stylesheets/news.css
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
%_kde_datadir/kde4/services/plasma-runner-contacts.desktop

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
%_kde_datadir/kde4/services/plasma-applet-weatherstation.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-news
Summary: Plasma applet news
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-news
Plasma applet news

%files -n plasma-applet-news
%defattr(-,root,root)
%_kde_datadir/kde4/services/plasma-applet-news.desktop
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
%_kde_datadir/kde4/services/plasma-applet-charselect.desktop
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
%_kde_datadir/kde4/services/plasma-applet-eyes.desktop

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
%_kde_datadir/kde4/services/plasma-applet-paste.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-timer
Summary: Plasma applet timer
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-timer
Plasma applet timer

%files -n plasma-applet-timer
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_timer.so
%_kde_datadir/kde4/services/plasma-applet-timer.desktop

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
%_kde_datadir/kde4/services/konquerorsessions.desktop
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
%_kde_datadir/kde4/services/katesessions.desktop
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
%_kde_datadir/kde4/services/konsolesessions.desktop
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
%_kde_datadir/kde4/services/browserhistory.desktop

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
%_kde_datadir/kde4/services/plasma-runner-spellchecker.desktop
%_kde_datadir/kde4/services/plasma-runner-spellchecker_config.desktop
%_kde_libdir/kde4/krunner_spellcheckrunner.so
%_kde_libdir/kde4/kcm_krunner_spellcheck.so

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

%define plasmaconverter_major 4
%define libplasmaconverter %mklibname plasmaconverter %plasmaconverter_major

%package -n %libplasmaconverter
Summary: %name library
Group: System/Libraries

%description -n %libplasmaconverter
%name library.

%post -n %libplasmaconverter -p /sbin/ldconfig
%postun -n %libplasmaconverter -p /sbin/ldconfig

%files -n %libplasmaconverter
%defattr(-,root,root,-)
%_kde_libdir/libplasmaconverter.so.%{plasmaconverter_major}*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: %libplasmaconverter
Requires: %libplasmacomicprovidercore
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
%setup -q
%patch0 -p0

%build
%cmake_kde4 
%make

%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

