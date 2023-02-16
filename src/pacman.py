# Created by Tom5521 or Angel
# Under the license GPL 3.0

# PY-pacman https://github.com/Tom5521/PY-pacman

# V1.2.0 MOD

from os import getcwd, chdir
from os import system as sys
from time import sleep as sl

current_directoy = getcwd()


def clear():
    sys("clear")


def installed():
    print("Installed")
    sl(1)


sp = " "


def check(nombre_check):
    comprobator = False
    chdir(current_directoy)
    clear()
    sys("pacman -Q " + nombre_check + "> /tmp/tmp-check")
    optemp = open("/tmp/tmp-check", "r")
    readtemp = optemp.read()
    if nombre_check in readtemp:
        comprobator = True
    else:
        comprobator = False
    sys("rm /tmp/tmp-check")
    return comprobator


def install(nombre_pacman, cond_1="", cond_2=""):
    match cond_1:
        case "-v":
            print("Installing " + nombre_pacman + "...")
            sys("sudo pacman -S " + nombre_pacman + sp + cond_2 + sp + " --noconfirm")
            print("Installed")
        case _:
            clear()
            print("Installing " + nombre_pacman + "...")
            sys(
                "sudo pacman -S "
                + nombre_pacman
                + " --noconfirm"
                + sp
                + cond_1
                + "|ls > .out && rm -rf .out"
            )
            clear()
            installed()


def refresh():
    clear()
    print("Updating repos...")
    sys("sudo pacman -Syy >/dev/null 2>&1")
    clear()
    print("Repos Updated")


def aur(nombre_aur):
    for i in nombre_aur.split():
        clear()
        url = "https://aur.archlinux.org/" + i + ".git"
        chdir("/tmp")
        print("Cloning " + i + "...")
        sys("git clone " + url + ">/dev/null 2>&1")
        clear()
        chdir(i)
        print("Installing " + i + "...")
        sys("makepkg -si --noconfirm >/dev/null 2>&1")
        clear()
        chdir(current_directoy)
        installed()


def upgrade(condu_1="", condu_2=""):
    match condu_1:
        case "-v":
            print("Updating...")
            sys("sudo pacman -Syu --noconfirm" + sp + condu_2)
        case _:
            clear()
            print("Updating...")
            sys("sudo pacman -Syu --noconfirm" + sp + condu_1 + sp + ">/dev/null 2>&1")
            clear()
            print("Completed update")


def remove(package):
    clear()
    sys("sudo pacman -R " + package + " --noconfirm" + ">/dev/null 2>&1")
    print("Removed")
