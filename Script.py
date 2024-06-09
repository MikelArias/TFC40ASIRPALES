import os

#Opción para actualizar la máquina
def actualizar_maquina():
    os.system('sudo apt update && sudo apt upgrade')
    print("Actualizado.")

#Opción para acceder a la página web Los40Asirpales
def acceder_enlace_1():
    os.system('xdg-open http://83.60.148.121/')
    print("Abriendo...")
    
#Opción para acceder a la radio para monitorearla
def acceder_enlace_2():
    os.system('xdg-open http://83.60.148.121:8000/')
    print("Abriendo...")

#Opción para acceder a gestionar la página WordPress
def acceder_enlace_3():
    os.system('xdg-open http://83.60.148.121/wp-admin/')
    print("Abriendo...")
    
#Opción para editar la playlist de Reggaeton
def playlist1():
    os.system('sudo nano /etc/ices2/ices-playlist.xml')
    print("Abriendo...")

#Opción para editar la playlist de Rock
def playlist2():
    os.system('sudo nano /etc/ices2/ices-playlist2.xml')
    print("Abriendo...")

#Opción para iniciar la radio
def radio():
    os.system('sudo ices2 /etc/ices2/ices-playlist.xml & sudo ices2 /etc/ices2/ices-playlist2.xml &')

#Menú que contiene las opciones
def mostrar_menu():
    print("1. Actualizar la máquina")
    print("2. Acceder a la página web Los40Asirpales")
    print("3. Acceder a la radio Los40Asirpales para monitorizacion")
    print("4. Configurar el servidor WordPress")
    print("5. Modificar Playlist Reggaeton")
    print("6. Modificar Playlist Rock")
    print("7. Iniciar radio")
    print("0. Salir")

#Bucle para que funcione el menú
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        actualizar_maquina()
    elif opcion == "2":
        acceder_enlace_1()
    elif opcion == "3":
        acceder_enlace_2()
    elif opcion == "4":
        acceder_enlace_3()
    elif opcion == "5":
        playlist1()
    elif opcion == "6":
        playlist2()
    elif opcion == "7":
        radio()
    elif opcion == "0":
        break
    else:
        print("Selecciona un número que esté en el menú")
