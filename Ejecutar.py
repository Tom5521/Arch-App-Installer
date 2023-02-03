
from os import system as sys
def clear():
    sys("clear")
clear()
sys("sudo pacman -Sy")
#sys("pacman -Q xonsh git > src/temp")
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
print("Elige que vercion ejecutar\n1:vercion xonsh(Stable)\n2:Vercion python(En desarrollo)")
pre_vers = int(input(":"))
if pre_vers == 1:
    sys("xonsh src/main.xsh")
if pre_vers == 2:
    sys("python src/main.py")
else:
    pass