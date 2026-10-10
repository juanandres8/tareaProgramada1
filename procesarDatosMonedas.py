#importación de funciones
from cargaDatos import leer
from procesarNombres import obtenerTexto

#Definción función obtener monedas
def obtenerMonedas(data):
    '''
    Funcionalidad:Permite obtener el código y el nombre de las monedas del archivo.toon.
    Entradas:
    -data:Líneas del archivo .toon que contiene los datos de los países.
    Salidas:
    -monedas:Retorna una lista con el código y nombre de cada moneda.
    '''
    monedas = []
    nombreCompleto = ""
    codigo = ""
    tasa = ""
    for linea in data:
        if "Moneda:" in linea and "Codigo Moneda:" not in linea:
            nombreCompleto = obtenerTexto(linea)
        elif "Codigo Moneda:" in linea:
            codigo = obtenerTexto(linea)
        elif "Tasa Cambio USD:" in linea:
            tasa = obtenerTexto(linea)
            # Crear la moneda con sus tres datos
            moneda = [codigo, nombreCompleto, float(tasa)]
            # Evitar monedas repetidas
            if moneda not in monedas:
                monedas.append(moneda)
    return monedas

#Definción función normalizar nombre de moneda
def normalizarMoneda(nombre):
    '''
    Funcionalidad:Permite normalizar el nombre de cada moneda.
    Entradas:
    -nombre:Nombre de la moneda que se quiere normalizar.
    Salidas:
    -resul:Retorna el nombre de la moneda ya normalizado.
    '''
    nombre=nombre.upper() #Mayúscula
    #Eliminar espacios
    inicio=0
    fin=len(nombre)-1
    while inicio<len(nombre)and nombre[inicio]==" ":
        inicio+=1
    while fin>=0 and nombre[fin]==" ":
        fin-=1
    nombreSinEspacios=""
    for posicion in range(inicio,fin+1):
        nombreSinEspacios+=nombre[posicion]
    nombre=nombreSinEspacios
    nombreListo=""
    encontrado=False
    for caracter in nombre:
        #Eliminar parentesis y remplazar caracteres especiales
        if caracter=="(":
            encontrado=True
        elif caracter==")":
            encontrado=False
        elif encontrado==False:
            if caracter in "ÁÀÂÃÄÅ":
                nombreListo+="A"
            elif caracter in "ÉÈÊË":
                nombreListo+="E"
            elif caracter in "ÍÌÎÏ":
                nombreListo+="I"
            elif caracter in "ÓÒÔÕÖ":
                nombreListo+="O"
            elif caracter in "ÚÙÛÜ":
                nombreListo+="U"
            elif caracter in "Ñ":
                nombreListo+="N"
            elif caracter in "Ç":
                nombreListo+="C"
            elif caracter in "'-`":
                nombreListo+=" "
            elif caracter=="_":
                nombreListo+=" "
            else:
                nombreListo+=caracter
        #Capitalizar
    resul=""
    palabraLista=True
    for caracter in nombreListo:
        if caracter==" ":
            resul+=caracter
            palabraLista=True
        else:
            if palabraLista==True:
                resul+=caracter.upper()
                palabraLista=False
            else:
                resul+=caracter.lower()
    return resul
#Definción de función crear formato para moneda
def formatoMonedas(data):
    '''
    Funcionalidad:Permite crear el formato "código-nombre" para cada moneda.
    Entradas:
    -data:Son las líneas leídas del archivo.toon.
    Salidas:
    -monedasFormato:Retorna una lista con las monedas en formato "código-nombre".
    '''
    monedas=obtenerMonedas(data)
    monedasFormato=[]
    for moneda in monedas:
        codigo=moneda[0]
        nombre=normalizarMoneda(moneda[1])
        formato=codigo+"-"+nombre
        monedasFormato.append(formato)
    return monedasFormato
