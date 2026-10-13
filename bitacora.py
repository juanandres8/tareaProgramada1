
# Importaciones
import pickle
import os
import csv
from datetime import datetime

# Definicion de funcion para registrar una accion
def registrarAccion(descripcion):
    '''
    Funcionalidad:
    Guarda una accion realizada en el menu dentro del archivo binario.
    Entradas:
    - descripcion: Texto que explica la accion realizada.
    Salidas:
    - No retorna ningun valor. Guarda el registro en bitacora.bin.
    '''
    # Obtener los registros guardados anteriormente
    registros = leerBitacora()
    # Obtener la fecha y hora actual
    fechaHora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Crear el registro con la fecha, hora y descripcion
    registro = (fechaHora, descripcion)
    # Agregar el nuevo registro a la lista
    registros.append(registro)

    try:
        # Abrir el archivo binario para guardar los registros
        archivo = open("bitacora.bin", "wb")
        # Guardar la lista utilizando el formato binario
        pickle.dump(registros, archivo)
        # Cerrar el archivo
        archivo.close()
    except Exception as error:
        # Mostrar un mensaje si ocurre un error al guardar
        print("Error al guardar la bitacora:", error)

# Definicion de funcion para leer la bitacora
def leerBitacora():
    '''
    Funcionalidad:
    Lee los registros almacenados en el archivo binario.

    Entradas:
    - No recibe parametros.

    Salidas:
    - registros: Lista de registros guardados.
    - Si el archivo no existe o no puede leerse, retorna una lista vacia.
    '''
    # Verificar si existe el archivo binario
    if not os.path.exists("bitacora.bin"):
        return []
    try:
        # Abrir el archivo en modo lectura binaria
        archivo = open("bitacora.bin", "rb")
        # Recuperar los registros almacenados
        registros = pickle.load(archivo)
        # Cerrar el archivo
        archivo.close()
        return registros
    except Exception as error:
        # Mostrar un mensaje si ocurre un error al leer
        print("Error al leer la bitacora:", error)
        return []

# Definicion de funcion para buscar registros por fecha
def buscarPorFecha():
    '''
    Funcionalidad:
    Busca los registros que coinciden con una fecha especifica.

    Entradas:
    - Fecha ingresada por el usuario en formato AAAA-MM-DD.

    Salidas:
    - Muestra los registros que coinciden con la fecha.
    '''
    # Obtener todos los registros guardados
    registros = leerBitacora()
    # Solicitar la fecha que se desea buscar
    fecha = input("Ingrese la fecha (AAAA-MM-DD): ")
    # Inicializar el contador de coincidencias
    encontrados = 0
    # Recorrer todos los registros
    for registro in registros:
        # Comparar la fecha ingresada con la fecha del registro
        if registro[0][:10] == fecha:
            # Mostrar el registro encontrado
            print(registro[0], "-", registro[1])
            # Aumentar la cantidad de coincidencias
            encontrados += 1
    # Verificar si se encontraron registros
    if encontrados == 0:
        print("No se encontraron registros para esa fecha.")

# Definicion de funcion para buscar por palabra clave
def buscarPorPalabra():
    '''
    Funcionalidad:
    Busca registros cuya descripcion contiene una palabra especifica.

    Entradas:
    - Palabra clave ingresada por el usuario.

    Salidas:
    - Muestra los registros que contienen la palabra buscada.
    '''
    # Obtener los registros almacenados
    registros = leerBitacora()
    # Solicitar la palabra que se desea buscar
    palabra = input("Ingrese una palabra clave: ").lower()
    # Inicializar el contador de coincidencias
    encontrados = 0
    # Recorrer todos los registros
    for registro in registros:
        # Comprobar si la palabra aparece en la descripcion
        if palabra in registro[1].lower():
            # Mostrar el registro encontrado
            print(registro[0], "-", registro[1])
            # Contabilizar la coincidencia
            encontrados += 1
    # Mostrar mensaje si no hubo coincidencias
    if encontrados == 0:
        print("No se encontraron coincidencias.")

# Definicion de funcion para mostrar todas las entradas
def mostrarTodas():
    '''
    Funcionalidad:
    Muestra todos los registros almacenados en la bitacora.

    Entradas:
    - No recibe parametros.

    Salidas:
    - Muestra la fecha, hora y descripcion de cada registro.
    '''
    # Recuperar los registros
    registros = leerBitacora()
    # Comprobar si existen registros
    if len(registros) == 0:
        print("La bitacora esta vacia.")
    else:
        # Recorrer y mostrar cada registro
        for registro in registros:
            print(registro[0], "-", registro[1])

# Definicion de funcion para exportar la bitacora a CSV
def exportarCSV():
    '''
    Funcionalidad:
    Exporta todos los registros de la bitacora a un archivo CSV.

    Entradas:
    - No recibe parametros.

    Salidas:
    - Crea el archivo bitacora.csv con la fecha, hora y descripcion.
    '''
    # Obtener todos los registros
    registros = leerBitacora()
    try:
        # Abrir el archivo CSV para escritura
        archivo = open("bitacora.csv", "w", newline="", encoding="utf-8")
        # Crear el escritor de datos CSV
        escritor = csv.writer(archivo, delimiter=";")
        # Escribir los encabezados de las columnas
        escritor.writerow(["Fecha y hora", "Descripcion"])
        # Escribir los registros
        for registro in registros:
            escritor.writerow([registro[0], registro[1]])
        # Cerrar el archivo
        archivo.close()
        print("Bitacora exportada a bitacora.csv.")
    except Exception as error:
        # Mostrar el error si no se puede exportar
        print("Error al exportar la bitacora:", error)

# Definicion de funcion para mostrar el submenu de bitacora
def menuBitacora():
    '''
    Funcionalidad:
    Presenta un submenu para consultar y exportar los registros.

    Entradas:
    - No recibe parametros.

    Salidas:
    - Ejecuta la opcion seleccionada hasta que el usuario decide salir.
    '''
    # Variable que controla la salida del submenu
    salir = False
    # Mantener el submenu activo mientras salir sea False
    while salir == False:
        # Mostrar las opciones disponibles
        print()
        print("-------------BITACORA------------ ")
        print("A) Buscar por fecha especifica")
        print("B) Buscar por palabra clave")
        print("C) Mostrar todas las entradas")
        print("D) Exportar bitacora a CSV")
        print("E) Salir del submenu")
        print()
        # Solicitar la opcion al usuario
        opcion = input("Seleccione una opcion: ").strip().upper()
        # Buscar registros por fecha
        if opcion == "A":
            buscarPorFecha()
        # Buscar registros por palabra clave
        elif opcion == "B":
            buscarPorPalabra()
        # Mostrar todos los registros
        elif opcion == "C":
            mostrarTodas()
        # Exportar los registros a CSV
        elif opcion == "D":
            exportarCSV()
        # Salir del submenu
        elif opcion == "E":
            salir = True
        # Manejar opciones incorrectas
        else:
            print("Opcion no valida.")
