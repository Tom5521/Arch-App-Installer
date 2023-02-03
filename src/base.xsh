#!/usr/bin/env xonsh

import sys
sys.path.insert(0, "src/")
import time
import palabras
def add_repos():
    while True:
        clear
        palabras.repositorios()
        print("Seleccione repos a instalar\n1:Repositorio endeavour OS\n2:Chaotic-AUR\n0:Atras")
        pregunta_repos = str(input(":"))
        if "1" in pregunta_repos: #Endeavour repo
            clear
            sudo pacman-key --keyserver keyserver.ubuntu.com -r 003DB8B0CB23504F
            sudo pacman-key --lsign 003DB8B0CB23504F
            clear
            sudo echo "[endeavouros]" >> /etc/pacman.conf
            sudo echo "SigLevel = PackageRequired" >> /etc/pacman.conf
            sudo echo "Include = /etc/pacman.d/endeavouros-mirrorlist" >> /etc/pacman.conf
            sudo cp src/endeavouros-mirrorlist /etc/pacman.d/
            clear
            sudo pacman -Sy
            clear
            echo Exito!
        if "2" in pregunta_repos: #Chaotic-AUR
            sudo pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com
            sudo pacman-key --lsign-key FBA220DFC880C036
            sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'
            clear
            sudo pacman -Sy
            clear
            sudo echo "[chaotic-aur]" >> /etc/pacman.conf
            sudo echo "Include = /etc/pacman.d/chaotic-mirrorlist" >> /etc/pacman.conf
            sudo pacman -Syy
            clear
        if pregunta_repos == "0":
            break

def yay_install():
    clear
    cd /tmp
    git clone https://aur.archlinux.org/yay.git
    clear
    cd yay
    makepkg --needed --noconfirm -si
    clear
    cd ~

def dependenciasG():
    clear
    echo Instalando dependencias para gaming...
    yay --noconfirm -S wine mangohud game-devices-udev gamemode linux-xanmod linux-xanmod-headers vulkan-icd-loader lib32-vulkan-icd-loader lib32-vulkan-intel vulkan-intel vkd3d lib32-vkd3d
    clear
    yes | yay
    clear

def el_resto():
    clear
    yay --noconfirm -S mkinitcpio-firmware python-lsp-server
    clear
    yay -Syu --noconfirm
    clear

