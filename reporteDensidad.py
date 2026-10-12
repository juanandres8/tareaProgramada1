# Importaciones
from reportePaises import obtenerDatosReporte

# Función para ordenar países por densidad
def ordenarDensidades(paises, mayor):
    '''
    Ordena los países según su densidad poblacional.
    mayor=True: de mayor a menor.
    mayor=False: de menor a mayor.
    '''
    ordenados = paises[:]
    for posicion in range(len(ordenados)):
        for comparar in range(posicion + 1, len(ordenados)):
            if mayor == True:
                condicion = ordenados[posicion][5] < ordenados[comparar][5]
            else:
                condicion = ordenados[posicion][5] > ordenados[comparar][5]
            if condicion:
                aux = ordenados[posicion]
                ordenados[posicion] = ordenados[comparar]
                ordenados[comparar] = aux
    return ordenados

# Función para generar el reporte HTML
def generarReporteDensidad(data):
    '''
    Genera un reporte HTML con las densidades,
    las categorías y las estadísticas poblacionales.
    '''
    try:
        paises = obtenerDatosReporte(data)
        if len(paises) == 0:
            print("No hay países para generar el reporte.")
            return
        archivo = open("reporteDensidad.html", "w", encoding="utf-8")
        # Estructura inicial
        archivo.write("<!DOCTYPE html>\n")
        archivo.write("<html>\n")
        archivo.write("<head>\n")
        archivo.write('<meta charset="UTF-8">\n')
        archivo.write("<title>Analisis de Densidad Poblacional Mundial</title>\n")

        # Diseño de la página
        archivo.write("<style>\n")
        archivo.write("body {font-family: Arial; margin: 30px; ""background-color: #f4f6f8;}\n")
        archivo.write( "h1, h2 {color: #234567;}\n")
        archivo.write("table {border-collapse: collapse; width: 100%; ""margin-bottom: 25px;}\n")
        archivo.write("th, td {border: 1px solid #999; " "padding: 8px; text-align: center;}\n")
        archivo.write("th {background-color: #234567; color: white;}\n")
        archivo.write("tr:nth-child(even) {background-color: #e1e8ef;}\n")
        archivo.write("pre {font-size: 14px;}\n")
        archivo.write("</style>\n")
        archivo.write("</head>\n")
        archivo.write("<body>\n")

        # Título
        archivo.write("<h1>Analisis de Densidad Poblacional Mundial</h1>\n")

        # Ordenar países
        mayores = ordenarDensidades(paises, True)
        menores = ordenarDensidades(paises, False)

        # Tabla de los 10 países con mayor densidad
        archivo.write("<h2>10 paises mas densamente poblados</h2>\n")
        archivo.write("<table>\n")
        archivo.write("<tr><th>Pais</th><th>Densidad (hab/km2)</th></tr>\n")

        for posicion in range(min(10, len(mayores))):
            pais = mayores[posicion]
            archivo.write("<tr><td>" + pais[0] + "</td><td>"+ format(pais[5], ".2f") + "</td></tr>\n")
        archivo.write("</table>\n")
        
        # Tabla de los 10 países con menor densidad
        archivo.write("<h2>10 paises menos densamente poblados</h2>\n")
        archivo.write("<table>\n")
        archivo.write("<tr><th>Pais</th><th>Densidad (hab/km2)</th></tr>\n")

        for posicion in range(min(10, len(menores))):
            pais = menores[posicion]
            archivo.write("<tr><td>" + pais[0] + "</td><td>"+ format(pais[5], ".2f") + "</td></tr>\n")
        archivo.write("</table>\n")

        # Contar países por categoría
        categorias = ["Megaciudad","Ciudad grande","Ciudad mediana", "Ciudad pequeña"]
        cantidades = [0, 0, 0, 0]

        for pais in paises:
            for posicion in range(len(categorias)):
                if pais[6] == categorias[posicion]:
                    cantidades[posicion] += 1

        # Gráfico de barras ASCII
        archivo.write("<h2>Distribucion de categorias</h2>\n")
        archivo.write("<pre>\n")
        for posicion in range(len(categorias)):
            barra = "#" * cantidades[posicion]
            archivo.write(categorias[posicion] + ": "+ barra + " (" + str(cantidades[posicion]) + ")\n")
        archivo.write("</pre>\n")

        # Calcular estadísticas
        poblacionTotal = 0
        areaTotal = 0
        densidadMaxima = mayores[0]
        densidadMinima = menores[0]

        for pais in paises:
            poblacionTotal += pais[3]
            areaTotal += pais[4]

        if areaTotal > 0:
            promedioGlobal = poblacionTotal / areaTotal
        else:
            promedioGlobal = 0

        # Mostrar estadísticas
        archivo.write("<h2>Estadisticas generales</h2>\n")
        archivo.write("<p>Densidad promedio global: "+ format(promedioGlobal, ".2f") + " hab/km2</p>\n")
        archivo.write("<p>Densidad maxima: " + densidadMaxima[0] + " - " + format(densidadMaxima[5], ".2f") + " hab/km2</p>\n")
        archivo.write( "<p>Densidad minima: " + densidadMinima[0] + " - "+ format(densidadMinima[5], ".2f") + " hab/km2</p>\n")

        # Porcentaje de países por categoría
        archivo.write("<h2>Porcentaje por categoria</h2>\n")
        archivo.write("<table>\n")
        archivo.write("<tr><th>Categoria</th><th>Cantidad</th>""<th>Porcentaje</th></tr>\n")

        for posicion in range(len(categorias)):
            porcentaje = cantidades[posicion] / len(paises) * 100
            archivo.write("<tr><td>" + categorias[posicion] + "</td><td>"+ str(cantidades[posicion]) + "</td><td>"+ format(porcentaje, ".2f") + "%</td></tr>\n")
        archivo.write("</table>\n")

        # Cerrar HTML
        archivo.write("</body>\n")
        archivo.write("</html>\n")
        archivo.close()
        print("Reporte de densidad generado correctamente.")

    except Exception as error:
        print("Error al generar el reporte de densidad:", error)
