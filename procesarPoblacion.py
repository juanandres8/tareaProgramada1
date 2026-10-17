#Opcion 3
from cargaDatos import leer
from procesarNombres import obtenerTexto

#def funciones
# Obtener los datos de población y área
def obtenerDatos(data):
    '''
    Funcionalidad: Obtiene el nombre, población y área de cada país.
    Entradas:
    -data: Líneas del archivo.toon.
    Salidas:
    -paises: Lista con nombre, población y área.
    '''
    paises = []
    for posicion in range(len(data)):
        if "Nombre:" in data[posicion]:
            nombre = obtenerTexto(data[posicion])
            poblacion = int(obtenerTexto(data[posicion + 3]))
            area = float(obtenerTexto(data[posicion + 4]))
            pais = [nombre, poblacion, area]
            paises.append(pais)
    return paises

# 1. Población total
def poblacionTotal(paises):
    '''
    Funcionalidad:
    Calcula la población total de todos los países.
    Entradas:
    - paises: Lista de países con sus datos.
    Salidas:
    - total: Suma de las poblaciones.
    '''
    total = 0
    for pais in paises:
        total += pais[1]
    return total

# 2. Población promedio
def poblacionPromedio(paises):
    '''
    Funcionalidad:
    Calcula la población promedio de los países.
    Entradas:
    - paises: Lista de países con sus datos.
    Salidas:
    - promedio: Promedio de las poblaciones.
    - 0: Si la lista está vacía.
    '''
    if len(paises)==0:
        return 0
    total = poblacionTotal(paises)
    promedio = total / len(paises)
    return promedio

# 3. Ordenamiento manual de poblaciones
def ordenarPoblaciones(poblaciones):
    '''
    Funcionalidad:
    Ordena las poblaciones de menor a mayor.
    Entradas:
    - poblaciones: Lista de cantidades de población.
    Salidas:
    - Modifica la lista original y la ordena de menor a mayor.
    '''
    for posicion in range(len(poblaciones)):
        for comparar in range(posicion + 1, len(poblaciones)):
            if poblaciones[posicion] > poblaciones[comparar]:
                aux = poblaciones[posicion]
                poblaciones[posicion] = poblaciones[comparar]
                poblaciones[comparar] = aux

# 3. Mediana
def medianaPoblacion(paises):
    '''
    Funcionalidad:
    Calcula la mediana de las poblaciones de los países.
    Entradas:
    - paises: Lista de países con sus datos.
    Salidas:
    - mediana: Valor central de las poblaciones ordenadas.
    - 0: Si la lista está vacía.
    '''
    if len(paises)==0:
        return 0
    poblaciones = []
    for pais in paises:
        poblaciones.append(pais[1])
    ordenarPoblaciones(poblaciones)
    mitad = len(poblaciones) // 2
    if len(poblaciones) % 2 == 0:
        mediana = (poblaciones[mitad - 1] + poblaciones[mitad]) / 2
    else:
        mediana = poblaciones[mitad]
    return mediana

# 4 y 5. Clasificación de países
def clasificarPaises(paises):
    '''
    Funcionalidad:
    Clasifica los países según su población.
    Entradas:
    - paises: Lista de países con sus datos.
    Salidas:
    - Imprime la cantidad de países de cada categoría:
      megaciudades, ciudades grandes, medianas y pequeñas.
    '''
    megaciudad = 0
    ciudadGrande = 0
    ciudadMediana = 0
    ciudadPequena = 0
    for pais in paises:
        poblacion = pais[1]
        if poblacion > 10000000:
            megaciudad += 1
        elif poblacion >= 1000000:
            ciudadGrande += 1
        elif poblacion >= 100000:
            ciudadMediana += 1
        else:
            ciudadPequena += 1
    print("-Cantidad de Megaciudades:", megaciudad)
    print("-Cantidad de Ciudades grandes:", ciudadGrande)
    print("-Cantidad de Ciudades medianas:", ciudadMediana)
    print("-Cantidad de Ciudades pequeñas:", ciudadPequena)

# 1. Área total
def areaTotal(paises):
    '''
    Funcionalidad:
    Calcula el área total de todos los países.
    Entradas:
    - paises: Lista de países con sus datos.
    Salidas:
    - total: Suma de las áreas.
    '''
    total = 0
    for pais in paises:
        total += pais[2]
    return total

# 2. Calcular densidades
def obtenerDensidades(paises):
    '''
    Funcionalidad:
    Calcula la densidad poblacional de cada país.
    Entradas:
    - paises: Lista de países con sus datos.
    Salidas:
    - densidades: Lista con el nombre de cada país y su densidad poblacional.
    '''
    densidades = []
    for pais in paises:
        nombre = pais[0]
        poblacion = pais[1]
        area = pais[2]
        if area > 0:
            densidad = poblacion / area
            densidades.append([nombre, densidad])
    return densidades


# Ordenamiento manual de densidades
def ordenarDensidades(densidades, mayor):
     '''
    Funcionalidad:
    Ordena las densidades poblacionales de los países.
    Entradas:
    - densidades: Lista con los nombres de los países y sus densidades.
    - mayor: Booleano que indica si se ordena de mayor a menor (True)
      o de menor a mayor (False).
    Salidas:
    - Modifica la lista original según el orden solicitado.
    '''

    for posicion in range(len(densidades)):
        for comparar in range(posicion + 1, len(densidades)):
            if mayor == True:
                condicion=densidades[posicion][1]<densidades[comparar][1]
            else:
                condicion=densidades[posicion][1]>densidades[comparar][1]
            if condicion:
                    aux = densidades[posicion]
                    densidades[posicion] = densidades[comparar]
                    densidades[comparar] = aux
                    

# 3. Diez países con mayor densidad
def mayorDensidad(paises):
    '''
    Funcionalidad:
    Muestra los diez países con mayor densidad poblacional.
    Entradas:
    - paises: Lista de países con sus datos.
    Salidas:
    - Imprime los nombres y las densidades de los diez países
      con mayor densidad, o de todos si hay menos de diez.
    '''
    densidades = obtenerDensidades(paises)
    ordenarDensidades(densidades, True)
    print("-Los 10 países con mayor densidad son:")
    for posicion in range(min(10,len(densidades))):
        print(str(posicion + 1) + ".",densidades[posicion][0], "-",densidades[posicion][1],"hab/km²" )

# 4. Diez países con menor densidad
def menorDensidad(paises):
     '''
    Funcionalidad:
    Muestra los diez países con menor densidad poblacional.
    Entradas:
    - paises: Lista de países con sus datos.
    Salidas:
    - Imprime los nombres y las densidades de los diez países
      con menor densidad, o de todos si hay menos de diez.
    '''
    densidades = obtenerDensidades(paises)
    ordenarDensidades(densidades, False)
    print("-Los 10 países con menor densidad son:")
    for posicion in range(min(10,len(densidades))):
        print(str(posicion + 1) + ".",densidades[posicion][0],"-",densidades[posicion][1],"hab/km²" )

