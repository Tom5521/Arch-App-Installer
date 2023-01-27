#!/usr/bin/env bash
sudo pacman -S xonsh git --noconfirm
cd .datos
sudo cp palabras.py /usr/lib/python3.10/
clear
echo Cargando...
xonsh base.xsh
#:v
