
#Creado Por Angel Alderete

#Arch-Instalator v3.3.0

from time import sleep as sl
import palabras
import base
from os import system as sys

###############################Comprobacion#de#yay###################################
yay_rem = True
sys("pacman -Q yay > src/temp")
test_open = open("src/temp","r")
test_read = test_open.read()            
if "yay" in test_read: yay_rem = False
else: yay_rem = True
sys("rm src/temp")
###############################Comprobacion#de#yay###################################
def clear():
    sys("clear")

while True:
    try:
        clear()
        palabras.texto_inicial()
        print("1:Apps y Drivers\n2:Gestores de paquetes\n3:Escritorios/WM's\n4:Cambiar Shell\n5:Borrar Basura\n6:Otros\n0:Salir")
        pregunta_inicial = str(input(":"))
        if "1" in pregunta_inicial: #Apps y dependencias
            clear()
            palabras.apps_y_drivers()
            print("1:Apps\n2:Drivers\n0:Atras")
            pregunta_apps_y_dependencias = str(input(":"))
            if "1" in pregunta_apps_y_dependencias: base.apps_desarrollo()#Apps
            if "2" in pregunta_apps_y_dependencias: base.dependencias_desarrollo()#Dependencias
            if pregunta_apps_y_dependencias == "DEFG": #Dependencias Gaming
                clear()
                palabras.gaming()
                base.dependenciasG()
            if "0" in pregunta_apps_y_dependencias: #Atras
                clear()
                pass
        if "2" in pregunta_inicial: base.pkgman()#Gestores de paquetes
        if "3" in pregunta_inicial: base.escritorios()#Escritorios/wm's
        if "4" in pregunta_inicial: base.cambiar_shell()#Cambiar shell
        if "5" in pregunta_inicial: #Borrar basura
            clear()
            palabras.borrar_basura()
            print("Elige una o mas opciones\n1:Escriba los paquetes que quiere eliminar seguidos de un salto de linea\n2:Borrado automatico\n0:Atras")
            rm_pre = str(input(":"))
            if "1" in rm_pre:
                ("nano rem")
                clear()
                ("sudo pacman -R - < rem --noconfirm")
                clear()
                ("rm rem")
                sl(0.5)
                break
            if "2" in rm_pre:
                clear()
                ("yay -c --noconfirm")
                clear()
                if yay_rem == True:
                    ("sudo pacman -R yay --noconfirm")
                    break
                clear()
                break
            if "0" in rm_pre:
                clear()
                pass
        if "6" in pregunta_inicial: base.otros()#Otros
        if "0" in pregunta_inicial: break#Salir
    except(ValueError,TypeError): print("Error")
clear()
palabras.Final()
