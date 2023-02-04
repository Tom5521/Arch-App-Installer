
from time import sleep as sl

import palabras
import pacman
from os import getcwd
from os import chdir
from os import system as sys
current_directory = getcwd()

def installed():
    print("Instalado")
    sl(1)

def clear():
    sys("clear")

def dependencias_desarrollo():
    while True:
        clear()
        palabras.drivers()
        print("1:Drivers Graficos\n2:Drivers de Sonido\n3:Bluetooth\n0:Atras")
        pregunta_drivers = str(input(":"))
        if "1" in pregunta_drivers:
            while True:
                clear()
                palabras.drivers_graficos()
                print("Elige tus especificaciones\n1:Nvidia\n2:Amd\n3:Intel(Open Source)\n0:Atras")
                pregunta_drivers_g = int(input(":"))
                if pregunta_drivers_g == 1: #Nvidia
                    clear()
                    palabras.nvidia()
                    print("Elige una vercion\n1:Propietario\n2:Open Source\n0:Atras")
                    pregunta_drivers_nvidia = str(input(":"))
                    if "1" in pregunta_drivers_nvidia:
                        clear()
                        chdir("/tmp")
                        sys("git clone https://aur.archlinux.org/nvidia-340xx.git")
                        chdir("nvidia-340xx")
                        clear()
                        sys("makepkg -si --noconfirm")
                        chdir(current_directory)
                        clear()
                    if "2" in pregunta_drivers_nvidia:
                        clear()
                        pacman.install("nvidia-open")
                        installed()
                if pregunta_drivers_g == 2: #AMD
                    clear()
                    palabras.amd()
                    print("Drivers...?\n1:Propietarios\n2:Open Source\n0:Atras")
                    pregunta_drivers_1 = int(input(":"))
                    if pregunta_drivers_1 == 1:
                        clear()
                        chdir("/tmp")
                        sys("git clone https://aur.archlinux.org/amdgpu-pro-installer.git")
                        chdir("amdgpu-pro-installer")
                        clear()
                        sys("makepkg -si --noconfirm")
                        clear()
                    if pregunta_drivers_1 == 2:
                        clear()
                        pacman.install(["xf86-video-ati","xf86-video-amdgpu"])
                        installed()
                    if pregunta_drivers_1 == 0:
                        clear()
                    else:
                        pass
                if pregunta_drivers_g == 3: #Intel
                    clear()
                    pacman.install("xf86-video-intel")
                    installed()
                if pregunta_drivers_g == 0: #Atras
                    clear()
                    break
                else:
                    pass
        if "2" in pregunta_drivers:
            clear()
            palabras.sonido()
            print("Elige una opcion\n1:Servidores de Audio\n2:Drivers de Sonido\n0:Atras")
            pregunta_drivers_s = str(input(":"))
            if "1" in pregunta_drivers_s:
                while True:
                    clear()
                    palabras.servidores_de_audio()
                    print("1:PulseAudio\n2:Pipewire\n0:Atras")
                    pregunta_drivers_s_s = str(input(":"))
                    if "1" in pregunta_drivers_s_s:
                        clear()
                        pacman.install("pulseaudio")
                        installed()
                    if "2" in pregunta_drivers_s_s:
                        clear()
                        pacman.install("pipewire")
                        installed()
                    if "0" in pregunta_drivers_s_s:
                        clear()
                        break
            if "2" in pregunta_drivers_s:
                while True:    
                    clear()
                    palabras.drivers_de_audio()
                    print("Elige una o mas opciones\n1:ALSA\n2:Jack\n3:Flac\n0:Atras")
                    pregunta_drivers_s_d = str(input(":"))
                    if "1" in pregunta_drivers_s_d:
                        clear()
                        pacman.install(["alsa","alsa-firmware"])
                        installed()
                    if "2" in pregunta_drivers_s_d:
                        clear()
                        pacman.install("jack2")
                        installed()
                    if "3" in pregunta_drivers_s_d:
                        clear() 
                        pacman.install("flac")
                        installed()
                    if "0" in pregunta_drivers_s_d:
                        break
                    else:
                        pass
            if "0" in pregunta_drivers_s:
                clear()
                pass    
        if "3" in pregunta_drivers:
            clear()
            pacman.install(["bluez","blueman"])
            clear()
            sys("sudo systemctl enable bluetooth.service")
            clear()
            installed()
        if "0" in pregunta_drivers:
            break
        else:
            pass

