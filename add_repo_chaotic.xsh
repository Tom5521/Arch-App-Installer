#!/bin/xonsh
sudo pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com
sudo pacman-key --lsign-key FBA220DFC880C036
sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'
yay

sudo echo "[chaotic-aur]" >> /etc/pacman.conf
sudo echo "Include = /etc/pacman.d/chaotic-mirrorlist" >> /etc/pacman.conf
yay

sudo echo "[endeavouros]" >> /etc/pacman.conf
sudo echo "SigLevel = PackageRequired" /etc/pacman.conf
sudo echo "Include = /etc/pacman.d/endeavouros-mirrorlist" >> /etc/pacman.conf
sudo cp endeavouros-mirrorlist /etc/pacman.d/
yay
sudo pacman-key --keyserver keyserver.ubuntu.com -r 003DB8B0CB23504F
sudo pacman-key --lsign 003DB8B0CB23504F

yes|yay --noconfirm
print("Exito")