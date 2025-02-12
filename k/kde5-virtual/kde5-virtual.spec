%ifarch %not_qt5_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name: kde5-virtual
Version: 5.28.4
Release: alt1

Group: Graphical desktop/KDE
Summary: Virtual packages for KDE 5
Url: https://www.altlinux.org/
License: Public Domain

#BuildArch: noarch

BuildRequires(pre): rpm-macros-qt5-webengine

%description
%summary

%package -n kde5-network-manager-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy network manager
Provides: kde5-network-manager = %EVR
Provides: kde5-network-manager-dummy = %EVR
Requires: kf5-filesystem
%description -n kde5-network-manager-0-dummy
%summary

%package -n kde5-network-manager-2-etcnet
Group: Graphical desktop/KDE
Summary: /etc/net network manager
Provides: kde5-network-manager = %EVR
Provides: kde5-network-manager-etcnet = %EVR
Requires: kf5-filesystem
Requires: etcnet alterator-net-wifi alterator-net-openvpn alterator-net-pppoe alterator-net-pptp alterator-net-l2tp
%description -n kde5-network-manager-2-etcnet
%summary

%package -n kde5-network-manager-4-nm
Group: Graphical desktop/KDE
Summary: NetworkManager network manager
Provides: kde5-network-manager = %EVR
Provides: kde5-network-manager-nm = %EVR
Requires: kf5-filesystem
Requires: plasma5-nm-maxi
%description -n kde5-network-manager-4-nm
%summary

%package -n kde5-video-player-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy video player
Provides: kde5-video-player = %EVR
Provides: kde5-video-player-dummy = %EVR
Requires: kf5-filesystem
%description -n kde5-video-player-0-dummy
%summary

%package -n kde5-video-player-2-dragon
Group: Graphical desktop/KDE
Summary: Dragon video player
Provides: kde5-video-player = %EVR
Provides: kde5-video-player-dragon = %EVR
Requires: kf5-filesystem
Requires: kde5-dragon
%description -n kde5-video-player-2-dragon
%summary

%package -n kde5-video-player-3-kaffeine
Group: Graphical desktop/KDE
Summary: Kaffeine video player
Provides: kde5-video-player = %EVR
Provides: kde5-video-player-kaffeine = %EVR
Requires: kf5-filesystem
Requires: kde5-kaffeine
%description -n kde5-video-player-3-kaffeine
%summary

%package -n kde5-video-player-4-smplayer
Group: Graphical desktop/KDE
Summary: SMplayer video player
Provides: kde5-video-player = %EVR
Provides: kde5-video-player-smplayer = %EVR
Requires: kf5-filesystem
Requires: kde5-smplayer
%description -n kde5-video-player-4-smplayer
%summary

%package -n kde5-video-player-5-haruna
Group: Graphical desktop/KDE
Summary: Haruna video player
Provides: kde5-video-player = %EVR
Provides: kde5-video-player-haruna = %EVR
Requires: kf5-filesystem
Requires: kde5-haruna
%description -n kde5-video-player-5-haruna
%summary

%package -n kde5-volume-control-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy volume control
Provides: kde5-volume-control = %EVR
Provides: kde5-volume-control-dummy = %EVR
Requires: kf5-filesystem
%description -n kde5-volume-control-0-dummy
%summary

%package -n kde5-volume-control-2-alsa
Group: Graphical desktop/KDE
Summary: Plasma KMix volume control
Provides: kde5-volume-control = %EVR
Provides: kde5-volume-control-kmix = %EVR
Requires: kf5-filesystem
Requires: kde5-kmix
#
Provides: kde5-volume-control-2-kmix = %EVR
Obsoletes: kde5-volume-control-2-kmix < %EVR
%description -n kde5-volume-control-2-alsa
%summary

%package -n kde5-volume-control-7-pipewire
Group: Graphical desktop/KDE
Summary: Plasma PipeWire volume control
Provides: kde5-volume-control = %EVR
Provides: kde5-volume-control-pipewire = %EVR
Requires: kf5-filesystem
Requires: plasma5-pa
Requires: pipewire pipewire-utils wireplumber
#
Provides: kde5-volume-control-4-pipewire = %EVR
Obsoletes: kde5-volume-control-4-pipewire < %EVR
%description -n kde5-volume-control-7-pipewire
%summary

%package -n kde5-volume-control-6-pulseaudio
Group: Graphical desktop/KDE
Summary: Plasma PulseAudio volume control
Provides: kde5-volume-control = %EVR
Provides: kde5-volume-control-pulseaudio = %EVR
Requires: kf5-filesystem
Requires: plasma5-pa
Requires: pulseaudio-daemon
#
Provides: kde5-volume-control-4-plasmapulse = %EVR
Obsoletes: kde5-volume-control-4-plasmapulse < %EVR
%description -n kde5-volume-control-6-pulseaudio
%summary

%package -n kde5-email-client-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy email client
Provides: kde5-email-client = %EVR
Provides: kde5-email-client-dummy = %EVR
Requires: kf5-filesystem
%description -n kde5-email-client-0-dummy
%summary

