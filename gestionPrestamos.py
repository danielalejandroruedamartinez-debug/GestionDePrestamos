from gestionHerramientas import ARCHIVOHISTORIAL
from gestionarJson import cargar, generar_id, guardar
from validaciones import validar_entero, validar_id_existente, validarMenu
from datetime import datetime

ARCHIVO_PRESTAMOS = "Prestamos.json"
ARCHIVO_HERRAMIENTAS = "Herramientas.json"

def crear_solicitud(id_usuario):

    prestamos = cargar(ARCHIVO_PRESTAMOS)
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)

    print("-- SOLICITUD DE PRÉSTAMO ---")

    id_herramienta = validar_id_existente(ARCHIVO_HERRAMIENTAS)

    herramienta_encontrada = next((h for h in herramientas if h["id"] == id_herramienta), None)

    if herramienta_encontrada["Cantidad"] <= 0:
        print("No hay stock disponible para esta herramienta.")
        return

    fecha_prestamo_dt = datetime.now()
    fecha_prestamo = fecha_prestamo_dt.strftime("%Y-%m-%d")

    while True:
        fecha_devolucion = input("Ingrese fecha de devolución (YYYY-MM-DD): ")

        try:
            fecha_devolucion_dt = datetime.strptime(fecha_devolucion, "%Y-%m-%d")

            if fecha_devolucion_dt <= fecha_prestamo_dt:
                print("La fecha de devolución debe ser posterior a la fecha actual.")
                continue

            break

        except ValueError:
            print("Formato inválido. Use YYYY-MM-DD.")


    if prestamos:
        nuevo_id = max(p["id_prestamo"] for p in prestamos) + 1
    else:
        nuevo_id = 1

    nueva_solicitud = {
        "id_prestamo": nuevo_id,
        "id_usuario": id_usuario,
        "id_herramienta": id_herramienta,
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": fecha_devolucion,
        "estado": "pendiente"
    }

    prestamos.append(nueva_solicitud)
    guardar(ARCHIVO_PRESTAMOS, prestamos)

    print("Solicitud registrada correctamente y enviada al administrador.")

def gestionar_prestamos():

    prestamos = cargar(ARCHIVO_PRESTAMOS)
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)

    pendientes = [p for p in prestamos if p["estado"] == "pendiente"]

    if not pendientes:
        print("No hay solicitudes pendientes.")
        return

    print("\n--- SOLICITUDES PENDIENTES ---")

    for p in pendientes:
        print(f"""
ID Préstamo: {p["id_prestamo"]}
Usuario: {p["id_usuario"]}
Herramienta: {p["id_herramienta"]}
Fecha préstamo: {p["fecha_prestamo"]}
Fecha devolución: {p["fecha_devolucion"]}
Estado: {p["estado"]}
---------------------------
""")
    while True:
        dato = input("Ingrese ID del préstamo a gestionar: ")
        id_prestamo = validar_entero(dato)

        if id_prestamo is None:
            continue

        prestamo = next(
            (p for p in pendientes if p["id_prestamo"] == id_prestamo),
            None
        )

        if prestamo is None:
            print("El ID no corresponde a un préstamo pendiente.")
            continue

        break

    while True:

        op = validarMenu("""
1. Aceptar
2. Rechazar
3. Salir
Seleccione: """, 1, 3)

        match op:

            case 1:

                herramienta = next(
                    (h for h in herramientas if h["id"] == prestamo["id_herramienta"]),
                    None
                )

                if herramienta and herramienta["Cantidad"] > 0:

                    herramienta["Cantidad"] -= 1
                    prestamo["estado"] = "aceptado"

                    guardar(ARCHIVO_HERRAMIENTAS, herramientas)
                    guardar(ARCHIVO_PRESTAMOS, prestamos)

                    print("Préstamo aprobado correctamente.")
                else:
                    print("No hay stock disponible.")

                break

            case 2:

                prestamo["estado"] = "rechazado"
                guardar(ARCHIVO_PRESTAMOS, prestamos)

                print("Solicitud rechazada.")
                break

            case 3:
                print("Saliendo...")
                break