#Definición de función contar monedas
def contarMonedasLetras(data,n):
    '''
    Funcionalidad:Permite contar cuántas monedas tienen exactamente n letras.
    Entradas:
    -data:Líneas del archivo.toon que contiene los datos.
    -n:Cantidad de letras que se quiere buscar.
    Salidas:
    -cantidad:Retorna la cantidad de monedas que tienen exactamente n letras.
    '''
    monedas=obtenerMonedas(data)
    cantidad=0
    for moneda in monedas:
        nombre=normalizarMoneda(moneda[1])
        cantidadLetras=0
        for caracter in nombre:
            if caracter!=" ":
                cantidadLetras+=1
        if cantidadLetras==n:
                cantidad+=1
    return cantidad

# Definición de función calcular promedio de tasas
def calcularPromedioTasas(monedas):
    '''
    Funcionalidad:
    Permite calcular la tasa de cambio promedio de las monedas.
    Entradas:
    - monedas: Lista que contiene el código, nombre y tasa de cada moneda.
    Salidas:
    - promedio: Retorna el promedio de las tasas de cambio.
    '''
    suma = 0
    cantidad = 0
    # Recorrer todas las monedas
    for moneda in monedas:
        tasa = float(moneda[2])
        suma += tasa
        cantidad += 1
    # Verificar que existan monedas
    if cantidad == 0:
        return 0
    # Calcular el promedio
    promedio = suma / cantidad
    return promedio

# Definición de función encontrar moneda fuerte y débil
def encontrarMonedaFuerteDebil(monedas):
    '''
    Funcionalidad:
    Permite encontrar la moneda con la tasa más alta
    y la moneda con la tasa más baja.
    Entradas:
    - monedas: Lista que contiene los datos de las monedas.
    Salidas:
    - fuerte: Moneda con la tasa más alta.
    - debil: Moneda con la tasa más baja.
    '''
    # Verificar que existan monedas
    if len(monedas) == 0:
        return None, None
    # Inicializar con la primera moneda
    fuerte = monedas[0]
    debil = monedas[0]
    # Comparar las tasas de todas las monedas
    for moneda in monedas:
        tasa = float(moneda[2])
        # Buscar la tasa más alta
        if tasa > float(fuerte[2]):
            fuerte = moneda
        # Buscar la tasa más baja
        if tasa < float(debil[2]):
            debil = moneda
    return fuerte, debil

# Definición de función contar monedas por tasa
def contarMonedasPorTasa(monedas):
    '''
    Funcionalidad:
    Permite contar cuántas monedas tienen una tasa
    mayor, igual o menor que 1 USD.
    Entradas:
    - monedas: Lista que contiene los datos de las monedas.
    Salidas:
    - mayores: Cantidad de monedas con tasa mayor que 1.
    - iguales: Cantidad de monedas con tasa igual a 1.
    - menores: Cantidad de monedas con tasa menor que 1.
    '''
    # Inicializar los contadores
    mayores = 0
    iguales = 0
    menores = 0
    # Recorrer las monedas
    for moneda in monedas:
        tasa = float(moneda[2])
        # Clasificar según la tasa de cambio
        if tasa > 1:
            mayores += 1
        elif tasa == 1:
            iguales += 1
        else:
            menores += 1
    return mayores, iguales, menores

# Definición de función ordenar monedas por tasa
def ordenarMonedasPorTasa(monedas):
    '''
    Funcionalidad:
    Permite ordenar las monedas por su tasa de cambio,
    de forma ascendente y descendente.
    Entradas:
    - monedas: Lista que contiene los datos de las monedas.
    Salidas:
    - ascendente: Lista ordenada de menor a mayor tasa.
    - descendente: Lista ordenada de mayor a menor tasa.
    '''
    # Crear una copia para no modificar la lista original
    ascendente = monedas.copy()
    # Ordenar las monedas de menor a mayor
    for i in range(len(ascendente)):
        for j in range(i + 1, len(ascendente)):
            # Comparar las tasas de cambio
            if float(ascendente[i][2]) > float(ascendente[j][2]):
                # Intercambiar las posiciones
                auxiliar = ascendente[i]
                ascendente[i] = ascendente[j]
                ascendente[j] = auxiliar
    # Copiar la lista ordenada
    descendente = ascendente.copy()
    # Invertir el orden para obtener el descendente
    descendente.reverse()
    return ascendente, descendente
