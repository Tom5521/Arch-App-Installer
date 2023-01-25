#!/usr/bin/env xonsh
import time
yay_rem = True
def base():
    clear
    sudo pacman -Syu git nano make --noconfirm
    clear
def yay_install():
    clear
    cd /tmp
    git clone https://aur.archlinux.org/yay.git
    clear
    cd yay
    makepkg --needed --noconfirm -si
    clear
    cd ~
def paru_install():
    clear
    cd /tmp
    git clone https://aur.archlinux.org/paru.git
    clear
    cd paru
    makepkg --needed --noconfirm -si
    clear
    cd ~
def pikaur_install():
    clear
    cd /tmp
    git clone https://aur.archlinux.org/pikaur.git
    clear
    cd pikaur
    makepkg -si --needed --noconfirm
    cd ~
    clear
def pamac_install():
    print("1:Instalar pamac AUR\n2:Instalar pamac Flatpak\n3:Instalar pamac nosnap\n0:Cancelar")
    pamac_pre1 = int(input(":"))
    if pamac_pre1 == 1: #pamac-aur
        clear
        cd /tmp
        git clone https://aur.archlinux.org/pamac-aur.git
        cd pamac-aur
        clear
        makepkg -si --needed --noconfirm
        cd ~
        clear
    if pamac_pre1 == 2: #pamac-flatpak
        clear
        cd /tmp
        git clone https://aur.archlinux.org/pamac-flatpak.git
        cd pamac-flatpak
        clear
        makepkg -si --needed --noconfirm
        cd ~
        clear
    if pamac_pre1 == 3: #pamac-nosnap
        clear
        cd /tmp
        git clone https://aur.archlinux.org/pamac-nosnap.git
        cd pamac-nosnap
        clear
        makepkg -si --needed --noconfirm
    if pamac_pre1 == 0: #Salida
        clear
        pass
    if pamac_pre1 > 3: #Error
        clear
        print("Selecciona solo una opcion")
        time.sleep(0.5)
        clear
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
    clear
    yes | yay --noconfirm -S mkinitcpio-firmware python-lsp-server
    clear
    yes | yay --noconfirm
    clear
def apps_desarrollo():
    while True:
        clear
        print("Escoje una categoria de apps a instalar\n1:Internet\n2:Imagen y Video\n3:Desarrollo\n4:Gaming\n5:Musica\n6:Entretenimiento\n0:Salir")
        apre = str(input(":"))
        if "1" in apre:
            clear
            print("")
        if "2" in apre:
            clear
        if "3" in apre:
            clear
        if "4" in apre:
            clear
        if "5" in apre:
            clear
        if "6" in apre:
            clear
        if "0" in appre:
            clear
            print("Saliendo...")
            time.sleep(0.1)
            break
def apps():
    clear
    yay --noconfirm -S kbackup gimp bitwarden qbittorrent scrcpy kdenlive  htop kruler neofetch python3 clementine obs-studio whatsapp-nativefier spotify firefox lutris btop vi vim neovim visual-studio-code-bin
    clear
    yay -Syu --noconfirm
    clear
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
        clear
    if shellpre == 2: #Shell zsh
        clear
        sudo pacman -S zsh --noconfirm
        clear
        chsh -s /bin/zsh
        clear
    if shellpre == 3: #Shell Bash
        clear
        sudo pacman -S bash --noconfirm
        clear
        chsh -s /bin/bash
        clear
    clear
def snapd_inst():
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
def pkgman():
    clear
    print("1:yay\n2:paru\n3:pikaur\n4:snapd\n5:flatpak\n6:Pamac\n0:Cancelar")
    pkgpre1 = str(input(":"))
    if "1" in pkgpre1: #Yay
        print("Instalar yay atravez de...\n1:Repositorio chaotic(Requiere añadirlo en la seccion de repos nesesarios)\n2:git clone(lento))")
        yayprk = int(input(":"))
        if yayprk == 1:
            print("Añadir repo chaotic?(Y-N)")
            add_repoch = str(input(":"))
            if add_repoch == "Y" or "y":
                sudo sh add-repo-ch.sh
                clear
                sudo pacman -S yay --noconfirm
                clear
                yay_rem = False
            if add_repoch == "N" or "n":
                yay_rem = False
                clear
                base()
                clear
                yay_install()
            else:
                clear
                print("No se seleciono ninguno")
                time.sleep(0.5)
                pass
        clear
    if "2" in pkgpre1: #Paru
        clear
        base()
        clear
        paru_install()
        clear
    if "3" in pkgpre1: #Pikaur
        cd /tmp
        git clone https://aur.archlinux.org/pikaur.git
        clear
        cd pikaur
        makepkg -si --noconfirm
        clear
    if "4" in pkgpre1: #Snapd
        snapd_inst()
    if "5" in pkgpre1: #Flatpak
        clear
        sudo pacman -S flatpak --noconfirm
        clear
    if "6" in pkgpre1: #Pamac
        pamac_install()
    if "0" in pkgpre1: #Cancelar
        clear
        print("Cancelando...")
        time.sleep(0.5)
        clear
    else:
        clear
        print("Coloca una opcion valida")
        time.sleep(0.5)
        clear