def add_repos():
    while True:
        clear()
        palabras.repositorios()
        print("Seleccione repos a instalar\n1:Repositorio endeavour OS\n2:Chaotic-AUR\n0:Atras")
        pregunta_repos = str(input(":"))
        if "1" in pregunta_repos: #Endeavour repo
            clear()
            sys("sudo pacman-key --keyserver keyserver.ubuntu.com -r 003DB8B0CB23504F")
            sys("sudo pacman-key --lsign 003DB8B0CB23504F")
            clear()
            sys('sudo echo "[endeavouros]" >> /etc/pacman.conf')
            sys('sudo echo "SigLevel = PackageRequired" >> /etc/pacman.conf')
            sys('sudo echo "Include = /etc/pacman.d/endeavouros-mirrorlist" >> /etc/pacman.conf')
            sys("sudo cp src/endeavouros-mirrorlist /etc/pacman.d/")
            clear()
            pacman.refresh()
            clear()
            sys("echo Exito!")
        if "2" in pregunta_repos: #Chaotic-AUR
            sys("sudo pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com")
            sys("sudo pacman-key --lsign-key FBA220DFC880C036")
            sys("sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'")
            clear()
            pacman.refresh()
            clear()
            sys('sudo echo "[chaotic-aur]" >> /etc/pacman.conf')
            sys('sudo echo "Include = /etc/pacman.d/chaotic-mirrorlist" >> /etc/pacman.conf')
            pacman.refresh()
            clear()
        if pregunta_repos == "0":
            break

def yay_install():
    clear()
    chdir("/tmp")
    sys("git clone https://aur.archlinux.org/yay.git")
    clear()
    chdir("yay")
    sys("makepkg --needed --noconfirm -si")
    sys("clear")
    chdir("~")

def dependenciasG():
    clear()
    sys("yay --noconfirm -S wine mangohud game-devices-udev gamemode linux-xanmod linux-xanmod-headers vulkan-icd-loader lib32-vulkan-icd-loader lib32-vulkan-intel vulkan-intel vkd3d lib32-vkd3d")
    clear()
    pacman.refresh()
    clear()

def el_resto():
    clear()
    sys("yay --noconfirm -S mkinitcpio-firmware python-lsp-server")
    clear()
    sys("yay -Syu --noconfirm")
    clear()

