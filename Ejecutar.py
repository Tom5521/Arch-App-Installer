
import os

from os import system as sys
def clear():
    sys("clear")
clear()
os.system("sudo cp src/palabras.py /usr/lib/python3.10/")
os.system("sudo cp src/baseINS.xsh /usr/lib/python3.10/")
sys("sudo pacman -Sy")
sys("pacman -Q xonsh git > src/test")
clear()
testop = open("src/test","r")
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
sys("xonsh src/visual.xsh")
sys("sudo rm /usr/lib/python3.10/baseINS.xsh")
sys("sudo rm /usr/lib/python3.10/palabras.py")