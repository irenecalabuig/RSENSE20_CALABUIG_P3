"""
Created on Thu Oct 22 09:45:17 2020

@author: Irene
"""

"""
EJERCICIO 5: acumular datos durante 5 segdundos, calcule el promedio y desviación estándar 
             representar en tiempo real
"""
## LIBRERÍAS
import csv
import serial
import time
import matplotlib.pyplot as plt
import statistics

### CONFIGURACIÓN ESP32 ###
puerto = "COM3"                       # número de puerto al que conecto el ESP32 
baudio = 115200                       # velocidad de datos de bits por segundo
esp32 = serial.Serial(puerto, baudio) # defino el objeto esp32 señalando el puerto y la velocidad
time.sleep(2) 

### VARIABLES ###
cont = 0

nombre_archivo ="datos.txt"

datos=[]

accx=[]   
accy=[]
accz=[]

meanx=[]
meany=[]
meanz=[]

devx=[]
devy=[]
devz=[]

t=[]

plt.figure()
plot1 = plt.subplot(2,2,1)
plot2 = plt.subplot(2,2,2)
plot3 = plt.subplot(2,2,3)

with open(nombre_archivo,'w',newline='') as csvFile:

    writer = csv.writer(csvFile,delimiter=';')
    while True:   
#        respuesta = esp32.readline()
#        print(respuesta)
#        datos.append(str(respuesta))
        respuesta = esp32.readline()
        respuesta = respuesta.decode("utf-8") #ser.readline returns a binary, convert to string
        respuesta = respuesta.replace(",", ";");
       
        datos.append(respuesta)
    
        if(cont>10):
            a,b,c= datos[cont].split(";") 
            t.append(cont-10)
            accx.append(float(a))   
            accy.append(float(b))
            accz.append(float(c)) 
            writer.writerow([float(a),float(b),float(c)]) 
            
            meanx.append(statistics.mean(accx))
            meany.append(statistics.mean(accy))
            meanz.append(statistics.mean(accz))
            
            devx.append(statistics.pstdev(accx))
            devy.append(statistics.pstdev(accy))
            devz.append(statistics.pstdev(accz))
            
        cont=cont+1
        if(cont>110):
            break
     
    
plot1.plot(t,accx,color='plum', label='Eje x')
plot1.plot(t,accy,color='lightsteelblue', label='Eje y')
plot1.plot(t,accz,color='lightseagreen', label='Eje z')

plot2.plot(t,meanx,color='plum', label='Eje x')
plot2.plot(t,meany,color='lightsteelblue', label='Eje y')
plot2.plot(t,meanz,color='lightseagreen', label='Eje z')

plot3.plot(t,devx,color='plum', label='Eje x')
plot3.plot(t,devy,color='lightsteelblue', label='Eje y')
plot3.plot(t,devz,color='lightseagreen', label='Eje z')

plot1.set_title(" MEDIDAS ACELERÓMETRO ")
plot1.set_ylabel("Aceleración (m/s2)")
plot1.set_xlabel("nº muestras")    
plot1.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)   

plot2.set_title(" MEDIA ")
plot2.set_ylabel("Aceleración (m/s2)")
plot2.set_xlabel("nº muestras")    
plot2.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)    

plot3.set_title(" DESVIACIÓN TÍPICA ")
plot3.set_ylabel("Aceleración (m/s2)")
plot3.set_xlabel("nº muestras")    
plot3.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)     

print("Fin")
esp32.close()
csvFile.close()