def apps_desarrollo():
    while True:
        clear()
        palabras.apps()
        print("Escoje una categoria de apps a instalar\n1:Internet\n2:Imagen y Video\n3:Desarrollo\n4:Gaming\n5:Musica\n6:Oficina\n0:Salir")
        apre = str(input(":"))
        if "1" in apre: #Internet
            clear()
            palabras.internet()
            print("Escoje una Categoria\n1:Navegador\n2:Email\n3:Mensajeria\n0:Atras")
            apre1 = str(input(":"))
            if "1" in apre1: #Navegador
                clear()
                palabras.navegadores()
                print("1:Firefox\n2:Chromium\n3:Opera\n4:Brave\n5:Chrome\n6:Tor\n0:Cancelar")
                pregunta_navegador = str(input(":"))
                if "1" in pregunta_navegador: #Firefox
                    clear()
                    pacman.install("firefox")
                    installed()
                if "2" in pregunta_navegador: #Chromium
                    clear()
                    pacman.install("chromium")
                    installed()
                if "3" in pregunta_navegador: #Opera
                    clear()
                    pacman.install("opera")
                    installed()
                if "4" in pregunta_navegador: #Brave
                    clear()
                    chdir("/tmp")
                    sys("git clone https://aur.archlinux.org/brave.git")
                    clear()
                    chdir("brave")
                    sys("makepkg -si --noconfirm")
                    clear()
                    chdir(current_directory)
                if "5" in pregunta_navegador: #Chrome
                    clear()
                    chdir("/tmp")
                    sys("git clone https://aur.archlinux.org/google-chrome.git")
                    clear()
                    chdir("google-chrome")
                    sys("makepkg -si --noconfirm")
                    clear()
                    chdir(current_directory)
                if "6" in pregunta_navegador: #Tor
                    clear()
                    pacman.install("tor")
                if "0" in pregunta_navegador: #Cancelar
                    pass
            if "2" in apre1: #Correo
                clear()
                palabras.mail()
                print("Seleciona la o las apps que quieres instalar\n1:Thunderbird\n2:Mailspring\n3:Kmail\n0:Atras")
                pregunta_correo = str(input(":"))
                if "1" in pregunta_correo: #Thunderbird
                    clear()
                    pacman.install("thunderbird")
                    installed()
                if "2" in pregunta_correo: #Mailspring
                    chdir("/tmp")
                    clear()
                    sys("git clone https://aur.archlinux.org/mailspring.git")
                    clear()
                    chdir("mailspring")
                    sys("makepkg -si --noconfirm")
                    clear()
                    chdir(current_directory)
                if "3" in pregunta_correo: #Kmail
                    clear()
                    pacman.install("kmail")
                    installed()
                if "0" in pregunta_correo: #Atras
                    pass
            if "3" in apre1: #Mensajeria
                clear()
                palabras.mensajeria()
                print("Elige lo que quieres instalar:\n1:Discord\n2:Skype\n3:Teamspeak\n4:Telegram\n5:Zoom\n0:Atras")
                pregunta_mensajes = str(input(":"))
                if "1" in pregunta_mensajes: #Discord
                    clear()
                    pacman.install("discord")
                    installed()
                if "2" in pregunta_mensajes: #Skype
                    chdir("/tmp")
                    clear()
                    sys("git clone https://aur.archlinux.org/skypeforlinux-stable-bin.git")
                    chdir("skypeforlinux-stable-bin")
                    clear()
                    sys("makepkg -si --noconfirm")
                    clear()
                    chdir(current_directory)
                if "3" in pregunta_mensajes: #Teamspeak
                    clear()
                    pacman.install("teamspeak3")
                    installed()
                if "4" in pregunta_mensajes: #Telegram
                    clear()
                    pacman.install("telegram-desktop")
                    installed()
                if "5" in pregunta_mensajes: #Zoom
                    clear()
                    chdir("/tmp")
                    sys("git clone https://aur.archlinux.org/zoom.git")
                    clear()
                    chdir("zoom")
                    sys("makepkg -si --noconfirm")
                    chdir(current_directory)
                    clear()
                if "0" in pregunta_mensajes: #Atras
                    pass
            if "0" in apre1: #Atras
                pass
        if "2" in apre: #Imagen y video
            clear()
            palabras.imagen_y_video()
            print("Selecciona que instalar\n1:vlc\n2:mpv\n3:gthumb\n4:gimp\n5:krita\n6:kdenlive\n7:Netflix\n8:Obs-Studio\n0:Atras")
            pregunta_video = str(input(":"))
            if "1" in pregunta_video: #vlc
                clear()
                pacman.install("vlc")
                installed()
            if "2" in pregunta_video: #mpv
                clear()
                pacman.install("mpv")
                installed()
            if "3" in pregunta_video: #gthumb
                clear()
                pacman.install("gthumb")
                installed()
            if "4" in pregunta_video: #gimp
                clear()
                pacman.install("gimp")
                installed()
            if "5" in pregunta_video: #krita
                clear()
                pacman.install("krita")
                installed()
            if "6" in pregunta_video: #kdenlive
                clear()
                pacman.install("kdenlive")
                installed()
            if "7" in pregunta_video: #Netfilx
                chdir("/tmp")
                clear()
                sys("git clone https://aur.archlinux.org/netflix-nativefier.git")
                clear()
                chdir("netflix-nativefier")
                sys("makepkg -si --noconfirm")
                clear()
            if "8" in pregunta_video: #Obs-studio
                clear()
                pacman.install("obs-studio")
                installed()
            if "0" in pregunta_video: #Atras
                pass
        if "3" in apre: #Desarrollo
            while True:
                clear()
                palabras.desarrollo()
                print("Apps de desarrollo\nElige que apps instalar\n1:VS code\n2:Code OSS\n3:Pycharm Comunity\n4:Eclipse-Java\n5:Kate\n6:Freecad\n7:Android Studio\n8:Anbox\n9:Github-cli\n10:Github-Desktop\n0:Atras")
                pregunta_ide = str(input(":"))
                if "1" in pregunta_ide: #VS Code
                    if pregunta_ide == "10":
                        pass
                    else:
                        chdir("/tmp")
                        clear()
                        sys("git clone https://aur.archlinux.org/visual-studio-code-bin.git")
                        chdir("visual-studio-code-bin")
                        clear()
                        sys("makepkg -si --noconfirm")
                        clear()
                        chdir(current_directory)
                if "2" in pregunta_ide: #Code OSS
                    clear()
                    pacman.install("code")
                    installed()
                if "3" in pregunta_ide: #Pycharm Comunity
                    clear()
                    pacman.install("pycharm-community-edition")
                    installed()
                if "4" in pregunta_ide: #Eclipse-Java
                    clear()
                    chdir("/tmp")
                    sys("git clone https://aur.archlinux.org/eclipse-java.git")
                    clear()
                    chdir("eclipse-java")
                    sys("makepkg -si --noconfirm")
                    chdir(current_directory)
                if "5" in pregunta_ide: #Kate
                    clear()
                    pacman.install("kate")
                    installed()
                if "6" in pregunta_ide: #Freecad
                    clear()
                    pacman.install("freecad")
                    installed()
                if "7" in pregunta_ide: #Android Studio
                    chdir("/tmp")
                    clear()
                    sys("git clone https://aur.archlinux.org/android-studio.git")
                    chdir("android-studio")
                    clear()
                    sys("makepkg -si --noconfirm")
                    chdir(current_directory)
                    clear()
                if "8" in pregunta_ide: #Anbox
                    chdir("/tmp")
                    clear()
                    sys("git clone https://aur.archlinux.org/anbox-git.git")
                    clear()
                    chdir("anbox-git")
                    sys("makepkg -si --noconfirm")
                    clear()
                    chdir(current_directory)
                if "9" in pregunta_ide: #Github Cli
                    clear()
                    pacman.install("github-cli")
                    installed()
                if "10" in pregunta_ide:
                    if pregunta_ide == "1" and "0":
                        pass
                    else:   
                        clear()
                        chdir("/tmp")
                        sys("git clone https://aur.archlinux.org/github-desktop.git")
                        clear()
                        chdir("github-desktop")
                        sys("makepkg -si --noconfirm")
                        clear()
                        chdir(current_directory)
                if pregunta_ide == "0": #Atras
                    break
        if "4" in apre: #Gaming
            clear()
            palabras.gaming()
            print("Escoje que instalar\n1:Steam\n2:Lutris\n3:Wine\n4:proton-ge\n5:Play on Linux\n6:Mindustry\n7:Drivers\n0:Atras")
            pregunta_juegos = str(input(":"))
            if "1" in pregunta_juegos: #Steam
                clear()
                pacman.install("steam")
                installed()
            if "2" in pregunta_juegos: #Lutris
                clear()
                pacman.install("lutris")
                installed()
            if "3" in pregunta_juegos: #Wine
                clear()
                pacman.install("wine")
                installed()
            if "4" in pregunta_juegos: #Proton-ge-custom-bin
                chdir("/tmp")
                clear()
                sys("git clone https://aur.archlinux.org/proton-ge-custom-bin.git")
                chdir("proton-ge-custom-bin")
                clear()
                sys("makepkg -si --noconfirm")
                clear()
                chdir(current_directory)
            if "5" in pregunta_juegos: #Play on Linux
                chdir("/tmp")
                clear()
                sys("git clone https://aur.archlinux.org/playonlinux.git")
                chdir("playonlinux")
                clear()
                sys("makepkg -si --noconfirm")
                clear()
                chdir(current_directory)
            if "6" in pregunta_juegos: #Mindustry
                clear()
                chdir("/tmp")
                sys("git clone https://aur.archlinux.org/mindustry-bin.git")
                chdir("mindustry-bin")
                clear()
                sys("makepkg -si --noconfirm")
                clear()
            if "7" in pregunta_juegos: #Drivers
                clear()
                dependencias_desarrollo()
            if "0" in pregunta_juegos: #Atras
                pass
            clear()
        if "5" in apre: #Musica
            clear()
            palabras.musica()
            print("Seleciona una o mas opciones\n1:Spotify\n2:Spotify-Adblock\n3:Spotube\n4:Clementine\n5:YT Music\n6:Audacity\n0:Atras")
            pregunta_musica = str(input(":"))
            if "1" in pregunta_musica: #Spotify
                clear()
                pacman.install("spotify-launcher")
                installed()
            if "2" in pregunta_musica: #Spotify Adblock
                chdir("/tmp")
                clear()
                sys("git clone https://aur.archlinux.org/spotify-adblock.git")
                chdir("spotify-adblock")
                clear()
                sys("makepkg -si --noconfirm")
                clear()
            if "3" in pregunta_musica: #Spotube
                chdir("/tmp")
                clear()
                sys("git clone https://aur.archlinux.org/spotube-bin.git")
                chdir("spotube-bin")
                clear()
                sys("makepkg -si --noconfirm")
                clear()
            if "4" in pregunta_musica: #Clementine
                clear()
                pacman.install("clementine")
                installed()
            if "5" in pregunta_musica: #YT Music
                chdir("/tmp")
                clear()
                sys("git clone https://aur.archlinux.org/youtube-music.git")
                chdir("youtube-music")
                clear()
                sys("makepkg -si --noconfirm")
                clear()
            if "6" in pregunta_musica: #Audacity
                clear()
                pacman.install("audacity")
                installed()
            if "0" in pregunta_musica: #Atras
                pass
            clear()
        if "6" in apre: #Oficina
            clear()
            palabras.oficina()
            print("--OFICINA--\nElige una o mas opciones\n1:LibreOffice\n2:OpenOffice\n3:OnlyOffice\n4:WPS Office\n0:Atras")
            pregunta_oficina = str(input(":"))
            if "1" in pregunta_oficina:
                clear()
                ("sudo pacman -S libreoffice --noconfirm")
            if "2" in pregunta_oficina:
                chdir("/tmp")
                clear()
                sys("git clone https://aur.archlinux.org/openoffice-bin.git")
                chdir("openoffice-bin")
                clear()
                sys("makepkg -si --noconfirm")
                chdir(current_directory)
            if "3" in pregunta_oficina:
                (" /tmp")
                clear()
                sys("git clone https://aur.archlinux.org/onlyoffice-bin.git")
                chdir("onlyoffice-bin")
                clear()
                sys("makepkg -si --noconfirm")
                chdir(current_directory)
            if "4" in pregunta_oficina:
                chdir("/tmp")
                clear()
                sys("git clone https://aur.archlinux.org/wps-office-all-dicts-win-languages.git")
                chdir("wps-office-all-dicts-win-languages")
                clear()
                sys("makepkg -si --noconfirm")
                chdir(current_directory)
            if "0" in pregunta_oficina:
                pass
        if "0" in apre: #Salir
            clear()
            print("Saliendo...")
            sl(0.1)
            break

