#!/usr/bin/env xonsh

#Creado Por Angel Alderete
#Instalador de mis cosas V-dev
#"Donde los commits crashean al iniciar"
#Re-estructurado

import palabras
import time
import baseINS as base
###############################Comprobacion#de#yay###################################
yay_rem = True
pacman -Q yay > src/test
test_open = open("src/test","r")
test_read = test_open.read()
if "yay" in test_read:
    yay_rem = False
else:
    yay_rem = True
###############################Comprobacion#de#yay###################################
while True:
    try:
        clear
        palabras.texto_inicial()
        print("1:Apps y dependencias\n2:Gestores de paquetes\n3:Escritorios/WM's\n4:Cambiar Shell\n5:Borrar Basura\n6:Otros\n0:Salir")
        pregunta_inicial = str(input(":"))
        if "1" in pregunta_inicial: #Apps y dependencias
            clear
            palabras.apps_y_dependencias()
            print("1:Apps\n2:Dependencias\n3:Dependencias(gaming,solo intel)\n0:Atras")
            pregunta_apps_y_dependencias = str(input(":"))
            if "1" in pregunta_apps_y_dependencias: #Apps
                clear
                palabras.apps()
                base.apps_desarrollo()
            if "2" in pregunta_apps_y_dependencias: #Dependencias
                clear
                base.el_resto()
            if "3" in pregunta_apps_y_dependencias: #Dependencias Gaming
                clear
                palabras.gaming()
                base.dependenciasG()
            if "0" in pregunta_apps_y_dependencias: #Atras
                clear
                pass
        if "2" in pregunta_inicial: #Gestores de paquetes
            clear
            palabras.gestores_de_paquetes()
            base.pkgman()
            pass
        if "3" in pregunta_inicial: #Escritorios/wm's
            clear
            palabras.escritorios()
            base.escritorios()
            pass
        if "4" in pregunta_inicial: #Cambiar shell
            clear
            palabras.cambiar_shell()
            base.cambiar_shell()
            pass
        if "5" in pregunta_inicial: #Borrar basura
            clear
            palabras.borrar_basura()
            base.borrar_basura()
            rm_pre = str(input())
            if "1" in rm_pre:
                nano rem
                clear
                sudo pacman -R - < rem --noconfirm
                clear
                rm rem
                time.sleep(0.5)
                break
            if "2" in rm_pre:
                clear
                yay -c --noconfirm
                clear
                if yay_rem == True:
                    sudo pacman -R yay --noconfirm
                    print("Saliendo...")
                    time.sleep(0.5)
                break
                clear
            if "0" in rm_pre:
                clear
                pass    
            print("Saliendo...")
            time.sleep(0.5)
            break
        if "6" in pregunta_inicial: #Otros
            clear
            palabras.otros()
            base.otros()
        if "0" in pregunta_inicial:#Salir
            break
    except(ValueError,TypeError):
        print("Error")
clear
rm src/test
palabras.Final()