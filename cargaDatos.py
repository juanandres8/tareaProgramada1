#Importación de librerias
import pickle
import csv
import json

#Definición de función para cargar los datos
def leer(nombreArchivoLeer):
    try:
        archivo=open(nombreArchivoLeer,"r", encoding="utf-8-sig")
        data=archivo.readlines(1000)
        for linea in data:
            print(linea,end="")
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

data=leer("nombreArchivoLeer.csv")
escribirToon(data)
    
    
    
    
