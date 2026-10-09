## Definición

**Timing**: cuánto dura una acción, en cuadros o en segundos. Y junto con él, el **spacing**: cómo se reparte el movimiento dentro de ese tiempo.

```txt
timing    el mismo gesto en 6 cuadros es un latigazo; en 24, una caricia
spacing   con el mismo timing, cuadros juntos cerca de las poses = suave;
          cuadros separados = rapido, con impacto
```

El timing da peso, tamaño y carácter. Una cosa grande tarda más en arrancar y en frenar.

---

## Idea central

**El ritmo es la información.** La cátedra lo dejó como regla de dos lados: *si es muy lento frustra al jugador, si es muy rápido no se entiende nada*. Y depende del contexto y de la estética, no de un número universal.

---

## Especificación para videojuegos

```txt
el gameplay fija el tiempo      preparacion, actividad y recuperacion en cuadros a la
                                frecuencia que declara el proyecto (por ejemplo, 60).
                                El animador encaja
                                poses en ese tiempo; no lo estira
cuadros de animacion no son     una caminata de 8 dibujos a 10 por segundo dura 0.8 s en
cuadros de simulacion           un juego que corre a 60: cada dibujo se sostiene 6 ticks.
                                Duracion = dibujos / dibujos por segundo, nunca dibujos / 60
mas dibujos no es mejor         el 2D se anima "en unos" (un dibujo por cuadro) o "en dos"
                                (cada dibujo dos cuadros): en dos es la norma de la animacion
                                tradicional a 24. Mas dibujos es mas memoria, no mas calidad
la velocidad de reproduccion    cambiar la velocidad del clip para que "coincida" cambia la
no es timing                    zancada contra el desplazamiento: los pies patinan
```

**Tres tiempos para una transición** (cátedra, 10-08):

```txt
utilitaria   casi inmediata. Abrir el inventario por decima vez
contextual   breve y controlada. Pasar de explorar a combatir
dramatica    lenta, si el contexto lo permite. Un final, una revelacion
```

**Una escala de referencia para caminar.** Williams da una escala por paso, a 24 cuadros por segundo: alrededor de 12 cuadros es una caminata natural, menos es apuro o carrera, y 16 o más es un paso lento. Es una referencia de cine para empezar, no un parámetro de juego: el parámetro sale de la velocidad del personaje y de su zancada (`RA-011`, regla 4).

---

## Cómo se juzga

```txt
se mide     la duracion del ciclo (animacion.py --gif) y la duracion por cuadro declarada
            en el manifiesto (RA-012); en motor, los cuadros de cada tramo contra el GDS
se juzga    si pesa lo que tiene que pesar y si el ritmo se lee
```

---

## Errores comunes

```txt
Timing uniforme: todo dura lo mismo, nada tiene peso.
Calcular la duracion con los fps del juego en vez de los de la animacion.
Animar a 60 dibujos por segundo "para que sea fluido".
Arreglar el patinaje cambiando la velocidad del clip.
Transiciones dramaticas en una accion que el jugador repite cien veces.
```

---

## Fuentes

- `59_The_Illusion_of_Life` — el principio.
- `60_The_Animators_Survival_Kit` — timing, spacing y la escala de la caminata.
- `61_Game_Anim` — el tiempo que fija el gameplay.
- `68_Apuntes_de_catedra_Animacion_2D_3D` — el ritmo y los tres tipos de transición.
- `RA-010` (con su tabla previa a `TL-012`) y `RA-011` del Área de Arte.
