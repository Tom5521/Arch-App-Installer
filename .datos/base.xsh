#!/usr/bin/env xonsh
import time
def base():
    clear
    sudo pacman -Sy
    clear
    sudo pacman -Su git devtools ntfs-3g neovim flatpak fakeroot gcc make vi vim neovim --noconfirm
    clear
def yay_install():
    clear
    cd /tmp
    git clone https://aur.archlinux.org/yay.git
    clear
    cd yay
    makepkg --noconfirm -si
    clear
    cd ~
def dependenciasG():
    clear
    echo Instalando dependencias para gaming...
    yay --noconfirm -S wine mangohud game-devices-udev gamemode linux-xanmod linux-xanmod-headers vulkan-icd-loader lib32-vulkan-icd-loader lib32-vulkan-intel vulkan-intel vkd3d lib32-vkd3d
    clear
    yes | yay --noconfirm
    clear
def el_resto():
    clear
    yay -S yay --noconfirm
    echo Instalando dependencias graficas...
    yes | yay --noconfirm -S mkinitcpio-firmware python-lsp-server
    clear
    yes | yay --noconfirm
def apps():
    clear
    yay --noconfirm -S kbackup gimp bitwarden lmms qbittorrent scrcpy kdenlive  htop kruler neofetch python3 clementine obs-studio whatsapp-nativefier spotify firefox lutris winetricks
    clear btop vi vim neovim
    flatpak --assumeyes install app/net.brinkervii.grapejuice/x86_64/stable
    clear
    yay -Syu --noconfirm
def permisos_snapd():
    clear
    sudo systemctl enable --now snapd.socket
    sudo ln -s /var/lib/snapd/snap /snap
    sudo systemctl enable --now snapd.apparmor
    sudo apparmor_parser -r /etc/apparmor.d/*snap-confine*
    sudo apparmor_parser -r /var/lib/snapd/apparmor/profiles/snap confine*
    clear
def cambiar_shell():
    clear
    print("1:fish\n2:zsh\n3:bash")
    shellpre = int(input("Que shell deseas poner?\n:"))
    if shellpre == 1: #Shell fish
        clear
        sudo pacman -S fish --noconfirm
        clear
        chsh -s /bin/fish
    if shellpre == 2: #Shell zsh
        clear
        sudo pacman -S zsh --noconfirm
        clear
        chsh -s /bin/zsh
    if shellpre == 3: #Shell Bash
        clear
        sudo pacman -S bash --noconfirm
        clear
        chsh -s /bin/bash
    clear
while True:
    try:
        clear
        print("1:Instalar Apps y dependencias\n2:Instalar snapd\n3:Instalar Solo yay\n4:Añadir repositorios nesesarios\n5:Cambiar Shell\n6:Borrar dependencias de instalacion(Significa que terminaste)\n0:Cancelar")
        pre1 = str(input("Seleccionar una o mas opciones\n:"))
        if "1" in pre1: #Menu de Apps y dependencias
            clear
            print("1:Solo Dependencias\n2:Solo Apps\n3:Ambos\n4:Instalar dependencias i3\n")
            pre2 = str(input(":"))
            if "1" in pre2:
                base()
                c = str(input("Instalar yay?-y/n\n:"))
                if c == "y":
                    yay_install()
                el_resto()
                b = str(input("Instalar apps y programas para gaming(Exclusivo graficas y prosesadores intel)?-y/n\n:"))
                if b == "y":
                    dependenciasG()
                clear
                print("Listo!")
            if "2" in pre2: #Instalar solo Apps
                base()
                yya = str(input("Instalar yay?-y/n\n:"))
                if yya == "y":
                    yay_install()
                apps()
                clear
            if "3" in pre2: #Instalar dependencias y Apps
                base()
                c = str(input("Instalar yay?-y/n\n:"))
                if c == "y":
                    yay_install()
                el_resto()
                b = str(input("Instalar dependencias para gaming?-y/n\n:"))
                if b == "y":
                    dependenciasG()
                apps()
                clear
                print("Listo!")
            if "4" in pre2: #Instalar i3
                clear
                yay -Su
                clear
                yay --noconfirm -S - < lista-de-paquetes-i3
                clear
                yes|yay --noconfirm -S gnome-screenshot alsa-utils xscreensaver acpid mousepad-git
                clear
                print("\nListo!\n")
        if "2" in pre1: #Instalar Snapd
            clear
            pr1 = int(input("Quieres descargar el paquete por...?\n1=yay(debe estar instalado)\n2=git clone\n:"))
            if pr1 == 1:
                clear
                yay --noconfirm -S snapd
                permisos_snapd()
                clear
                print("\nListo!\n")
            if pr1 == 2:
                clear
                cd /tmp
                git clone https://aur.archlinux.org/snapd.git
                cd snapd
                makepkg --noconfirm -si
                permisos_snapd()
                cd ~
                clear
                print("\nListo!\n")
            if pr1 < 2:
                clear
                print("Selecciona Correctamente")
                time.sleep(0.5)
        if "3" in pre1: #Instalar yay
            clear
            yay_install()
            clear
            print("\nListo!\n")
        if "4" in pre1: #Instalar repos
            clear
            print("Instando repos...")
            sudo repos.sh
            clear
        if "5" in pre1: #Cambiar Shell
            cambiar_shell()
        if "6" in pre1: #Borrar basura
            clear
            yes|yay
            clear
            yes|yay -c
            clear
            yes|sudo pacman -R yay xonsh
            clear
            print("Saliendo...")
            sl(0.5)
            break
        if "0" in pre1: #Salida
            clear
            print("Cancelando...")
            break
        else: #Error
            clear
            print("Pon un numero")
            sl(1.5)
            clear
    except (ValueError):
        clear
        print("Pon un numero")
        time.sleep(1.5)
        clear
clear
print("Instalacion Terminada")
