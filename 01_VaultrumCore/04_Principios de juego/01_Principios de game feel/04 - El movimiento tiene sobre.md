## Definición

**El movimiento tiene sobre**: lo que el jugador maneja acelera, sostiene y frena con **números declarados** —el sobre ADSR: ataque, decaimiento, sostenido, liberación—, elegidos según la metáfora. Se mueve en curvas y no en saltos de valor, y se mueve igual en cualquier máquina.

---

## Idea central

Es la capa que produce predicción, y la que se describe peor: *"resbaloso"*, *"pesado"*, *"duro"*. El sobre convierte esos adjetivos en parámetros.

```txt
sobre corto    ajustado y responsivo
sobre largo    suelto y fluido: flotante si lo largo es el ataque, sobre hielo si es
               la liberacion
```

Ninguno es el correcto. La **metáfora** decide cuál espera el jugador: un auto con frenado de nave se siente roto aunque frene perfecto, y cuanto más real la metáfora, más angosta la franja que el jugador acepta.

Las dos mitades no pesan igual. Medido con jugadores, la **liberación** decide cuán responsivo se siente el control —se sostiene alto mientras el frenado ronde 0.25 s o menos— y el **ataque** decide cuán flotante —un ataque de más de un segundo flota—. Por eso el frenado tiene ventana propia, y más corta.

Y **predecible** quiere decir predecible en todas las máquinas: un suavizado escrito por cuadro da un movimiento distinto a 30 y a 144 fps, y el jugador no puede anticipar algo que cambia con el hardware.

---

## Especificación en Unity

```txt
parametros   aceleracion, velocidad maxima y desaceleracion en unidades/s y segundos,
             en el ScriptableObject del avatar. Nunca literales en el codigo
curvas       AnimationCurve cuando el sobre no es lineal; la forma la dice el GDS
paso         el movimiento se integra con el paso fijo. Un Lerp con factor constante
             por cuadro no se usa: depende del framerate (03_Matematica_del_movimiento)
fisica       con Rigidbody, el sobre se escribe sobre la velocidad. Si se usa el
             damping del motor, su valor es parte del sobre y se declara como tal
baseline     ataque al 90% en 0.1-0.2 s · liberacion 0.08-0.15 s (02_Game_feel)
```

---

## Quién lo aplica

```txt
Game Design    declara la metafora y el sobre. El Balanceador fija los valores iniciales
Programacion   implementa el sobre sin inventar valores, y lo hace independiente del framerate
Arte           el arranque y el frenado de la animacion acompanan el sobre: no lo contradicen
Calidad        mide el sobre en el motor y lo compara con el GDS
```

---

## Cómo se juzga

```txt
se mide     el ataque y la liberacion medidos en el motor (velocidad contra tiempo)
            contra los del GDS; el mismo recorrido grabado a 30 y a 144 fps llega igual
se juzga    si el sobre es el que la metafora promete
```

Cuando el playtest dice un adjetivo, se mide su parámetro antes de tocar nada: *flotante* es el ataque; *resbaloso*, *sobre hielo*, *duro* o *rígido*, la liberación; *pesado*, primero la latencia medida y después el ataque.

---

## Errores comunes

```txt
Velocidad binaria: quieto o a fondo, sin ataque ni liberacion.
Valores de movimiento escritos en el codigo.
Suavizado por cuadro que cambia con el framerate.
Alargar el frenado "para dar peso": se siente sobre hielo.
Afinar por adjetivos sin medir el sobre.
Una metafora realista con fisica de cursor.
```

---

## Fuentes

- `02_Game_feel` (Fundamentos) — el sobre de respuesta y el baseline.
- `05_Game_Feel` (Fuentes) — el sobre ADSR, resultados predecibles y movimiento orgánico (esta última, lectura Vaultrum sin confrontar con el capítulo 17).
- `70_Measuring_Game_Feel_Acceleration` (Fuentes) — el sobre medido con jugadores.
- `03_Matematica_del_movimiento` y `01_Bucle_de_simulacion` (Construcción) — el suavizado independiente del framerate y el paso fijo.
