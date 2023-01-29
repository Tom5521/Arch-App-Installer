
from os import system as sys
def clear():
    sys("clear")
clear()
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