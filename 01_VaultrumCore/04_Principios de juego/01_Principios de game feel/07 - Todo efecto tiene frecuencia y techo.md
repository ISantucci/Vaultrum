## Definición

**Todo efecto tiene frecuencia y techo**: cada efecto se diseña multiplicado por las veces que pasa en un minuto de juego real. Todo efecto acumulable tiene un techo que no se puede pasar. Lo que se repite varía sin volverse azar. Y su costo se mide contra el presupuesto de cuadro.

---

## Idea central

El juice se prueba de a un evento y se sufre en serie. Un efecto precioso puede ser un defecto por pura repetición:

```txt
hitstop de 6 cuadros  x  40 veces por minuto  =  240 cuadros  =  4 s de juego congelado
                                                                 por minuto, a 60 fps
```

Lo mismo pasa con la acumulación: diez enemigos que mueren juntos disparan diez sacudidas sumadas, y en la oleada grande el jugador no sabe qué lo mató.

La repetición también cansa sin sumarse: diez veces el mismo sonido se vuelven uno solo. La **novedad** de Swink es esto —el mismo input no da exactamente lo mismo—, con un límite: la variación queda por debajo de lo que se lee como azar.

---

## Especificación en Unity

```txt
frecuencia    el GDS declara cuantas veces por minuto pasa cada efecto, contado en una
              partida real o simulada, y cuanto tiempo congela el que congela
hitstop       0-2 cuadros en eventos frecuentes, 4-8 en raros. Time.timeScale frena todo lo
              que corre en tiempo escalado (fisica, Animator, particulas), pero no el audio
              ni lo que usa tiempo sin escalar: se declara que tiene que frenar y que no.
              El hitstop se cuenta en tiempo sin escalar (unscaledDeltaTime o
              WaitForSecondsRealtime), o no termina. Durante el congelado el input se sigue
              leyendo y entra al buffer: el Input System en Dynamic Update, porque en Fixed
              Update, con timeScale en 0, no entra nada
techos        screenshake por trauma con clamp a 1. Cinemachine Impulse no trae ni trauma
              ni techo: los impulsos activos se suman, asi que el limite se implementa
              aparte, o se usa un trauma propio sobre el Noise. Para particulas y efectos,
              un contador explicito de instancias activas o un sistema compartido con
              Emit(): Max Particles limita cada sistema por separado, y el pool no limita
              cuantos hay activos. Para sonido, un contador de voces por evento
variacion     pitch aleatorio de +-5 a 15% en sonidos repetidos, por voz: una AudioSource
              por voz desde un pool, porque cambiar el pitch de una fuente compartida
              cambia tambien lo que ya esta sonando. Y dos a cuatro variantes de clip en
              los mas frecuentes
costo         efectos y particulas desde un pool (ObjectPool<T>), nunca Instantiate por
              evento; medido en el Profiler con el peor caso en pantalla
```

---

## Quién lo aplica

```txt
Game Design    declara frecuencia y techo de cada efecto; el Balanceador cuenta los
               eventos por minuto
Programacion   implementa los techos y el pool, y mide el costo
Arte           entrega efectos con su cantidad maxima de particulas declarada
Calidad        provoca el peor caso —la oleada grande, diez eventos juntos— y lo mide en el
               Profiler y en video a 1/4
```

---

## Cómo se juzga

```txt
se mide     eventos por minuto por duracion de congelado; el techo efectivo provocando
            diez eventos juntos; el framerate en el peor caso contra el objetivo declarado
se juzga    si la variacion se oye todavia como el mismo evento
```

---

## Errores comunes

```txt
Probar el efecto una vez y aprobarlo.
Sacudidas que se suman sin techo.
Instantiate y Destroy por cada impacto.
Un hitstop con timeScale que congela tambien la animacion del menu de pausa.
El mismo clip, sin variacion, en el sonido que mas se repite.
```

---

## Fuentes

- `02_Game_feel` (Fundamentos) — la prueba de la repetición, el baseline de hitstop y de pitch, el juice que se come el presupuesto.
- `11_Camara_y_encuadre` (Fundamentos) — el modelo de trauma, su techo y su decay.
- `61_Juicing_Your_Cameras_With_Math` (Documentos) — la sacudida con decaimiento y presupuesto.
- `Frame Budget` y `Object Pool` (Core) — el presupuesto de cuadro y el pool.
