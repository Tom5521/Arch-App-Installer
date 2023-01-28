#!/usr/bin/env xonsh

#Creado Por Angel Alderete
#Instalador de mis cosas-V2
#Re-estructurado

import palabras
import time
import baseINS as base
yay_rem = True

while True:
    try:
        clear
        palabras.texto_inicial()
        print("1:Apps y dependencias\n2:Gestores de paquetes\n3:Escritorios/WM's\n4:Cambiar Shell\n5:Borrar Basura\n6:Otros\n0:Salir")
        pregunta_inicial = str(input(":"))
        if "1" in pregunta_inicial:
            clear
            palabras.apps_y_dependencias()
            print("1:Apps\n2:Dependencias\n3:Dependencias(gaming,solo intel)\n0:Atras")
            pregunta_apps_y_dependencias = str(input(":"))
            if "1" in pregunta_apps_y_dependencias:
                clear
                palabras.apps()
                base.apps_desarrollo()
            if "2" in pregunta_apps_y_dependencias:
                clear
                palabras.gestores_de_paquetes()
                base.pkgman()
            if "3" in pregunta_apps_y_dependencias:
                clear
                palabras.gaming()
                base.dependenciasG()
            if "0" in pregunta_apps_y_dependencias:
                clear
                pass
        if "2" in pregunta_inicial:
            clear
            palabras.gestores_de_paquetes()
            base.pkgman()
            pass
        if "3" in pregunta_inicial:
            clear
            palabras.escritorios()
            base.escritorios()
            pass
        if "4" in pregunta_inicial:
            clear
            palabras.cambiar_shell()
            base.cambiar_shell()
            pass
        if "5" in pregunta_inicial:
            clear
            palabras.borrar_basura()
            base.borrar_basura()
            break
        if "6" in pregunta_inicial:
            clear
            palabras.otros()
            base.otros()
        if "0" in pregunta_inicial:
            break
    except(ValueError,TypeError):
        print("Error")
clear
palabras.Final()