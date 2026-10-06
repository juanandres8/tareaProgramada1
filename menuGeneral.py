#-------------------------------------------
#Menú General
#-------------------------------------------
# Importación de librerías
# Se importan todas las funciones creadas en los otros archivos
from cargaDatos import *
from procesarNombres import *
from procesarPoblacion import *
#-------------------------------------------
# Carga inicial de los datos
#-------------------------------------------
# Se leen los datos del archivo CSV
data = leer("nombreArchivoLeer.csv")
escribirToon(data)

# Leer los datos del archivo .toon
dataToon = leer("paises.toon")

# Normalizar los nombres
actualizarNombres(dataToon)

# Volver a leer el .toon después de normalizar
dataToon = leer("paises.toon")

# Obtener datos para la opción 3
paises = obtenerDatos(dataToon)

def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    # Variable que controla cuándo termina el menú
    salir=False
     # El menú se mantiene activo mientras salir sea False
    while salir ==False:
        print()
        print("Seleccione una opcion")
        print("Opcion #1: Cargar datos de países desde archivo")
        print("Opcion #2: Procesar y normalizar nombres de países")
        print("Opcion #3: rocesar datos poblacionales y geográficos")
        print("Opcion #4: Procesar datos de monedas")
        print("Opcion #5: Generar reporte de países en TXT")
        print("Opcion #6: Generar reporte de monedas en HTML")
        print("Opcion #7: Generar reporte de densidad poblacional en HTML")
        print("Opcion #8: Bitácora de registros")
        print("Opcion #9: Salir")
        # Se solicita al usuario que seleccione una opción
        opcion=int(input())
       
        if opcion== 1:
                print()  # Muestra la cantidad de países cargados
                print("Cantidad de países cargados:", cantidadPaises(data))
                print()  # Muestra los 5 países con mayor población
                mayorPoblacion(data)
                print()  # Muestra los 5 países con menor área
                menorArea(data)
                print()  # Muestra la cantidad de monedas diferentes
                print("Cantidad de monedas descargadas:", cantidadMonedas(data))
                print()  # Muestra las 5 monedas con mayor valor frente al USD
                monedasMayorValor(data)
                print()  # Muestra las 5 monedas con menor valor frente al USD
                monedasMenorValor(data)
        elif opcion== 2:
                
                # Leer el .toon
                dataToon = leer("paises.toon")
                # Actualizar los nombres
                actualizarNombres(dataToon)
                # Volver a leer después de actualizar
                dataToon = leer("paises.toon")
                # Calcula la longitud promedio de los nombres
                print( "-Longitud promedio de nombres: ",longitudPromedio(dataToon))
                print() # Obtiene el país con el nombre más largo
                paisLargo = nombreMasLargo(dataToon)
                print("-País con nombre más largo: "+ paisLargo+ " - "+ str(len(paisLargo)))
                print() # Obtiene el país con el nombre más corto
                paisCorto = nombreMasCorto(dataToon)
                print("-País con nombre más corto: "+ paisCorto+ " - "+ str(len(paisCorto)))
                print()  # Solicita una letra al usuario
                letra = input("Ingrese una letra: ")
                # Cuenta cuántos países contienen esa letra
                cantidad = cantidadLetraEnPaises(dataToon,letra)
                print("-Cantidad de países que contienen la letra "+ letra+ ": "+ str(cantidad))
        elif opcion== 3:
                # Calcula la población total
                print("-Población total del mundo:", poblacionTotal(paises))
                print() # Calcula la población promedio
                print("-Población mundial promedio:", poblacionPromedio(paises))
                print() # Calcula la mediana de las poblaciones
                print("-Mediana de poblaciones:", medianaPoblacion(paises))
                print()# Clasifica los países según su población
                print("-Clasificación de países:")
                clasificarPaises(paises)
                print() # Calcula el área total
                print("-Área total de todos los países:", areaTotal(paises), "km²")
                print()# Muestra los 10 países con mayor densidad poblacional
                mayorDensidad(paises)
                print()# Muestra los 10 países con menor densidad poblacional
                menorDensidad(paises)
        elif opcion ==9:
            # Cambia el valor de salir a True para terminar el ciclo while
                salir=True
     # Mensaje que aparece al cerrar el menú
    return print("Menú cerrado")
##pp
menu()
