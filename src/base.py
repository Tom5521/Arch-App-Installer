
from time import sleep as sl
import palabras
from os import chdir,getcwd
from os import system as sys

class pacman:
    def install(nombre_pacman):
        deco.clear()
        print("Instalando " + nombre_pacman + "...")
        sys("sudo pacman -S " + nombre_pacman + " --noconfirm|ls > .out && rm -rf .out")
        deco.clear()
        deco.installed()
    
    def refresh():
        deco.clear()
        print("Actualizando repos...")
        sys("sudo pacman -Syy >/dev/null 2>&1")

    def aur(nombre_aur):
        deco.clear()
        url = "https://aur.archlinux.org/" + nombre_aur + ".git"
        chdir("/tmp")
        print("Clonando " + nombre_aur + "...")
        sys("git clone "+ url + ">/dev/null 2>&1")
        deco.clear()
        chdir(nombre_aur)
        print("Instalando " + nombre_aur + "...")
        sys("makepkg -si --noconfirm >/dev/null 2>&1")
        deco.clear()
        chdir(getcwd())
        deco.installed()

    def upgrade():
        deco.clear()
        print("Actualizando...")
        sys("sudo pacman -Syu --noconfirm >/dev/null 2>&1")

class deco:
    def clear():
        sys("clear")

    def installed():
        print("Instalado")
        sl(1)

def dependencias_desarrollo():
    while True:
        deco.clear()
        palabras.drivers()
        print("1:Drivers Graficos\n2:Drivers de Sonido\n3:Bluetooth\n0:Atras")
        pregunta_drivers = str(input(":"))
        if "1" in pregunta_drivers:
            while True:
                deco.clear()
                palabras.drivers_graficos()
                print("Elige tus especificaciones\n1:Nvidia\n2:Amd\n3:Intel(Open Source)\n0:Atras")
                pregunta_drivers_g = int(input(":"))
                if pregunta_drivers_g == 1: #Nvidia
                    deco.clear()
                    palabras.nvidia()
                    print("Elige una vercion\n1:Propietario\n2:Open Source\n0:Atras")
                    pregunta_drivers_nvidia = str(input(":"))
                    if "1" in pregunta_drivers_nvidia:
                        pacman.aur("nvidia-340xx")
                    if "2" in pregunta_drivers_nvidia:
                        pacman.install("nvidia-open")
                if pregunta_drivers_g == 2: #AMD
                    deco.clear()
                    palabras.amd()
                    print("Drivers...?\n1:Propietarios\n2:Open Source\n0:Atras")
                    pregunta_drivers_1 = int(input(":"))
                    if pregunta_drivers_1 == 1:
                        pacman.aur("amdgpu-pro-installer")
                    if pregunta_drivers_1 == 2:
                        deco.clear()
                        pacman.install("xf86-video-ati xf86-video-amdgpu")
                    if pregunta_drivers_1 == 0:
                        deco.clear()
                        pass
                if pregunta_drivers_g == 3: #Intel
                    pacman.install("xf86-video-intel")
                if pregunta_drivers_g == 0: #Atras
                    deco.clear()
                    break
                else:
                    pass
        if "2" in pregunta_drivers:
            deco.clear()
            palabras.sonido()
            print("Elige una opcion\n1:Servidores de Audio\n2:Drivers de Sonido\n0:Atras")
            pregunta_drivers_s = str(input(":"))
            if "1" in pregunta_drivers_s:
                while True:
                    deco.clear()
                    palabras.servidores_de_audio()
                    print("1:PulseAudio\n2:Pipewire\n0:Atras")
                    pregunta_drivers_s_s = str(input(":"))
                    if "1" in pregunta_drivers_s_s:
                        pacman.install("pulseaudio")
                    if "2" in pregunta_drivers_s_s:
                        pacman.install("pipewire")
                    if "0" in pregunta_drivers_s_s:
                        deco.clear()
                        break
            if "2" in pregunta_drivers_s:
                while True:    
                    deco.clear()
                    palabras.drivers_de_audio()
                    print("Elige una o mas opciones\n1:ALSA\n2:Jack\n3:Flac\n0:Atras")
                    pregunta_drivers_s_d = str(input(":"))
                    if "1" in pregunta_drivers_s_d:
                        pacman.install("alsa alsa-firmware")
                    if "2" in pregunta_drivers_s_d:
                        pacman.install("jack2")
                    if "3" in pregunta_drivers_s_d:
                        pacman.install("flac")
                    if "0" in pregunta_drivers_s_d:
                        break
                    else:
                        pass
            if "0" in pregunta_drivers_s:
                deco.clear()
                pass    
        if "3" in pregunta_drivers:
            pacman.install("bluez blueman")
            deco.clear()
            sys("sudo systemctl enable bluetooth.service")
            deco.clear()
        if "0" in pregunta_drivers:
            break
        else:
            pass

