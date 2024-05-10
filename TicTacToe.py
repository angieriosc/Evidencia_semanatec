# Importa funciones específicas de la biblioteca 'turtle' y un método 'line' de 'freegames'
from turtle import *
from freegames import line


board = {}  # Diccionario que verifica el estado de cada cuadrícula

# Función para dibujar la cuadrícula del juego
def grid():
    line(-67, 200, -67, -200) # Línea vertical izquierda
    line(67, 200, 67, -200)   # Línea vertical derecha
    line(-200, -67, 200, -67) # Línea horizontal inferior
    line(-200, 67, 200, 67)   # Línea horizontal superior

# Función para dibujar la letra X
def drawx(x, y):
    color('red')  # Establece el color de X a rojo
    line(x + 17, y + 17, x + 117, y + 117)
    line(x + 17, y + 117, x + 117, y + 17)

# Función para dibujar el círculo O
def drawo(x, y):
    color('blue')  # Establece el color de O a azul
    up()
    goto(x + 67, y + 17)
    down()
    circle(50)     # Dibuja el círculo con radio 62

# Función para redondear un valor hacia abajo al tamaño de la cuadrícula
def floor(value):
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0}     # Estado del jugador actual, 0 para X, 1 para O
players = [drawx, drawo]  # Lista de funciones de dibujo para X y O

# Función que maneja el evento de clic en una posición del tablero
def tap(x, y):
    x = floor(x)
    y = floor(y)
    key = (x, y)
    if key in board:  # Verifica si la casilla está ocupada
        return        # Si está ocupada, no hace nada
    board[key] = state['player']  # Marca la casilla como ocupada
    player = state['player']
    draw = players[player]
    draw(x, y)       # Dibuja la marca del jugador en la casilla
    update()         # Actualiza la pantalla
    state['player'] = not player  # Cambia al siguiente jugador

# Configuración inicial de la pantalla
setup(420, 420, 370, 0)  # Configura el tamaño y posición inicial de la ventana
hideturtle()              # Oculta la tortuga
tracer(False)             # Desactiva la animación para dibujar instantáneamente
grid()                    # Dibuja la cuadrícula del juego
update()                  # Actualiza la pantalla
onscreenclick(tap)        # Establece la función 'tap' como manejador de clics en la pantalla
done()                    # Finaliza el bucle de eventos de turtle
