from turtle import *  # Importa todas las funciones de Turtle
from freegames import line  # Importa la función line del módulo freegames

# Función para dibujar la cuadrícula del juego
def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)  # Línea vertical izquierda
    line(67, 200, 67, -200)    # Línea vertical derecha
    line(-200, -67, 200, -67)  # Línea horizontal inferior
    line(-200, 67, 200, 67)    # Línea horizontal superior

# Función para dibujar la letra X
def drawx(x, y):
    """Draw X player."""
    line(x, y, x + 133, y + 133)   # Dibuja la primera diagonal de la X
    line(x, y + 133, x + 133, y)   # Dibuja la segunda diagonal de la X

# Función para dibujar el círculo
def drawo(x, y):
    """Draw O player."""
    up()
    goto(x + 67, y + 5)   # Posiciona el cursor para dibujar el círculo
    down()
    circle(62)            # Dibuja el círculo con radio 62

# Función para redondear un valor hacia abajo al tamaño de la cuadrícula
def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0}   # Estado del jugador actual, 0 para X, 1 para O
players = [drawx, drawo]  # Lista de funciones de dibujo para X y O

# Función que maneja el evento de clic en una posición del tablero
def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']  # Obtiene el jugador actual
    draw = players[player]   # Obtiene la función de dibujo correspondiente
    draw(x, y)   # Dibuja X o O en la posición clickeada
    update()    # Actualiza la pantalla
    state['player'] = not player   # Cambia al siguiente jugador

# Configuración inicial de la pantalla
setup(420, 420, 370, 0)   # Configura el tamaño y la posición de la ventana
hideturtle()              # Oculta el cursor de Turtle
tracer(False)             # Desactiva la animación de Turtle
grid()                    # Dibuja la cuadrícula del juego
update()                  # Actualiza la pantalla
onscreenclick(tap)        # Asigna la función tap al evento de clic
done()                    # Finaliza el programa
