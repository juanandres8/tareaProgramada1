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
    monedas=[]
    nombreCompleto=""
    for linea in data:
        if "Moneda:"in linea and "Codigo Moneda:" not in linea
        :
            nombreCompleto=obtenerTexto(linea)
        elif "Codigo Moneda:"in linea:
            codigo=obtenerTexto(linea)
            moneda=[codigo,nombreCompleto]
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