def add_repos():
    while True:
        deco.clear()
        palabras.repositorios()
        print("Seleccione repos a instalar\n1:Repositorio endeavour OS\n2:Chaotic-AUR\n0:Atras")
        pregunta_repos = str(input(":"))
        if "1" in pregunta_repos: #Endeavour repo
            deco.clear()
            sys("sudo pacman-key --keyserver keyserver.ubuntu.com -r 003DB8B0CB23504F")
            sys("sudo pacman-key --lsign 003DB8B0CB23504F")
            deco.clear()
            sys('sudo echo "[endeavouros]" >> /etc/pacman.conf')
            sys('sudo echo "SigLevel = PackageRequired" >> /etc/pacman.conf')
            sys('sudo echo "Include = /etc/pacman.d/endeavouros-mirrorlist" >> /etc/pacman.conf')
            sys("sudo cp src/endeavouros-mirrorlist /etc/pacman.d/")
            deco.clear()
            pacman.refresh()
            deco.clear()
            sys("echo Exito!")
        if "2" in pregunta_repos: #Chaotic-AUR
            sys("sudo pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com")
            sys("sudo pacman-key --lsign-key FBA220DFC880C036")
            sys("sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'")
            deco.clear()
            pacman.refresh()
            deco.clear()
            sys('sudo echo "[chaotic-aur]" >> /etc/pacman.conf')
            sys('sudo echo "Include = /etc/pacman.d/chaotic-mirrorlist" >> /etc/pacman.conf')
            pacman.refresh()
            deco.clear()
        if pregunta_repos == "0":
            break

def dependenciasG():
    deco.clear()
    sys("yay --noconfirm -S wine mangohud game-devices-udev gamemode linux-xanmod linux-xanmod-headers vulkan-icd-loader lib32-vulkan-icd-loader lib32-vulkan-intel vulkan-intel vkd3d lib32-vkd3d")
    deco.clear()
    pacman.refresh()
    deco.clear()

def el_resto():
    deco.clear()
    sys("yay --noconfirm -S mkinitcpio-firmware python-lsp-server")
    deco.clear()
    sys("yay -Syu --noconfirm")
    deco.clear()

