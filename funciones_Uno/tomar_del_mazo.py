from mazo import mazo
from repartir_cartas import *
import random 

'''
caso 3 encuentra la carta en la primer carta tomada, no entra en la iteracion
caso 1:encuentra una carta jugable entrando en la iteracion,regresa las cartas que el jugador saco y la nueva carta tope
caso 2: Saca tarjetas pero se acaba el mazo, la funcion retorna el monton de cartas que saco
    y la carta_tope tal y como la recibio
caso 0 : no hay mazo del cual tomar cartas, retorna la carta_tope tal y como la recibio
'''

def tomar_del_mazo():
    global carta_tope, cartas_jugadas
    cartas_tomadas = []
    if len(mazo) > 0:
        carta_tomada = mazo.pop()  # Toma una carta inicialmente

        print(f'Carta tomada: {carta_tomada}')  # imprime la carta

        while (carta_tomada[0] != carta_tope[0] and carta_tomada[1] != carta_tope[1]): #Mientras la carta no sea valida
            cartas_tomadas.append(carta_tomada)  # Como no es valida la agrega a las cartas tomadas
            print(f'\nMonton de cartas tomadas hasta el momento: {cartas_tomadas}\n')
            print('Carta no valida, continua sacando cartas')
            carta_tomada = mazo.pop()  # Saca otra carta
            print(f'Carta tomada: {carta_tomada}\n')


            # Caso 2, encuentra una carta jugable iterando
            if carta_tomada[0] == carta_tope[0] or carta_tomada[1] == carta_tope[1]:  # Si es valida
                print(f'Carta Valida:  {carta_tomada}\n')  # La imprime
                carta_tope = carta_tomada  # La tira(la nueva carta tope es la carta que tomo)
                cartas_jugadas.append(carta_tomada)  # La agrega a la pila de cartas jugadas
                return 2, cartas_tomadas  # Regresa caso 2, y las cartas tomadas

            # caso 3, se acaba el mazo antes de que se consiga una carta jugable
            if len(mazo) == 0:  # si  no hay tarjetas en el mazo que se puedan sacar
                print('Chin, ya no hay cartas por sacar\n')
                print('Se pasa el turno al siguiente jugador\n')
                return 3, cartas_tomadas  # Regresa caso 3, y las cartas tomadas


        # Caso 1, no entra al while pq le sale a la primera
        print(f'Carta valida: {carta_tomada}')
        carta_tope = carta_tomada  # La tira(la nueva carta tope es la carta que tomo)

        cartas_jugadas.append(carta_tomada)  # agrega la carta a la pila de cartas jugadas
        return 1, []  # regresa caso 1, y sin cartas tomadas

    # No hay cartas en el mazo
    else:
        return 0, []  # Regresa caso 0, y sin cartas tomadas