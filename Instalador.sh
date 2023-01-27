#!/usr/bin/env bash
sudo cp palabras.py /usr/lib/python3.10/
sudo pacman -S xonsh git nano --noconfirm
cd .datos
xonsh base.xsh
#:v