%package -n kde5-email-client-2-kmail
Group: Graphical desktop/KDE
Summary: KMail email client
Provides: kde5-email-client = %EVR
Provides: kde5-email-client-kmail = %EVR
Requires: kf5-filesystem
Requires: kde5-kmail kde5-pim-addons-kmail kde5-pim-addons-plugins bogofilter bogofilter-utils
Requires: kde5-akonadi-import-wizard kde5-kmail-account-wizard kde5-mbox-importer kde5-pim-sieve-editor
Requires: kde5-grantlee-editor
%description -n kde5-email-client-2-kmail
%summary

%package -n kde5-email-client-4-thunderbird
Group: Graphical desktop/KDE
Summary: Thunderbird email client
Provides: kde5-email-client = %EVR
Provides: kde5-email-client-thunderbird = %EVR
Requires: kf5-filesystem
Requires: thunderbird thunderbird-ru thunderbird-lightning-ru
#Requires: thunderbird-enigmail http://bugs.altlinux.org/36447
%description -n kde5-email-client-4-thunderbird
%summary

%package -n kde5-audio-player-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy audio player
Provides: kde5-audio-player = %EVR
Provides: kde5-audio-player-dummy = %EVR
Requires: kf5-filesystem
%description -n kde5-audio-player-0-dummy
%summary

%package -n kde5-audio-player-2-elisa
Group: Graphical desktop/KDE
Summary: Elisa audio player
Provides: kde5-audio-player = %EVR
Provides: kde5-audio-player-elisa = %EVR
Requires: kf5-filesystem
Requires: kde5-elisa
%description -n kde5-audio-player-2-elisa
%summary

%package -n kde5-audio-player-4-qmmp
Group: Graphical desktop/KDE
Summary: QMMP audio player
Provides: kde5-audio-player = %EVR
Provides: kde5-audio-player-qmmp = %EVR
Requires: kf5-filesystem
Requires: qmmp1
%description -n kde5-audio-player-4-qmmp
%summary

%package -n kde5-messenger-client-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy messaging client
Provides: kde5-messenger-client = %EVR
Provides: kde5-messenger-client-dummy = %EVR
Requires: kf5-filesystem
%description -n kde5-messenger-client-0-dummy
%summary

%package -n kde5-messenger-client-2-kopete
Group: Graphical desktop/KDE
Summary: Kopete messaging client
Provides: kde5-messenger-client = %EVR
Provides: kde5-messenger-client-kopete = %EVR
Requires: kf5-filesystem
Requires: kde5-kopete
%description -n kde5-messenger-client-2-kopete
%summary

%package -n kde5-messenger-client-6-mix
Group: Graphical desktop/KDE
Summary: Mixed messaging client
Provides: kde5-messenger-client = %EVR
Provides: kde5-messenger-client-mix = %EVR
Requires: kf5-filesystem
#Requires: choqok
#Requires: jami
#Requires: kde5-konversation
%ifnarch armh ppc64le aarch64
#Requires: telegram-desktop
%endif
Requires: psi-plus psi-plus-l10n psi-plus-plugin-autoreply psi-plus-plugin-cleaner psi-plus-plugin-conferencelogger psi-plus-plugin-contentdownloader
Requires: psi-plus-plugin-enummessages psi-plus-plugin-historykeeper psi-plus-plugin-image psi-plus-plugin-imagepreview psi-plus-plugin-messagefilter
Requires: psi-plus-plugin-otr psi-plus-plugin-stopspam psi-plus-plugin-storagenotes
%description -n kde5-messenger-client-6-mix
%summary

%package -n kde5-display-manager-0-dummy
Group: Graphical desktop/KDE
Summary:  Dummy Display Manager collective package
Provides: kde5-display-manager = %EVR
Provides: kde5-display-manager-dummy = %EVR
Requires: kf5-filesystem
%description -n kde5-display-manager-0-dummy
%summary

%package -n kde5-display-manager-7-lightdm
Group: Graphical desktop/KDE
Summary:  LightDM Display Manager collective package
Provides: kde5-display-manager = %EVR
Provides: kde5-display-manager-lightdm = %EVR
Requires: kf5-filesystem
Requires: lightdm-kde-greeter dm-tool
Provides: kde5-display-manager-4-lightdm = %EVR
Obsoletes: kde5-display-manager-4-lightdm < %EVR
%description -n kde5-display-manager-7-lightdm
%summary

%package -n kde5-display-manager-6-lightdmgtk
Group: Graphical desktop/KDE
Summary:  LightDM Display Manager collective package
Provides: kde5-display-manager = %EVR
Provides: kde5-display-manager-lightdmgtk = %EVR
Requires: kf5-filesystem
Requires: lightdm-gtk-greeter lightdm-gtk-greeter-settings dm-tool
%description -n kde5-display-manager-6-lightdmgtk
%summary

%package -n kde5-display-manager-5-sddm
Group: Graphical desktop/KDE
Summary: SDDM Display Manager collective package
Provides: kde5-display-manager-2-sddm = %EVR
Obsoletes: kde5-display-manager-2-sddm < %EVR
Provides: kde5-display-manager = %EVR
Provides: kde5-display-manager-sddm = %EVR
Requires: kf5-filesystem
Requires: sddm sddm-theme-breeze plasma5-sddm-kcm dm-tool
%description -n kde5-display-manager-5-sddm
%summary