def escritorios():
    sudo pacman -Syy
    clear
    print("1:XFCE4\n2:GNOME\n3:KDE Plasma\n4:LXDE\n5:Cinnamon\n6:Mate\n0:Cancelar")
    desk_pre = str(input(":"))
    if "1" in desk_pre:
        clear
        sudo pacman -S xfce4 xfce4-goodies --noconfirm
        clear
    if "2" in desk_pre:
        clear
        sudo pacman -S gnome gnome-extra --noconfirm
        clear
    if "3" in desk_pre:
        clear
        sudo pacman -S plasma --noconfirm
        clear
    if "4" in desk_pre:
        clear
        sudo pacman -S lxde --noconfirm
        clear
    if "5" in desk_pre:
        clear
        sudo pacman -S cinnamon --noconfirm
        clear
    if "6" in desk_pre:
        clear
        sudo pacman -S mate --noconfirm
        clear
    if "0" in desk_pre:
        pass
    else:
        clear
        print("Seleciona una o mas opciones")
        time.sleep(0.5)
##########################Zona de Interaccion###############################
while True:
    try:
        clear
        print("1:Instalar Apps y dependencias\n2:Instalar gestores de paquetes\n3:Añadir Escritorios\n4:Añadir repositorios nesesarios\n5:Cambiar Shell\n6:Borrar dependencias de instalacion(Significa que terminaste)\n0:Cancelar\nEs recomendable instalar el gestor de aur yay en la seccion de gestores de paquetes para facilitar la instalacion")
        pre1 = str(input("Seleccionar una o mas opciones\n:"))
        if "1" in pre1: #Menu de Apps y dependencias
            clear
            print("1:Solo Dependencias\n2:Solo Apps\n3:Instalar dependencias i3\n4:Instalar dependencias para gaming(Exclusivo graficas y prosesadores intel)\n0:Cancelar")
            pre2 = str(input(":"))
            if "1" in pre2:
                base()
                yayy = str(input("Instalar yay?(Si no lo quiere al finalizar su instalacion en la seccion de borrar dependencias de instalacion puede borrarlo)-y/n\n:"))
                if yayy == "y":
                    yay_install()
                el_resto()
                clear
                print("Listo!")
            if "2" in pre2: #Instalar solo Apps
                base()
                yyay = str(input("Instalar yay?(Si no lo quiere al finalizar su instalacion en la seccion de borrar dependencias de instalacion puede borrarlo)-Y/n\n:"))
                if yyay == "y":
                    yay_install()
                apps()
                clear
                print("Listo!")
            if "3" in pre2: #Instalar i3
                clear
                yay -Su
                clear
                yay --noconfirm -S - < lista-de-paquetes-i3
                clear
                yes|yay --noconfirm -S gnome-screenshot alsa-utils xscreensaver acpid mousepad-git
                clear
                print("\nListo!\n")
            if "4" in pre2:
                dependenciasG()
            if pre2 == "0": #Cancelar
                pass
        if "2" in pre1: #Menu de gestores de paquetes (pkgman)
            clear
            pkgman()
            clear
        if "3" in pre1: #Inciar Escritorios
            clear
            escritorios()
            clear
        if "4" in pre1: #Instalar repos
            clear
            print("Instando repos...")
            sudo sh add-endOS-repo.sh
            sudo sh ad-repo-ch.sh
            clear
        if "5" in pre1: #Cambiar Shell
            cambiar_shell()
        if "6" in pre1: #Borrar basura
            clear
            print("Elige una o mas opciones\n1:Escriba los paquetes que quiere eliminar seguidos de un salto de linea\n2:Borrado automatico")
            rm_pre = str(input())
            if "1" in rm_pre:
                nano rem
                clear
                sudo pacman -R - < rem --noconfirm
                clear
                rm rem
            if "2" in rm_pre:
                clear
                yes|yay -c
                clear
                if yay_rem == True:
                    sudo pacman -R yay --noconfirm
                if flat_rem == True:
                    sudo pacman -R flatpak --noconfirm
                sudo pacman -R xonsh --noconfirm
            clear
            print("Saliendo...")
            time.sleep(0.5)
            break
        if "0" in pre1: #Salida
            clear
            print("Cancelando...")
            break
        else: #Error
            clear
            print("Pon un numero")
            time.sleep(1.5)
            clear
    except (ValueError):
        clear
        print("Pon un numero")
        time.sleep(1.5)
        clear
clear
print("Instalacion Terminada")
