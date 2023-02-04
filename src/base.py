
from time import sleep as sl

import palabras
#import pacman
from os import getcwd
from os import chdir
from os import system as sys


def installed():
    print("Instalado")
    sl(1)

class pacman:
    def install(nombre_pacman):
        sys("clear")
        sys("sudo pacman -S " + nombre_pacman + " --noconfirm|ls > .out && rm -rf .out")
        sys("clear")
        installed()
    def refresh():
        sys(clear)
        sys("sudo pacman -Syy|ls > .out && rm -rf .out")

def clear():
    sys("clear")

def aur(nombre):
    clear()
    url = "https://aur.archlinux.org/" + nombre + ".git"
    chdir("/tmp")
    sys("git clone "+ url)
    clear()
    chdir(nombre)
    sys("makepkg -si --noconfirm")
    clear()
    chdir(getcwd())
    installed()

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
                        aur("nvidia-340xx")
                    if "2" in pregunta_drivers_nvidia:
                        clear()
                        pacman.install("nvidia-open")
                if pregunta_drivers_g == 2: #AMD
                    clear()
                    palabras.amd()
                    print("Drivers...?\n1:Propietarios\n2:Open Source\n0:Atras")
                    pregunta_drivers_1 = int(input(":"))
                    if pregunta_drivers_1 == 1:
                        aur("amdgpu-pro-installer")
                    if pregunta_drivers_1 == 2:
                        clear()
                        pacman.install(["xf86-video-ati","xf86-video-amdgpu"])
                    if pregunta_drivers_1 == 0:
                        clear()
                    else:
                        pass
                if pregunta_drivers_g == 3: #Intel
                    clear()
                    pacman.install("xf86-video-intel")
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
                    if "2" in pregunta_drivers_s_s:
                        clear()
                        pacman.install("pipewire")
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
                    if "2" in pregunta_drivers_s_d:
                        clear()
                        pacman.install("jack2")
                    if "3" in pregunta_drivers_s_d:
                        clear() 
                        pacman.install("flac")
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
                if "2" in pregunta_navegador: #Chromium
                    clear()
                    pacman.install("chromium")
                if "3" in pregunta_navegador: #Opera
                    clear()
                    pacman.install("opera")
                if "4" in pregunta_navegador: #Brave
                    aur("brave")
                if "5" in pregunta_navegador: #Chrome
                    aur("google-chrome")
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
                if "2" in pregunta_correo: #Mailspring
                    aur("mailspring")
                if "3" in pregunta_correo: #Kmail
                    clear()
                    pacman.install("kmail")
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
                if "2" in pregunta_mensajes: #Skype
                    aur("skypeforlinux-stable-bin")
                if "3" in pregunta_mensajes: #Teamspeak
                    clear()
                    pacman.install("teamspeak3")
                if "4" in pregunta_mensajes: #Telegram
                    clear()
                    pacman.install("telegram-desktop")
                if "5" in pregunta_mensajes: #Zoom
                    aur("zoom")
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
            if "2" in pregunta_video: #mpv
                clear()
                pacman.install("mpv")
            if "3" in pregunta_video: #gthumb
                clear()
                pacman.install("gthumb")
            if "4" in pregunta_video: #gimp
                clear()
                pacman.install("gimp")
            if "5" in pregunta_video: #krita
                clear()
                pacman.install("krita")
            if "6" in pregunta_video: #kdenlive
                clear()
                pacman.install("kdenlive")
            if "7" in pregunta_video: #Netfilx
                aur("netflix-nativefier")
            if "8" in pregunta_video: #Obs-studio
                clear()
                pacman.install("obs-studio")
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
                        aur("visual-studio-code-bin")
                if "2" in pregunta_ide: #Code OSS
                    clear()
                    pacman.install("code")
                if "3" in pregunta_ide: #Pycharm Comunity
                    clear()
                    pacman.install("pycharm-community-edition")
                if "4" in pregunta_ide: #Eclipse-Java
                    aur("eclipse-java")
                if "5" in pregunta_ide: #Kate
                    clear()
                    pacman.install("kate")
                if "6" in pregunta_ide: #Freecad
                    clear()
                    pacman.install("freecad")
                if "7" in pregunta_ide: #Android Studio
                    aur("android-studio")
                if "8" in pregunta_ide: #Anbox
                    aur("anbox-git")
                if "9" in pregunta_ide: #Github Cli
                    clear()
                    pacman.install("github-cli")
                if "10" in pregunta_ide:
                    if pregunta_ide == "1" and "0":
                        pass
                    else:   
                        aur("github-desktop")
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
            if "2" in pregunta_juegos: #Lutris
                clear()
                pacman.install("lutris")
            if "3" in pregunta_juegos: #Wine
                clear()
                pacman.install("wine")
            if "4" in pregunta_juegos: #Proton-ge-custom-bin
                aur("proton-ge-custom-bin")
            if "5" in pregunta_juegos: #Play on Linux
                aur("playonlinux")
            if "6" in pregunta_juegos: #Mindustry
                aur("mindustry-bin")
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
            if "2" in pregunta_musica: #Spotify Adblock
                aur("spotify-adblock")
            if "3" in pregunta_musica: #Spotube
                aur("spotube-bin")
            if "4" in pregunta_musica: #Clementine
                clear()
                pacman.install("clementine")
            if "5" in pregunta_musica: #YT Music
                aur("youtube-music")
            if "6" in pregunta_musica: #Audacity
                clear()
                pacman.install("audacity")
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
                aur("openoffice-bin")
            if "3" in pregunta_oficina:
                aur("onlyoffice-bin")
            if "4" in pregunta_oficina:
                aur("wps-office-all-dicts-win-languages")
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
        aur("snapd")
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
        aur("yay")
        clear()
    if "2" in pkgpre1: #Paru
        clear()
        aur("paru")
    if "3" in pkgpre1: #Pikaur
        aur("pikaur")
    if "4" in pkgpre1: #Snapd
        snapd_inst()
    if "5" in pkgpre1: #Flatpak
        clear()
        pacman.install("flatpak")
        clear()
    if "6" in pkgpre1: #Pamac
        clear()
        palabras.pamac()
        print("1:Instalar pamac AUR\n2:Instalar pamac Flatpak\n3:Instalar pamac nosnap\n0:Cancelar")
        pamac_pre1 = int(input(":"))
        if pamac_pre1 == 1: #pamac-aur
            aur("pamac-aur")
        if pamac_pre1 == 2: #pamac-flatpak
            aur("pamac-flatpak")
        if pamac_pre1 == 3: #pamac-nosnap
            aur("pamac-nosnap")
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
        if "2" in pregunta_wm_1:
            clear()
            pacman.install("awesome")
        if "3" in pregunta_wm_1:
            clear()
            pacman.install("icewm")
        if "4" in pregunta_wm_1:
            clear()
            pacman.install("bspwm")
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
            clear()
        if "2" in desk_pre: #GNOME
            clear()
            pacman.install(["gnome","gnome-extra"])
            clear()
        if "3" in desk_pre: #KDE Plasma
            clear()
            pacman.install("plasma")
            clear()
        if "4" in desk_pre: #LXDE
            clear()
            pacman.install("lxde")
            clear()
        if "5" in desk_pre: #Cinnamon
            clear()
            pacman.install("cinnamon")
            clear()
        if "6" in desk_pre: #Mate
            clear()
            pacman.install("mate")
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
                if "2" in pregunta_kernel:
                    aur("linux-xanmod")
                if "3" in pregunta_kernel:
                    clear()
                    pacman.install(["linux-zen","linux-zen-headers"])
                if "0" in pregunta_kernel:
                    break
        if "0" in pregunta_otros:
            break

def borrar_basura():
    clear()
    palabras.borrar_basura()
    print("Elige una o mas opciones\n1:Escriba los paquetes que quiere eliminar seguidos de un salto de linea\n2:Borrado automatico\n0:Atras")
