from datetime import datetime

from gestionarJson import cargar, guardar, generar_id
from validaciones import validar_entero, nombre_valido, numero_valido, direccion_valida
from gestionHerramientas import ARCHIVOHISTORIAL, listar_herramienta

ARCHIVO = "Usuarios.json"

def guardar_usuario():
    usuarios=cargar(ARCHIVO)

    nombre=input('Ingrese el nombre del usuario ')
    while nombre_valido(nombre)==False:
        nombre=input('Ingrese un nombre de usuario valido ')
    
    
    apellido=input('ingrese el apellido del usuario ')
    while nombre_valido(apellido)==False:
        apellido=input('Ingrese un apellido valido ')
    
    telefono=input('Ingrese su numero telefonico sin espacios ')
    while numero_valido(telefono)==False:
        telefono=input('ingrese numero valido ')
    
    direccion=input('ingrese su direccion correctamente ')
    while direccion_valida(direccion)==False:
        direccion=input('ingrese una direccion valida ')
    
    listar_herramienta()
    
    Herramienta_escogida = input("Ingrese el ID de la herramienta del usuario: ").strip()

    while not Herramienta_escogida.isdigit() or not existeHerramienta(Herramienta_escogida):
        Herramienta_escogida = input("Error, ID inválido o no existe. Ingrese nuevamente: ").strip()

    herramienta = obtenerHerramienta(Herramienta_escogida)

    print("\nHerramienta encontrada:")
    print("ID:", herramienta["id"])
    print("Nombre:", herramienta["Nombre"])
    print("Categoría:", herramienta["Categoria"])
    print("Estado:", herramienta["Estado"])
    print("Cantidad:", herramienta["Cantidad"])
    
    nuevo_usuario={
        "id": generar_id(usuarios) ,
        "Nombre": nombre,
        "Apellido": apellido,
        "Telefono": telefono,
        "Direccion": direccion,
        "id_herramienta": Herramienta_escogida
    }
    usuarios.append(nuevo_usuario)
    guardar(ARCHIVO,usuarios)
    print('UUSUARIO GUARDADO!')

def listar_usuario():
    usuarios=cargar(ARCHIVO)

    if not usuarios:
        print ("No hay usuarios\n")
        return

    for elemento in usuarios:
        print(f'ID: {elemento["id"]} -> Nombre: {elemento["Nombre"]} -> Apellido: {elemento["Apellido"]} -> Telefono: {elemento["Telefono"]} -> Direccion: {elemento["Direccion"]} -> id_herramienta: {elemento["id_herramienta"]}')
    print()


def existeHerramienta(id_herramienta):
    lista_herramientas = cargar("Herramientas.json")

    for elemento in lista_herramientas:
        if int(id_herramienta) == elemento["id"]:
            return True

    return False


def obtenerHerramienta(id_herramienta):
    lista_herramientas = cargar("Herramientas.json")

    for elemento in lista_herramientas:
        if int(id_herramienta) == elemento["id"]:
            return elemento

    return None

def eliminar_usuario():
    id_usuario=input('ingrese el id a eliminar ')
    lista_usuarios = cargar(ARCHIVO)

    id_usuario = int(id_usuario)

    for usuario in lista_usuarios:
        if usuario["id"] == id_usuario:
            lista_usuarios.remove(usuario)
            guardar(ARCHIVO, lista_usuarios)
            print("Usuario eliminado correctamente.")
            return True
    
    print("No existe un usuario con ese ID.")
    return False

def actualizar_usuario():
    id_usuarios=input('Ingrese el id a actualizar ')
    listar_usuario=cargar(ARCHIVO)
    
    id_usuarios= validar_entero(id_usuarios)

    while(id_usuarios==None):
        listar_usuario ()
        id_usuarios=validar_entero("Error, Escoja el id a actualizar ")
        
    for elemento in listar_usuario:
        if id_usuarios==elemento["id"]:
            nombre=input('Ingrese el nombre del usuario ')
            while nombre_valido(nombre)==False:
                nombre=input('Ingrese un nombre valido ')
            elemento["Nombre"]=nombre

            apellido=input('Ingrese el apellido del usuario ')
            while nombre_valido(apellido)==False:
                apellido=input('ingrese un apellido valido ')
            elemento["Apellido"]=apellido

            telefono=input('Ingrese el telefono del usuario ')
            while numero_valido(telefono)==False:
                telefono=input('Ingrese un numero valido ')
            elemento["Telefono"]=telefono

            direccion=input('Ingrese la direccion ')
            while direccion_valida(direccion)==None:
                direccion=input('Ingrese una direccion valida ')
            elemento["Direccion"]=direccion

            listar_herramienta()
    
            Herramienta_escogida = input("Ingrese el ID de la herramienta del usuario: ").strip()

            while not Herramienta_escogida.isdigit() or not existeHerramienta(Herramienta_escogida):
                Herramienta_escogida = input("Error, ID inválido o no existe. Ingrese nuevamente: ").strip()

            herramienta = obtenerHerramienta(Herramienta_escogida)

            print("\nHerramienta encontrada:")
            print("ID:", herramienta["id"])
            print("Nombre:", herramienta["Nombre"])
            print("Categoría:", herramienta["Categoria"])
            print("Estado:", herramienta["Estado"])
            print("Cantidad:", herramienta["Cantidad"])

            guardar(ARCHIVO, listar_usuario)
            print('Usuario actualizado!')
            return
    print("La herramienta no existe. \n")