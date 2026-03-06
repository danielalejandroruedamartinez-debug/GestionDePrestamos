from datetime import datetime

from gestionarJson import cargar, generar_id, guardar
from validaciones import validarMenu, validar_id_existente, validar_acceso
from gestionUsuarios import guardar_usuario, listar_usuario, eliminar_usuario, actualizar_usuario
from gestionHerramientas import ARCHIVOEXAMEN, ARCHIVOHISTORIAL, guardar_herramientas, eliminar_herramienta, listar_herramienta, actualizar_herramienta, listar_herramienta_examen
from gestionPrestamos import crear_solicitud, gestionar_prestamos

ARCHIVO= "Usuarios.json"




def herramientas():
    while True:
        op2=validarMenu('''
                            1. Agregar
                            2. Actualizar
                            3. Eliminar
                            4. Listar
                            5. Salir
                            ''',1,5)
        while op2==None:
                op2=validarMenu('Error, intente nuevamente!',1,5)
        match op2:
            case 1:
                historiales=cargar(ARCHIVOHISTORIAL)
                historial={
                    "id": generar_id(historiales),
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "accion": "agregar herramienta"
                }
                historiales.append(historial)
                guardar(ARCHIVOHISTORIAL, historiales)
                guardar_herramientas()
            case 2:
                historiales=cargar(ARCHIVOHISTORIAL)
                historial={
                    "id": generar_id(historiales),
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "accion": "actualizar herramienta"
                }
                historiales.append(historial)
                guardar(ARCHIVOHISTORIAL, historiales)
                actualizar_herramienta()
            case 3:
                historiales=cargar(ARCHIVOHISTORIAL)
                historial={
                    "id": generar_id(historiales),
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "accion": "eliminar herramienta"
                }
                historiales.append(historial)
                guardar(ARCHIVOHISTORIAL, historiales)
                eliminar_herramienta()
            case 4:
                historiales=cargar(ARCHIVOHISTORIAL)
                historial={
                    "id": generar_id(historiales),
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "accion": "listar herramientas"
                }
                historiales.append(historial)
                guardar(ARCHIVOHISTORIAL, historiales)
                listar_herramienta()
            case 5:
                print('...')
            case _:
                print('No se encontró la opción.')
        if op2==5:
            break

def personas():
    while True:
        op2=validarMenu('''
                            1. Agregar
                            2. Actualizar
                            3. Eliminar
                            4. Listar
                            5. Salir
                            ''',1,5)
        while op2==None:
                op2=validarMenu('Error, intente nuevamente!',1,5)
        match op2:
            case 1:
                historiales=cargar(ARCHIVOHISTORIAL)
                historial={
                    "id": generar_id(historiales),
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "accion": "agregar usuario"
                }
                historiales.append(historial)
                guardar(ARCHIVOHISTORIAL, historiales)
                guardar_usuario()
            case 2:
                historiales=cargar(ARCHIVOHISTORIAL)
                historial={
                    "id": generar_id(historiales),
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "accion": "actualizar usuario"
                }
                historiales.append(historial)
                guardar(ARCHIVOHISTORIAL, historiales)
                actualizar_usuario()
            case 3:
                historiales=cargar(ARCHIVOHISTORIAL)
                historial={
                    "id": generar_id(historiales),
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "accion": "eliminar usuario"
                }
                historiales.append(historial)
                guardar(ARCHIVOHISTORIAL, historiales)
                listar_usuario()
                eliminar_usuario()
            case 4:
                historiales=cargar(ARCHIVOHISTORIAL)
                historial={
                    "id": generar_id(historiales),
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "accion": "listar usuarios"
                }
                historiales.append(historial)
                guardar(ARCHIVOHISTORIAL, historiales)
                listar_usuario()
            case 5:
                print('...')
            case _:
                print('No se encontró la opción.')
        if op2==5:
            break

def menu_admin():
    while True:
        op=validarMenu('''
                        1. Usuario
                        2. Herramienta
                        3. Buscar usuario
                        4. Gestionar prestamos
                        5. Historial de herramientas examen
                        6. Salir
                        ''',1,6)   
        while op==None:
            op=validarMenu('Error, intente nuevamente!',1,6)
        match op:
            case 1:
                personas()
            case 2:
                herramientas()
            case 3:
                historiales=cargar(ARCHIVOHISTORIAL)
                historial={
                    "id": generar_id(historiales),
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "accion": "buscar usuario"
                }
                historiales.append(historial)
                guardar(ARCHIVOHISTORIAL, historiales)
                buscar_usuario (ARCHIVO)
            case 4:
                historiales=cargar(ARCHIVOHISTORIAL)
                historial={
                    "id": generar_id(historiales),
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "accion": "Gestionar prestamos"
                }
                historiales.append(historial)
                guardar(ARCHIVOHISTORIAL, historiales)
                gestionar_prestamos()
            case 5:
                historiales=cargar(ARCHIVOEXAMEN)
                listar_herramienta_examen()
            case 6:
                print('Gracias por usar nuestro servicio')
            case _:
                print('NO SE ENCUENTRA LA OPCION')
        if op==6: 
            break

