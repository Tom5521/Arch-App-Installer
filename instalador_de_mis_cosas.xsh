#!/usr/bin/env xonsh
import time
def base():
    clear
    sudo pacman -Sy
    clear
    sudo pacman -Su wget git devtools fish tar ntfs-3g rofi neovim btop flatpak fakeroot gcc make vi vim neovim --noconfirm
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
    yay --noconfirm -S kbackup gimp bitwarden lmms qbittorrent scrcpy kdenlive  htop kruler neofetch python3 clementine obs-studio archlinux-tweak-tool-git whatsapp-nativefier spotify firefox lutris winetricks
    clear
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
    shellpre = int(input("Que shell deseas poner?"))
    if shellpre == 1:
        clear
        sudo pacman -S fish --noconfirm
        chsh -s /bin/fish
    if shellpre == 2:
        clear
        sudo pacman -S zsh --noconfirm
        chsh -s /bin/zsh
    if shellpre == 3:
        clear
        sudo pacman -S bash --noconfirm
        chsh -s /bin/bash
    clear
while True:
    try:
        clear
        print("1=Solo dependencias\n2=Solo Apps\n3=Ambos\n4=Instalar snapd\n5=Instalar Solo yay\n6=Instalar dependencias i3(Requiere repos externos)\n7=Añadir repositorios nesesarios\n8=Cambiar Shell\n0=Salir")
        pre1 = int(input("Seleccionar Opcion\n:"))
        if pre1 == 1: #Instalar solo dependencias
            base()
            c = str(input("Instalar yay?-y/n\n"))
            if c == "y":
                yay_install()
            el_resto()
            b = str(input("Instalar apps y programas para gaming?-y/n\n:"))
            if b == "y":
                dependenciasG()
            clear
            print("Listo!")
        if pre1 == 2: #Instalar solo Apps
            apps()
            clear
        if pre1 == 3: #Instalar dependencias y Apps
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
        if pre1 == 4: #Instalar Snapd
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
        if pre1 == 5: #Instalar yay
            clear
            yay_install()
            clear
            print("\nListo!\n")
        if pre1 == 6: #Instalar i3
            clear
            yay -Su
            clear
            yay --noconfirm -S - < lista-de-paquetes
            clear
            yes|yay --noconfirm -S gnome-screenshot alsa-utils xscreensaver acpid mousepad-git
            clear
            print("\nListo!\n")
        if pre1 == 7: #Instalar repos
            clear
            print("Instando repos...")
            sudo repos.sh
            clear
        if pre1 == 8: #Cambiar Shell
            cambiar_shell()
        if pre1 == 0: #Salida
            clear
            print("Saliendo...")
            break
        if pre1 > 7: #Error
            clear
            print("No se selecciono ninguno")
            time.sleep(1)
            clear
    except (ValueError):
        clear
        print("Pon un numero")
        time.sleep(1.5)
        clear
clear
print("Instalacion Terminada")
