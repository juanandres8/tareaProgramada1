#Opción 1
#Definición de función para cargar los datos
def leer(nombreArchivoLeer):
    '''
    Funcionalidad: Permite abrir el archivo  y leer el contenido.
    Entradas:
    -nombreArchivoLeer: Nombre del archivo donde están almacenados los datos.
    Salidas:
    -data:Son las líneas leídas del archivo.
    '''
    try:
        archivo=open(nombreArchivoLeer,"r", encoding="utf-8-sig")
        data=archivo.readlines()
        archivo.close()
        return data
    except:
        print("Error al leer el archivo: ",nombreArchivoLeer)
#Definición de función para crear toon
def escribirToon(data):
    '''
    Funcionalidad:Permite crear el archivo.toon y almacenar los datos de los países obtenidos del csv.
    Entradas:
    -data:Líneas del archivo.csv que contiene los datos de los países.
    Salidas:
    -No retorna nada, pues solo escribe los datos en el archivo.toon.
    '''
    try:
        archivo=open("paises.toon","w",encoding="utf-8-sig")
        for posicionPais in range(1,len(data)):#Se inicia en 1 para omitir el encabezado
            campo=data[posicionPais].strip().split(";")
            archivo.write("-país:\n")
            archivo.write(' Nombre: \"'+campo[0]+'"\n')
            archivo.write(' Capital: \"'+campo[1]+'"\n')
            archivo.write(' Codigo: \"'+campo[2]+'"\n')
            archivo.write(' Población: \"'+campo[3]+'"\n')
            archivo.write(' Aréa: \"'+campo[4]+'"\n')
            archivo.write(' Moneda: \"'+campo[5]+'"\n')
            archivo.write(' Codigo Moneda: \"'+campo[6]+'"\n')
            archivo.write(' Tasa Cambio USD: \"'+campo[7]+'"\n')
        archivo.close()
    except:
        print("Error al interactuar con el archivo.Toon: ")
#Definición de función para cantidad de países cargados
def cantidadPaises(data):
    '''
    Funcionalidad:Permite contar la cantidad de países que existen en el archivo.csv.
    Entradas:
    -data:Líneas del archivo.csv que contiene los datos de los países.
    Salidas:
    -Cantidad:Retorna la cantidad de países cargados.
    '''
    cantidad=len(data)-1
    return cantidad
#Definición de función para países con mayor población
def mayorPoblacion(data):
    '''
    Funcionalidad:Permite ordenar los países de mayor a menor según su población, teniendo en cuenta solo los 5 con mayor población.
    Entradas:
    -data:Líneas del archivo.csv que contiene los datos de los países.
    Salidas:
    -Muestra en la consola los nombres de los países y la población de los 5 países con mayor población.
    '''
    paises=data
    for posicionPais in range(1,len(paises)):
        for posicionComparar in range(posicionPais+1,len(paises)):
            pais=paises[posicionPais].strip().split(";")
            comparar=paises[posicionComparar].strip().split(";")
            poblacionPais=int(pais[3])
            poblacionComparar=int(comparar[3])
            if poblacionPais<poblacionComparar:
                aux=paises[posicionPais]
                paises[posicionPais]=paises[posicionComparar]
                paises[posicionComparar]=aux
    print("-Los 5 países con mayor población son: ")
    for posicion in range(1,6):
        pais=paises[posicion].strip().split(";")
        print(str(posicion)+"."+pais[0],"-",pais[3])
#Definición de función para países con menor área
def menorArea(data):
    '''
    Funcionalidad:Permite ordenar los países de menor a mayor según su área, teniendo en cuenta solo los 5 con menor área.
    Entradas:
    -data:Líneas del archivo.csv que contiene los datos de los países.
    Salidas:
    -Muestra en la consola los nombres de los países y el área de los 5 países con menor área.
    '''
    paises=data[:]
    for posicionPais in range(1,len(paises)):
        for posicionComparar in range(posicionPais+1,len(paises)):
            pais=paises[posicionPais].strip().split(";")
            comparar=paises[posicionComparar].strip().split(";")
            areaActual=float(pais[4])
            areaComparar=float(comparar[4])
            if areaActual>areaComparar:
                aux=paises[posicionPais]
                paises[posicionPais]=paises[posicionComparar]
                paises[posicionComparar]=aux
    print("-Los 5 países con menor área son: ")
    for posicion in range(1,6):
        pais=paises[posicion].strip().split(";")
        print(str(posicion)+"."+pais[0],"-",pais[4])
