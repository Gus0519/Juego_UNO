from mazo import *
import random

def repartir_cartas():
    #Revolver las cartas
    random.shuffle(mazo)
    valido = False
    while valido == False:
        entrada = int(input('El numero de personas que jugaran(2-10 jugadores):  '))
        if entrada >= 2 and entrada <=10:
            valido = True
        else:
            print('Error, ingresa un numero valido')
        
    num_jugador = [*range(1,entrada+1)]
    jugadores = {}
    contador = 1
    nombres = [] #Crea una lista con los nombres de los jugadores
    for i in num_jugador: #Repite el proceso por cada jugador
        nombre = input(f'Ingresa el nombre del jugador {contador}: ')
        nombres.append(nombre.capitalize())
        jugadores[nombre.capitalize()] = []#en esta lista se asignaran sus cartas
        contador+=1
    
    for k in range(7):   #Reparte siete cartas 
        for n in nombres: #Para cada uno de los jugadores
            aux = jugadores[n]
            aux.append(mazo.pop())
            jugadores[n] = aux
    return jugadores,nombres
    
    
cartas_por_jugador,nombres = repartir_cartas()
print(cartas_por_jugador)
print(nombres)