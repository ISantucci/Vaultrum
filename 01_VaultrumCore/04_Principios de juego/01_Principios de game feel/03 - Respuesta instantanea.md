## Definición

**Respuesta instantánea**: toda acción del jugador tiene un **acuse perceptible en dos cuadros** (33 ms a 60 fps), y la cadena completa —del dispositivo a la pantalla— no pasa del **tope de su género** que fija `10_Input_y_respuesta`: 65 ms como baseline de acción, 50 ms en plataformas de precisión y fighting. 100 ms es el borde donde el control deja de sentirse instantáneo: nunca el objetivo. El acuse es la acción empezando; la confirmación es su resultado, cuando pasa.

---

## Idea central

Es un umbral de percepción, no de gusto. El lazo humano de corrección —ver, decidir, moverse— dura unos 240 ms, y sobre eso Swink fija los bordes del control en tiempo real:

```txt
menos de 100 ms     se percibe instantaneo
100 a 240 ms        se percibe pesado, aunque el jugador no sepa nombrar por que
mas de 240 ms       deja de sentirse control: se siente dar una orden y esperar
```

Swink marca dónde deja de existir el control. Un jugador de acción lo juzga antes: entre 60 y 100 ms ya lo siente pesado y, sin saberlo, se culpa a sí mismo; arriba de 100 ms culpa al juego. Por eso, en acción, el número es el de `10_Input_y_respuesta` y no el borde de la percepción.

**Acusar no es lo mismo que confirmar.** Al apretar, la acción empieza —el personaje despega, el arma retrocede, suena el click—: eso es el acuse, es obligatorio y va en los dos primeros cuadros. El impacto, la muerte, la recogida se confirman cuando pasan, no al apretar. Un efecto de impacto en el momento del pulsado le enseña al jugador que apretar alcanza.

---

## Especificación en Unity

```txt
input        Input System leyendo acciones en Update; el primer cambio visible en el mismo
             cuadro o el siguiente. A 60 fps un cuadro son 16.7 ms: la cadena de 65 ms
             son unos cuatro cuadros, y la cola de GPU y el VSync ya se comen
             entre uno y tres
animacion    las transiciones a una accion del jugador sin Has Exit Time y con duracion
             de transicion minima. La anticipacion de una accion propia, uno o dos cuadros
             o ninguno: el peso va despues del input, no antes
audio        el clip arranca sin silencio al principio y con ataque menor a 20 ms;
             la fuente ya existe, no se instancia al apretar. DSP Buffer Size en Best
             latency: el buffer de audio suma latencia por fuera del cuadro
efecto       dentro de los ~100 ms del evento que confirma: llegando despues, se lee
             como otro evento
```

---

## Quién lo aplica

```txt
Game Design    declara cual es el primer feedback de cada accion del jugador
Arte           acorta o muda la anticipacion de las acciones propias
Programacion   lee el input y dispara el primer cambio sin esperar el paso fijo
Calidad        mide la latencia con camara, no la supone
```

---

## Cómo se juzga

```txt
se mide     el acuse, en el motor: 2 cuadros desde el cuadro en que se lee el input
            (registro de Time.frameCount). La cadena, con camara: pantalla y mano a
            240 fps, cuadros contados (4.17 ms cada uno), mediana de tres tomas, contra
            el tope del genero en 10_Input_y_respuesta. El acuse sonoro se mide con camara
se juzga    si el primer cambio se lee como respuesta a esa accion y no a otra
```

---

## Errores comunes

```txt
Copiar la preparacion de una animacion de cine en el salto del jugador.
Leer el pulsado solo en FixedUpdate.
Una transicion de Animator que espera a que termine la animacion anterior.
Un sonido con silencio al principio del archivo.
El efecto de impacto disparado al apretar, y no al impactar.
Medir la latencia "a ojo" en el Editor.
```

---

## Fuentes

- `10_Input_y_respuesta` (Fundamentos) — la cadena de latencia en siete tramos y cómo se mide.
- `02_Game_feel` (Fundamentos) — los umbrales de percepción y confirmar el resultado, no el input.
- `05_Game_Feel` y `70_Measuring_Game_Feel_Acceleration` (Fuentes) — los umbrales de Swink.
- `02 - Anticipacion`, en `Principios de animacion` (Core) — la anticipación en la acción del jugador.
