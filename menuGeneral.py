#-------------------------------------------
#Menú General
#-------------------------------------------
# Importación de librerías
# Se importan todas las funciones creadas en los otros archivos
import cargaDatos 
from procesarNombres import *
from procesarPoblacion import *
import procesarDatosMonedas
import reportePaises
import reporteMonedas
from datetime import datetime
#-------------------------------------------

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
        print("==========MENÚ GENERAL==========")
        print("Opcion #1: Cargar datos de países desde archivo")
        print("Opcion #2: Procesar y normalizar nombres de países")
        print("Opcion #3: rocesar datos poblacionales y geográficos")
        print("Opcion #4: Procesar datos de monedas")
        print("Opcion #5: Generar reporte de países en TXT")
        print("Opcion #6: Generar reporte de monedas en HTML")
        print("Opcion #7: Generar reporte de densidad poblacional en HTML")
        print("Opcion #8: Bitácora de registros")
        print("Opcion #9: Salir")
        print("=================================")
        # Se solicita al usuario que seleccione una opción
        try:
            opcion=int(input("Ingrese una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número.")
            opcion=0
        if opcion== 1:
            # Se leen los datos del archivo CSV
            data = cargaDatos.leer("nombreArchivoLeer.csv")
            cargaDatos.escribirToon(data)
            print()
            print("Cantidad de países cargados:", cargaDatos.cantidadPaises(data))
            print()  # Muestra los 5 países con mayor población
            cargaDatos.mayorPoblacion(data)
            print()  # Muestra los 5 países con menor área
            cargaDatos.menorArea(data)
            print()
            #Fecha y hora de carga de datos
            fecha=datetime.now()
            print("Fecha y hora de carga:",fecha.strftime("%d/%m/%Y %H:%M:%S"))
            print()
            print()  # Muestra la cantidad de monedas diferentes
            print("Cantidad de monedas descargadas:", cargaDatos.cantidadMonedas(data))
            print()  # Muestra las 5 monedas con mayor valor frente al USD
            cargaDatos.monedasMayorValor(data)
            print()  # Muestra las 5 monedas con menor valor frente al USD
            cargaDatos.monedasMenorValor(data)
        elif opcion== 2:
            # Leer el .toon
            dataToon = cargaDatos.leer("paises.toon")
            # Actualizar los nombres
            if dataToon:
                actualizarNombres(dataToon)
            # Volver a leer después de actualizar
                dataToon = cargaDatos.leer("paises.toon")
                if dataToon:
                    # Calcula la longitud promedio de los nombres
                    print( "-Longitud promedio de nombres: ",longitudPromedio(dataToon))
                    print() # Obtiene el país con el nombre más largo
                    paisLargo = nombreMasLargo(dataToon)
                    print("-País con nombre más largo: "+ paisLargo+ " - "+ str(len(paisLargo)))
                    print() # Obtiene el país con el nombre más corto
                    paisCorto = nombreMasCorto(dataToon)
                    print("-País con nombre más corto: "+ paisCorto+ " - "+ str(len(paisCorto)))
                    print()  # Solicita una letra al usuario
                    letra = input("Ingrese una letra: ").strip()
                    while len(letra)!=1 or not letra.isalpha():
                        print("ERROR: Debe ingresar una sola letra.")
                        letra= input("Ingrese una letra: ").strip()
                    # Cuenta cuántos países contienen esa letra
                    cantidad = cantidadLetraEnPaises(dataToon,letra)
                    print("-Cantidad de países que contienen la letra "+ letra+ ": "+ str(cantidad))
                else:
                    print("Error: El archivo de paises esta vacio")
            else:
                print("Erro: No se pudo leer el archivo de países")
        elif opcion==3:
            # Leer el .toon
            dataToon = cargaDatos.leer("paises.toon")
            if dataToon:
                paises=obtenerDatos(dataToon)
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
            else:
                print("Erro: No se pudo leer el archivo de países")
        elif opcion==4:
            # Leer los datos actualizados del archivo .toon
            dataToon =cargaDatos.leer("paises.toon")
            if dataToon:
                # Obtener las monedas con su código y nombre
                monedas =procesarDatosMonedas.obtenerMonedas(dataToon)
                # Mostrar las monedas normalizadas
                print("Monedas:")
                print(procesarDatosMonedas.formatoMonedas(dataToon))
                print()
                # Contar monedas según la cantidad de letras
                n=0
                while n<=0:
                    try:
                        n = int(input("Ingrese la cantidad de letras: "))
                        if n<=0:
                            print("ERROR: Ingrese un número mayor a cero.")
                    except ValueError:
                        print("ERROR: Debe ingresar un número entero")
                cantidad =procesarDatosMonedas.contarMonedasLetras(dataToon, n)
                print("Cantidad de monedas con", n, "letras:", cantidad)
                print()
                # Verificar si las monedas contienen tasas de cambio
                if len(monedas) > 0 and len(monedas[0]) >= 3:
                    # Calcular la tasa de cambio promedio
                    promedio = procesarDatosMonedas.calcularPromedioTasas(monedas)
                    print("Tasa de cambio promedio:", promedio)
                    print()
                    # Encontrar la moneda más fuerte y la más débil
                    fuerte, debil = procesarDatosMonedas.encontrarMonedaFuerteDebil(monedas)
                    print("Moneda más fuerte:", fuerte)
                    print("Moneda más débil:", debil)
                    print()
                    # Contar las monedas según su tasa
                    mayores, iguales, menores = procesarDatosMonedas.contarMonedasPorTasa(monedas)
                    print("Tasas mayores a 1 USD:", mayores)
                    print("Tasas iguales a 1 USD:", iguales)
                    print("Tasas menores a 1 USD:", menores)
                    print()
                    # Ordenar las monedas por tasa
                    ascendente, descendente = procesarDatosMonedas.ordenarMonedasPorTasa(monedas)
                    print("Orden ascendente:", ascendente)
                    print("Orden descendente:", descendente)
                else:
                    print("No se pueden calcular las tasas.")
                    print("Las monedas solo contienen código y nombre.")
                    print("Falta obtener la tasa de cambio de cada moneda.")
            else:
                print("ERROR: No se pudo leer el archivo de países.")
        elif opcion==5:
            dataToon=cargaDatos.leer("paises.toon")
            if dataToon is not None:
                paises=reportePaises.obtenerDatosReporte(dataToon)
                reportePaises.generarReportePaises(paises)
                print("Reporte de países generado")
        elif opcion==6:
            dataToon=cargaDatos.leer("paises.toon")
            if dataToon is not None:
                monedas=reporteMonedas.obtenerMonedas(dataToon)
                reporteMonedas.generarReporteMonedas(monedas)
        elif opcion==7:
            dataToon = cargaDatos.leer("paises.toon")
            if dataToon:
                reporteDensidad.generarReporteDensidad(dataToon)
            else:
                print("Error: No se pudo leer el archivo de países.")
        elif opcion ==9:
            # Cambia el valor de salir a True para terminar el ciclo while
                salir=True
    # Mensaje que aparece al cerrar el menú
    print("Menú cerrado")
##pp
menu()