def menu_usuario():
    while True:
        op=validarMenu('''
                        1. Usuarios
                        2. Herramientas
                        3. Solicitar prestamo
                        4. Salir
                        ''',1,4)   
        while op==None:
            op=validarMenu('Error, intente nuevamente!',1,4)
        match op:
            case 1:
                historiales=cargar(ARCHIVOHISTORIAL)
                historial={
                    "id": generar_id(historiales),
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "accion": "listar usuarios"
                }
                historiales.append(historial)
                guardar(ARCHIVOHISTORIAL, historiales)
                listar_usuario()
            case 2:
                historiales=cargar(ARCHIVOHISTORIAL)
                historial={
                    "id": generar_id(historiales),
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "accion": "listar herramientas"
                }
                historiales.append(historial)
                guardar(ARCHIVOHISTORIAL, historiales)
                listar_herramienta()
            case 3:
                historiales=cargar(ARCHIVOHISTORIAL)
                historial={
                    "id": generar_id(historiales),
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "accion": "solicitar prestamo"
                }
                historiales.append(historial)
                guardar(ARCHIVOHISTORIAL, historiales)
                crear_solicitud(id_usuario=validar_id_existente(ARCHIVO))
            case 4:
                print('Gracias por usar nuestro servicio')
            case _:
                print('NO SE ENCUENTRA LA OPCION')
        if op==4: 
            break

def login():

    while True:
        op = validarMenu(
            '''
            1. Admin
            2. Usuario
            3. Salir
            ''',
            1, 3
        )

        while op is None:
            op = validarMenu('Error, intente nuevamente!', 1, 3)

        match op:

            case 1:
                contraseña = input('Ingrese la contraseña: ')
                while validar_acceso(contraseña) == False:
                    contraseña = input('Ingrese la contraseña correcta: ')
                menu_admin()

            case 2:
                
                validar_id_existente(ARCHIVO)
                
                menu_usuario()

            case 3:
                print('Gracias por usar nuestro servicio')
                break

            case _:
                print('NO SE ENCUENTRA LA OPCIÓN')

def buscar_usuario(ARCHIVO):
    while True:
        datos = cargar(ARCHIVO)

        opcion=validarMenu('''
                        1. Buscar por ID
                        2. Buscar por Nombre
                        3. Buscar por Apellido
                        4. Salir
                        ''',1,4)
        while opcion==None:
            opcion=validarMenu('Error, intente nuevamente!',1,4)
        match opcion:
    
            case 1:
                dato = input("Ingrese el ID: ")

                if not dato.isdigit():
                    print("Error: debe ingresar un número válido.")
                    return

                id_buscar = int(dato)

                for elemento in datos:
                    if elemento["id"] == id_buscar:
                        print("\nUsuario encontrado:")
                        for clave, valor in elemento.items():
                            print(f"{clave}: {valor}")
                        return

                print("No existe un usuario con ese ID.")

    
            case 2:
                nombre_buscar = input("Ingrese el nombre: ").strip().lower()
                encontrados = False

                for elemento in datos:
                    if elemento["Nombre"].lower() == nombre_buscar:
                        print("\nUsuario encontrado:")
                        for clave, valor in elemento.items():
                            print(f"{clave}: {valor}")
                        print("-" * 30)
                        encontrados = True

                if not encontrados:
                    print("No se encontraron usuarios con ese nombre.")

    
            case 3:
                apellido_buscar = input("Ingrese el apellido: ").strip().lower()
                encontrados = False

                for elemento in datos:
                    if elemento["Apellido"].lower() == apellido_buscar:
                        print("\nUsuario encontrado:")
                        for clave, valor in elemento.items():
                            print(f"{clave}: {valor}")
                        print("-" * 30)
                        encontrados = True

                if not encontrados:
                    print("No se encontraron usuarios con ese apellido.")
        
            case 4:
                print('Gracias por usar nuestro servicio')
        

            case _:
                print("No se encuentra la opcion")
        if opcion== 4:
            break


