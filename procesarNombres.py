from cargaDatos import leer 
#Definición función aux
def obtenerTexto(linea):
    '''
    Funcionalidad:Permite obtener el texto que se encuentra entre comillas de una linea.
    Entradas:
    -linea:Es cada línea del archivo.toon de la cual se quiere obtener el texto.
    Salidas:
    -texto:Retorna el texto encontrado entre comillas.
    '''
    texto=""
    encontrado=False
    for caracter in linea: 
        if caracter=="\"":
            encontrado=not encontrado
        elif encontrado and caracter!="\n":
            texto+=caracter
    return texto
#Definición función nombres países
def obtenerNombres(data):
    '''
    Funcionalidad:Permite obtener el nombre de cada país en una lista.
    Entradas:
    -data:Líneas del archivo.toon que contiene los datos de los países.
    Salidas:
    -nombres:Retorna una lista con todos los nombres de los países.
    '''
    nombres=[]
    for linea in data:
        if "Nombre:"in linea:
            nombres.append(obtenerTexto(linea))
    return nombres
#Definición función normalizar nombres países
def normalizarNombre(nombre):
    '''
    Funcionalidad:Permite normalizar el nombre de un país, eliminando espacios innecesarios,contenido entre paréntesis y caracteres especiales,para luego capitalizar cada palabra.
    Entradas:
    -nombre:Nombre del país que se quiere normalizar.
    Salidas:
    -resul:Retorna el nombre del país normalizado.
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
#Definción función normalizar todos los nombres
def normalizarNombres(data):
    '''
    Funcionalidad:Permite obtener una lista con los nombres de los países ya normalizados.
    Entradas:
    -data:Líneas del archivo.toon que contiene los datos de los países.
    Salidas:
    -nombresNormalizados:Retorna una lista con los nombres de los países ya normalizados.
    '''
    nombres=obtenerNombres(data)
    nombresNormalizados=[]
    for nombre in nombres:
        nombresNormalizados.append(normalizarNombre(nombre))
    return nombresNormalizados
#Definición función para actualizar datos en el .toon
def actualizarNombres(data):
    '''
    Funcionalidad:Permite actualizar los nombres de los países en el .toon por sus nombres ya normalizados.
    Entradas:
    -data:Líneas del archivo.toon que contiene los datos de los países.
    Salidas:
    -No retorna nada, solamente actualiza los  nombres en el .toon
    '''
    try:
        archivo=open("paises.toon","w",encoding="utf-8-sig")
        for linea in data:
            if "Nombre:"in linea:
                texto=obtenerTexto(linea)
                nombreNormalizado=normalizarNombre(texto)
                archivo.write(' Nombre: "'+nombreNormalizado+'"\n')
            else:
                archivo.write(linea)
        archivo.close()
    except:
        print("ERROR al actualizar el archivo paises.toon")

#Definición función longitud promedio de los nombres
def longitudPromedio(data):
    '''
    Funcionalidad:Permite obtener la longitud promedio de todos los nombres de los países.
    Entradas:
    -data:Líneas del archivo.toon que contiene los datos de los países.
    Salidas:
    -Promedio:Retorna la longitud promedio de los nombres de los países.
    '''
    nombres=normalizarNombres(data)
    suma=0
    for nombre in nombres:
        suma+=len(nombre)
    promedio=suma//len(nombres)
    return promedio
#Definición función país con nombre más largo
def nombreMasLargo(data):
    '''
    Funcionalidad:Permite obtener el país con el nombre más largo.
    Entradas:
    -data:Líneas del archivo.toon que contiene los datos de los países.
    Salidas:
    -mayor:Retorna el nombre del país con mayor longitud.
    '''
    nombres=normalizarNombres(data)
    mayor=nombres[0]
    for nombre in nombres:
        if len(nombre)>len(mayor):
            mayor=nombre
    return mayor
#Definición función país con nombre más corto
def nombreMasCorto(data):
    '''
    Funcionalidad:Permite obtener el país con el nombre más corto.
    Entradas:
    -data:Líneas del archivo.toon que contiene los datos de los países.
    Salidas:
    -menor:Retorna el nombre del país con menor longitud.
    '''
    nombres=normalizarNombres(data)
    menor=nombres[0]
    for nombre in nombres:
        if len(nombre)<len(menor):
            menor=nombre
    return menor
#Definición función Cantidad de países que contienen una cierta letra
def cantidadLetraEnPaises(data,letra):
    '''
    Funcionalidad:Permite obtener la cantidad de países que contienen una letra determinada.
    Entradas:
    -data:Líneas del archivo.toon que contiene los datos de los países.
    -letra:Letra que se quiere buscar en los nombres de los países.
    Salidas:
    -cantidad:Retorna la cantidad de países que tienen la letra indicada.
    '''
    nombres=normalizarNombres(data)
    cantidad=0
    for nombre in nombres:
        for caracter in nombre:
            if caracter.lower()==letra.lower():
                cantidad+=1
                break
    return cantidad
#PP
data=leer("paises.toon")
actualizarNombres(data)
print("-Longitud promedio de nombres: ",longitudPromedio(data))
print()
paisLargo=nombreMasLargo(data)
print("-País con nombre más largo: "+paisLargo+" - "+str(len(paisLargo)))
print()
paisCorto=nombreMasCorto(data)
print("-País con nombre más corto: "+paisCorto+" - "+str(len(paisCorto)))
print()
letra=input("Ingrese una letra: ")
cantidad=cantidadLetraEnPaises(data,letra)
print("-Cantidad de países que contienen la letra "+letra+": "+str(cantidad))




        
            
            
            
    

                    
    
