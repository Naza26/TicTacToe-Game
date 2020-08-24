import gamelib

import math

def juego_crear():
    """Inicializar el estado del juego"""
    matriz = []
    for fila in range(10):
        matriz.append([""]*10)
    return matriz

grilla = juego_crear()

for i in range(len(grilla)):
    print(grilla[i])


def mappeo_pixeles(y,x):
    # Quiero que cada celda mida 30 pixeles
    # De 0 a 30 px => [0], De 30 a 60 px => [1], De 60 a 90 px => [2], De 90 a 120 px => [3], De 120 a 150 px => [4], De 150 a 180 px => [5],
    # De 180 a 210 px => [6], De 210 a 240 px => [7], De 240 a 270 px => [8], De 270 a 300 px => [9]

    print("X: {}".format(x))
    print("Y: {}".format(y))

    if x / 30 == 0:
        pos_fila = 0 
    else:
        div_celda = x / 30
        pos_fila = math.ceil(div_celda) - 1
    if y / 30 == 0:
        pos_columna = 0
    else:
        div_celda = y / 30
        pos_columna = math.ceil(div_celda) - 1

    return pos_fila, pos_columna

def celda_vacia(grilla, y, x):

    nueva_grilla_juego = [x[:] for x in grilla]

    tupla_pixeles = mappeo_pixeles(y,x)

    pos_fila, pos_columna = tupla_pixeles

    try:
        if x <= 300 or y <= 300:

            celda_vacia = nueva_grilla_juego[pos_fila][pos_columna] == ""

            return celda_vacia
    except:
        print("Usted esta afuera del tablero")



def juego_actualizar(grilla, y, x, turno):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    nueva_grilla_juego = [x[:] for x in grilla]

    tupla_pixeles = mappeo_pixeles(y,x)

    pos_fila, pos_columna = tupla_pixeles

    primer_turno = "Turno de: {}".format("O")

    segundo_turno = "Turno de: {}".format("X")

    vacio = celda_vacia(grilla, y, x)

    try:
        if x <= 300 or y <= 300:
            if turno == 0:
                if vacio:
                    print(primer_turno)
                    nueva_grilla_juego[pos_fila][pos_columna] = "O"
                else:
                    return nueva_grilla_juego, turno #Si la celda esta ocupada no modifico el tablero y no cambio el turno
            else:
                if vacio:
                    print(segundo_turno)
                    nueva_grilla_juego[pos_fila][pos_columna] = "X"
                else:
                    return nueva_grilla_juego, turno
            turno += 1
            turno = turno % 2

    except IndexError:
        print("Usted esta fuera del tablero")


    return nueva_grilla_juego, turno


def turnos(turno):
    if turno == 0:
        turno = "Turno de: O"
    else:
        turno = "Turno de X"
    return turno

def centro_celda(pos_fila, pos_columna):
    
    mitad_celda_fila = 15 + 30 * pos_fila
    
    mitad_celda_columna = 15 + 30 * pos_columna

    return mitad_celda_fila, mitad_celda_columna

def juego_mostrar(grilla, turno):
    """Actualizar la ventana"""
    
    nueva_grilla_juego = [x[:] for x in grilla]

    draw_line(0, 300, 300, 300, fill='blue', width=2) #Esto es el tablero de gamelib

    turno = turnos(turno)
    
    draw_text(turno, 0, 250, fill='green',size=100) #Esto cambia los turnos en gamelib

    
    for fila in range(len(nueva_grilla_juego[0])):
        for columna in range(len(nueva_grilla_juego)):
            centro_celda_columna, centro_celda_fila = centro_celda(fila,columna)
            if nueva_grilla_juego[fila][columna] == "O":
                gamelib.draw_text('O', centro_celda_fila, centro_celda_columna, fill='orange', anchor='c')
                #print(centro_celda_fila, centro_celda_columna)
            if nueva_grilla_juego[fila][columna] == "X":
                gamelib.draw_text('X', centro_celda_fila, centro_celda_columna, fill='orange', anchor='c')
                #print(centro_celda_fila, centro_celda_columna)
def draw_line(x1, y1, x2, y2, **options):

    #Lineas Horizontales
    gamelib.draw_line(0, 300, 300, 300, fill='blue', width=2)
    gamelib.draw_line(0, 270, 300, 270, fill='blue', width=2)
    gamelib.draw_line(0, 240, 300, 240, fill='blue', width=2)
    gamelib.draw_line(0, 210, 300, 210, fill='blue', width=2)
    gamelib.draw_line(0, 180, 300, 180, fill='blue', width=2)
    gamelib.draw_line(0, 150, 300, 150, fill='blue', width=2)
    gamelib.draw_line(0, 120, 300, 120, fill='blue', width=2)
    gamelib.draw_line(0, 90, 300, 90, fill='blue', width=2)
    gamelib.draw_line(0, 60, 300, 60, fill='blue', width=2)
    gamelib.draw_line(0, 30, 300, 30, fill='blue', width=2)
    gamelib.draw_line(0, 0, 300, 0, fill='blue', width=2)

    #Lineas verticales
    gamelib.draw_line(300, 0, 300, 300, fill='red', width=2)
    gamelib.draw_line(270, 0, 270, 300, fill='red', width=2)
    gamelib.draw_line(240, 0, 240, 300, fill='red', width=2)
    gamelib.draw_line(210, 0, 210, 300, fill='red', width=2)
    gamelib.draw_line(180, 0, 180, 300, fill='red', width=2)
    gamelib.draw_line(150, 0, 150, 300, fill='red', width=2)
    gamelib.draw_line(120, 0, 120, 300, fill='red', width=2)
    gamelib.draw_line(90, 0, 90, 300, fill='red', width=2)
    gamelib.draw_line(60, 0, 60, 300, fill='red', width=2)
    gamelib.draw_line(30, 0, 30, 300, fill='red', width=2)
    gamelib.draw_line(0, 0, 0, 300, fill='red', width=2)


def draw_text(turno, x, y, size = 200, **options):
    gamelib.draw_text(turno, 300, 350, fill='green', anchor='se')    

def main():
    juego = juego_crear()
    turno = 0
    # Ajustar el tamaño de la ventana
    gamelib.resize(300, 350)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego,turno)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego, turno = juego_actualizar(juego, x, y, turno)
            print(juego)

gamelib.init(main)