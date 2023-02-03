
from os import system as sys

def clear():
    sys("clear")

clear()

sys("sudo pacman -Sy")
sys("pacman -Q git > src/temp")

clear()

testop = open("src/temp","r")
test = testop.read()

if "git" in test:
    pass
else:
    clear()
    sys("sudo pacman -S git --noconfirm")
    clear()

clear()

sys("python src/main.py")