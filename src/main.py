# Creado por Tom5521 o Angel pa'los cuates
# Bajo la licencia GPL 3.0

# Arch-Instalator MAIN v4.0.0

from time import sleep as sl
import palabras, pacman
from os import system as sys
from os import listdir, mkdir


def clear():
    sys("clear")


clear()
syupd = listdir("/tmp")
if "inst-temp" in syupd:
    pass
else:
    print("Actualizando Repositorios...")
    sys("sudo pacman -Syy >/dev/null 2>&1")
    mkdir("/tmp/inst-temp")

if pacman.check("git") == True:
    pass
else:
    print("git no esta instalado")
    sl(2)
    clear()
    pacman.install("git")


def dependencias_desarrollo():
    while True:
        clear()
        palabras.drivers()
        print("1:Drivers Gráficos\n2:Drivers de Sonido\n3:Bluetooth\n0:Atrás")
        pregunta_drivers = str(input(":"))
        if "1" in pregunta_drivers:
            while True:
                clear()
                palabras.drivers_graficos()
                print(
                    "Elige tus especificaciones\n1:Nvidia\n2:Amd\n3:Intel(Open Source)\n0:Atrás"
                )
                pregunta_drivers_g = float(input(":"))
                match pregunta_drivers_g:
                    case 1:  # Nvidia
                        clear()
                        palabras.nvidia()
                        print(
                            "Elige una version\n1:Propietario\n2:Open Source\n0:Atrás"
                        )
                        pregunta_drivers_nvidia = int(input(":"))
                        match pregunta_drivers_nvidia:
                            case 1:
                                pacman.aur("nvidia-340xx")
                            case 2:
                                pacman.install("nvidia-open")
                    case 2:  # AMD
                        clear()
                        palabras.amd()
                        print("Drivers...?\n1:Propietarios\n2:Open Source\n0:Atrás")
                        pregunta_drivers_1 = int(input(":"))
                        match pregunta_drivers_1:
                            case 1:
                                pacman.aur("amdgpu-pro-installer")
                            case 2:
                                pacman.install("xf86-video-ati xf86-video-amdgpu")
                            case _:
                                pass
                    case 3:
                        pacman.install("xf86-video-intel")  # Intel
                    case 0:  # Atrás
                        clear()
                        break
                    case _:
                        pass
        if "2" in pregunta_drivers:
            clear()
            palabras.sonido()
            print(
                "Elige una opcion\n1:Servidores de Audio\n2:Drivers de Sonido\n0:Atrás"
            )
            pregunta_drivers_s = str(input(":"))
            if "1" in pregunta_drivers_s:
                while True:
                    clear()
                    palabras.servidores_de_audio()
                    print("1:PulseAudio\n2:Pipewire\n0:Atrás")
                    pregunta_drivers_s_s = str(input(":"))
                    if "1" in pregunta_drivers_s_s:
                        pacman.install("pulseaudio")
                    if "2" in pregunta_drivers_s_s:
                        pacman.install("pipewire")
                    if "0" in pregunta_drivers_s_s:
                        break
            if "2" in pregunta_drivers_s:
                while True:
                    clear()
                    palabras.drivers_de_audio()
                    print("Elige una o mas opciones\n1:ALSA\n2:Jack\n3:Flac\n0:Atrás")
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
                clear()
                pass
        if "3" in pregunta_drivers:
            pacman.install("bluez blueman")
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
        print(
            "Seleccione repos a instalar\n1:Repositorio endeavour OS\n2:Chaotic-AUR\n0:Atrás"
        )
        pregunta_repos = str(input(":"))
        if "1" in pregunta_repos:  # Endeavour repo
            clear()
            sys("sudo pacman-key --keyserver keyserver.ubuntu.com -r 003DB8B0CB23504F")
            sys("sudo pacman-key --lsign 003DB8B0CB23504F")
            clear()
            sys('sudo echo "[endeavouros]" >> /etc/pacman.conf')
            sys('sudo echo "SigLevel = PackageRequired" >> /etc/pacman.conf')
            sys(
                'sudo echo "Include = /etc/pacman.d/endeavouros-mirrorlist" >> /etc/pacman.conf'
            )
            sys("sudo cp src/endeavouros-mirrorlist /etc/pacman.d/")
            clear()
            pacman.refresh()
            clear()
            sys("echo Exito!")
        if "2" in pregunta_repos:  # Chaotic-AUR
            sys(
                "sudo pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com"
            )
            sys("sudo pacman-key --lsign-key FBA220DFC880C036")
            sys(
                "sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'"
            )
            clear()
            pacman.refresh()
            clear()
            sys('sudo echo "[chaotic-aur]" >> /etc/pacman.conf')
            sys(
                'sudo echo "Include = /etc/pacman.d/chaotic-mirrorlist" >> /etc/pacman.conf'
            )
            pacman.refresh()
            clear()
        if pregunta_repos == "0":
            break


