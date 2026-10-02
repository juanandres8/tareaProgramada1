from cargaDatos import leer 

#Definición función nombres países
def obtenerNombres(data):
    nombres=[]
    for linea in data:
        if "Nombre:"in linea:
            nombre=""
            encontrado=False
            for caracter in linea:
                if caracter=="\"":
                    if encontrado==False:
                        encontrado=True
                    else:
                        encontrado=False
                elif encontrado==True and caracter!="\n":
                    nombre+=caracter
            nombres.append(nombre)
    return nombres
#Definición función normalizar nombres países
def normalizarNombre(nombre):
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
    nombres=obtenerNombres(data)
    nombresNormalizados=[]
    for nombre in nombres:
        nombresNormalizados.append(normalizarNombre(nombre))
    return nombresNormalizados
#Definición función para actualizar datos en el .toon
def actualizarNombres(data):
    try:
        archivo=open("paises.toon","w",encoding="utf-8-sig")
        for linea in data:
            if "Nombre:"in linea:
                nombre=""
                encontrado=False
                for caracter in linea:
                    if caracter=="\"":
                        if encontrado==False:
                            encontrado=True
                        else:
                            encontrado=False
                    elif encontrado==True:
                        nombre+=caracter
                nombre=normalizarNombre(nombre)
                archivo.write(' Nombre: "'+nombre+'"\n')
            else:
                archivo.write(linea)
        archivo.close()
    except:
        print("ERROR al actualizar el archivo paises.toon")

#Definición función longitud promedio de los nombres
def longitudPromedio(data):
    nombres=normalizarNombres(data)
    suma=0
    cantidad=0
    for nombre in nombres:
        suma+=len(nombre)
        cantidad+=1
    promedio=suma//cantidad
    return"-Longitud promedio de nombres: "+str(promedio)
#Definición función país con nombre más largo
def nombreMasLargo(data):
    nombres=normalizarNombres(data)
    mayor=nombres[0]
    for nombre in nombres:
        if len(nombre)>len(mayor):
            mayor=nombre
    return "-País con nombre más largo: "+mayor+" - "+str(len(mayor))
#Definición función país con nombre más corto
def nombreMasCorto(data):
    nombres=normalizarNombres(data)
    menor=nombres[0]
    for nombre in nombres:
        if len(nombre)<len(menor):
            menor=nombre
    return "-País con nombre más corto: "+menor+" - "+str(len(menor))
#Definición función Cantidad de países que contienen una cierta letra
def cantidadPaises(data,letra):
    nombres=normalizarNombres(data)
    cantidad=0
    for nombre in nombres:
        encontrado=False
        for caracter in nombre:
            if caracter.lower()==letra.lower():
                encontrado=True
        if encontrado==True:
            cantidad+=1
    return "-Cantidad de países que contienen la letra "+letra+": "+str(cantidad)
#PP
data=leer("paises.toon")
actualizarNombres(data)
print(longitudPromedio(data))
print(nombreMasLargo(data))
print(nombreMasCorto(data))
letra=input("Ingrese una letra: ")
print(cantidadPaises(data,letra))




        
            
            
            
    

                    
    
