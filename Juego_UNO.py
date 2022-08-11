import random
import time

mazo = [['Azul',0],['Azul',1],['Azul',1],['Azul',2],['Azul',2]
        ,['Azul',3],['Azul',3],['Azul',4],['Azul',4],['Azul',5]
        ,['Azul',5],['Azul',6],['Azul',6],['Azul',7],['Azul',7],
        ['Azul',8],['Azul',8],['Azul',9],['Azul',9],
        ['Rojo',0],['Rojo',1],['Rojo',1],['Rojo',2],['Rojo',2]
        ,['Rojo',3],['Rojo',3],['Rojo',4],['Rojo',4],['Rojo',5]
        ,['Rojo',5],['Rojo',6],['Rojo',6],['Rojo',7],['Rojo',7],
        ['Rojo',8],['Rojo',8],['Rojo',9],['Rojo',9],
        ['Verde',0],['Verde',1],['Verde',1],['Verde',2],['Verde',2]
        ,['Verde',3],['Verde',3],['Verde',4],['Verde',4],['Verde',5]
        ,['Verde',5],['Verde',6],['Verde',6],['Verde',7],['Verde',7],
        ['Verde',8],['Verde',8],['Verde',9],['Verde',9],
        ['Amarillo',0],['Amarillo',1],['Amarillo',1],['Amarillo',2],['Amarillo',2]
        ,['Amarillo',3],['Amarillo',3],['Amarillo',4],['Amarillo',4],['Amarillo',5]
        ,['Amarillo',5],['Amarillo',6],['Amarillo',6],['Amarillo',7],['Amarillo',7],
        ['Amarillo',8],['Amarillo',8],['Amarillo',9],['Amarillo',9]]


def repartir_cartas():
    # Revolver las cartas
    random.shuffle(mazo)
    valido = False
    entrada = None
    while valido == False:
        entrada = int(input('El numero de personas que jugaran(2-10 jugadores):  '))
        if entrada >= 2 and entrada <= 10:
            valido = True
        else:
            print('Error, ingresa un numero valido')

    num_jugador = [*range(1, entrada + 1)]
    jugadores = {}
    contador = 1
    nombres = []  # Crea una lista con los nombres de los jugadores
    for i in num_jugador:  # Repite el proceso por cada jugador
        nombre = input(f'Ingresa el nombre del jugador {contador}: ')
        nombres.append(nombre.capitalize())
        jugadores[nombre.capitalize()] = []  # en esta lista se asignaran sus cartas
        contador += 1

    for k in range(7):  # Reparte siete cartas
        for n in nombres:  # Para cada uno de los jugadores
            aux = jugadores[n]
            aux.append(mazo.pop())
            jugadores[n] = aux
    return jugadores, nombres

def tomar_del_mazo():
    global carta_tope, cartas_jugadas
    cartas_tomadas = []
    if len(mazo) > 0:
        carta_tomada = mazo.pop()  # Toma una carta inicialmente

        print(f'Carta tomada: {carta_tomada}')  # imprime la carta

        while (carta_tomada[0] != carta_tope[0] and carta_tomada[1] != carta_tope[1]): #Mientras la carta no sea valida
            cartas_tomadas.append(carta_tomada)  # Como no es valida la agrega a las cartas tomadas
            time.sleep(1.4)
            print(f'Monton de cartas tomadas hasta el momento: {cartas_tomadas}\n')
            time.sleep(1.4)
            print('Carta no valida, continua sacando cartas')
            carta_tomada = mazo.pop()  # Saca otra carta
            time.sleep(2.0)
            print(f'Carta tomada: {carta_tomada}\n')


            # Caso 2, encuentra una carta jugable iterando
            if carta_tomada[0] == carta_tope[0] or carta_tomada[1] == carta_tope[1]:  # Si es valida
                time.sleep(2.0)
                print(f'Carta Valida:  {carta_tomada}\n')  # La imprime
                carta_tope = carta_tomada  # La tira(la nueva carta tope es la carta que tomo)
                cartas_jugadas.append(carta_tomada)  # La agrega a la pila de cartas jugadas
                return 2, cartas_tomadas  # Regresa caso 2, y las cartas tomadas

            # caso 3, se acaba el mazo antes de que se consiga una carta jugable
            if len(mazo) == 0:  # si  no hay tarjetas en el mazo que se puedan sacar
                print('Chin, ya no hay cartas por sacar\n')
                print('Se pasa el turno al siguiente jugador\n')
                return 3, cartas_tomadas  # Regresa caso 3, y las cartas tomadas


        # Caso 1, no entra al while porque le sale a la primera
        time.sleep(2.0)
        print(f'Carta valida: {carta_tomada}')
        carta_tope = carta_tomada  # La tira(la nueva carta tope es la carta que tomo)

        cartas_jugadas.append(carta_tomada)  # agrega la carta a la pila de cartas jugadas
        return 1, []  # regresa caso 1, y sin cartas tomadas

    # No hay cartas en el mazo
    else:
        return 0, []  # Regresa caso 0, y sin cartas tomadas


