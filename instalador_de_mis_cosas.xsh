#!/usr/bin/env xonsh
def base():
    sudo pacman -Syu wget git asp bat devtools fish zsh tar ntfs-3g rofi neovim mousepad-git btop flatpak fakeroot gcc make vi vim neovim --noconfirm
def yay_install():
    cd /tmp
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg --noconfirm -si
    cd ~
def dependenciasG():
    echo Instalando dependencias para gaming...
    yay --noconfirm -S wine mangohud lutris game-devices-udev winetricks gamemode linux-xanmod
    yes | yay --noconfirm
def el_resto():
    yay -S yay --noconfirm
    echo Instalando dependencias graficas...
    yes | yay --noconfirm -S vulkan-icd-loader lib32-vulkan-icd-loader lib32-vulkan-intel vulkan-intel vkd3d lib32-vkd3d mkinitcpio-firmware python-lsp-server
    yes | yay --noconfirm
def apps():
    yay --noconfirm -S kbackup gimp bitwarden lmms qbittorrent scrcpy kdenlive  htop kruler neofetch python3 clementine obs-studio archlinux-tweak-tool-git whatsapp-nativefier spotify firefox
    flatpak --assumeyes install app/net.brinkervii.grapejuice/x86_64/stable
    yay -Syu --noconfirm
def permisos_snapd():
    sudo systemctl enable --now snapd.socket
    sudo ln -s /var/lib/snapd/snap /snap
    sudo systemctl enable --now snapd.apparmor
    sudo apparmor_parser -r /etc/apparmor.d/*snap-confine*
    sudo apparmor_parser -r /var/lib/snapd/apparmor/profiles/snap confine*
def cambiar_shell():
    sudo chsh -s /bin/fish angel
while True:
    try:
        print("1=Solo dependencias\n2=Solo Apps\n3=Ambos\n4=Instalar snapd\n5=Instalar Solo yay\n6=Instalar dependencias i3(Requiere repo endeavouros)\n7=Instalar xfce\n8=Añadir repositorios nesesarios\n0=Salir")
        a = int(input("Seleccionar Opcion\n:"))
        if a == 1:
            base()
            c = str(input("Instalar yay?-y/n\n"))
            if c == "y":
                yay_install()
            cambiar_shell()
            el_resto()
            b = str(input("Instalar dependencias para gaming?-y/n\n:"))
            if b == "y":
                dependenciasG()
            print("Listo!")
        if a == 2:
            apps()
            cambiar_shell()
        if a == 3:
            base()
            cambiar_shell()
            c = str(input("Instalar yay?-y/n\n:"))
            if c == "y":
                yay_install()
            el_resto()
            b = str(input("Instalar dependencias para gaming?-y/n\n:"))
            if b == "y":
                dependenciasG()
            apps()
            print("Listo!")
        if a == 4:
            pr1 = int(input("Quieres descargar el paquete por...?\n1=yay(debe estar instalado)\n2=git clone\n:"))
            if pr1 == 1:
                yay --noconfirm -S snapd
                permisos_snapd()
                print("\nListo!\n")
            if pr1 == 2:
                cd /tmp
                git clone https://aur.archlinux.org/snapd.git
                cd snapd
                makepkg --noconfirm -si
                permisos_snapd()
                cd ~
                print("\nListo!\n")
        if a == 5:
            yay_install()
            print("\nListo!\n")
        if a == 6:
            yay --noconfirm -S - < i3
            yes|yay --noconfirm -S gnome-screenshot alsa-utils xscreensaver acpid
            print("\nListo!\n")
        if a == 7:
            sudo pacman -S xfce4-goodies xfce4 --noconfirm
        if a == 8:
            sudo xonsh add_repo_chaotic.sh
        if a == 0:
            print("Saliendo...")
            break
        if a > 8:
            print("No se selecciono ninguno")
    except (ValueError):
        print("Por favor pon el valor correcto")
