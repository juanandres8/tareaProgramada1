# Importaciones
from reportePaises import obtenerDatosReporte

# Función para ordenar países por densidad
def ordenarDensidades(paises, mayor):
    '''
    Funcionalidad:
    Ordena los países según su densidad poblacional.
    mayor=True: de mayor a menor.
    mayor=False: de menor a mayor.
    Entradas:
    - paises: lista de países.
    - mayor: indica el orden de clasificación.
    Salida:
    - Lista de países ordenada por densidad.
    '''
    # Crear una copia de la lista original
    ordenados = paises[:]
    # Recorrer las posiciones de la lista
    for posicion in range(len(ordenados)):
        # Comparar el país actual con los siguientes
        for comparar in range(posicion + 1, len(ordenados)):
            # Determinar el orden según el parámetro mayor
            if mayor == True:
                condicion = ordenados[posicion][5] < ordenados[comparar][5]
            else:
                condicion = ordenados[posicion][5] > ordenados[comparar][5]
            # Intercambiar los países si están en el orden incorrecto
            if condicion:
                aux = ordenados[posicion]
                ordenados[posicion] = ordenados[comparar]
                ordenados[comparar] = aux
    # Devolver la lista ordenada
    return ordenados

# Función para generar el reporte HTML
def generarReporteDensidad(data):
    '''
    Funcionalidad:
    Genera un reporte HTML con las densidades,
    las categorías y las estadísticas poblacionales.
    Entrada:
    - data: información de los países.
    Salida:
    - Archivo reporteDensidad.html.
    '''
    try:
        # Obtener los datos necesarios para el reporte
        paises = obtenerDatosReporte(data)
        # Comprobar que existan países
        if len(paises) == 0:
            print("No hay países para generar el reporte.")
            return
        # Abrir el archivo HTML para escribir el reporte
        archivo = open("reporteDensidad.html", "w", encoding="utf-8")
        # Crear la estructura inicial del documento HTML
        archivo.write("<!DOCTYPE html>\n")
        archivo.write("<html>\n")
        archivo.write("<head>\n")
        # Establecer la codificación de caracteres
        archivo.write('<meta charset="UTF-8">\n')
        # Definir el título de la página
        archivo.write("<title>Analisis de Densidad Poblacional Mundial</title>\n")
        # Definir los estilos visuales del reporte
        archivo.write("<style>\n")
        archivo.write("body {font-family: Arial; margin: 30px; background-color: #f4f6f8;}\n")
        archivo.write("h1, h2 {color: #234567;}\n")
        archivo.write("table {border-collapse: collapse; width: 100%; margin-bottom: 25px;}\n")
        archivo.write("th, td {border: 1px solid #999; padding: 8px; text-align: center;}\n")
        archivo.write("th {background-color: #234567; color: white;}\n")
        archivo.write("tr:nth-child(even) {background-color: #e1e8ef;}\n")
        # Usar una fuente monoespaciada para conservar la alineación del gráfico
        archivo.write("pre {font-size: 14px; font-family: monospace;}\n")
        archivo.write("</style>\n")
        archivo.write("</head>\n")
        archivo.write("<body>\n")
        # Mostrar el título principal del reporte
        archivo.write("<h1>Analisis de Densidad Poblacional Mundial</h1>\n")
        # Ordenar los países de mayor a menor y de menor a mayor densidad
        mayores = ordenarDensidades(paises, True)
        menores = ordenarDensidades(paises, False)
        # Crear la tabla de los diez países con mayor densidad
        archivo.write("<h2>10 paises mas densamente poblados</h2>\n")
        archivo.write("<table>\n")
        archivo.write("<tr><th>Pais</th><th>Densidad (hab/km2)</th></tr>\n")
        # Mostrar hasta diez países, según la cantidad disponible
        for posicion in range(min(10, len(mayores))):
            pais = mayores[posicion]
            archivo.write( "<tr><td>" + pais[0] + "</td><td>" + format(pais[5], ".2f") + "</td></tr>\n")
        archivo.write("</table>\n")
        # Crear la tabla de los diez países con menor densidad
        archivo.write("<h2>10 paises menos densamente poblados</h2>\n")
        archivo.write("<table>\n")
        archivo.write("<tr><th>Pais</th><th>Densidad (hab/km2)</th></tr>\n")
        # Evitar acceder a posiciones inexistentes
        for posicion in range(min(10, len(menores))):
            pais = menores[posicion]
            archivo.write("<tr><td>" + pais[0] + "</td><td>"+ format(pais[5], ".2f") + "</td></tr>\n")
        archivo.write("</table>\n")
        # Definir las categorías de población
        categorias = ["Megaciudad","Ciudad grande","Ciudad mediana","Ciudad pequeña"]
        # Inicializar el contador de cada categoría
        cantidades = [0, 0, 0, 0]
        # Contar cuántos países pertenecen a cada categoría
        for pais in paises:
            for posicion in range(len(categorias)):
                # Comparar la categoría del país con las categorías definidas
                if pais[6] == categorias[posicion]:
                    cantidades[posicion] += 1
        # Crear el gráfico de barras ASCII
        archivo.write("<h2>Distribucion de categorias</h2>\n")
        archivo.write("<pre>\n")
        # Recorrer las categorías para generar sus barras
        for posicion in range(len(categorias)):
            # Reservar el mismo espacio para cada nombre
            # Esto permite que todas las barras comiencen alineadas
            categoria = categorias[posicion].ljust(16)
            # Crear una barra según la cantidad de países
            barra = "#" * cantidades[posicion]
            # Escribir la categoría, la barra y su cantidad
            archivo.write( categoria + ": " + barra+ " (" + str(cantidades[posicion]) + ")\n")
        archivo.write("</pre>\n")
        # Inicializar las variables para las estadísticas
        poblacionTotal = 0
        areaTotal = 0
        # Obtener el país con densidad máxima y mínima
        densidadMaxima = mayores[0]
        densidadMinima = menores[0]
        # Sumar la población y el área de todos los países
        for pais in paises:
            poblacionTotal += pais[3]
            areaTotal += pais[4]
        # Comprobar que el área total sea mayor que cero
        if areaTotal > 0:
            promedioGlobal = poblacionTotal / areaTotal
        else:
            # Evitar una división entre cero
            promedioGlobal = 0
        # Mostrar las estadísticas generales
        archivo.write("<h2>Estadisticas generales</h2>\n")
        archivo.write("<p>Densidad promedio global: "+ format(promedioGlobal, ".2f") + " hab/km2</p>\n")
        archivo.write("<p>Densidad maxima: " + densidadMaxima[0] + " - "+ format(densidadMaxima[5], ".2f") + " hab/km2</p>\n")
        archivo.write("<p>Densidad minima: " + densidadMinima[0] + " - "+ format(densidadMinima[5], ".2f") + " hab/km2</p>\n")
        # Crear la tabla del porcentaje de países por categoría
        archivo.write("<h2>Porcentaje por categoria</h2>\n")
        archivo.write("<table>\n")
        archivo.write("<tr><th>Categoria</th><th>Cantidad</th>""<th>Porcentaje</th></tr>\n")
        # Calcular el porcentaje correspondiente a cada categoría
        for posicion in range(len(categorias)):
            porcentaje = cantidades[posicion] / len(paises) * 100
            # Escribir los datos de cada categoría en la tabla
            archivo.write("<tr><td>" + categorias[posicion] + "</td><td>"+ str(cantidades[posicion]) + "</td><td>"+ format(porcentaje, ".2f") + "%</td></tr>\n")
        archivo.write("</table>\n")
        # Cerrar las etiquetas del documento HTML
        archivo.write("</body>\n")
        archivo.write("</html>\n")
        # Cerrar el archivo para guardar los cambios
        archivo.close()
        # Informar que el reporte se generó correctamente
        print("Reporte de densidad generado correctamente.")
    # Controlar posibles errores durante la generación del reporte
    except Exception as error:
        print("Error al generar el reporte de densidad:", error)
