# Evidencia_semanatec
Evidencia final de la semana tec

## Angélica Ríos Cuentas - A01705651 
## Actividad realizada: Pacman 
La primera modificación que hice fue que los fantasmas se movieran más rápido. Esto se logró al modificar en la función move() la parte de ontimer(move, 100). Aqui se hacia un delay de 1 segundo por lo que lo cambie a ontimer(move, 10) para que disminuyera el tiempo de delay, haciendo que los fantasmas se movieran más rápido.
La segunda modificación que realice fue el cambio del tablero para esto inverti los colores del tablero para que en vez de ser afuera negro y adentro azul  bgcolor('black') path.color('blue') se viera afuera azul y adentro negro bgcolor('blue') path.color('black'). Además modifiqué la matriz tiles que a través de 1 y 0 traza el mapa, para que tuviera una forma diferente a la original.
