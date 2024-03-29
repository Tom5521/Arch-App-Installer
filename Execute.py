# Created by Tom5521 or Angel
# Under the license GPL 3.0
# ArchAppInstaller EXECUTE v4.2.0

from time import sleep as sl
from src import pacman, words
from os import system as sys
from os import listdir, mkdir


def clear():
    sys("clear")


clear()
syupd = listdir("/tmp")
if "inst-temp" in syupd:
    pass
else:
    print("Updating repositories...")
    sys("sudo pacman -Syy >/dev/null 2>&1")
    mkdir("/tmp/inst-temp")

if pacman.check("git") == True:
    pass
else:
    print("git is not installed")
    sl(2)
    clear()
    pacman.install("git")


def dependencias_desarrollo():
    while True:
        clear()
        words.drivers()
        print("1:Graphic drivers\n2:Sound drivers\n3:Bluetooth\n0:back")
        pregunta_drivers = str(input(":"))
        if "1" in pregunta_drivers:
            while True:
                clear()
                words.graphic_drivers()
                print(
                    "Choose your specifications\n1:Nvidia\n2:Amd\n3:Intel(Open Source)\n0:Back"
                )
                pregunta_drivers_g = float(input(":"))
                match pregunta_drivers_g:
                    case 1:  # Nvidia
                        clear()
                        words.nvidia()
                        print("Choose a version\n1:Proprietary\n2:Open Source\n0:Back")
                        pregunta_drivers_nvidia = int(input(":"))
                        match pregunta_drivers_nvidia:
                            case 1:
                                pacman.aur("nvidia-340xx")
                            case 2:
                                pacman.install("nvidia-open")
                    case 2:  # AMD
                        clear()
                        words.amd()
                        print("Drivers...?\n1:Propiery\n2:Open Source\n0:Back")
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
            words.sound()
            print("Choose an option\n1:Audio servers\n2:Sound drivers\n0:Back")
            pregunta_drivers_s = str(input(":"))
            if "1" in pregunta_drivers_s:
                while True:
                    clear()
                    words.sound_servers()
                    print("1:PulseAudio\n2:Pipewire\n0:Back")
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
                    words.sound_drivers()
                    print("Choose one or more options\n1:ALSA\n2:Jack\n3:Flac\n0:Back")
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
        if "0" in pregunta_drivers:
            break
        else:
            pass