def cambiar_shell():
    clear()
    palabras.cambiar_shell()
    print("1:fish\n2:zsh\n3:bash\n0:Atras")
    shellpre = int(input("Que shell deseas poner?\n:"))
    if shellpre == 1: #Shell fish
        clear()
        pacman.install("fish")
        clear()
        sys("chsh -s /bin/fish")
        clear()
    if shellpre == 2: #Shell zsh
        clear()
        pacman.install("zsh")
        clear()
        sys("chsh -s /bin/zsh")
        clear()
    if shellpre == 3: #Shell Bash
        clear()
        pacman.install("bash")
        clear()
        sys("chsh -s /bin/bash")
        clear()
    if shellpre == 0:
        pass
    clear()

def snapd_inst():
    clear()
    pr1 = int(input("Quieres descargar el paquete por...?\n1=yay(debe estar instalado)\n2=git clone\n:"))
    if pr1 == 1:
        clear()
        sys("yay --noconfirm -S snapd")
        clear()
        sys("sudo systemctl enable --now snapd.socket")
        sys("sudo ln -s /var/lib/snapd/snap /snap")
        sys("sudo systemctl enable --now snapd.apparmor")
        sys("sudo apparmor_parser -r /etc/apparmor.d/*snap-confine*")
        sys("sudo apparmor_parser -r /var/lib/snapd/apparmor/profiles/snap confine*")
        clear()
        print("\nListo!\n")
    if pr1 == 2:
        clear()
        chdir("/tmp")
        sys("git clone https://aur.archlinux.org/snapd.git")
        chdir("snapd")
        sys("makepkg --noconfirm -si")
        clear()
        sys("sudo systemctl enable --now snapd.socket")
        sys("sudo ln -s /var/lib/snapd/snap /snap")
        sys("sudo systemctl enable --now snapd.apparmor")
        sys("sudo apparmor_parser -r /etc/apparmor.d/*snap-confine*")
        sys("sudo apparmor_parser -r /var/lib/snapd/apparmor/profiles/snap confine*")
        clear()
        chdir(current_directory)
        clear()
        print("\nListo!\n")
    if pr1 < 2:
        clear("")
        print("Selecciona Correctamente")
        sl(0.5)

