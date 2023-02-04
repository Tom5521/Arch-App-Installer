
import os
from os import system as sys

def clear():
    sys("clear")
    pass


syupd = os.listdir("/tmp")
if "inst-temp" in syupd:
    pass
else:
    sys("sudo pacman -Sy")
    os.mkdir("/tmp/inst-temp")
def clear():
    sys("clear")
    pass

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

sys("sudo python src/main.py")