def apps_desarrollo():
    while True:
        clear()
        palabras.apps()
        print(
            "Escoje una categoria de apps a instalar\n1:Internet\n2:Imagen y Video\n3:IDE's\n4:Herramientas desarrollo\n5:Gaming\n6:Musica\n7:Oficina\n0:Salir"
        )
        apre = str(input(":"))
        if "1" in apre:  # Internet
            while True:
                clear()
                palabras.internet()
                print(
                    "Escoje una Categoria\n1:Navegador\n2:Email\n3:Mensajeria\n0:Atrás"
                )
                apre1 = str(input(":"))
                if "1" in apre1:  # Navegador
                    while True:
                        clear()
                        palabras.navegadores()
                        print(
                            "1:Firefox\n2:Chromium\n3:Opera\n4:Brave\n5:Chrome\n6:Tor\n0:Cancelar"
                        )
                        pregunta_navegador = str(input(":"))
                        if "1" in pregunta_navegador:
                            pacman.install("firefox")  # Firefox
                        if "2" in pregunta_navegador:
                            pacman.install("chromium")  # Chromium
                        if "3" in pregunta_navegador:
                            pacman.install("opera")  # Opera
                        if "4" in pregunta_navegador:
                            pacman.aur("brave")  # Brave
                        if "5" in pregunta_navegador:
                            pacman.aur("google-chrome")  # Chrome
                        if "6" in pregunta_navegador:
                            pacman.install("tor")  # Tor
                        if "0" in pregunta_navegador:
                            break  # Cancelar
                if "2" in apre1:  # Correo
                    while True:
                        clear()
                        palabras.mail()
                        print(
                            "Seleciona la o las apps que quieres instalar\n1:Thunderbird\n2:Mailspring\n3:Kmail\n0:Atrás"
                        )
                        pregunta_correo = str(input(":"))
                        if "1" in pregunta_correo:
                            pacman.install("thunderbird")  # Thunderbird
                        if "2" in pregunta_correo:
                            pacman.aur("mailspring")  # Mailspring
                        if "3" in pregunta_correo:
                            pacman.install("kmail")  # Kmail
                        if "0" in pregunta_correo:
                            break  # Atrás
                if "3" in apre1:  # Mensajeria
                    while True:
                        clear()
                        palabras.mensajeria()
                        print(
                            "Elige lo que quieres instalar:\n1:Discord\n2:Skype\n3:Teamspeak\n4:Telegram\n5:Zoom\n0:Atrás"
                        )
                        pregunta_mensajes = str(input(":"))
                        if "1" in pregunta_mensajes:
                            pacman.install("discord")  # Discord
                        if "2" in pregunta_mensajes:
                            pacman.aur("skypeforlinux-stable-bin")  # Skype
                        if "3" in pregunta_mensajes:
                            pacman.install("teamspeak3")  # Teamspeak
                        if "4" in pregunta_mensajes:
                            pacman.install("telegram-desktop")  # Telegram
                        if "5" in pregunta_mensajes:
                            pacman.aur("zoom")  # Zoom
                        if "0" in pregunta_mensajes:
                            break  # Atrás
                if "0" in apre1:  # Atrás
                    break
        if "2" in apre:  # Imagen y video
            while True:
                clear()
                palabras.imagen_y_video()
                print(
                    "Selecciona que instalar\n1:vlc\n2:mpv\n3:gthumb\n4:gimp\n5:krita\n6:kdenlive\n7:Netflix\n8:Obs-Studio\n0:Atrás"
                )
                pregunta_video = str(input(":"))
                if "1" in pregunta_video:
                    pacman.install("vlc")  # vlc
                if "2" in pregunta_video:
                    pacman.install("mpv")  # mpv
                if "3" in pregunta_video:
                    pacman.install("gthumb")  # gthumb
                if "4" in pregunta_video:
                    pacman.install("gimp")  # gimp
                if "5" in pregunta_video:
                    pacman.install("krita")  # krita
                if "6" in pregunta_video:
                    pacman.install("kdenlive")  # kdenlive
                if "7" in pregunta_video:
                    pacman.aur("netflix-nativefier")  # Netfilx
                if "8" in pregunta_video:
                    pacman.install("obs-studio")  # Obs-studio
                if "0" in pregunta_video:
                    break  # Atrás
        if "3" in apre:  # IDE's
            while True:
                clear()
                palabras.desarrollo()
                print(
                    "Apps de desarrollo\nElige que apps instalar\n1:VS code\n2:Code OSS\n3:Pycharm Comunity\n4:Eclipse-Java\n5:Sublime Text\n6:Android Studio\n7:Anbox\n0:Atrás"
                )
                pregunta_ide = str(input(":"))
                if "1" in pregunta_ide:  # VS Code
                    pacman.aur("visual-studio-code-bin")
                if "2" in pregunta_ide:
                    pacman.install("code")  # Code OSS
                if "3" in pregunta_ide:
                    # Pycharm Comunity
                    pacman.install("pycharm-community-edition")
                if "4" in pregunta_ide:
                    pacman.aur("eclipse-java")  # Eclipse-Java
                if "5" in pregunta_ide:
                    pacman.aur("sublime-text-4")  # Sublime Text
                if "6" in pregunta_ide:
                    pacman.aur("android-studio")  # Android Studio
                if "7" in pregunta_ide:
                    pacman.aur("anbox-git")  # Anbox
                if pregunta_ide == "0":
                    break  # Atrás
        if "4" in apre:  # Desarrollo
            while True:
                clear()
                palabras.desarrollo()
                print(
                    "Elige una o mas opciones\n1:JDK/JRE\n2:Golang\n3:Python(3.11)\n4:git\n5:cmake\n6:gcc\n7:Rust\n0:Atras"
                )
                pregunta_desarrollo = str(input(":"))
                if "1" in pregunta_desarrollo:
                    pacman.aur("jdk", "jre")
                if "2" in pregunta_desarrollo:
                    pacman.install("go go-tools")
                if "3" in pregunta_desarrollo:
                    pacman.aur("python311")
                if "4" in pregunta_desarrollo:
                    pacman.install("git")
                if "5" in pregunta_desarrollo:
                    pacman.install("cmake")
                if "6" in pregunta_desarrollo:
                    pacman.install("gcc")
                if "7" in pregunta_desarrollo:
                    pacman.install("rust")
                if "0" in pregunta_desarrollo:
                    break
        if "5" in apre:  # Gaming
            while True:
                clear()
                palabras.gaming()
                print(
                    "Escoje que instalar\n1:Steam\n2:Lutris\n3:Wine\n4:proton-ge\n5:Play on Linux\n6:Mindustry\n7:Tlauncher\n8:Grapejuice(Roblox)\n9:Drivers\n0:Atrás"
                )
                pregunta_juegos = str(input(":"))
                if "1" in pregunta_juegos:
                    pacman.install("steam")  # Steam
                if "2" in pregunta_juegos:
                    pacman.install("lutris")  # Lutris
                if "3" in pregunta_juegos:
                    pacman.install("wine")  # Wine
                if "4" in pregunta_juegos:
                    pacman.aur("proton-ge-custom-bin")  # Proton-ge-custom-bin
                if "5" in pregunta_juegos:
                    pacman.aur("playonlinux")  # Play on Linux
                if "6" in pregunta_juegos:
                    pacman.aur("mindustry-bin")  # Mindustry
                if "7" in pregunta_juegos:
                    pacman.aur("tlauncher")
                if "8" in pregunta_juegos:
                    pacman.aur("grapejuice")  # Grapejuice
                if "9" in pregunta_juegos:
                    dependencias_desarrollo()  # Drivers
                if "0" in pregunta_juegos:  # Atrás
                    break
        if "6" in apre:  # Musica
            while True:
                clear()
                palabras.musica()
                print(
                    "Seleciona una o mas opciones\n1:Spotify\n2:Spotify-Adblock\n3:Spotube\n4:Clementine\n5:YT Music\n6:Audacity\n0:Atrás"
                )
                pregunta_musica = str(input(":"))
                if "1" in pregunta_musica:
                    pacman.aur("spotify")  # Spotify
                if "2" in pregunta_musica:  # Spotify
                    spotify_check = pacman.check("spotify")
                    match spotify_check:
                        case True:
                            pass
                        case False:
                            pacman.aur("spotify")
                    pacman.aur("spotify-adblock")
                if "3" in pregunta_musica:
                    pacman.aur("spotube-bin")  # Spotube
                if "4" in pregunta_musica:
                    pacman.install("clementine")  # Clementine
                if "5" in pregunta_musica:
                    pacman.aur("youtube-music")  # YT Music
                if "6" in pregunta_musica:
                    pacman.install("audacity")  # Audacity
                if "0" in pregunta_musica:
                    break
        if "7" in apre:  # Oficina
            while True:
                clear()
                palabras.oficina()
                print(
                    "--OFICINA--\nElige una o mas opciones\n1:LibreOffice\n2:OpenOffice\n3:OnlyOffice\n4:WPS Office\n0:Atrás"
                )
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
                    break
        if "0" in apre:  # Salir
            clear()
            break


