def validar_entero(dato):

    if dato == "":
        print("Error: no se ingresó ningún valor.")
        return None

    elif not dato.isdigit():
        print("Error: debe ingresar solo números enteros positivos.")
        return None

    elif int(dato) == 0:
        print("Error: el número debe ser mayor que cero.")
        return None

    else:
        return int(dato)


def validarMenu(mensaje, minimo, maximo):
    try:
        dato=int(input(mensaje))
        if dato<minimo or dato>maximo:
            return None
        else:
            return dato
    except:
        return None


def nombre_valido(mensaje):
    if mensaje.isalpha():
        return True
    elif mensaje.strip()=="":
        print("Dato vacio")
        return False
    else:
        print("Dato invalido, ingrese solo letras")
        return False


def numero_valido(mensaje):
    dato = mensaje.strip()

    if dato == "":
        print("Número vacío")
        return False

    if len(dato) == 10 and dato.isdigit():
        return True
    else:
        print("Número inválido, ingrese solo números de 10 dígitos")
        return False


def direccion_valida(direccion):
    dato = direccion.lower().strip()

    tipos_via = ["calle", "carrera", "avenida", "transversal", "diagonal"]

    if not any(dato.startswith(tipo) for tipo in tipos_via):
        print("Debe empezar con Calle, Carrera, Avenida, Transversal o Diagonal")
        return False

    partes = dato.split()

    if len(partes) < 3:
        print("Formato incompleto")
        return False

    numeros = [p for p in partes if any(c.isdigit() for c in p)]

    if len(numeros) < 2:
        print("Faltan números de dirección")
        return False

    return True


def validar_estado(estado):
    dato = estado.lower().strip()

    partes = dato.split()
    if len(partes) > 1:
        print("Ingrese un solo estado ")
        return False

    tipos_estado = ["obsoleta", "dañada", "perfecta", "funcional", "arreglada"]

    if not any(dato.startswith(tipo) for tipo in tipos_estado):
        print("Estado incorrecto. Debe ser: obsoleta, dañada, perfecta, funcional o arreglada")
        return False

    return True


def validar_acceso(contraseña):
    contraseña_correcta = "1234"
    
    if contraseña == contraseña_correcta:
        print("Acceso concedido.")
        return True
    else:
        print("Contraseña incorrecta.")
        return False


def validar_id_existente(ARCHIVO):
    from gestionarJson import cargar
    from validaciones import validar_entero 

    datos = cargar(ARCHIVO)

    while True:
        dato = input("Ingrese el ID del usuario: ")

        id_ingresado = validar_entero(dato)

        if id_ingresado is None:
            continue

        for elemento in datos:
            if elemento["id"] == id_ingresado:
                return id_ingresado

        print("Error: el ID no existe en el archivo.")


from gestionarJson import cargar, guardar
from datetime import datetime

ARCHIVO_HISTORIAL = "Historial.json"

def registrar_accion(id_usuario, accion, detalle=""):
    
    historial = cargar(ARCHIVO_HISTORIAL)

    if historial is None:
        historial = []

    nueva_accion = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "usuario": id_usuario,
        "accion": accion,
        "detalle": detalle
    }

    historial.append(nueva_accion)

    guardar(ARCHIVO_HISTORIAL, historial)

    
ARCHIVO_HISTORIAL = "HistorialExamen.json"

def registrar_accion_Examen(id_herramienta, accion, detalle=""):
    
    historial = cargar(ARCHIVO_HISTORIAL)

    if historial is None:
        historial = []

    nueva_accion = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "herramienta": id_herramienta,
        "accion": accion,
        "detalle": f" La herramienta: {detalle}, ha sido actualizada"
    }

    historial.append(nueva_accion)

    guardar(ARCHIVO_HISTORIAL, historial)



print ("esto es una prueva de commit")