def pkgman():
    clear()
    palabras.gestores_de_paquetes()
    print("1:yay\n2:paru\n3:pikaur\n4:snapd\n5:flatpak\n6:Pamac\n0:Cancelar")
    pkgpre1 = str(input(":"))
    if "1" in pkgpre1: #Yay
        yay_install()
        clear()
    if "2" in pkgpre1: #Paru
        clear()
        chdir("/tmp")
        sys("git clone https://aur.archlinux.org/paru.git")
        clear()
        chdir("paru")
        sys("makepkg --needed --noconfirm -si")
        clear()
        chdir(current_directory)
    if "3" in pkgpre1: #Pikaur
        clear()
        chdir("/tmp")
        sys("git clone https://aur.archlinux.org/pikaur.git")
        clear()
        chdir("pikaur")
        sys("makepkg -si --needed --noconfirm")
        chdir(current_directory)
        clear()
    if "4" in pkgpre1: #Snapd
        snapd_inst()
    if "5" in pkgpre1: #Flatpak
        clear()
        pacman.install("flatpak")
        installed()
        clear()
    if "6" in pkgpre1: #Pamac
        clear()
        palabras.pamac()
        print("1:Instalar pamac AUR\n2:Instalar pamac Flatpak\n3:Instalar pamac nosnap\n0:Cancelar")
        pamac_pre1 = int(input(":"))
        if pamac_pre1 == 1: #pamac-aur
            clear()
            chdir("/tmp")
            sys("git clone https://aur.archlinux.org/pamac-aur.git")
            sys(" pamac-aur")
            clear()
            sys("makepkg -si --needed --noconfirm")
            chdir(current_directory)
            clear()
        if pamac_pre1 == 2: #pamac-flatpak
            clear()
            chdir("/tmp")
            sys("git clone https://aur.archlinux.org/pamac-flatpak.git")
            chdir("pamac-flatpak")
            clear()
            sys("makepkg -si --needed --noconfirm")
            chdir(current_directory)
            clear()
        if pamac_pre1 == 3: #pamac-nosnap
            clear()
            chdir("/tmp")
            sys("git clone https://aur.archlinux.org/pamac-nosnap.git")
            chdir("pamac-nosnap")
            clear()
            sys("makepkg -si --needed --noconfirm")
        if pamac_pre1 == 0: #Salida
            clear()
            pass
        if pamac_pre1 > 3: #Error
            clear()
            print("Selecciona solo una opcion")
            sl(0.5)
            clear()
        if "0" in pkgpre1: #Cancelar
            pass