def cambiar_shell():
    while True:
        clear()
        palabras.cambiar_shell()
        print("1:fish\n2:zsh\n3:bash\n0:Atrás")
        shellpre = int(input("Que shell deseas poner?\n:"))
        match shellpre:
            case 1:
                pacman.install("fish")
                sys("chsh -s /bin/fish")
                clear()
            case 2:
                pacman.install("zsh")
                sys("chsh -s /bin/zsh")
                clear()
            case 3:
                pacman.install("bash")
                sys("chsh -s /bin/bash")
                clear()
            case 0:
                break
        clear()


def pkgman():
    while True:
        clear()
        palabras.gestores_de_paquetes()
        print("1:yay\n2:paru\n3:pikaur\n4:snapd\n5:flatpak\n6:Pamac\n0:Cancelar")
        pkgpre1 = str(input(":"))
        if "1" in pkgpre1:
            pacman.aur("yay")  # Yay
        if "2" in pkgpre1:
            pacman.aur("paru")  # Paru
        if "3" in pkgpre1:
            pacman.aur("pikaur")  # Pikaur
        if "4" in pkgpre1:
            clear()  # Snapd
            palabras.snapd()
            pacman.aur("snapd")
            clear()
            sys("sudo systemctl enable --now snapd.socket")
            sys("sudo ln -s /var/lib/snapd/snap /snap")
            sys("sudo systemctl enable --now snapd.apparmor")
            sys("sudo apparmor_parser -r /etc/apparmor.d/*snap-confine*")
            sys(
                "sudo apparmor_parser -r /var/lib/snapd/apparmor/profiles/snap confine*"
            )
            clear()
            print("\nListo!\n")
        if "5" in pkgpre1:
            pacman.install("flatpak")  # Flatpak
        if "6" in pkgpre1:  # Pamac
            clear()
            palabras.pamac()
            print(
                "1:Instalar pamac AUR\n2:Instalar pamac Flatpak\n3:Instalar pamac nosnap\n0:Cancelar"
            )
            pamac_pre1 = int(input(":"))
            match pamac_pre1:
                case 1:
                    pacman.aur("pamac-aur")
                case 2:
                    pacman.aur("pamac-flatpak")
                case 3:
                    pacman.aur("pamac-nosnap")
                case 0:
                    clear()
                    pass
                case _:
                    print("No se selecciono ninguno")
        if "0" in pkgpre1:  # Cancelar
            break


