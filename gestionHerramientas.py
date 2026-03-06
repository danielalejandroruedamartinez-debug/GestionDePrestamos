import datetime

from gestionarJson import cargar, guardar, generar_id
from validaciones import registrar_accion_Examen, validar_entero, validarMenu, nombre_valido, validar_estado

ARCHIVO= "Herramientas.json"
ARCHIVOHISTORIAL = "Historial.json"
ARCHIVOEXAMEN = "HistorialExamen.json"
def guardar_herramientas():
    herramientas=cargar(ARCHIVO)

    nombre=input('Ingrese el nombre de la  herramienta')
    while nombre_valido(nombre)==False or existeNombre(nombre)==True:
        nombre=input('Ingrese un nombre valido ')
    
    categoria=input('Ingrese la cateroria de la herramienta')
    while nombre_valido(categoria)==False or existeNombre(categoria)==True:
        categoria=input('Ingrese una categoria valida')

    estado=input('Ingrese el estado de la herramienta (obsoleta, dañada,perfecta,funcional)')
    while validar_estado(estado)==False or existeNombre(estado)==True:
        estado=input('Ingrese un estado valido')

    cantidad=input('Ingrese la cantidad de la herramienta')
    while validar_entero(cantidad)==None:
        cantidad=input('Ingrese una cantidad valida')

    nueva_herramienta={
        "id": generar_id(herramientas) ,
        "Nombre": nombre,
        "Categoria": categoria,
        "Estado": estado,
        "Cantidad": int(cantidad)
    }
    herramientas.append(nueva_herramienta)
    guardar(ARCHIVO,herramientas)
    print('HERRAMIENTA GUARDADA!')

def listar_herramienta  ():
    herramientas=cargar(ARCHIVO)

    if not herramientas:
        print ("No existe la herramienta\n")
        return

    for elemento in herramientas:
        print(f'ID: {elemento["id"]} -> Nombre: {elemento["Nombre"]} -> Categoria: {elemento["Categoria"]} -> Estado: {elemento["Estado"]}-> Cantidad: {elemento["Cantidad"]} ')
    print()

def existeNombre(nombre):
    herramientas=cargar(ARCHIVO)
    for elemento in herramientas:
        if nombre.lower()==elemento["Nombre"].lower():
            return True
    return False


def actualizar_herramienta():
    herramientas = cargar(ARCHIVO)
    listar_herramienta()

    # Validar ID correctamente
    while True:
        dato = input("Escoja el id a actualizar: ")
        id_herramienta = validar_entero(dato)

        if id_herramienta is not None:
            break

    for elemento in herramientas:
        if id_herramienta == elemento["id"]:

            # Nombre
            while True:
                nombre = input('Ingrese el nombre de la herramienta: ')
                if nombre_valido(nombre):
                    break
            elemento["Nombre"] = nombre

            # Categoría
            while True:
                categoria = input('Ingrese la categoria: ')
                if nombre_valido(categoria):
                    break
            elemento["Categoria"] = categoria

            # Estado
            while True:
                estado = input('Ingrese el estado de la herramienta: ')
                if validar_estado(estado):
                    break
            elemento["Estado"] = estado
            registrar_accion_Examen(elemento["id"], "actualizar_herramienta", f"Nombre: {nombre}, Categoria: {categoria}, Estado: {estado}")

            # Cantidad (CORREGIDO)
            while True:
                dato = input('Ingrese la cantidad: ')
                cantidad = validar_entero(dato)

                if cantidad is not None:
                    break

            elemento["Cantidad"] = cantidad

            guardar(ARCHIVO, herramientas)
            print('Herramienta actualizada!')
            return
        

    print("La herramienta no existe.\n")
    

def eliminar_herramienta():
    herramientas = cargar(ARCHIVO)
    listar_herramienta()

    # Validar ID correctamente
    while True:
        dato = input("Escoja el id a eliminar: ")
        id_herramienta = validar_entero(dato)

        if id_herramienta is not None:
            break

    # Buscar y eliminar
    for i, elemento in enumerate(herramientas):
        if id_herramienta == elemento["id"]:
            herramientas.pop(i)
            guardar(ARCHIVO, herramientas)
            print("Herramienta eliminada!")
            return

    print("La herramienta no existe.\n")

def listar_herramienta_examen  ():
    herramientas=cargar(ARCHIVOEXAMEN)

    if not herramientas:
        print ("No existe la herramienta\n")
        return

    for elemento in herramientas:
        print(f'fecha: {elemento["fecha"]} -> herramienta: {elemento["herramienta"]} -> accion: {elemento["accion"]} -> detalle: {elemento["detalle"]} ')
    print()