def apps_desarrollo():
    while True:
        deco.clear()
        palabras.apps()
        print("Escoje una categoria de apps a instalar\n1:Internet\n2:Imagen y Video\n3:Desarrollo\n4:Gaming\n5:Musica\n6:Oficina\n0:Salir")
        apre = str(input(":"))
        if "1" in apre: #Internet
            deco.clear()
            palabras.internet()
            print("Escoje una Categoria\n1:Navegador\n2:Email\n3:Mensajeria\n0:Atras")
            apre1 = str(input(":"))
            if "1" in apre1: #Navegador
                deco.clear()
                palabras.navegadores()
                print("1:Firefox\n2:Chromium\n3:Opera\n4:Brave\n5:Chrome\n6:Tor\n0:Cancelar")
                pregunta_navegador = str(input(":"))
                if "1" in pregunta_navegador: #Firefox
                    pacman.install("firefox")
                if "2" in pregunta_navegador: #Chromium
                    pacman.install("chromium")
                if "3" in pregunta_navegador: #Opera
                    pacman.install("opera")
                if "4" in pregunta_navegador: #Brave
                    pacman.aur("brave")
                if "5" in pregunta_navegador: #Chrome
                    pacman.aur("google-chrome")
                if "6" in pregunta_navegador: #Tor
                    pacman.install("tor")
                if "0" in pregunta_navegador: #Cancelar
                    pass
            if "2" in apre1: #Correo
                deco.clear()
                palabras.mail()
                print("Seleciona la o las apps que quieres instalar\n1:Thunderbird\n2:Mailspring\n3:Kmail\n0:Atras")
                pregunta_correo = str(input(":"))
                if "1" in pregunta_correo: #Thunderbird
                    pacman.install("thunderbird")
                if "2" in pregunta_correo: #Mailspring
                    pacman.aur("mailspring")
                if "3" in pregunta_correo: #Kmail
                    pacman.install("kmail")
                if "0" in pregunta_correo: #Atras
                    pass
            if "3" in apre1: #Mensajeria
                deco.clear()
                palabras.mensajeria()
                print("Elige lo que quieres instalar:\n1:Discord\n2:Skype\n3:Teamspeak\n4:Telegram\n5:Zoom\n0:Atras")
                pregunta_mensajes = str(input(":"))
                if "1" in pregunta_mensajes: #Discord
                    pacman.install("discord")
                if "2" in pregunta_mensajes: #Skype
                    pacman.aur("skypeforlinux-stable-bin")
                if "3" in pregunta_mensajes: #Teamspeak
                    pacman.install("teamspeak3")
                if "4" in pregunta_mensajes: #Telegram
                    pacman.install("telegram-desktop")
                if "5" in pregunta_mensajes: #Zoom
                    pacman.aur("zoom")
                if "0" in pregunta_mensajes: #Atras
                    pass
            if "0" in apre1: #Atras
                pass
        if "2" in apre: #Imagen y video
            deco.clear()
            palabras.imagen_y_video()
            print("Selecciona que instalar\n1:vlc\n2:mpv\n3:gthumb\n4:gimp\n5:krita\n6:kdenlive\n7:Netflix\n8:Obs-Studio\n0:Atras")
            pregunta_video = str(input(":"))
            if "1" in pregunta_video: #vlc
                pacman.install("vlc")
            if "2" in pregunta_video: #mpv
                pacman.install("mpv")
            if "3" in pregunta_video: #gthumb
                pacman.install("gthumb")
            if "4" in pregunta_video: #gimp
                pacman.install("gimp")
            if "5" in pregunta_video: #krita
                pacman.install("krita")
            if "6" in pregunta_video: #kdenlive
                pacman.install("kdenlive")
            if "7" in pregunta_video: #Netfilx
                pacman.aur("netflix-nativefier")
            if "8" in pregunta_video: #Obs-studio
                pacman.install("obs-studio")
            if "0" in pregunta_video: pass#Atras
        if "3" in apre: #Desarrollo
            while True:
                deco.clear()
                palabras.desarrollo()
                print("Apps de desarrollo\nElige que apps instalar\n1:VS code\n2:Code OSS\n3:Pycharm Comunity\n4:Eclipse-Java\n5:Kate\n6:Freecad\n7:Android Studio\n8:Anbox\n9:Github-cli\n10:Github-Desktop\n0:Atras")
                pregunta_ide = str(input(":"))
                if "1" in pregunta_ide: #VS Code
                    if pregunta_ide == "10": pass
                    else: pacman.aur("visual-studio-code-bin")
                if "2" in pregunta_ide: #Code OSS
                    pacman.install("code")
                if "3" in pregunta_ide: #Pycharm Comunity
                    pacman.install("pycharm-community-edition")
                if "4" in pregunta_ide: #Eclipse-Java
                    pacman.aur("eclipse-java")
                if "5" in pregunta_ide: #Kate
                    pacman.install("kate")
                if "6" in pregunta_ide: #Freecad
                    pacman.install("freecad")
                if "7" in pregunta_ide: #Android Studio
                    pacman.aur("android-studio")
                if "8" in pregunta_ide: #Anbox
                    pacman.aur("anbox-git")
                if "9" in pregunta_ide: #Github Cli
                    pacman.install("github-cli")
                if "10" in pregunta_ide:
                    if pregunta_ide == "1" and "0": pass
                    else: pacman.aur("github-desktop")
                if pregunta_ide == "0": #Atras
                    break
        if "4" in apre: #Gaming
            deco.clear()
            palabras.gaming()
            print("Escoje que instalar\n1:Steam\n2:Lutris\n3:Wine\n4:proton-ge\n5:Play on Linux\n6:Mindustry\n7:Drivers\n0:Atras")
            pregunta_juegos = str(input(":"))
            if "1" in pregunta_juegos: #Steam
                pacman.install("steam")
            if "2" in pregunta_juegos: #Lutris
                pacman.install("lutris")
            if "3" in pregunta_juegos: #Wine
                pacman.install("wine")
            if "4" in pregunta_juegos: #Proton-ge-custom-bin
                pacman.aur("proton-ge-custom-bin")
            if "5" in pregunta_juegos: #Play on Linux
                pacman.aur("playonlinux")
            if "6" in pregunta_juegos: #Mindustry
                pacman.aur("mindustry-bin")
            if "7" in pregunta_juegos: #Drivers
                deco.clear()
                dependencias_desarrollo()
            if "0" in pregunta_juegos: #Atras
                pass
            deco.clear()
        if "5" in apre: #Musica
            deco.clear()
            palabras.musica()
            print("Seleciona una o mas opciones\n1:Spotify\n2:Spotify-Adblock\n3:Spotube\n4:Clementine\n5:YT Music\n6:Audacity\n0:Atras")
            pregunta_musica = str(input(":"))
            if "1" in pregunta_musica: #Spotify
                pacman.install("spotify-launcher")
            if "2" in pregunta_musica: #Spotify Adblock
                pacman.aur("spotify-adblock")
            if "3" in pregunta_musica: #Spotube
                pacman.aur("spotube-bin")
            if "4" in pregunta_musica: #Clementine
                pacman.install("clementine")
            if "5" in pregunta_musica: #YT Music
                pacman.aur("youtube-music")
            if "6" in pregunta_musica: #Audacity
                pacman.install("audacity")
            if "0" in pregunta_musica: #Atras
                pass
            deco.clear()
        if "6" in apre: #Oficina
            deco.clear()
            palabras.oficina()
            print("--OFICINA--\nElige una o mas opciones\n1:LibreOffice\n2:OpenOffice\n3:OnlyOffice\n4:WPS Office\n0:Atras")
            pregunta_oficina = str(input(":"))
            if "1" in pregunta_oficina:
                pacman.install("libreoffice")
            if "2" in pregunta_oficina:
                pacman.aur("openoffice-bin")
            if "3" in pregunta_oficina:
                pacman.aur("onlyoffice-bin")
            if "4" in pregunta_oficina:
                pacman.aur("wps-office-all-dicts-win-languages")
            if "0" in pregunta_oficina:
                pass
        if "0" in apre: #Salir
            deco.clear()
            print("Saliendo...")
            sl(0.1)
            break

