"""
Created on Thu Oct 22 09:45:17 2020

@author: Irene

"""
"""
EJERCICIO 4: almacenar datos en un fichero .txt separando las variable por ';'
"""
## LIBRERÍAS
import csv
import serial
import time

### CONFIGURACIÓN ESP32 ###
puerto = "COM3"                       # número de puerto al que conecto el ESP32 
baudio = 115200                       # velocidad de datos de bits por segundo
esp32 = serial.Serial(puerto, baudio) # defino el objeto esp32 señalando el puerto y la velocidad
time.sleep(2)  

### VARIABLES ###
cont = 0
datos=[]
nombre_archivo ="datos.txt"


with open(nombre_archivo,'w',newline='') as csvFile:

    writer = csv.writer(csvFile,delimiter=';')
    while True:   
        salida = esp32.readline()          # devuelve un número binario
        salida = salida.decode("utf-8")    # cast de binario a string
        salida = salida.replace(",", ";"); # reemplazar ',' por ';'       
        datos.append(salida)               # añade los elementos salida a la lista datos[]
    
        if(cont>10):                       # cuando llega a este valor, la señal recibida por el sensor es estable 
            a,b,c= datos[cont].split(";")  # divide la cadena cada vez aue ve ';'    
            writer.writerow([float(a),float(b),float(c)])                   
           
        cont=cont+1
        if(cont>110):
            break     
 

esp32.close()
csvFile.close()