def escritorios():
    while True:
        clear()
        palabras.escritorios_wms()
        print("1:WM's\n2:Escritorios\n0:Atrás")
        pregunta_wm = str(input(":"))
        if "1" in pregunta_wm:
            while True:
                clear()
                palabras.wms()
                print("1:i3wm\n2:awesome\n3:icewm\n4:bspwm\n0:Atrás")
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
                    clear()
                    break
        if "2" in pregunta_wm:
            while True:
                clear()
                palabras.escritorios()
                print(
                    "1:XFCE4\n2:GNOME\n3:KDE Plasma\n4:LXDE\n5:Cinnamon\n6:Mate\n0:Cancelar"
                )
                desk_pre = str(input(":"))
                if "1" in desk_pre:
                    pacman.install("xfce4 xfce4-goodies")  # XFCE4
                if "2" in desk_pre:
                    pacman.install("gnome-extra gnome")  # GNOME
                if "3" in desk_pre:
                    pacman.install("plasma")  # KDE Plasma
                if "4" in desk_pre:
                    pacman.install("lxde")  # LXDE
                if "5" in desk_pre:
                    pacman.install("cinnamon")  # Cinnamon
                if "6" in desk_pre:
                    pacman.install("mate")  # Mate
                if "0" in desk_pre:
                    break  # Cancelar
        if "0" in pregunta_wm:
            clear()
            break


