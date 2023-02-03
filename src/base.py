
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