def jugar_turno(cartas_del_jugador, nombre_en_turno):  # (cartas_por_jugador[nombre],nombre)
    global carta_tope, contador_empate, cartas_jugadas
    carta_tope = cartas_jugadas[len(cartas_jugadas) - 1]  # guarda la carta de la cima de la pila

    time.sleep(2.0)
    print(f'Es tu turno {nombre_en_turno}'.center(30, '*'))
    # Imprime todo su juego de cartas
    time.sleep(1.0)
    print('Tus cartas disponibles son: ')

    cartas_jugables = []  # Almacenara las cartas que puede tirar

    for carta in cartas_del_jugador:
        time.sleep(0.5)
        print(carta)
        if (carta[0] == carta_tope[0]) or (carta[1] == carta_tope[1]):  # Determina cuales cartas se pueden tirar
            cartas_jugables.append(carta)

    # Imprimira las cartas que puede tirar con un numero asociado
    contador = 1
    if len(cartas_jugables) > 0:  # si tiene cartas que pueda jugar
        time.sleep(1.0)
        print('Las cartas que puedes jugar son: ')
        time.sleep(1.0)
        for carta in cartas_jugables:
            time.sleep(0.2)
            print(f'{contador}->{carta}')
            contador += 1

        time.sleep(0.5)
        eleccion = int(input('Ingresa el numero asociado a la carta que quieres tirar: '))
        carta_elegida = cartas_jugables.pop(eleccion - 1)
        print(f'\nLa carta elegida es: {carta_elegida}\n')
        cartas_jugadas.append(carta_elegida)  # Agrega la carta a las cartas jugadas
        carta_tope = cartas_del_jugador.pop(cartas_del_jugador.index(carta_elegida))

        # Caso 0, tiene una carta jugable, la tira y le devuelve sus cartas restantes
        contador_empate = 0  # Se reinicia porque no se pasa el turno
        return cartas_del_jugador  # caso,cartas_del_jugador


    # Tomar del mazo
    else:
        time.sleep(1.0)
        print('\nUpss,no tienes cartas que puedas tirar, debes tomar del mazo'.center(50, '-'))
        # carta_tope = cartas_jugadas[len(cartas_jugadas)-1]

        caso, cartas_tomadas = tomar_del_mazo()

        if caso == 1:  # Encuentra una carta valida en la primera carta sacada
            contador_empate = 0  # Se reinicia porque no se paso el turno
            time.sleep(0.5)
            print(carta_tope)
            return cartas_del_jugador  # cartas_del_jugador(despues de tirar)

        elif caso == 2:  # Encuentra una carta jugable iterando, regresa las cartas
            time.sleep(1.4)
            print(f'Las cartas tomadas del mazo son: {cartas_tomadas}')
            cartas_del_jugador += cartas_tomadas  # Le suma las cartas que tomo
            contador_empate = 0  # Se reinicia porque no se paso el turno
            return cartas_del_jugador

        elif caso == 3:  # Se acaba el mazo antes de encontrar una carta tirable
            print('Se acabaron las cartas del mazo ._.')
            print(f'Las cartas tomadas del mazo son: {cartas_tomadas}')
            cartas_del_jugador += cartas_tomadas  # le suma las cartas que tomo
            contador_empate += 1  # Se aumenta en 1 porque se pasa el turno sin tirar
            return cartas_del_jugador

        elif caso == 0:  # ya no hay cartas en el mazo
            print('No hay cartas que puedas tomar')
            contador_empate += 1  # Se aumenta en 1 porque se pasa el turno sin tirar
            return cartas_del_jugador


def desempate(cartas_por_jugador, nombres):
    sum_valores_por_jugador = []

    for nombre in nombres:  # Por cada jugador
        suma = 0
        for carta in cartas_por_jugador[nombre]:  # Por cada carta de cada jugador
            suma += carta[1]
        sum_valores_por_jugador.append(suma)

    ganador = nombres[sum_valores_por_jugador.index(min(sum_valores_por_jugador))]

    return ganador

#Juego
print("Bienvenido al Juego UNO".center(50),' ')
time.sleep(1.0)
print('\nEDA-16 Semestre 2022-2')
print('Desarrollado por:')
time.sleep(1.0)
print("De la rosa Lara Gustavo")
time.sleep(1.0)
print('\n\n')
time.sleep(2.0)
print('Empieza el juego'.center(30, '*'))
print()
time.sleep(1.0)


cartas_por_jugador, nombres = repartir_cartas() #Reparte correctamente
cartas_jugadas = []
cartas_jugadas.append(mazo.pop()) #toma la primera carta

carta_tope = cartas_jugadas[len(cartas_jugadas)-1]


print(f'\nPrimera carta: -> {carta_tope}')

sin_tarjetas = False #Condicion 1 para que se acabe el juego
contador_empate = 0 #Condicion 2 para que se acabe el juego
ganador = ''

while sin_tarjetas == False and contador_empate != len(nombres):
    for nombre in nombres:
        cartas_por_jugador[nombre] = jugar_turno(cartas_por_jugador[nombre], nombre)
        print(f'{carta_tope}'.center(50,'-'))

        if len(cartas_por_jugador[nombre]) == 0:
            ganador = nombre
            sin_tarjetas = True

if sin_tarjetas == True:
    print(f'Ganador: {ganador}'.center(50,'*'))
#Si nadie acaba sus tarjetas y todos pasan, se efectua el desempate
if contador_empate == len(nombres):
    print('\nNos vamos al desempate')
    ganador = desempate(cartas_por_jugador, nombres)
    print(f'El ganador es: {ganador}')