def otros():
    while True:
        clear()
        palabras.otros()
        print(
            "1:Intalar dependencias i3(requiere repo chaotic)\n2:Instalar repos\n3:Instalar Kernels\n0:Atrás"
        )
        pregunta_otros = str(input(":"))
        if "1" in pregunta_otros:
            clear()
            sys("sudo pacman -S - < lista-de-paquetes-i3 --noconfirm ")
            clear()
            sys(
                "sudo pacman -S gnome-screenshot alsa-utils xscreensaver acpid mousepad-git --noconfirm"
            )
            clear()
        if "2" in pregunta_otros:
            add_repos()
            clear()
        if "3" in pregunta_otros:
            while True:
                clear()
                palabras.kernels()
                print("1:Linux\n2:xanmod\n3:zen\n0:Atrás")
                pregunta_kernel = str(input(":"))
                match pregunta_kernel:
                    case "1":
                        pacman.install("linux linux-headers")
                    case "2":
                        pacman.aur("linux-xanmod", "linux-xanmod-headers")
                    case "3":
                        pacman.install("linux-zen linux-zen-headers")
                    case "0":
                        break
        if "0" in pregunta_otros:
            break


while True:
    try:
        clear()
        palabras.texto_inicial()
        print(
            "1:Apps y Drivers\n2:Gestores de paquetes\n3:Escritorios/WM's\n4:Cambiar Shell\n5:Otros\n0:Salir"
        )
        pregunta_inicial = str(input(":"))
        if "1" in pregunta_inicial:  # Apps y dependencias
            clear()
            palabras.apps_y_drivers()
            print("1:Apps\n2:Drivers\n0:Atrás")
            pregunta_apps_y_dependencias = str(input(":"))
            if "1" in pregunta_apps_y_dependencias:
                apps_desarrollo()  # Apps
            if "2" in pregunta_apps_y_dependencias:
                dependencias_desarrollo()  # Dependencias
            if "0" in pregunta_apps_y_dependencias:  # Atrás
                clear()
                pass
        if "2" in pregunta_inicial:
            pkgman()  # Gestores de paquetes
        if "3" in pregunta_inicial:
            escritorios()  # Escritorios/wm's
        if "4" in pregunta_inicial:
            cambiar_shell()  # Cambiar shell
        if "5" in pregunta_inicial:
            otros()  # Otros
        if pregunta_inicial == "mierda":  # Mierda
            sys("espeak mierda >/dev/null 2>&1")
        if "0" in pregunta_inicial:
            break  # Salir
    except (ValueError, TypeError):
        print("Error")
clear()
palabras.Final()