def add_repos():
    while True:
        clear()
        words.repositories()
        print(
            "Select repositories to install\n1:Repository Endeavour OS\n2:Chaotic-AUR\n0:Back"
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
        words.apps()
        print(
            "Select an app category to install\n1:internet\n2:Image and video\n3:Development tools\n4:gaming\n5:musica\n6:Office\n0:Back"
        )
        apre = str(input(":"))
        if "1" in apre:  # Internet
            while True:
                clear()
                words.internet()
                print(
                    "Hide a category\n1:Browser\n2:Email\n3:Messenger service\n0:Back"
                )
                apre1 = str(input(":"))
                if "1" in apre1:  # Navegador
                    while True:
                        clear()
                        words.browers()
                        print(
                            "1:Firefox\n2:Chromium\n3:Opera\n4:Brave\n5:Chrome\n6:Tor\n0:Back"
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
                        words.mail()
                        print(
                            "Select the apps you want to install\n1:Thunderbird\n2:Mailspring\n3:Kmail\n0:Back"
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
                        words.messaging()
                        print(
                            "Choose what you want to install:\n1:Discord\n2:Skype\n3:Teamspeak\n4:Telegram\n5:Zoom\n0:Back"
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
                words.image_and_video()
                print(
                    "Select to install\n1:vlc\n2:mpv\n3:gthumb\n4:gimp\n5:krita\n6:kdenlive\n7:Netflix\n8:Obs-Studio\n0:Back"
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
                words.development_apps()
                print(
                    "Choose that apps install\n1:VS code\n2:Code OSS\n3:Pycharm Comunity\n4:Eclipse-Java\n5:Sublime Text\n6:Android Studio\n7:Anbox\n8:JDK/JRE\n9:Golang\n10:Python(3.11)\n11:git\n12:cmake\n13:gcc\n14:Rust\n0:Back"
                )
                pregunta_ide = str(input(":"))
                for i in pregunta_ide.split():
                    match i:
                        case "1":
                            pacman.aur("visual-studio-code-bin")
                        case "2":
                            pacman.install("code")
                        case "3":
                            pacman.install("pycharm-community-edition")
                        case "4":
                            pacman.aur("eclipse-java")
                        case "5":
                            pacman.aur("sublime-text-4")
                        case "6":
                            pacman.aur("android-studio")
                        case "7":
                            pacman.aur("anbox-git")
                        case "8":
                            pacman.aur("jdk jre")
                        case "9":
                            pacman.install("go go-tools")
                        case "10":
                            pacman.aur("python311")
                        case "11":
                            pacman.install("git")
                        case "12":
                            pacman.install("cmake")
                        case "13":
                            pacman.install("gcc")
                        case "14":
                            pacman.install("rust")
                        case _:
                            pass
                if "0" in pregunta_ide:
                    break  # Atrás
        if "4" in apre:  # Gaming
            while True:
                clear()
                words.gaming()
                print(
                    "Select app to install\n1:Steam\n2:Lutris\n3:Wine\n4:proton-ge\n5:Play on Linux\n6:Mindustry\n7:Tlauncher\n8:Grapejuice(Roblox)\n9:Drivers\n0:Back"
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
        if "5" in apre:  # Musica
            while True:
                clear()
                words.music()
                print(
                    "Select one or more options\n1:Spotify\n2:Spotify-Adblock\n3:Spotube\n4:Clementine\n5:YT Music\n6:Audacity\n0:Back"
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
        if "6" in apre:  # Oficina
            while True:
                clear()
                words.office()
                print(
                    "Choose one or more options\n1:LibreOffice\n2:OpenOffice\n3:OnlyOffice\n4:WPS Office\n0:Back"
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
        words.change_shell()
        print("1:fish\n2:zsh\n3:bash\n0:Atrás")
        shellpre = int(input("What Shell you want use?\n:"))
        match shellpre:
            case 1:
                if pacman.check("fish") == False:
                    pacman.install("fish")
                sys("chsh -s /bin/fish")
                clear()
            case 2:
                if pacman.check("zsh") == False:
                    pacman.install("zsh")
                sys("chsh -s /bin/zsh")
                clear()
            case 3:
                if pacman.check("bash") == False:
                    pacman.install("bash")
                sys("chsh -s /bin/bash")
                clear()
            case 0:
                break
            case _:
                pass
        clear()


def pkgman():
    while True:
        clear()
        words.package_managers()
        print("1:yay\n2:paru\n3:pikaur\n4:snapd\n5:flatpak\n6:Pamac\n0:Back")
        pkgpre1 = str(input(":"))
        if "1" in pkgpre1:
            pacman.aur("yay")  # Yay
        if "2" in pkgpre1:
            pacman.aur("paru")  # Paru
        if "3" in pkgpre1:
            pacman.aur("pikaur")  # Pikaur
        if "4" in pkgpre1:
            clear()  # Snapd
            words.snapd()
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
            words.pamac()
            print(
                "1:Install pamac AUR\n2:Install pamac Flatpak\n3:Install pamac nosnap\n0:Cancelar"
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
                    print("Nothing Selected")
        if "0" in pkgpre1:  # Cancelar
            break


def escritorios():
    while True:
        clear()
        words.desk_wms()
        print("1:WM's\n2:Desks\n0:Back")
        pregunta_wm = str(input(":"))
        if "1" in pregunta_wm:
            while True:
                clear()
                words.wms()
                print("1:i3wm\n2:awesome\n3:icewm\n4:bspwm\n0:Atrás")
                pregunta_wm_1 = str(input(":"))
                if "1" in pregunta_wm_1:
                    pacman.install("i3 i3lock i3 autotiling i3blocks i3status")
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
                words.desks()
                print(
                    "1:XFCE4\n2:GNOME\n3:KDE Plasma\n4:LXDE\n5:Cinnamon\n6:Mate\n0:Back"
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
        words.other()
        print(
            "1:Install i3 dependencies(requiere repo chaotic)\n2:Replace\n3:Install Kernels\n0:Back"
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
                words.kernels()
                print("1:Linux\n2:xanmod\n3:zen\n0:Back")
                pregunta_kernel = str(input(":"))
                match pregunta_kernel:
                    case "1":
                        pacman.install("linux linux-headers")
                    case "2":
                        pacman.aur("linux-xanmod linux-xanmod-headers")
                    case "3":
                        pacman.install("linux-zen linux-zen-headers")
                    case "0":
                        break
        if "0" in pregunta_otros:
            break


while True:
    try:
        clear()
        words.start_text()
        print(
            "1:Apps and Drivers\n2:Package managers\n3:Desks/WM's\n4:Change Shell\n5:Others\n0:Back"
        )
        pregunta_inicial = str(input(":"))
        if "1" in pregunta_inicial:  # Apps y dependencias
            clear()
            words.apps_and_drivers()
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
        if pregunta_inicial == "shit":  # Mierda
            sys("espeak shit >/dev/null 2>&1")
        if "0" in pregunta_inicial:
            break  # Salir
    except (ValueError, TypeError):
        print("Error")
clear()
words.final()
