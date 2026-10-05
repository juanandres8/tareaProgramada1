#-------------------------------------------
#Menú General
#-------------------------------------------
#Importacion de librerias
from cargaDatos import *
from procesarNombres import *
from procesarPoblacion import *

#def funciones
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

    salir=False
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
        opcion=int(input())
       
        if opcion== 1:
                print()
                print("Cantidad de países cargados:", cantidadPaises(data))
                print()
                mayorPoblacion(data)
                print()
                menorArea(data)
                print()
                print("Cantidad de monedas descargadas:", cantidadMonedas(data))
                print()
                monedasMayorValor(data)
                print()
                monedasMenorValor(data)
        elif opcion== 2:
                
                # Leer el .toon
                dataToon = leer("paises.toon")

                # Actualizar los nombres
                actualizarNombres(dataToon)

                # Volver a leer después de actualizar
                dataToon = leer("paises.toon")

                print( "-Longitud promedio de nombres: ",longitudPromedio(dataToon))
                print()
                paisLargo = nombreMasLargo(dataToon)
                print("-País con nombre más largo: "+ paisLargo+ " - "+ str(len(paisLargo)))
                print()
                paisCorto = nombreMasCorto(dataToon)
                print("-País con nombre más corto: "+ paisCorto+ " - "+ str(len(paisCorto)))
                print()
                letra = input("Ingrese una letra: ")
                cantidad = cantidadLetraEnPaises(dataToon,letra)
                print("-Cantidad de países que contienen la letra "+ letra+ ": "+ str(cantidad))
        elif opcion== 3:
                print("-Población total del mundo:", poblacionTotal(paises))
                print()
                print("-Población mundial promedio:", poblacionPromedio(paises))
                print()
                print("-Mediana de poblaciones:", medianaPoblacion(paises))
                print()
                print("-Clasificación de países:")
                clasificarPaises(paises)
                print()
                print("-Área total de todos los países:", areaTotal(paises), "km²")
                print()
                mayorDensidad(paises)
                print()
                menorDensidad(paises)
        elif opcion ==9:
                salir=True
    return print("Menú cerrado")
##pp
menu()
