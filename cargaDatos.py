#Importación de librerias
import pickle
import csv
import json

#Definición de función para cargar los datos
def leer(nombreArchivoLeer):
    try:
        archivo=open(nombreArchivoLeer,"r", encoding="utf-8-sig")
        data=archivo.readlines()
        archivo.close()
        return data
    except:
        print("Error al leer el archivo: ",nombreArchivoLeer)
#Definición de función para crear toon
def escribirToon(data):
    try:
        archivo=open("paises.toon","w",encoding="utf-8-sig")
        for i in range(1,len(data)):
            campo=data[i].strip().split(";")
            archivo.write("-país:\n")
            archivo.write(" Nombre: \""+campo[0]+"\n")
            archivo.write(" Capital: \""+campo[1]+"\n")
            archivo.write(" Codigo: \""+campo[2]+"\n")
            archivo.write(" Población: \""+campo[3]+"\n")
            archivo.write(" Aréa: \""+campo[4]+"\n")
            archivo.write(" Moneda: \""+campo[5]+"\n")
            archivo.write(" Codigo Moneda: \""+campo[6]+"\n")
            archivo.write(" Tasa Cambio USD: \""+campo[7]+"\n")
        archivo.close()
    except:
        print("Error al leer el archivo.Toon: ")
#PP
data=leer("nombreArchivoLeer.csv")
escribirToon(data)
#Definición de función para cantidad de países cargados
def cantidadPaises(data):
    cantidad=0
    for posicionPais in range(1,len(data)):
        cantidad+=1
    return "-Cantidad de países cargados: "+str(cantidad)
#PP
print(cantidadPaises(data))
print()
#Definición de función para países con mayor población
def mayorPoblacion(data):
    paises=data[:]
    for posicionPais in range(1,len(paises)):
        for posicionComparar in range(posicionPais+1,len(paises)):
            datoPais=paises[posicionPais].strip().split(";")
            datoComparar=paises[posicionComparar].strip().split(";")
            if int(datoPais[3])<int(datoComparar[3]):
                aux=paises[posicionPais]
                paises[posicionPais]=paises[posicionComparar]
                paises[posicionComparar]=aux
    print("-Los 5 países con mayor población son: ")
    for posicion in range(1,6):
        datoPais=paises[posicion].strip().split(";")
        print(str(posicion)+"."+datoPais[0],"-",datoPais[3])
#PP
mayorPoblacion(data)
print()
#Definición de función para países con menor área
def menorArea(data):
    paises=data[:]
    for posicionPais in range(1,len(paises)):
        for posicionComparar in range(posicionPais+1,len(paises)):
            datoPais=paises[posicionPais].strip().split(";")
            datoComparar=paises[posicionComparar].strip().split(";")
            if float(datoPais[4])>float(datoComparar[4]):
                aux=paises[posicionPais]
                paises[posicionPais]=paises[posicionComparar]
                paises[posicionComparar]=aux
    print("-Los 5 países con menor área son: ")
    for posicion in range(1,6):
        datoPais=paises[posicion].strip().split(";")
        print(str(posicion)+"."+datoPais[0],"-",datoPais[4])
menorArea(data)
print()
#Definición función fecha de la tasa de cambio

#Definición función obtener monedas sin repetir
def obtenerMonedas(data):
    monedas=[]
    for posicionPais in range(1,len(data)):
        datoPais=data[posicionPais].strip().split(";")
        moneda=[datoPais[5],datoPais[6],float(datoPais[7])]
        if moneda not in monedas:
            monedas.append(moneda)
    return monedas
#Definición función contar monedad
def cantidadMonedas(data):
    monedas=obtenerMonedas(data)
    cantidad=0
    for moneda in monedas:
        cantidad+=1
    return "-Cantidad de monedas descargadas: "+str(cantidad)
#PP
print(cantidadMonedas(data))
print()
#Definición función monedas con mayor valor
def monedasMayorValor(data):
    monedas=obtenerMonedas(data)
    monedasOrdenadas=monedas[:]
    for posicionMoneda in range(len(monedasOrdenadas)):
        for posicionComparar in range(posicionMoneda+1,len(monedasOrdenadas)):
            if monedasOrdenadas[posicionMoneda][2]>monedasOrdenadas[posicionComparar][2]:
                aux=monedasOrdenadas[posicionMoneda]
                monedasOrdenadas[posicionMoneda]=monedasOrdenadas[posicionComparar]
                monedasOrdenadas[posicionComparar]=aux
    print("-Los 5 monedas con mayor valor frente al USD son: ")
    for posicion in range(1,6):
        print(str(posicion)+"."+monedasOrdenadas[posicion-1][0],"-",monedasOrdenadas[posicion-1][2])
#PP
monedasMayorValor(data)
print()
#Definición función monedas con menor valor
def monedasMenorValor(data):
    monedas=obtenerMonedas(data)
    monedasOrdenadas=monedas[:]
    for posicionMoneda in range(len(monedasOrdenadas)):
        for posicionComparar in range(posicionMoneda+1,len(monedasOrdenadas)):
            if monedasOrdenadas[posicionMoneda][2]<monedasOrdenadas[posicionComparar][2]:
                aux=monedasOrdenadas[posicionMoneda]
                monedasOrdenadas[posicionMoneda]=monedasOrdenadas[posicionComparar]
                monedasOrdenadas[posicionComparar]=aux
    print("-Los 5 monedas con menor valor frente al USD son: ")
    for posicion in range(1,6):
        print(str(posicion)+"."+monedasOrdenadas[posicion+1][0],"-",monedasOrdenadas[posicion+1][2])
monedasMenorValor(data)

            
 
    
