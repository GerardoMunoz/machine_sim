from machine import Pin
from time import sleep
import math

coseno=machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
cuadrada=machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
rampa=machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)

tabla1=[0.0,0,1,3,5,7,9,12,14,14,15,15,14,12,10,7.5,5,3,1,0,0.0]
tabla2=[0,0,0,0,0,0,0,0,0,0,15,15,15,15,15,15,15,15,15,15]
tabla3=[0,0.75,1.5,2.25,3,3.75,4.5,5.25,6,6.75,7.5,8.25,9,9.75,10.5,11.25,12,12.75,13.5,14.25,15]

def est_sig_sal(estado, entrada):
    if estado == 'inicio':
        salida = [0,0,0]
        #print ('estoy en incio...')
        if entrada == [1,0,0]:
            estado = 'coseno'
        elif entrada == [0,1,0]:
            estado = 'cuadrada'
        elif entrada == [0,0,1]:
            estado = 'rampa'
            
    elif estado == 'coseno':
        salida = [1,0,0]
        #print ('Estoy en coseno...')
        if entrada == [0,1,0]:
            estado = 'cuadrada'
        elif entrada == [0,0,1]:
            estado = 'rampa'
            
    elif estado == 'cuadrada':
        salida = [0,1,0]
        #print ('Estoy en cuadrada')
        if entrada == [1,0,0]:
            estado = 'coseno'
        elif entrada == [0,0,1]:
            estado = 'rampa'
            
    elif estado == 'rampa':
        salida=[0,0,1]
        #print ('Estoy en rampa')
        if entrada == [1,0,0]:
            estado = 'coseno'
        elif entrada == [0,1,0]:
            estado = 'cuadrada'
            
    return estado,salida

estado='inicio'

while True:
    
        entrada=[not coseno.value(),not cuadrada.value(),not rampa.value()]
        if(entrada[0]==1):
            for j in range (20):
                print(tabla1[j])
                sleep(0.05)
               
        if(entrada[1]==1):
            for j in range (20):
                
                print(tabla2[j])
                sleep(0.05)
        if(entrada[2]==1):
            for j in range (20):
                
                print(tabla3[j])
                sleep(0.05)
    
        