def cambiar_shell():
    deco.clear()
    palabras.cambiar_shell()
    print("1:fish\n2:zsh\n3:bash\n0:Atras")
    shellpre = int(input("Que shell deseas poner?\n:"))
    match shellpre:
        case 1:
            pacman.install("fish")
            sys("chsh -s /bin/fish")
            deco.clear()
        case 2:
            pacman.install("zsh")
            sys("chsh -s /bin/zsh")
            deco.clear()
        case 3:
            pacman.install("bash")
            sys("chsh -s /bin/bash")
            deco.clear()
        case 0: pass
    deco.clear()

def snapd_inst():
    deco.clear()
    palabras.snapd()
    pr1 = int(input("Quieres descargar el paquete por...?\n1=yay(debe estar instalado)\n2=git clone\n:"))
    if pr1 == 1:
        deco.clear()
        sys("yay --noconfirm -S snapd")
        deco.clear()
        def snapd_perms():
            sys("sudo systemctl enable --now snapd.socket")
            sys("sudo ln -s /var/lib/snapd/snap /snap")
            sys("sudo systemctl enable --now snapd.apparmor")
            sys("sudo apparmor_parser -r /etc/apparmor.d/*snap-confine*")
            sys("sudo apparmor_parser -r /var/lib/snapd/apparmor/profiles/snap confine*")
        snapd_perms()
        deco.clear()
        print("\nListo!\n")
    if pr1 == 2:
        pacman.aur("snapd")
        deco.clear()
        snapd_perms()
        deco.clear()
        chdir(getcwd())
        deco.clear()
        print("\nListo!\n")
    if pr1 < 2:
        deco.clear()
        print("Selecciona Correctamente")
        sl(0.5)

