# Evidencia Semana Tec

## Angélica Ríos Cuentas - A01705651 
### Actividad realizada: Pacman 

En esta actividad realicé dos modificaciones importantes:

1. **Velocidad de los fantasmas:** La primera modificación consistió en aumentar la velocidad de los fantasmas. Esto se logró modificando la función `move()`. Anteriormente, la línea `ontimer(move, 100)` establecía un retraso de 1 segundo entre movimientos. Cambié esto a `ontimer(move, 10)` para reducir el tiempo de retraso a 0.1 segundo, lo que provocó que los fantasmas se movieran más rápido.

2. **Cambio en el diseño del tablero:** La segunda modificación implicó cambiar el diseño del tablero. Invertí los colores del tablero para que el exterior fuera azul y el interior negro  (`bgcolor('blue')` y `path.color('black')`), en lugar de la configuración original que era exterior negro e interior azul (`bgcolor('black')` y `path.color('blue')`). Además, ajusté la matriz `tiles`, que define el mapa a través de valores binarios (1 y 0), para que tuviera una forma diferente a la original.

Estas modificaciones mejoraron la experiencia del juego y agregaron un toque personalizado al diseño del tablero.

# Evidencia_semanatec
## A01706282 - Laura Helena Molina Jiménez
### Evidencia final de la semana tec

Juego de Tic Tac Toe

En este proyecto se tuvo por objetivo modificar el programa TicTacToe.py.
Para estos cambios se pidió modificar el tamaño y el color de los símbolos 
"X" y "O" y centrarlos, así como validar si una casilla ya se encuentra 
ocupada.

Las funciones que fueron modificadas fueron 'drawx()', 'drawo()' y 'tap()'.

Dentro de 'drawx()' se modificaron las coordenadas para la generación de "X" 
y se agregó la función color para cambiar el color de "X".

En la  función 'drawo()' se modificaron las coordenadas para la generación de 
"O" así como el radio de "O". Se agregó la función color para cambiar el 
color de "O".

Para la validar si una casilla está ocupada se creó un diccionario y en la 
función 'tap()' se crea una llave que representa la casilla en la que se ha
hecho click y valida que no esté dicha llave en el diccionario. En caso de
no estar se actualiza el diccionario, en caso de estar ocupada no regresa
ninguna salida.

Asimismo, durante la realización de la entrega se estuvo haciendo control de
versiones con git, utilizando los comandos como git add -A, git commit -m,
git push, git pull, etc. Por último, mediante la isntalación y suo de la 
herramienta Flake8 se validó que el código de TicTacToe.py cumpliera con los
estándares de PEP8.