def escritorios():
    clear()
    palabras.escritorios_wms()
    print("1:WM's\n2:Escritorios\n0:Atras")
    pregunta_wm = str(input(":"))
    if "1" in pregunta_wm:
        clear()
        palabras.wms()
        print("1:i3wm\n2:awesome\n3:icewm\n4:bspwm\n0:Atras")
        pregunta_wm_1 = str(input(":"))
        if "1" in pregunta_wm_1:
            clear()
            pacman.install("i3")
            installed()
        if "2" in pregunta_wm_1:
            clear()
            pacman.install("awesome")
            installed()
        if "3" in pregunta_wm_1:
            clear()
            pacman.install("icewm")
            installed()
        if "4" in pregunta_wm_1:
            clear()
            pacman.install("bspwm")
            installed()
        if "0" in pregunta_wm_1:
            clear()
            pass
    if "2" in pregunta_wm:
        clear()
        palabras.escritorios()
        print("1:XFCE4\n2:GNOME\n3:KDE Plasma\n4:LXDE\n5:Cinnamon\n6:Mate\n0:Cancelar")
        desk_pre = str(input(":"))
        if "1" in desk_pre: #XFCE4
            clear()
            pacman.install(["xfce4","xfce4-goodies"])
            installed()
            clear()
        if "2" in desk_pre: #GNOME
            clear()
            pacman.install(["gnome","gnome-extra"])
            installed()
            clear()
        if "3" in desk_pre: #KDE Plasma
            clear()
            pacman.install("plasma")
            installed()
            clear()
        if "4" in desk_pre: #LXDE
            clear()
            pacman.install("lxde")
            installed()
            clear()
        if "5" in desk_pre: #Cinnamon
            clear()
            pacman.install("cinnamon")
            installed()
            clear()
        if "6" in desk_pre: #Mate
            clear()
            pacman.install("mate")
            installed()
            clear()
        if "0" in desk_pre: #Cancelar
            pass
    if "0" in pregunta_wm:
        clear()
        pass

