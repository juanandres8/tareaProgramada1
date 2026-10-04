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
    Funcionalidad: Calcula la población total.
    '''
    total = 0
    for pais in paises:
        total += pais[1]
    return total

# 2. Población promedio
def poblacionPromedio(paises):
    '''
    Funcionalidad: Calcula la población promedio.
    '''
    total = poblacionTotal(paises)
    promedio = total / len(paises)
    return promedio

# 3. Ordenamiento manual de poblaciones
def ordenarPoblaciones(poblaciones):
    '''
    Funcionalidad: Ordena las poblaciones de menor a mayor
    utilizando ordenamiento manual.
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
    Funcionalidad: Calcula la mediana de las poblaciones.
    '''
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
    Funcionalidad: Clasifica los países según su población.
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
    Funcionalidad: Calcula el área total de todos los países.
    '''
    total = 0
    for pais in paises:
        total += pais[2]
    return total

# 2. Calcular densidades
def obtenerDensidades(paises):
    '''
    Funcionalidad: Calcula la densidad poblacional de cada país.
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
    Funcionalidad: Ordena las densidades manualmente.
    '''
    for posicion in range(len(densidades)):
        for comparar in range(posicion + 1, len(densidades)):
            if mayor == True:
                if densidades[posicion][1] < densidades[comparar][1]:
                    aux = densidades[posicion]
                    densidades[posicion] = densidades[comparar]
                    densidades[comparar] = aux
            else:
                if densidades[posicion][1] > densidades[comparar][1]:
                    aux = densidades[posicion]
                    densidades[posicion] = densidades[comparar]
                    densidades[comparar] = aux

# 3. Diez países con mayor densidad
def mayorDensidad(paises):
    '''
    Funcionalidad: Muestra los 10 países con mayor densidad.
    '''
    densidades = obtenerDensidades(paises)
    ordenarDensidades(densidades, True)
    print("-Los 10 países con mayor densidad son:")
    for posicion in range(10):
        print(str(posicion + 1) + ".",densidades[posicion][0], "-",densidades[posicion][1],"hab/km²" )

# 4. Diez países con menor densidad
def menorDensidad(paises):
    '''
    Funcionalidad: Muestra los 10 países con menor densidad.
    '''
    densidades = obtenerDensidades(paises)
    ordenarDensidades(densidades, False)
    print("-Los 10 países con menor densidad son:")
    for posicion in range(10):
        print(str(posicion + 1) + ".",densidades[posicion][0],"-",densidades[posicion][1],"hab/km²" )
#pp
data = leer("paises.toon")
paises = obtenerDatos(data)

