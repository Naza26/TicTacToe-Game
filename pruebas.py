
import math
    # Quiero que cada celda mida 30 pixeles
    # De 0 a 30 px => [0], De 30 a 60 px => [1], De 60 a 90 px => [2], De 90 a 120 px => [3], De 120 a 150 px => [4], De 150 a 180 px => [5],
    # De 180 a 210 px => [6], De 210 a 240 px => [7], De 240 a 270 px => [8], De 270 a 300 px => [9]
def mappeo_pixeles(y, x):

	print("X: {}".format(x))
	print("Y: {}".format(y))

	if x / 30 == 0:
		div_celda = x / 30
		pos_fila = div_celda - 1

	if x / 30 != 0:
		div_celda = x / 30
		pos_fila = math.ceil(div_celda) - 1

	print("Posicion de la fila: {}".format(pos_fila))

	if y / 30 == 0:
		div_celda = y / 30
		pos_columna = div_celda - 1

	if y / 30 != 0:
		div_celda = y / 30
		pos_columna = math.ceil(div_celda) - 1

	print("Posicion de la columna: {}".format(pos_columna))

	return pos_fila, pos_columna

# assert mappeo_pixeles(61, 61) == (2, 2)
# assert mappeo_pixeles(61, 31) == (1, 2)
# assert mappeo_pixeles(11, 11) == (0, 0)
# assert mappeo_pixeles(121, 121) == (4, 4)
# assert mappeo_pixeles(1, 1) == (0, 0)
# assert mappeo_pixeles(300, 300) == (9,9)
# assert mappeo_pixeles(257, 15) == (0,8)
def juego_crear():
    """Inicializar el estado del juego"""
    matriz = []
    for fila in range(10):
        matriz.append([""]*10)
    return matriz

grilla = juego_crear()

for i in range(len(grilla)):
    print(grilla[i])

# def turnos(grilla,x, y):

#     tupla_pixeles = mappeo_pixeles(x,y)

#     pos_fila, pos_columna = tupla_pixeles

#     jugador_turno = "Turno de: {}"

#     primer_turno = "Turno de: {}".format("O")

#     segundo_turno = "Turno de: {}".format("X")

#     lista_turnos = [primer_turno]


#     if x <= 300 and y <= 300: #Deberia poder hacer click porque estoy adentro del juego. El juego es de 300px por 300px
#       for x in range(len(grilla)):
#         for y in range(len(grilla[0])):
#           #lista_turnos.append(segundo_turno)
#           print(len(lista_turnos))
#           for indice in range(len(lista_turnos)):
#             if indice % 2 == 0:
#               lista_turnos.append(segundo_turno)
#             if indice % 2 != 0:
#               lista_turnos.append(primer_turno)
#             print(len(lista_turnos))    
#             return lista_turnos[-1]


# print(turnos(grilla,95,30))

def juego_actualizar(grilla, x, y):

    nueva_grilla_juego = [x[:] for x in grilla]

    tupla_pixeles = mappeo_pixeles(60,200)

    pos_fila, pos_columna = tupla_pixeles

    primer_turno = "Turno de: {}".format("O")

    segundo_turno = "Turno de: {}".format("X")

    turno = 0


    if turno == 0:
        print(primer_turno)
        nueva_grilla_juego[pos_columna][pos_fila] = "O" #O la llamada al dibujo
        return nueva_grilla_juego
    else:
        print(segundo_turno)
        nueva_grilla_juego[pos_columna][pos_fila] = "X"
        turno += 1
        turno = turno % 2
        return nueva_grilla_juego

print(juego_actualizar(grilla, 100,100))