def otros():
    while True:
        clear()
        palabras.otros()
        print("1:Intalar dependencias i3(requiere yay)\n2:Instalar repos\n3:Instalar Kernels\n0:Atras")
        pregunta_otros = str(input(":"))
        if "1" in pregunta_otros:
            clear()
            sys("yay --noconfirm -S - < lista-de-paquetes-i3")
            clear()
            sys("yay --noconfirm -S gnome-screenshot alsa-utils xscreensaver acpid mousepad-git")
            clear()
        if "2" in pregunta_otros:
            add_repos()
            clear()
        if "3" in pregunta_otros:
            while True:
                clear()
                palabras.kernels()
                print("1:Linux\n2:xanmod\n3:zen\n0:Atras")
                pregunta_kernel = str(input(":"))
                if "1" in pregunta_kernel:
                    clear()
                    pacman.install(["linux","linux-headers"])
                    installed()
                if "2" in pregunta_kernel:
                    clear()
                    chdir("/tmp")
                    sys("git clone https://aur.archlinux.org/linux-xanmod.git")
                    chdir("linux-xanmod")
                    clear()
                    sys("makepkg -si --noconfirm")
                    clear()
                    chdir(current_directory)
                if "3" in pregunta_kernel:
                    clear()
                    pacman.install(["linux-zen","linux-zen-headers"])
                    installed()
                if "0" in pregunta_kernel:
                    break
        if "0" in pregunta_otros:
            break

def borrar_basura():
    clear()
    palabras.borrar_basura()
    print("Elige una o mas opciones\n1:Escriba los paquetes que quiere eliminar seguidos de un salto de linea\n2:Borrado automatico\n0:Atras")
