
import time
import palabras
from os import system as sys

def clear():
    sys("clear")

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
            sys("sudo pacman -Sy")
            clear()
            sys("echo Exito!")
        if "2" in pregunta_repos: #Chaotic-AUR
            sys("sudo pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com")
            sys("sudo pacman-key --lsign-key FBA220DFC880C036")
            sys("sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'")
            clear()
            sys("sudo pacman -Sy")
            clear()
            sys('sudo echo "[chaotic-aur]" >> /etc/pacman.conf')
            sys('sudo echo "Include = /etc/pacman.d/chaotic-mirrorlist" >> /etc/pacman.conf')
            sys('sudo pacman -Syy')
            clear()
        if pregunta_repos == "0":
            break

def yay_install():
    clear()
    ("cd /tmp")
    ("git clone https://aur.archlinux.org/yay.git")
    clear()
    ("cd yay")
    ("makepkg --needed --noconfirm -si")
    ("clear")
    ("cd ~")

def dependenciasG():
    clear()
    sys("yay --noconfirm -S wine mangohud game-devices-udev gamemode linux-xanmod linux-xanmod-headers vulkan-icd-loader lib32-vulkan-icd-loader lib32-vulkan-intel vulkan-intel vkd3d lib32-vkd3d")
    clear()
    sys("sudo pacman -Syu")
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
                    sys("sudo pacman -S firefox --noconfirm")
                if "2" in pregunta_navegador: #Chromium
                    clear()
                    sys("sudo pacman -S chromium --noconfirm")
                if "3" in pregunta_navegador: #Opera
                    clear()
                    sys("sudo pacman -S opera --noconfirm")
                if "4" in pregunta_navegador: #Brave
                    clear()
                    sys("cd /tmp")
                    sys("git clone https://aur.archlinux.org/brave.git")
                    clear()
                    sys("cd brave")
                    sys("makepkg -si --noconfirm")
                    clear()
                    sys("cd ~")
                if "5" in pregunta_navegador: #Chrome
                    clear()
                    sys("cd /tmp")
                    sys("git clone https://aur.archlinux.org/google-chrome.git")
                    clear()
                    sys("cd google-chrome")
                    sys("makepkg -si --noconfirm")
                    clear()
                    sys("cd ~")
                if "6" in pregunta_navegador: #Tor
                    clear()
                    sys("sudo pacman -S tor --noconfirm")
                if "0" in pregunta_navegador: #Cancelar
                    pass
            if "2" in apre1: #Correo
                clear()
                palabras.mail()
                print("Seleciona la o las apps que quieres instalar\n1:Thunderbird\n2:Mailspring\n3:Kmail\n0:Atras")
                pregunta_correo = str(input(":"))
                if "1" in pregunta_correo: #Thunderbird
                    clear()
                    sys("sudo pacman -S thunderbird --noconfirm")
                if "2" in pregunta_correo: #Mailspring
                    sys("cd /tmp")
                    clear()
                    sys("git clone https://aur.archlinux.org/mailspring.git")
                    clear()
                    sys("cd mailspring")
                    sys("makepkg -si --noconfirm")
                    clear()
                    sys("cd ~")
                if "3" in pregunta_correo: #Kmail
                    clear()
                    sys("sudo pacman -S kmail --noconfirm")
                if "0" in pregunta_correo: #Atras
                    pass
            if "3" in apre1: #Mensajeria
                clear()
                palabras.mensajeria()
                print("Elige lo que quieres instalar:\n1:Discord\n2:Skype\n3:Teamspeak\n4:Telegram\n5:Zoom\n0:Atras")
                pregunta_mensajes = str(input(":"))
                if "1" in pregunta_mensajes: #Discord
                    clear()
                    sys("sudo pacman -S discord --noconfirm")
                if "2" in pregunta_mensajes: #Skype
                    sys("cd /tmp")
                    clear()
                    sys("git clone https://aur.archlinux.org/skypeforlinux-stable-bin.git")
                    sys("cd skypeforlinux-stable-bin")
                    clear()
                    sys("makepkg -si --noconfirm")
                    clear()
                    sys("cd ~")
                if "3" in pregunta_mensajes: #Teamspeak
                    clear()
                    sys("sudo pacman -S teamspeak3 --noconfirm")
                if "4" in pregunta_mensajes: #Telegram
                    clear()
                    sys("sudo pacman -S telegram-desktop --noconfirm")
                if "5" in pregunta_mensajes: #Zoom
                    clear()
                    sys("cd /tmp")
                    sys("git clone https://aur.archlinux.org/zoom.git")
                    clear()
                    sys("cd zoom")
                    sys("makepkg -si --noconfirm")
                    sys("cd ~")
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
                sys("sudo pacman -S vlc --noconfirm")
            if "2" in pregunta_video: #mpv
                clear()
                sys("sudo pacman -S mpv --noconfirm")
            if "3" in pregunta_video: #gthumb
                clear()
                sys("sudo pacman -S gthumb --noconfirm")
            if "4" in pregunta_video: #gimp
                clear()
                sys("sudo pacman -S gimp --noconfirm")
            if "5" in pregunta_video: #krita
                clear()
                sys("sudo pacman -S krita --noconfirm")
            if "6" in pregunta_video: #kdenlive
                clear()
                sys("sudo pacman -S kdenlive --noconfirm")
            if "7" in pregunta_video: #Netfilx
                sys("cd /tmp")
                clear()
                sys("git clone https://aur.archlinux.org/netflix-nativefier.git")
                clear()
                sys("cd netflix-nativefier")
                sys("makepkg -si --noconfirm")
                clear()
            if "8" in pregunta_video: #Obs-studio
                clear()
                sys("sudo pacman -S obs-studio --noconfirm")
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
                        sys("cd /tmp")
                        clear()
                        sys("git clone https://aur.archlinux.org/visual-studio-code-bin.git")
                        sys("cd visual-studio-code-bin")
                        clear()
                        sys("makepkg -si --noconfirm")
                        clear()
                        sys("cd ~")
                if "2" in pregunta_ide: #Code OSS
                    clear()
                    sys("sudo pacman -S code --noconfirm")
                if "3" in pregunta_ide: #Pycharm Comunity
                    clear()
                    sys("sudo pacman -S pycharm-community-edition --noconfirm")
                if "4" in pregunta_ide: #Eclipse-Java
                    clear()
                    sys("cd /tmp")
                    sys("git clone https://aur.archlinux.org/eclipse-java.git")
                    clear()
                    sys("cd eclipse-java")
                    sys("makepkg -si --noconfirm")
                    sys("cd ~")
                if "5" in pregunta_ide: #Kate
                    clear()
                    sys("sudo pacman -S kate --noconfirm")
                if "6" in pregunta_ide: #Freecad
                    clear()
                    sys("sudo pacman -S freecad --noconfirm")
                if "7" in pregunta_ide: #Android Studio
                    sys("cd /tmp")
                    clear()
                    sys("git clone https://aur.archlinux.org/android-studio.git")
                    ("cd android-studio")
                    clear()
                    sys("makepkg -si --noconfirm")
                    sys("cd ~")
                    clear()
                if "8" in pregunta_ide: #Anbox
                    sys("cd /tmp")
                    clear()
                    sys("git clone https://aur.archlinux.org/anbox-git.git")
                    clear()
                    sys("cd anbox-git")
                    sys("makepkg -si --noconfirm")
                    clear()
                    sys("cd ~")
                if "9" in pregunta_ide: #Github Cli
                    clear()
                    sys("sudo pacman -S github-cli --noconfirm")
                if "10" in pregunta_ide:
                    if pregunta_ide == "1" and "0":
                        pass
                    else:   
                        clear()
                        sys("cd /tmp")
                        sys("git clone https://aur.archlinux.org/github-desktop.git")
                        clear()
                        sys("cd github-desktop")
                        sys("makepkg -si --noconfirm")
                        clear()
                        sys("cd ~")
                if pregunta_ide == "0": #Atras
                    break
        if "4" in apre: #Gaming
            clear()
            palabras.gaming()
            print("Escoje que instalar\n1:Steam\n2:Lutris\n3:Wine\n4:proton-ge\n5:Play on Linux\n6:Mindustry\n7:Drivers\n0:Atras")
            pregunta_juegos = str(input(":"))
            if "1" in pregunta_juegos: #Steam
                clear()
                ("sudo pacman -S steam --noconfirm")
            if "2" in pregunta_juegos: #Lutris
                clear()
                ("sudo pacman -S lutris --noconfirm")
            if "3" in pregunta_juegos: #Wine
                clear()
                ("sudo pacman -S wine --noconfirm")
            if "4" in pregunta_juegos: #Proton-ge-custom-bin
                sys("cd /tmp")
                clear()
                sys("git clone https://aur.archlinux.org/proton-ge-custom-bin.git")
                sys("cd proton-ge-custom-bin")
                clear()
                sys("makepkg -si --noconfirm")
                clear()
                sys("cd ~")
            if "5" in pregunta_juegos: #Play on Linux
                sys("cd /tmp")
                clear()
                sys("git clone https://aur.archlinux.org/playonlinux.git")
                sys("cd playonlinux")
                clear()
                sys("makepkg -si --noconfirm")
                clear()
                sys("cd ~")
            if "6" in pregunta_juegos: #Mindustry
                clear()
                sys("cd /tmp")
                sys("git clone https://aur.archlinux.org/mindustry-bin.git")
                sys("cd mindustry-bin")
                clear()
                sys("makepkg -si --noconfirm")
                clear()
            if "7" in pregunta_juegos: #Drivers
                clear()
                #dependencias_desarrollo() --rc
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
                ("sudo pacman -S spotify-launcher --noconfirm")
            if "2" in pregunta_musica: #Spotify Adblock
                sys("cd /tmp")
                clear()
                sys("git clone https://aur.archlinux.org/spotify-adblock.git")
                sys("cd spotify-adblock")
                clear()
                sys("makepkg -si --noconfirm")
                clear()
            if "3" in pregunta_musica: #Spotube
                sys("cd /tmp")
                clear()
                sys("git clone https://aur.archlinux.org/spotube-bin.git")
                sys("cd spotube-bin")
                clear()
                sys("makepkg -si --noconfirm")
                clear()
            if "4" in pregunta_musica: #Clementine
                clear()
                sys("sudo pacman -S clementine --noconfirm")
            if "5" in pregunta_musica: #YT Music
                sys("cd /tmp")
                clear()
                sys("git clone https://aur.archlinux.org/youtube-music.git")
                sys("cd youtube-music")
                clear()
                sys("makepkg -si --noconfirm")
                clear()
            if "6" in pregunta_musica: #Audacity
                clear()
                sys("sudo pacman -S audacity --noconfirm")
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
                sys("cd /tmp")
                clear()
                sys("git clone https://aur.archlinux.org/openoffice-bin.git")
                sys("cd openoffice-bin")
                clear()
                sys("makepkg -si --noconfirm")
                sys("cd ~")
            if "3" in pregunta_oficina:
                ("cd /tmp")
                clear()
                sys("git clone https://aur.archlinux.org/onlyoffice-bin.git")
                sys("cd onlyoffice-bin")
                clear()
                sys("makepkg -si --noconfirm")
                sys("cd ~")
            if "4" in pregunta_oficina:
                sys("cd /tmp")
                clear()
                sys("git clone https://aur.archlinux.org/wps-office-all-dicts-win-languages.git")
                sys("cd wps-office-all-dicts-win-languages")
                clear()
                sys("makepkg -si --noconfirm")
                sys("cd ~")
            if "0" in pregunta_oficina:
                pass
        if "0" in apre: #Salir
            clear()
            print("Saliendo...")
            time.sleep(0.1)
            break


