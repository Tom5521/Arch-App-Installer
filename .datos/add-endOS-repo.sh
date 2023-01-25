#!/usr/bin/env bash
clear
sudo pacman-key --keyserver keyserver.ubuntu.com -r 003DB8B0CB23504F
sudo pacman-key --lsign 003DB8B0CB23504F
clear
sudo echo "[endeavouros]" >> /etc/pacman.conf
sudo echo "SigLevel = PackageRequired" >> /etc/pacman.conf
sudo echo "Include = /etc/pacman.d/endeavouros-mirrorlist" >> /etc/pacman.conf
sudo cp endeavouros-mirrorlist /etc/pacman.d/
clear
sudo pacman -Syu --noconfirm
clear
echo Exito!
#Esta llenito de clears innesesarios xD