def apps_desarrollo():
    while True:
        clear
        palabras.apps()
        print("Escoje una categoria de apps a instalar\n1:Internet\n2:Imagen y Video\n3:Desarrollo\n4:Gaming\n5:Musica\n6:Oficina\n0:Salir")
        apre = str(input(":"))
        if "1" in apre: #Internet
            clear
            palabras.internet()
            print("Escoje una Categoria\n1:Navegador\n2:Email\n3:Mensajeria\n0:Atras")
            apre1 = str(input(":"))
            if "1" in apre1: #Navegador
                clear
                palabras.navegadores()
                print("1:Firefox\n2:Chromium\n3:Opera\n4:Brave\n5:Chrome\n6:Tor\n0:Cancelar")
                pregunta_navegador = str(input(":"))
                if "1" in pregunta_navegador: #Firefox
                    clear
                    sudo pacman -S firefox --noconfirm
                if "2" in pregunta_navegador: #Chromium
                    clear
                    sudo pacman -S chromium --noconfirm
                if "3" in pregunta_navegador: #Opera
                    clear
                    sudo pacman -S opera --noconfirm
                if "4" in pregunta_navegador: #Brave
                    clear
                    cd /tmp
                    git clone https://aur.archlinux.org/brave.git
                    clear
                    cd brave
                    makepkg -si --noconfirm
                    clear
                    cd ~
                if "5" in pregunta_navegador: #Chrome
                    clear
                    cd /tmp
                    git clone https://aur.archlinux.org/google-chrome.git
                    clear
                    cd google-chrome
                    makepkg -si --noconfirm
                    clear
                    cd ~
                if "6" in pregunta_navegador: #Tor
                    clear
                    sudo pacman -S tor --noconfirm
                if "0" in pregunta_navegador: #Cancelar
                    pass
            if "2" in apre1: #Correo
                clear
                palabras.mail()
                print("Seleciona la o las apps que quieres instalar\n1:Thunderbird\n2:Mailspring\n3:Kmail\n0:Atras")
                pregunta_correo = str(input(":"))
                if "1" in pregunta_correo: #Thunderbird
                    clear
                    sudo pacman -S thunderbird --noconfirm
                if "2" in pregunta_correo: #Mailspring
                    cd /tmp
                    clear
                    git clone https://aur.archlinux.org/mailspring.git
                    clear
                    cd mailspring
                    makepkg -si --noconfirm
                    clear
                    cd ~
                if "3" in pregunta_correo: #Kmail
                    clear
                    sudo pacman -S kmail --noconfirm
                if "0" in pregunta_correo: #Atras
                    pass
            if "3" in apre1: #Mensajeria
                clear
                palabras.mensajeria()
                print("Elige lo que quieres instalar:\n1:Discord\n2:Skype\n3:Teamspeak\n4:Telegram\n5:Zoom\n0:Atras")
                pregunta_mensajes = str(input(":"))
                if "1" in pregunta_mensajes: #Discord
                    clear
                    sudo pacman -S discord --noconfirm
                if "2" in pregunta_mensajes: #Skype
                    cd /tmp
                    clear
                    git clone https://aur.archlinux.org/skypeforlinux-stable-bin.git
                    cd skypeforlinux-stable-bin
                    clear
                    makepkg -si --noconfirm
                    clear
                    cd ~
                if "3" in pregunta_mensajes: #Teamspeak
                    clear
                    sudo pacman -S teamspeak3 --noconfirm
                if "4" in pregunta_mensajes: #Telegram
                    clear
                    sudo pacman -S telegram-desktop --noconfirm
                if "5" in pregunta_mensajes: #Zoom
                    clear
                    cd /tmp
                    git clone https://aur.archlinux.org/zoom.git
                    clear
                    cd zoom
                    makepkg -si --noconfirm
                    cd ~
                    clear
                if "0" in pregunta_mensajes: #Atras
                    pass
            if "0" in apre1: #Atras
                pass
        if "2" in apre: #Imagen y video
            clear
            palabras.imagen_y_video()
            print("Selecciona que instalar\n1:vlc\n2:mpv\n3:gthumb\n4:gimp\n5:krita\n6:kdenlive\n7:Netflix\n8:Obs-Studio\n0:Atras")
            pregunta_video = str(input(":"))
            if "1" in pregunta_video: #vlc
                clear
                sudo pacman -S vlc --noconfirm
            if "2" in pregunta_video: #mpv
                clear
                sudo pacman -S mpv --noconfirm
            if "3" in pregunta_video: #gthumb
                clear
                sudo pacman -S gthumb --noconfirm
            if "4" in pregunta_video: #gimp
                clear
                sudo pacman -S gimp --noconfirm
            if "5" in pregunta_video: #krita
                clear
                sudo pacman -S krita --noconfirm
            if "6" in pregunta_video: #kdenlive
                clear
                sudo pacman -S kdenlive --noconfirm
            if "7" in pregunta_video: #Netfilx
                cd /tmp
                clear
                git clone https://aur.archlinux.org/netflix-nativefier.git
                clear
                cd netflix-nativefier
                makepkg -si --noconfirm
                clear
            if "8" in pregunta_video: #Obs-studio
                clear
                sudo pacman -S obs-studio --noconfirm
            if "0" in pregunta_video: #Atras
                pass
        if "3" in apre: #Desarrollo
            while True:
                clear
                palabras.desarrollo()
                print("Apps de desarrollo\nElige que apps instalar\n1:VS code\n2:Code OSS\n3:Pycharm Comunity\n4:Eclipse-Java\n5:Kate\n6:Freecad\n7:Android Studio\n8:Anbox\n9:Github-cli\n10:Github-Desktop\n0:Atras")
                pregunta_ide = str(input(":"))
                if "1" in pregunta_ide: #VS Code
                    if pregunta_ide == "10":
                        pass
                    else:
                        cd /tmp
                        clear
                        git clone https://aur.archlinux.org/visual-studio-code-bin.git
                        cd visual-studio-code-bin
                        clear
                        makepkg -si --noconfirm
                        clear
                        cd ~
                if "2" in pregunta_ide: #Code OSS
                    clear
                    sudo pacman -S code --noconfirm
                if "3" in pregunta_ide: #Pycharm Comunity
                    clear
                    sudo pacman -S pycharm-community-edition --noconfirm
                if "4" in pregunta_ide: #Eclipse-Java
                    clear
                    cd /tmp
                    git clone https://aur.archlinux.org/eclipse-java.git
                    clear
                    cd eclipse-java
                    makepkg -si --noconfirm
                    cd ~
                if "5" in pregunta_ide: #Kate
                    clear
                    sudo pacman -S kate --noconfirm
                if "6" in pregunta_ide: #Freecad
                    clear
                    sudo pacman -S freecad --noconfirm
                if "7" in pregunta_ide: #Android Studio
                    cd /tmp
                    clear
                    git clone https://aur.archlinux.org/android-studio.git
                    cd android-studio
                    clear
                    makepkg -si --noconfirm
                    cd ~
                    clear
                if "8" in pregunta_ide: #Anbox
                    cd /tmp
                    clear
                    git clone https://aur.archlinux.org/anbox-git.git
                    clear
                    cd anbox-git
                    makepkg -si --noconfirm
                    clear
                    cd ~
                if "9" in pregunta_ide: #Github Cli
                    clear
                    sudo pacman -S github-cli --noconfirm
                if "10" in pregunta_ide:
                    if pregunta_ide == "1" and "0":
                        pass
                    else:   
                        clear
                        cd /tmp
                        git clone https://aur.archlinux.org/github-desktop.git
                        clear
                        cd github-desktop
                        makepkg -si --noconfirm
                        clear
                        cd ~
                if pregunta_ide == "0": #Atras
                    break
        if "4" in apre: #Gaming
            clear
            palabras.gaming()
            print("Escoje que instalar\n1:Steam\n2:Lutris\n3:Wine\n4:proton-ge\n5:Play on Linux\n6:Mindustry\n7:Drivers\n0:Atras")
            pregunta_juegos = str(input(":"))
            if "1" in pregunta_juegos: #Steam
                clear
                sudo pacman -S steam --noconfirm
            if "2" in pregunta_juegos: #Lutris
                clear
                sudo pacman -S lutris --
            if "3" in pregunta_juegos: #Wine
                clear
                sudo pacman -S wine --noconfirm
            if "4" in pregunta_juegos: #Proton-ge-custom-bin
                cd /tmp
                clear
                git clone https://aur.archlinux.org/proton-ge-custom-bin.git
                cd proton-ge-custom-
                clear
                makepkg -si --noconfirm
                clear
                cd ~
            if "5" in pregunta_juegos: #Play on Linux
                cd /tmp
                clear
                git clone https://aur.archlinux.org/playonlinux.git
                cd playonlinux
                clear
                makepkg -si --noconfirm
                clear
                cd ~
            if "6" in pregunta_juegos: #Mindustry
                clear
                cd /tmp
                git clone https://aur.archlinux.org/mindustry-bin.git
                cd mindustry-bin
                clear
                makepkg -si --noconfirm
                clear
            if "7" in pregunta_juegos: #Drivers
                clear
                dependencias_desarrollo()
            if "0" in pregunta_juegos: #Atras
                pass
            clear
        if "5" in apre: #Musica
            clear
            palabras.musica()
            print("Seleciona una o mas opciones\n1:Spotify\n2:Spotify-Adblock\n3:Spotube\n4:Clementine\n5:YT Music\n6:Audacity\n0:Atras")
            pregunta_musica = str(input(":"))
            if "1" in pregunta_musica: #Spotify
                clear
                sudo pacman -S spotify-launcher --noconfirm
            if "2" in pregunta_musica: #Spotify Adblock
                cd /tmp
                clear
                git clone https://aur.archlinux.org/spotify-adblock.git
                cd spotify-adblock
                clear
                makepkg -si --noconfirm
                clear
            if "3" in pregunta_musica: #Spotube
                cd /tmp
                clear
                git clone https://aur.archlinux.org/spotube-bin.git
                cd spotube-bin
                clear
                makepkg -si --noconfirm
                clear
            if "4" in pregunta_musica: #Clementine
                clear
                sudo pacman -S clementine --noconfirm
            if "5" in pregunta_musica: #YT Music
                cd /tmp
                clear
                git clone https://aur.archlinux.org/youtube-music.git
                cd youtube-music
                clear
                makepkg -si --noconfirm
                clear
            if "6" in pregunta_musica: #Audacity
                clear
                sudo pacman -S audacity --noconfirm
            if "0" in pregunta_musica: #Atras
                pass
            clear
        if "6" in apre: #Oficina
            clear
            palabras.oficina()
            print("--OFICINA--\nElige una o mas opciones\n1:LibreOffice\n2:OpenOffice\n3:OnlyOffice\n4:WPS Office\n0:Atras")
            pregunta_oficina = str(input(":"))
            if "1" in pregunta_oficina:
                clear
                sudo pacman -S libreoffice --noconfirm
            if "2" in pregunta_oficina:
                cd /tmp
                clear
                git clone https://aur.archlinux.org/openoffice-bin.git
                cd openoffice-bin
                clear
                makepkg -si --noconfirm
                cd ~
            if "3" in pregunta_oficina:
                cd /tmp
                clear
                git clone https://aur.archlinux.org/onlyoffice-bin.git
                cd onlyoffice-bin
                clear
                makepkg -si --noconfirm
                cd ~
            if "4" in pregunta_oficina:
                cd /tmp
                clear
                git clone https://aur.archlinux.org/wps-office-all-dicts-win-languages.git
                cd wps-office-all-dicts-win-languages
                clear
                makepkg -si --noconfirm
                cd ~
            if "0" in pregunta_oficina:
                pass
        if "0" in apre: #Salir
            clear
            print("Saliendo...")
            time.sleep(0.1)
            break

