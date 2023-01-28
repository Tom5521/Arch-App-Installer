
import os

from os import system as sys
def clear():
    sys("clear")
clear()
os.system("sudo cp src/palabras.py /usr/lib/python3.10/")
os.system("sudo cp src/base_defs.xsh /usr/lib/python3.10/")
sys("sudo pacman -Sy")
sys("pacman -Q xonsh git > src/temp")
clear()
testop = open("src/temp","r")
test = testop.read()
if "xonsh" in test:
    pass
else:
    clear()
    sys("sudo pacman -S xonsh --noconfirm")
    clear()
if "git" in test:
    pass
else:
    clear()
    sys("sudo pacman -S git --noconfirm")
    clear()
clear()
sys("xonsh src/main.xsh")
sys("sudo rm /usr/lib/python3.10/base_defs.xsh")
sys("sudo rm /usr/lib/python3.10/palabras.py")