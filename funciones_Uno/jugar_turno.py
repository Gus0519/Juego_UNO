
def jugar_turno(cartas_del_jugador, nombre_en_turno):  # (cartas_por_jugador[nombre],nombre)
    global carta_tope, contador_empate, cartas_jugadas
    carta_tope = cartas_jugadas[len(cartas_jugadas) - 1]  # guarda la carta de la cima de la pila

    print(f'Es tu turno {nombre_en_turno}'.center(30, '*'))
    # Imprime todo su juego de cartas
    print('Tus cartas disponibles son: ')

    cartas_jugables = []  # Almacenara las cartas que puede tirar

    for carta in cartas_del_jugador:
        print(carta)
        if (carta[0] == carta_tope[0]) or (carta[1] == carta_tope[1]):  # Determina cuales cartas se pueden tirar
            cartas_jugables.append(carta)

    # Imprimira las cartas que puede tirar con un numero asociado
    contador = 1
    if len(cartas_jugables) > 0:  # si tiene cartas que pueda jugar
        print('Las cartas que puedes jugar son: ')
        for carta in cartas_jugables:
            print(f'{contador}->{carta}')
            contador += 1

        eleccion = int(input('Ingresa el numero asociado a la carta que quieres tirar: '))
        carta_elegida = cartas_jugables.pop(eleccion - 1)
        print(f'\nLa carta elegida es: {carta_elegida}\n')
        cartas_jugadas.append(carta_elegida) #Agrega la carta a las cartas jugadas
        carta_tope = cartas_del_jugador.pop(cartas_del_jugador.index(carta_elegida))

        # Caso 0, tiene una carta jugable, la tira y le devuelve sus cartas restantes
        contador_empate = 0  # Se reinicia porque no se pasa el turno
        return cartas_del_jugador  # caso,cartas_del_jugador


    # Tomar del mazo
    else:
        print('\nUpss,no tienes cartas que puedas tirar, debes tomar del mazo'.center(50,'-'))
        # carta_tope = cartas_jugadas[len(cartas_jugadas)-1]

        caso, cartas_tomadas = tomar_del_mazo()

        if caso == 1:  # Encuentra una carta valida en la primera carta sacada
            contador_empate = 0  # Se reinicia porque no se paso el turno
            print(carta_tope)
            return cartas_del_jugador  #cartas_del_jugador(despues de tirar)

        elif caso == 2: #Encuentra una carta jugable iterando, regresa las cartas
            print(f'Las cartas tomadas del mazo son: {cartas_tomadas}')
            cartas_del_jugador += cartas_tomadas #Le suma las cartas que tomo
            contador_empate = 0 #Se reinicia porque no se paso el turno
            return cartas_del_jugador

        elif caso == 3: #Se acaba el mazo antes de encontrar una carta tirable
            print('Se acabaron las cartas del mazo ._.')
            print(f'Las cartas tomadas del mazo son: {cartas_tomadas}')
            cartas_del_jugador += cartas_tomadas #le suma las cartas que tomo
            contador_empate += 1 #Se aumenta en 1 porque se pasa el turno sin tirar
            return cartas_del_jugador

        elif caso == 0: #ya no hay cartas en el mazo
            print('No hay cartas que puedas tomar')
            contador_empate += 1 #Se aumenta en 1 porque se pasa el turno sin tirar
            return cartas_del_jugador