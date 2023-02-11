# Creado por Tom5521 o Angel pa'los cuates
# Bajo la licencia GPL 3.0

# Arch-Instalator EJECUTOR v3.4.1

from os import listdir, mkdir
from os import system as sys


def clear():
    sys("clear")
    pass


clear()
syupd = listdir("/tmp")
if "inst-temp" in syupd:
    pass
else:
    print("Actualizando Repositorios...")
    sys("sudo pacman -Syy >/dev/null 2>&1")
    mkdir("/tmp/inst-temp")
clear()

sys("pacman -Q git > src/temp")

clear()

testop = open("src/temp", "r")
test = testop.read()

if "git" in test:
    pass
else:
    clear()
    print("Instalando git...")
    sys("sudo pacman -S git --noconfirm |ls > .out && rm -rf .out")
sys("rm src/temp")
sys("python src/main.py")
