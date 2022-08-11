def desempate(cartas_por_jugador,nombres):
    sum_valores_por_jugador = []
    
    for nombre in nombres: #Por cada jugador
        suma = 0
        for carta in cartas_por_jugador[nombre]: #Por cada carta de cada jugador
            suma += carta[1]
        sum_valores_por_jugador.append(suma)
        
    ganador = nombres[sum_valores_por_jugador.index(min(sum_valores_por_jugador))]
    
    return ganador

# cartas_por_jugador = {'Gus':[['Azul',6],['Rojo',8],['Verde',2],['Azul',8]]
#                     ,'Pedro':[['Azul',4],['Rojo',5],['Azul',9],['Amarillo',6],['Amarillo',8]],
#                     'Pepe':[['Verde',2]]}
# nombres = ['Gus','Pedro','Pepe']


# ganador = desempate(cartas_por_jugador, nombres)
# print(ganador)