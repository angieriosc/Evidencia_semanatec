# Evidencia_semanatec
A01706282 - Laura Helena Molina Jiménez
Evidencia final de la semana tec

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
