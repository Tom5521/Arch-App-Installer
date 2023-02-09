
# Creado por Tom5521 o Angel pa'los cuates
# Bajo la licencia GPL 3.0

# Arch-Instalator MAIN v3.4.0

from time import sleep as sl
import palabras
import base
import pacman
from os import system as sys


def clear():
    sys("clear")


yay_test = pacman.check("yay")
match yay_test:
    case True:
        yay_rem = False
    case _:
        pass
while True:
    try:
        clear()
        palabras.texto_inicial()
        print("1:Apps y Drivers\n2:Gestores de paquetes\n3:Escritorios/WM's\n4:Cambiar Shell\n5:Borrar Basura\n6:Otros\n0:Salir")
        pregunta_inicial = str(input(":"))
        if "1" in pregunta_inicial:  # Apps y dependencias
            clear()
            palabras.apps_y_drivers()
            print("1:Apps\n2:Drivers\n0:Atrás")
            pregunta_apps_y_dependencias = str(input(":"))
            if "1" in pregunta_apps_y_dependencias:
                base.apps_desarrollo()  # Apps
            if "2" in pregunta_apps_y_dependencias:
                base.dependencias_desarrollo()  # Dependencias
            if pregunta_apps_y_dependencias == "DEFG":  # Dependencias Gaming
                clear()
                palabras.gaming()
                base.basura.dependenciasG()
            if "0" in pregunta_apps_y_dependencias:  # Atrás
                clear()
                pass
        if "2" in pregunta_inicial:
            yay_rem = base.pkgman()  # Gestores de paquetes
        if "3" in pregunta_inicial:
            base.escritorios()  # Escritorios/wm's
        if "4" in pregunta_inicial:
            base.cambiar_shell()  # Cambiar shell
        if "5" in pregunta_inicial:  # Borrar basura
            clear()
            palabras.borrar_basura()
            print("Elige una o mas opciones\n1:Escriba los paquetes que quiere eliminar seguidos de un salto de linea\n2:Borrado automatico\n0:Atrás")
            rm_pre = str(input(":"))
            match rm_pre:
                case "1":
                    clear()
                    sys("nano rem")
                    clear()
                    sys("sudo pacman -R - < rem --noconfirm|ls > .out && rm -rf .out")
                    sys("rm rem")
                    break
                case "2":
                    clear()
                    sys("yay -c --noconfirm|ls > .out && rm -rf .out")
                    match yay_rem:
                        case True:
                            clear()
                            sys("sudo pacman -R yay --noconfirm|ls > .out && rm -rf .out")
                        case False:
                            pass
                        case _: break
                case "0": pass
        if "6" in pregunta_inicial:
            base.otros()  # Otros
        if "0" in pregunta_inicial:
            break  # Salir
    except (ValueError, TypeError):
        print("Error")
clear()
palabras.Final()