%files -n kde5-network-manager-0-dummy
%files -n kde5-network-manager-2-etcnet
%files -n kde5-network-manager-4-nm

%files -n kde5-video-player-0-dummy
%files -n kde5-video-player-2-dragon
%files -n kde5-video-player-3-kaffeine
%files -n kde5-video-player-4-smplayer
%files -n kde5-video-player-5-haruna

%files -n kde5-volume-control-0-dummy
%files -n kde5-volume-control-2-alsa
%files -n kde5-volume-control-6-pulseaudio
%files -n kde5-volume-control-7-pipewire

%files -n kde5-email-client-0-dummy
%if_enabled qtwebengine
%files -n kde5-email-client-2-kmail
%endif
%ifnarch armh
%files -n kde5-email-client-4-thunderbird
%endif

%files -n kde5-audio-player-0-dummy
%files -n kde5-audio-player-2-elisa
%files -n kde5-audio-player-4-qmmp

%files -n kde5-messenger-client-0-dummy
%files -n kde5-messenger-client-2-kopete
%files -n kde5-messenger-client-6-mix

%files -n kde5-display-manager-0-dummy
%files -n kde5-display-manager-5-sddm
%files -n kde5-display-manager-6-lightdmgtk
%files -n kde5-display-manager-7-lightdm

%changelog
* Thu Jul 18 2024 Sergey V Turchin <zerg@altlinux.org> 5.28.4-alt1
- add kde5-display-manager-lightdmgtk

* Wed Jul 17 2024 Sergey V Turchin <zerg@altlinux.org> 5.28.3-alt2
- fix description

* Tue Feb 20 2024 Sergey V Turchin <zerg@altlinux.org> 5.28.3-alt1
- increase kde5-volume-control-pipewire priority over pulseaudio

* Fri Dec 29 2023 Sergey V Turchin <zerg@altlinux.org> 5.28.2-alt1
- update pipewire requires

* Mon Dec 25 2023 Sergey V Turchin <zerg@altlinux.org> 5.28.1-alt1
- update pipewire requires

* Fri Oct 20 2023 Sergey V Turchin <zerg@altlinux.org> 5.28.0-alt2
- add url to package info

* Thu Oct 19 2023 Sergey V Turchin <zerg@altlinux.org> 5.28.0-alt1
- exclude telepathy

* Fri May 26 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt1
- set lightdm by default

* Thu Jan 26 2023 Sergey V Turchin <zerg@altlinux.org> 5.25.0-alt1
- add kde5-volume-control-pipewire

* Thu Jul 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.0-alt1
- require dm-tool for display-manager

* Wed Apr 06 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.1-alt1
- add kde5-video-player-haruna

* Mon Feb 21 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.0-alt2
- using not_qt5_qtwebengine_arches macro

* Mon Feb 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.0-alt1
- update requires

* Wed Nov 03 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.0-alt1
- use lightdm-kde-greeter for lightdm

* Thu Aug 26 2021 Andrey Cherepanov <cas@altlinux.org> 5.21.5-alt1.1
- NMU: thunderbird is built for pc64le, but not for armh

* Wed Jul 21 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.5-alt1
- drop all requires from kde5-messenger-client-mix exept psi-plus

* Wed May 12 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.4-alt1
- don't require thunderbird on ppc64le

* Fri Apr 23 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.3-alt1
- requires sddm-theme-breeze for kde5-display-manager-sddm

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.2-alt1
- add requires for lightdm-gtk-greeter-settings

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.1-alt1
- don't prefer lightdm over sddm

* Mon Apr 05 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.0-alt1
- add virtual kde5-display-manager

* Tue Feb 16 2021 Sergey V Turchin <zerg@altlinux.org> 5.20.1-alt1
- add konversation to kde5-messenger-client-mix

* Tue Nov 24 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.0-alt2
- change requires from psi to psi-plus

* Fri Nov 20 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.0-alt1
- add kde5-messenger-client-mix

* Mon Apr 20 2020 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- update kmail requires

* Fri Mar 20 2020 Sergey V Turchin <zerg@altlinux.org> 5.16.0-alt1
- add kde5-audio-player-elisa

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- add kde5-messenger-client

* Thu Apr 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- remove thunderbird-enigmail requires (http://bugs.altlinux.org/36447)

* Tue Mar 26 2019 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- add enigmail to thunderbird

* Mon Mar 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- update Plasma requires

* Thu Mar 23 2017 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- update kmail requires

* Tue Jul 05 2016 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt2
- fix requires

* Tue Jul 05 2016 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- add dummies for all alternatives
- add kaffeine video player

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- update requires

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- add kde5-audio-player

* Fri Apr 22 2016 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt1
- add kde5-volume-control and kde5-email-client

* Fri Apr 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- add kde5-video-player

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt1
- fix requires

* Mon Mar 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- initial build
