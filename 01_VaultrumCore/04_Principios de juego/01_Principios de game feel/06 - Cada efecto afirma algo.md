## Definición

**Cada efecto afirma algo**: todo efecto —visual, sonoro, de cámara— es una oración sobre el estado del juego. Si no cambia lo que el jugador sabe, es ruido; si además tapa lo que tiene que seguir mirando, es un defecto. Y se dispara cuando pasa lo que afirma.

---

## Idea central

La falta de feel se siente como un defecto del juego. El exceso se siente como un defecto del **jugador**: un juego con demasiado juice parece confuso, y el que juega cree que es él el que no entiende. Por eso el exceso es el error más caro de detectar.

Dos pruebas deciden cada efecto:

```txt
la oracion     escribir en una linea que afirma. Si no se puede, o si otro efecto ya
               lo afirma, sobra
la oclusion    ¿tapa lo que el jugador sigue mirando? La pelota, el proximo apoyo,
               el enemigo, el camino. Si lo tapa, se recorta, por mucho que guste
```

Y una regla de reparto: **los tres eventos que siempre necesitan firma propia** —el que el jugador causa más veces, el que le cuesta algo y el que le da algo— suenan y se ven distintos entre sí. Si suenan igual, el juego se siente plano por más efectos que tenga.

---

## Especificación en Unity

```txt
la tabla       cada efecto del GDS tiene su fila: evento | efecto | que afirma
el disparo     el efecto se suscribe al evento del resultado (impacto, muerte, recogida),
               no al callback del input. El acuse de la accion no es de esta capa: es capa 1
               (03 - Respuesta instantanea)
oclusion       particulas y destellos en un orden de render que no tape al objeto que se
               sigue; el screenshake va despues del confiner, para que el borde no se coma la
               sacudida, y el confiner se achica en la amplitud maxima del shake (techo 3%)
               para no mostrar fuera del nivel (11_Camara_y_encuadre)
tres firmas    los tres eventos se distinguen por sonido con los ojos cerrados, y por
               forma o movimiento sin depender del color
```

---

## Quién lo aplica

```txt
Game Design    escribe la tabla con la oracion de cada efecto
UI/UX          fija cuanta senal entra por cada canal; un efecto que no entra, no entra
Arte           cada efecto visual dice lo que dice su fila, y nada mas
Programacion   suscribe cada efecto al evento de su resultado
Calidad        corre la prueba de la oracion y la de la oclusion jugando, y revisa en
               video a 1/4 de velocidad los efectos que se pisan
```

---

## Cómo se juzga

```txt
se mide     cada efecto del codigo tiene fila en el GDS; ningun efecto esta suscripto al
            input (el acuse no cuenta: es capa 1);
            los tres eventos clave tienen clips y efectos distintos
se juzga    si la oracion se lee jugando, y si algo tapa lo que importa
```

---

## Errores comunes

```txt
El mismo sonido para golpear, recibir y recoger: tres eventos, cero informacion.
El efecto al apretar el boton, no al pasar la cosa.
Particulas encima del objeto que hay que seguir.
Screenshake como sinonimo de "importante": si todo sacude, nada sacude.
Un efecto que solo se entiende con sonido.
```

---

## Fuentes

- `02_Game_feel` (Fundamentos) — la regla que separa juice de ruido, sus pruebas y los antipatrones.
- `60_Juice_It_or_Lose_It` y `59_The_Art_of_Screenshake` (Documentos) — el juice agregado de a un efecto, y el exceso a propósito.
- `16_Audio_como_gameplay` (Fundamentos) — el audio que confirma, advierte y ubica.
- `11_Camara_y_encuadre` (Fundamentos) — el orden del pipeline de cámara.
