import os

def actualizar_maquina():
    os.system('sudo apt update && sudo apt upgrade')
    print("Actualizado.")

def acceder_enlace_1():
    os.system('xdg-open http://83.60.148.121/')
    print("Abriendo...")

def acceder_enlace_2():
    os.system('xdg-open http://83.60.148.121:8000/')
    print("Abriendo...")

def acceder_enlace_3():
    os.system('xdg-open http://83.60.148.121/wp-admin/')
    print("Abriendo...")

def playlist1():
    os.system('sudo nano /etc/ices2/ices-playlist.xml')
    print("Abriendo...")

def playlist2():
    os.system('sudo nano /etc/ices2/ices-playlist2.xml')
    print("Abriendo...")

def db():
    os.system('sudo ')

def mostrar_menu():
    print("1. Actualizar la máquina")
    print("2. Acceder a la página web Los40Asirpales")
    print("3. Acceder a la radio Los40Asirpales para monitorizacion")
    print("4. Configurar el servidor WordPress")
    print("5. Modificar Playlist Reggaeton")
    print("6. Modificar Playlist Rock")
    print("0. Salir")

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
        db()
    elif opcion == "0":
        break
    else:
        print("Selecciona un número que esté en el menú")
