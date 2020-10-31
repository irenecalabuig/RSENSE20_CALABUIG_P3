
"""
Created on Thu Oct 22 09:45:17 2020

@author: Irene
"""

"""
EJERCICIO 3: acceder al puerto serie y m por pantalla los datos en tiempo real
"""
## LIBRERÍAS
import serial
import time

### CONFIGURACIÓN ESP32 ###
puerto = "COM3"                       # número de puerto al que conecto el ESP32 
baudio = 115200                       # velocidad de datos de bits por segundo
esp32 = serial.Serial(puerto, baudio) # defino el objeto esp32 señalando el puerto y la velocidad
time.sleep(2)                         # espero 2s para que se acople el puerto serie

### VARIABLES ###
cont = 0

while True:    
    while cont>10:                      # cuando llega a este valor, la señal recibida por el sensor es estable 
        salida = esp32.readline()       # devuelve un número binario
        salida = salida.decode("utf-8") # cast de binario a string
        print(salida)
    cont = cont +1;
    
    
    
    
    