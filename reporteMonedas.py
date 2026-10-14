#Importación
from procesarDatosMonedas import obtenerMonedas, calcularPromedioTasas
from procesarDatosMonedas import encontrarMonedaFuerteDebil
from procesarDatosMonedas import normalizarMoneda
from cargaDatos import leer
from datetime import datetime

#Funciones
# Definición de función para clasificar las monedas
def clasificarMoneda(tasa):
    '''
    Funcionalidad:
    Clasifica una moneda según su tasa de cambio con respecto al dólar estadounidense.

    Entradas:
    -tasa: Tasa de cambio de la moneda.

    Salidas:
    -clasificacion: Fuerte, Igual o Débil.
    '''
    if tasa > 1:
        clasificacion = "Fuerte"

    elif tasa == 1:
        clasificacion = "Igual"

    else:
        clasificacion = "Débil"

    return clasificacion

# Definición de función para generar el reporte HTML
def generarReporteMonedas(monedas):
    '''
    Funcionalidad:
    Genera un archivo HTML con la información y las estadísticas de las monedas.
    Entradas:
    -monedas: Lista con los datos de las monedas.
    Salidas:
    -Archivo reporteMonedas.html.
    '''
    try:
        archivo = open("reporteMonedas.html", "w", encoding="utf-8")
        # Estructura inicial del HTML
        archivo.write("<!DOCTYPE html>\n")
        archivo.write("<html>\n")
        archivo.write("<head>\n")
        archivo.write('<meta charset="UTF-8">\n')
        archivo.write("<title>Reporte de Análisis de Monedas</title>\n")
        archivo.write("</head>\n")
        # Formato de la tabla
        archivo.write("<style>\n")
        archivo.write("table {border-collapse: collapse; width: 100%;}\n")
        archivo.write("th, td {text-align: center; padding: 8px;}\n")
        archivo.write("tr:nth-child(even) {background-color: lightgray;}\n")
        archivo.write("</style>\n")
        # Contenido de la página
        archivo.write("<body>\n")
        # Título Principal
        archivo.write("<h1>Reporte de Análisis de Monedas</h1>\n")
        # Fecha y hora
        fecha = datetime.now()
        archivo.write("<h2>Fecha de generación: " +fecha.strftime("%d/%m/%Y %H:%M:%S") +"</h2>\n")
        # Estadísticas generales
        totalMonedas = len(monedas)
        promedio = calcularPromedioTasas(monedas)
        archivo.write("<h3>Estadísticas generales</h3>\n")
        archivo.write("<p>Total de monedas analizadas: " +str(totalMonedas) + "</p>\n")
        archivo.write("<p>Promedio de tasas de cambio: " +format(promedio, ".4f") + "</p>\n")
        if totalMonedas>0:
            fuerte, debil = encontrarMonedaFuerteDebil(monedas)
            archivo.write("<p>Moneda más fuerte: "+normalizarMoneda(fuerte[1])+" (" + fuerte[0] + ")" + " - Tasa: " +format(fuerte[2], ".4f") + "</p>\n")
            archivo.write("<p>Moneda más débil: " +normalizarMoneda(debil[1]) +" (" + debil[0] + ")"+" - Tasa: " +format(debil[2], ".4f") + "</p>\n")
        # Tabla de monedas
        archivo.write("<h2>Tabla de monedas</h2>\n")
        archivo.write('<table border="1">\n')
        # Encabezados de la tabla
        archivo.write("<tr>\n")
        archivo.write("<th>Código</th>\n")
        archivo.write("<th>Nombre normalizado</th>\n")
        archivo.write("<th>Tasa de cambio</th>\n")
        archivo.write("<th>Relación con USD</th>\n")
        archivo.write("</tr>\n")
        # Datos de las monedas
        for moneda in monedas:
            codigo = moneda[0]
            nombre = normalizarMoneda(moneda[1])
            tasa = moneda[2]
            clasificacion = clasificarMoneda(tasa)
            archivo.write("<tr>\n")
            archivo.write("<td>" + codigo + "</td>\n")
            archivo.write("<td>" + nombre + "</td>\n")
            archivo.write("<td>" + format(tasa, ".4f") + "</td>\n")
            archivo.write("<td>" + clasificacion + "</td>\n")
            archivo.write("</tr>\n")
        archivo.write("</table>\n")
        # Cierre del HTML
        archivo.write("</body>\n")
        archivo.write("</html>\n")
        archivo.close()
        print("Reporte de monedas generado correctamente.")
    except:
        print("Error al generar el reporte de monedas.")

