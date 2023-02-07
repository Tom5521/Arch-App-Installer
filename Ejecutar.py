
import os
from os import system as sys

def clear():
    sys("clear")
    pass

clear()

syupd = os.listdir("/tmp")
if "inst-temp" in syupd:
    pass
else:
    print("Actualizando Repositorios...")
    sys("sudo pacman -Syy >/dev/null 2>&1")
    os.mkdir("/tmp/inst-temp")
clear()

sys("pacman -Q git > src/temp")

clear()

testop = open("src/temp","r")
test = testop.read()

if "git" in test:
    pass
else:
    clear()
    sys("sudo pacman -S git --noconfirm")

sys("python src/main.py")