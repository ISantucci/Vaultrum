## Definición

**El feel se prueba en gris y se cierra jugando**: el feel se valida antes del arte, con formas simples, y moverse tiene que gustar aun en un cuarto vacío. Y no se da por cerrado porque compila: se cierra cuando una persona lo jugó y lo miró, o se declara **no verificado**.

---

## Idea central

Swink lo llama **respuesta atractiva**: el movimiento tiene que ser lindo por sí solo, sin contexto ni objetivo, en un espacio vacío. Si no gusta con cubos, el arte no lo va a arreglar; lo va a tapar.

Y el feel es la parte de un juego que **menos se puede verificar leyendo**. El código puede compilar, los eventos pueden emitirse y los efectos pueden estar todos declarados, y nadie haber visto uno solo. En un proyecto real pasó exactamente eso: una entrega declaró veinte sonidos y una decena de efectos visuales compilados, y ninguno escuchado ni visto, y el feel quedó como verificación pendiente sin que nada frenara la entrega.

Cinco pruebas, todas jugando:

```txt
sin audio        lo que se vuelve ilegible estaba sostenido solo por el sonido: es una
                 falla de accesibilidad
sin capa 3       si se vuelve incontrolable, el problema estaba en la simulacion y el
                 juice lo tapaba
las tres         despues de un minuto: ¿que pasa? ¿que podes hacer? ¿como vas?
preguntas
video a 1/4      los efectos que se pisan solo se ven aca
eventos/minuto   el insumo de la prueba de la repeticion
```

---

## Especificación en Unity

```txt
cuarto gris     una escena de prueba con el avatar, piso, paredes y obstaculos en
                primitivas, sin arte ni efectos: ahi se afina la capa 2
interruptores   capa 3 y audio apagables en build de desarrollo, desde un menu de debug o
                un ScriptableObject de configuracion
grabacion       para un playtest, captura externa: el Unity Recorder corre solo en el
                Editor y fija el framerate, asi que la partida no va en tiempo real.
                El Recorder, solo para recorridos guionados
evidencia       el QA cita la sesion jugada: quien, en que build, que vio. Si el canal de
                ejecucion no tiene Editor ni build corriendo, el feel se declara
                NO VERIFICADO en el VE, con esas palabras
```

---

## Quién lo aplica

```txt
Produccion     el plan pone el cuarto gris antes del arte, y el VE no da el feel por
               cerrado sin una sesion jugada
Game Design    escribe en el GDS como se valida el feel
Programacion   arma el cuarto gris y los interruptores
Calidad        corre las cinco pruebas y las cita
el owner       juega la sesion que la IA no puede jugar
```

---

## Cómo se juzga

```txt
se mide     las cinco pruebas corridas y citadas en el QA, con build y fecha
se juzga    si moverse gusta. Eso es juicio de una persona jugando, y se declara como juicio
```

---

## Errores comunes

```txt
Arte antes que feel.
"Compila" como cierre del feel.
Un QA que verifica el feel leyendo el codigo.
Validar el feel con un video que ninguna persona jugo.
Un VE que no dice que el feel quedo sin verificar.
```

---

## Fuentes

- `02_Game_feel` (Fundamentos) — cómo se mide en playtest.
- `05_Game_Feel` (Fuentes) — respuesta atractiva.
- `13_Playtesting_y_validacion` (Fundamentos) — el protocolo de playtest.
- `05_Fundamentos_de_experiencia_ludica` (Fundamentos) — Pilar 3: el feel validado con el prototipo gris.
- `Verificacion parcial declarada` y `Alcance del instrumento` (Core) — lo que no se verificó se declara, y la forma de terminado no es evidencia de terminado.
