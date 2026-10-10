#Importaciones
from procesarNombres import normalizarNombre, obtenerTexto
from procesarPoblacion import  obtenerDatos, poblacionTotal, areaTotal
#Funciones
#Función para clasificar un pais
def categoriaPoblacion(poblacion):
    '''
    Funcionalidad:
    Determina la categoría de un país según su población.
    Entradas:
    -poblacion: Cantidad de habitantes del país.
    Salidas:
    -categoria: Retorna la categoría correspondiente.
    '''
    if poblacion > 10000000:
        categoria = "Megaciudad"

    elif poblacion >= 1000000:
        categoria = "Ciudad grande"

    elif poblacion >= 100000:
        categoria = "Ciudad mediana"

    else:
        categoria = "Ciudad pequeña"

    return categoria

# Definición de función para obtener los datos del reporte
def obtenerDatosReporte(data):
    '''
    Funcionalidad:
    Obtiene los datos de los países necesarios para el reporte TXT.

    Entradas:
    -data: Líneas del archivo TOON.

    Salidas:
    -paises: Lista con los datos de cada país.
    '''
    paises = []
    for i in range(0, len(data), 9):
        nombre = normalizarNombre(obtenerTexto(data[i + 1]))
        capital = normalizarNombre(obtenerTexto(data[i + 2]))
        codigo = obtenerTexto(data[i + 3])
        poblacion = int(obtenerTexto(data[i + 4]))
        area = float(obtenerTexto(data[i + 5]))
        moneda=obtenerTexto(data[i+6])
        codigoMoneda=obtenerTexto(data[i+7])
        tasaCambio = float(obtenerTexto(data[i + 8]))
        if area > 0:
            densidad = poblacion / area
        else:
            densidad = 0
        categoria = categoriaPoblacion(poblacion)
        pais =[nombre, capital, codigo, poblacion, area, densidad, categoria, moneda, codigoMoneda, tasaCambio]
        paises.append(pais)
    return paises

# Definición de función para generar el reporte TXT
def generarReportePaises(paises):
    '''
    Funcionalidad:
    Genera un archivo TXT con la información de los países y un resumen general.
    Entradas:
    -paises: Lista con los datos procesados de cada país.
    Salidas:
    -Archivo reportePaises.txt con los datos y el resumen.
    '''
    try:
        archivo = open("reportePaises.txt", "w", encoding="utf-8")
        archivo.write("REPORTE DE PAISES\n")
        archivo.write("-----------------------------------------\n")
        # Escribir la información de cada país
        for pais in paises:
            archivo.write(
                "El pais " + pais[0] +" tiene como capital "+ pais[1] +", su código ISO es " + pais[2] + 
                ", tiene " + str(pais[3]) + " habitantes" + ", un área de " + str(pais[4]) + " km2" +
                ", su moneda es " + pais[7] + ", código " + pais[8]+ ", y hay "+str(round(pais[9], 2)) + " por cada dólar.\n")
            archivo.write("Densidad poblacional: " + str(round(pais[5], 2))+" hab/km2\n")
            archivo.write("Categoría: "+pais[6]+"\n")
            archivo.write("-----------------------------------------\n")
        # Calcular los datos del resumen
        totalPaises = len(paises)
        poblacion = 0
        area = 0
        for pais in paises:
            poblacion += pais[3]
            area += pais[4]
        if totalPaises > 0:
            promedioPoblacion = poblacion / totalPaises
            promedioArea = area / totalPaises
        else:
            promedioPoblacion = 0
            promedioArea = 0
        # Escribir el resumen final
        archivo.write("\nRESUMEN GENERAL\n")
        archivo.write("-----------------------------------------\n")
        archivo.write("Total de paises: " + str(totalPaises) + "\n")
        archivo.write("Poblacion total: " + str(poblacion) + "\n")
        archivo.write("Area total: " + str(area) + " km2\n")
        archivo.write("Promedio de poblacion: " +
                      str(round(promedioPoblacion, 2)) + "\n")
        archivo.write("Promedio de area: " +
                      str(round(promedioArea, 2)) + " km2\n")
        archivo.close()
    except:
        print("Error al generar el reporte de paises.")