#Definición función fecha de la tasa de cambio

#Definición función obtener monedas sin repetir
def obtenerMonedas(data):
    '''
    Funcionalidad:Permite obtener las monedas de los países pero sin repetir.
    Entradas:
    -data:Líneas del archivo.csv que contiene los datos de los países.
    Salidas:
    -monedas:Retorna una lista con el nombre de la moneda,su código y su tasa de cambio,sin monedas repetidas.
    '''
    monedas=[]
    for posicionPais in range(1,len(data)):
        pais=data[posicionPais].strip().split(";")
        moneda=[pais[5],pais[6],float(pais[7])]
        if moneda not in monedas:
            monedas.append(moneda)
    return monedas
#Definición función contar monedad
def cantidadMonedas(data):
    '''
    Funcionalidad:Permite obtener la cantidad de monedas diferentes de los países.
    Entradas:
    -data:Líneas del archivo.csv que contiene los datos de los países.
    Salidas:
    -len(monedas)=Retorna la cantidad de monedas descargadas
    '''
    monedas=obtenerMonedas(data)
    return len(monedas)
#Definición función monedas con mayor valor
def monedasMayorValor(data):
    '''
    Funcionalidad:Permite ordenar las monedas de mayor a menor valor frente al USD,teniendo en cuenta solo los 5 mayores.
    Entradas:
    -data:Líneas del archivo.csv que contiene los datos de los países.
    Salidas:
    -Muestra en la consola el nombre y la tasa de cambio de las 5 monedas con mayor valor frente al USD.
    '''
    monedasOrdenadas=obtenerMonedas(data)
    for posicionMoneda in range(len(monedasOrdenadas)):
        for posicionComparar in range(posicionMoneda+1,len(monedasOrdenadas)):
            if monedasOrdenadas[posicionMoneda][2]>monedasOrdenadas[posicionComparar][2]:
                aux=monedasOrdenadas[posicionMoneda]
                monedasOrdenadas[posicionMoneda]=monedasOrdenadas[posicionComparar]
                monedasOrdenadas[posicionComparar]=aux
    print("-Los 5 monedas con mayor valor frente al USD son: ")
    for posicion in range(1,6):
        moneda=monedasOrdenadas[posicion-1]
        print(str(posicion)+"."+moneda[0],"-",moneda[2])
#Definición función monedas con menor valor
def monedasMenorValor(data):
    '''
    Funcionalidad:Permite ordenar las monedas de menor a mayor valor frente al USD,teniendo en cuenta solo los 5 menores.
    Entradas:
    -data:Líneas del archivo.csv que contiene los datos de los países.
    Salidas:
    -Muestra en la consola el nombre y la tasa de cambio de las 5 monedas con menor valor frente al USD.
    '''
    monedasOrdenadas=obtenerMonedas(data)
    for posicionMoneda in range(len(monedasOrdenadas)):
        for posicionComparar in range(posicionMoneda+1,len(monedasOrdenadas)):
            if monedasOrdenadas[posicionMoneda][2]<monedasOrdenadas[posicionComparar][2]:
                aux=monedasOrdenadas[posicionMoneda]
                monedasOrdenadas[posicionMoneda]=monedasOrdenadas[posicionComparar]
                monedasOrdenadas[posicionComparar]=aux
    print("-Los 5 monedas con menor valor frente al USD son: ")
    for posicion in range(1,6):
        moneda=monedasOrdenadas[posicion-1]
        print(str(posicion)+"."+moneda[0],"-",moneda[2])

#Programa Principal(Prueba)
data=leer("nombreArchivoLeer.csv")
escribirToon(data)
print("-Cantidad de países cargados: "+str(cantidadPaises(data)))
print()
mayorPoblacion(data)
print()
menorArea(data)
print()
print("-Cantidad de monedas descargadas: "+str(cantidadMonedas(data)))
print()
monedasMayorValor(data)
print()
monedasMenorValor(data)

            
 
    
