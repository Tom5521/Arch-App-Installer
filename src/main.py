# Creado por Tom5521 o Angel pa'los cuates
# Bajo la licencia GPL 3.0

# Arch-Instalator MAIN v3.4.1

from time import sleep as sl
import palabras
import base
import pacman
from os import system as sys


def clear():
    sys("clear")


while True:
    try:
        clear()
        palabras.texto_inicial()
        print(
            "1:Apps y Drivers\n2:Gestores de paquetes\n3:Escritorios/WM's\n4:Cambiar Shell\n5:Otros\n0:Salir"
        )
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
            base.pkgman()  # Gestores de paquetes
        if "3" in pregunta_inicial:
            base.escritorios()  # Escritorios/wm's
        if "4" in pregunta_inicial:
            base.cambiar_shell()  # Cambiar shell
        if "5" in pregunta_inicial:
            base.otros()  # Otros
        if "0" in pregunta_inicial:
            break  # Salir
    except (ValueError, TypeError):
        print("Error")
clear()
palabras.Final()