def pkgman():
    deco.clear()
    palabras.gestores_de_paquetes()
    print("1:yay\n2:paru\n3:pikaur\n4:snapd\n5:flatpak\n6:Pamac\n0:Cancelar")
    pkgpre1 = str(input(":"))
    if "1" in pkgpre1: #Yay
        pacman.aur("yay")
        deco.clear()
    if "2" in pkgpre1: #Paru
        deco.clear()
        pacman.aur("paru")
    if "3" in pkgpre1: #Pikaur
        pacman.aur("pikaur")
    if "4" in pkgpre1: #Snapd
        snapd_inst()
    if "5" in pkgpre1: #Flatpak
        pacman.install("flatpak")
    if "6" in pkgpre1: #Pamac
        deco.clear()
        palabras.pamac()
        print("1:Instalar pamac AUR\n2:Instalar pamac Flatpak\n3:Instalar pamac nosnap\n0:Cancelar")
        pamac_pre1 = int(input(":"))
        match pamac_pre1:
            case 1: pacman.aur("pamac-aur")
            case 2: pacman.aur("pamac-flatpak")
            case 3: pacman.aur("pamac-nosnap")
            case 0: 
                deco.clear 
                pass
            case _: print("No se selecciono ninguno")
        if "0" in pkgpre1: #Cancelar
            pass

def escritorios():
    deco.clear()
    palabras.escritorios_wms()
    print("1:WM's\n2:Escritorios\n0:Atras")
    pregunta_wm = str(input(":"))
    if "1" in pregunta_wm:
        deco.clear()
        palabras.wms()
        print("1:i3wm\n2:awesome\n3:icewm\n4:bspwm\n0:Atras")
        pregunta_wm_1 = str(input(":"))
        if "1" in pregunta_wm_1:
            pacman.install("i3")
        if "2" in pregunta_wm_1:
            pacman.install("awesome")
        if "3" in pregunta_wm_1:
            pacman.install("icewm")
        if "4" in pregunta_wm_1:
            pacman.install("bspwm")
        if "0" in pregunta_wm_1:
            deco.clear()
            pass
    if "2" in pregunta_wm:
        deco.clear()
        palabras.escritorios()
        print("1:XFCE4\n2:GNOME\n3:KDE Plasma\n4:LXDE\n5:Cinnamon\n6:Mate\n0:Cancelar")
        desk_pre = str(input(":"))
        if "1" in desk_pre: #XFCE4
            pacman.install("xfce4 xfce4-goodies")
        if "2" in desk_pre: #GNOME
            pacman.install("gnome-extra gnome")
        if "3" in desk_pre: #KDE Plasma
            pacman.install("plasma")
        if "4" in desk_pre: #LXDE
            pacman.install("lxde")
        if "5" in desk_pre: #Cinnamon
            pacman.install("cinnamon")
        if "6" in desk_pre: #Mate
            pacman.install("mate")
        if "0" in desk_pre: #Cancelar
            pass
    if "0" in pregunta_wm:
        deco.clear()
        pass

def otros():
    while True:
        deco.clear()
        palabras.otros()
        print("1:Intalar dependencias i3(requiere yay)\n2:Instalar repos\n3:Instalar Kernels\n0:Atras")
        pregunta_otros = str(input(":"))
        if "1" in pregunta_otros:
            deco.clear()
            sys("yay --noconfirm -S - < lista-de-paquetes-i3")
            deco.clear()
            sys("yay --noconfirm -S gnome-screenshot alsa-utils xscreensaver acpid mousepad-git")
            deco.clear()
        if "2" in pregunta_otros:
            add_repos()
            deco.clear()
        if "3" in pregunta_otros:
            while True:
                deco.clear()
                palabras.kernels()
                print("1:Linux\n2:xanmod\n3:zen\n0:Atras")
                pregunta_kernel = str(input(":"))
                match pregunta_kernel:
                    case "1": pacman.install("linux linux-headers")
                    case "2": pacman.aur("linux-xanmod")
                    case "3": pacman.install("linux-zen linux-zen-headers")
                    case "0": break
        if "0" in pregunta_otros:
            break

