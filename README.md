# Evidencia Semana Tec

## Angélica Ríos Cuentas - A01705651 
### Actividad realizada: Pacman 

En esta actividad realicé dos modificaciones importantes:

1. **Velocidad de los fantasmas:** La primera modificación consistió en aumentar la velocidad de los fantasmas. Esto se logró modificando la función `move()`. Anteriormente, la línea `ontimer(move, 100)` establecía un retraso de 1 segundo entre movimientos. Cambié esto a `ontimer(move, 10)` para reducir el tiempo de retraso a 0.1 segundo, lo que provocó que los fantasmas se movieran más rápido.

2. **Cambio en el diseño del tablero:** La segunda modificación implicó cambiar el diseño del tablero. Invertí los colores del tablero para que el exterior fuera azul y el interior negro, en lugar de la configuración original que era exterior negro e interior azul (`bgcolor('black')` y `path.color('blue')`). Además, ajusté la matriz `tiles`, que define el mapa a través de valores binarios (1 y 0), para que tuviera una forma diferente a la original.

Estas modificaciones mejoraron la experiencia del juego y agregaron un toque personalizado al diseño del tablero.