def cambiar_shell():
    clear
    palabras.cambiar_shell()
    print("1:fish\n2:zsh\n3:bash\n0:Atras")
    shellpre = int(input("Que shell deseas poner?\n:"))
    if shellpre == 1: #Shell fish
        clear
        sudo pacman -S fish --noconfirm
        clear
        chsh -s /bin/fish
        clear
    if shellpre == 2: #Shell zsh
        clear
        sudo pacman -S zsh --noconfirm
        clear
        chsh -s /bin/zsh
        clear
    if shellpre == 3: #Shell Bash
        clear
        sudo pacman -S bash --noconfirm
        clear
        chsh -s /bin/bash
        clear
    if shellpre == 0:
        pass
    clear

def snapd_inst():
    clear
    pr1 = int(input("Quieres descargar el paquete por...?\n1=yay(debe estar instalado)\n2=git clone\n:"))
    if pr1 == 1:
        clear
        yay --noconfirm -S snapd
        clear
        sudo systemctl enable --now snapd.socket
        sudo ln -s /var/lib/snapd/snap /snap
        sudo systemctl enable --now snapd.apparmor
        sudo apparmor_parser -r /etc/apparmor.d/*snap-confine*
        sudo apparmor_parser -r /var/lib/snapd/apparmor/profiles/snap confine*
        clear
        print("\nListo!\n")
    if pr1 == 2:
        clear
        cd /tmp
        git clone https://aur.archlinux.org/snapd.git
        cd snapd
        makepkg --noconfirm -si
        clear
        sudo systemctl enable --now snapd.socket
        sudo ln -s /var/lib/snapd/snap /snap
        sudo systemctl enable --now snapd.apparmor
        sudo apparmor_parser -r /etc/apparmor.d/*snap-confine*
        sudo apparmor_parser -r /var/lib/snapd/apparmor/profiles/snap confine*
        clear
        cd ~
        clear
        print("\nListo!\n")
    if pr1 < 2:
        clear
        print("Selecciona Correctamente")
        time.sleep(0.5)

def pkgman():
    clear
    palabras.gestores_de_paquetes()
    print("1:yay\n2:paru\n3:pikaur\n4:snapd\n5:flatpak\n6:Pamac\n0:Cancelar")
    pkgpre1 = str(input(":"))
    if "1" in pkgpre1: #Yay
        print("Instalar yay atravez de...\n1:Repositorio chaotic(Requiere añadirlo en la seccion de repos nesesarios)\n2:git clone(lento))")
        yayprk = int(input(":"))
        if yayprk == 1:
            print("Añadir repo chaotic?(Y-N)")
            add_repoch = str(input(":"))
            if add_repoch == "Y" or "y":
                sudo sh repos/add-repo-ch.sh
                clear
                sudo pacman -S yay --noconfirm
                clear
                yay_rem = False
            if add_repoch == "N" or "n":
                yay_rem = False
                clear
                yay_install()
            else:
                clear
                print("No se seleciono ninguno")
                time.sleep(0.5)
                pass
        clear
    if "2" in pkgpre1: #Paru
        clear
        cd /tmp
        git clone https://aur.archlinux.org/paru.git
        clear
        cd paru
        makepkg --needed --noconfirm -si
        clear
        cd ~
    if "3" in pkgpre1: #Pikaur
        clear
        cd /tmp
        git clone https://aur.archlinux.org/pikaur.git
        clear
        cd pikaur
        makepkg -si --needed --noconfirm
        cd ~
        clear
    if "4" in pkgpre1: #Snapd
        snapd_inst()
    if "5" in pkgpre1: #Flatpak
        clear
        sudo pacman -S flatpak --noconfirm
        clear
    if "6" in pkgpre1: #Pamac
        clear
        palabras.pamac()
        print("1:Instalar pamac AUR\n2:Instalar pamac Flatpak\n3:Instalar pamac nosnap\n0:Cancelar")
        pamac_pre1 = int(input(":"))
        if pamac_pre1 == 1: #pamac-aur
            clear
            cd /tmp
            git clone https://aur.archlinux.org/pamac-aur.git
            cd pamac-aur
            clear
            makepkg -si --needed --noconfirm
            cd ~
            clear
        if pamac_pre1 == 2: #pamac-flatpak
            clear
            cd /tmp
            git clone https://aur.archlinux.org/pamac-flatpak.git
            cd pamac-flatpak
            clear
            makepkg -si --needed --noconfirm
            cd ~
            clear
        if pamac_pre1 == 3: #pamac-nosnap
            clear
            cd /tmp
            git clone https://aur.archlinux.org/pamac-nosnap.git
            cd pamac-nosnap
            clear
            makepkg -si --needed --noconfirm
        if pamac_pre1 == 0: #Salida
            clear
            pass
        if pamac_pre1 > 3: #Error
            clear
            print("Selecciona solo una opcion")
            time.sleep(0.5)
            clear
        if "0" in pkgpre1: #Cancelar
            pass

def escritorios():
    clear
    palabras.escritorios_wms()
    print("1:WM's\n2:Escritorios\n0:Atras")
    pregunta_wm = str(input(":"))
    if "1" in pregunta_wm:
        clear
        palabras.wms()
        print("1:i3wm\n2:awesome\n3:icewm\n4:bspwm\n0:Atras")
        pregunta_wm_1 = str(input(":"))
        if "1" in pregunta_wm_1:
            clear
            sudo pacman -S i3 --noconfirm
        if "2" in pregunta_wm_1:
            clear
            sudo pacman -S awesome --noconfirm
        if "3" in pregunta_wm_1:
            clear
            sudo pacman -S icewm --noconfirm
        if "4" in pregunta_wm_1:
            clear
            sudo pacman -S bspwm -- noconfirm
        if "0" in pregunta_wm_1:
            clear
            pass
    if "2" in pregunta_wm:
        clear
        palabras.escritorios()
        print("1:XFCE4\n2:GNOME\n3:KDE Plasma\n4:LXDE\n5:Cinnamon\n6:Mate\n0:Cancelar")
        desk_pre = str(input(":"))
        if "1" in desk_pre: #XFCE4
            clear
            sudo pacman -S xfce4 xfce4-goodies --noconfirm
            clear
        if "2" in desk_pre: #GNOME
            clear
            sudo pacman -S gnome gnome-extra --noconfirm
            clear
        if "3" in desk_pre: #KDE Plasma
            clear
            sudo pacman -S plasma --noconfirm
            clear
        if "4" in desk_pre: #LXDE
            clear
            sudo pacman -S lxde --noconfirm
            clear
        if "5" in desk_pre: #Cinnamon
            clear
            sudo pacman -S cinnamon --noconfirm
            clear
        if "6" in desk_pre: #Mate
            clear
            sudo pacman -S mate --noconfirm
            clear
        if "0" in desk_pre: #Cancelar
            pass
    if "0" in pregunta_wm:
        clear
        pass

def otros():
    while True:
        clear
        palabras.otros()
        print("1:Intalar dependencias i3(requiere yay)\n2:Instalar repos\n3:Instalar Kernels\n0:Atras")
        pregunta_otros = str(input(":"))
        if "1" in pregunta_otros:
            clear
            yay --noconfirm -S - < lista-de-paquetes-i3
            clear
            yay --noconfirm -S gnome-screenshot alsa-utils xscreensaver acpid mousepad-git
            clear
        if "2" in pregunta_otros:
            add_repos()
            clear
        if "3" in pregunta_otros:
            while True:
                clear
                palabras.kernels()
                print("1:Linux\n2:xanmod\n3:zen\n0:Atras")
                pregunta_kernel = str(input(":"))
                if "1" in pregunta_kernel:
                    clear
                    sudo pacman -S linux linux-headers --noconfirm
                if "2" in pregunta_kernel:
                    clear
                    cd /tmp
                    git clone https://aur.archlinux.org/linux-xanmod.git
                    cd linux-xanmod
                    clear
                    makepkg -si --noconfirm
                    clear
                    cd ~
                if "3" in pregunta_kernel:
                    clear
                    sudo pacman -S linux-zen linux-zen-headers --noconfirm
                if "0" in pregunta_kernel:
                    break
        if "0" in pregunta_otros:
            break

def borrar_basura():
    clear
    palabras.borrar_basura()
    print("Elige una o mas opciones\n1:Escriba los paquetes que quiere eliminar seguidos de un salto de linea\n2:Borrado automatico\n0:Atras")

def dependencias_desarrollo():
    while True:
        clear
        palabras.drivers()
        print("1:Drivers Graficos\n2:Drivers de Sonido\n3:Bluetooth\n0:Atras")
        pregunta_drivers = str(input(":"))
        if "1" in pregunta_drivers:
            while True:
                clear
                palabras.drivers_graficos()
                print("Elige tus especificaciones\n1:Nvidia\n2:Amd\n3:Intel(Open Source)\n0:Atras")
                pregunta_drivers_g = int(input(":"))
                if pregunta_drivers_g == 1: #Nvidia
                    clear
                    palabras.nvidia()
                    print("Elige una vercion\n1:Propietario\n2:Open Source\n0:Atras")
                    pregunta_drivers_nvidia = str(input(":"))
                    if "1" in pregunta_drivers_nvidia:
                        clear
                        cd /tmp
                        git clone https://aur.archlinux.org/nvidia-340xx.git
                        cd nvidia-340xx
                        clear
                        makepkg -si --noconfirm
                        cd ~
                        clear
                    if "2" in pregunta_drivers_nvidia:
                        clear
                        sudo pacman -S nvidia-open --noconfirm 
                if pregunta_drivers_g == 2: #AMD
                    clear
                    palabras.amd()
                    print("Drivers...?\n1:Propietarios\n2:Open Source\n0:Atras")
                    pregunta_drivers_1 = int(input(":"))
                    if pregunta_drivers_1 == 1:
                        clear
                        cd /tmp
                        git clone https://aur.archlinux.org/amdgpu-pro-installer.git
                        cd amdgpu-pro-installer
                        clear
                        makepkg -si --noconfirm
                        clear
                    if pregunta_drivers_1 == 2:
                        clear
                        sudo pacman -S xf86-video-ati xf86-video-amdgpu --noconfirm
                    if pregunta_drivers_1 == 0:
                        clear
                    else:
                        pass
                if pregunta_drivers_g == 3: #Intel
                    clear
                    sudo pacman -S xf86-video-intel --noconfirm
                if pregunta_drivers_g == 0: #Atras
                    clear
                    break
                else:
                    pass
        if "2" in pregunta_drivers:
            clear
            palabras.sonido()
            print("Elige una opcion\n1:Servidores de Audio\n2:Drivers de Sonido\n0:Atras")
            pregunta_drivers_s = str(input(":"))
            if "1" in pregunta_drivers_s:
                while True:
                    clear
                    palabras.servidores_de_audio()
                    print("1:PulseAudio\n2:Pipewire\n0:Atras")
                    pregunta_drivers_s_s = str(input(":"))
                    if "1" in pregunta_drivers_s_s:
                        clear
                        sudo pacman -S pulseaudio --noconfirm
                    if "2" in pregunta_drivers_s_s:
                        clear
                        sudo pacman -S pipewire --noconfirm
                    if "0" in pregunta_drivers_s_s:
                        clear
                        break
            if "2" in pregunta_drivers_s:
                while True:    
                    clear
                    palabras.drivers_de_audio()
                    print("Elige una o mas opciones\n1:ALSA\n2:Jack\n3:Flac\n0:Atras")
                    pregunta_drivers_s_d = str(input(":"))
                    if "1" in pregunta_drivers_s_d:
                        clear
                        sudo pacman -S alsa alsa-firmware --noconfirm
                    if "2" in pregunta_drivers_s_d:
                        clear
                        sudo pacman -S jack2 --noconfirm
                    if "3" in pregunta_drivers_s_d:
                        clear 
                        sudo pacman -S flac --noconfirm
                    if "0" in pregunta_drivers_s_d:
                        break
                    else:
                        pass
            if "0" in pregunta_drivers_s:
                clear
                pass    
        if "3" in pregunta_drivers:
            clear
            sudo pacman -S bluez blueman --noconfirm
            clear
            sudo systemctl enable bluetooth.service
            clear
        if "0" in pregunta_drivers:
            break
        else:
            pass
