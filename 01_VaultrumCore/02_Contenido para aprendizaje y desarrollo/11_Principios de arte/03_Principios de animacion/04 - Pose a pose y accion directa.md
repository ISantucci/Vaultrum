## Definición

Dos maneras de construir un movimiento:

```txt
accion directa   se anima cuadro tras cuadro, desde el principio hasta el final
pose a pose      primero las poses clave, despues los pasajes, despues los intermedios
```

Y el **blocking**, que la cátedra del owner define como *la forma más básica de animar*: la primera pasada de un pose a pose, con las claves solas y la interpolación **constante** —cada pose se sostiene hasta la siguiente—, para aprobar poses y tiempos antes de suavizar nada.

```txt
clave        un momento relevante de la accion
pasaje       la pose que decide como se va de una clave a otra (breakdown)
intermedio   lo demas (in-between)
```

---

## Idea central

```txt
directa      espontanea y fluida, y deriva: el personaje cambia de tamano, de lugar,
             de proporcion, sin que nadie lo decida
pose a pose  controlada: lo importante se decide y se aprueba antes de que exista
             lo demas
```

**En 3D y en UI la computadora hace los intermedios**: el pose a pose es el método por defecto, y la acción directa vuelve como simulación (pelo, tela, partículas).

---

## Especificación para videojuegos

```txt
locomocion y contactos    pose a pose. Primero los contactos I y D, aprobados; despues
                          lo demas (RA-011). Ocho dibujos sueltos no aseguran continuidad
efectos y lo caotico      fuego, humo, agua: directa, o simulacion
el orden de aprobacion    blocking en constante -> se aprueban poses y tiempos ->
                          recien ahi se suaviza. Suavizar antes esconde el timing
```

**Cuántas poses clave lleva cada acción.** Es la pregunta que el área contestaba de memoria. Punto de partida, no ley: lo que decide es que la acción se lea.

```txt
caminata     contacto, descenso, paso, elevacion — por pierna: 8 en el ciclo.
             Los dos contactos se aprueban primero (RA-011)
carrera      contacto, descenso, impulso, VUELO — por pierna. Sin vuelo no es carrera:
             es una caminata rapida
idle         base, respiracion y regreso: 2 o 3. Poco movimiento, ciclo largo,
             interrumpible en cualquier cuadro
salto        preparacion, despegue, ascenso, apice, caida, aterrizaje, recuperacion.
             En juego, ascenso y caida son clips separados: un techo corta el ascenso
ataque       preparacion, extension, impacto, recuperacion. El impacto es un evento
dano         impacto, reaccion, recuperacion
pulsar       aproximar, palma abierta, contacto, retirada. El evento va en el contacto
```

Cuántos **cuadros** dura cada una es `09 - Timing`. Cuántas **claves se guardan** en el archivo, y qué cuesta, es `Claves por tipo de animacion` en la rama Arte de Optimización: son tres preguntas distintas.

**Menos claves, más fácil de manipular** (`68_Apuntes_de_catedra_Animacion_2D_3D`): una animación con una clave en cada cuadro no se puede editar. El ritmo se ajusta moviendo las claves en el tiempo y el reparto con las curvas (`Curvas e interpolacion`).

---

## Cómo se juzga

```txt
se mide     en un ciclo in-place: que la linea de apoyo no derive, que el ultimo cuadro
            no repita al primero y que el enlace no salte (animacion.py --in-place)
se juzga    que pierna apoya en cada contacto, siguiendo un pie y despues el otro sobre la
            plancha numerada (RA-011). Ningun instrumento de pixeles lo dice
```

---

## Errores comunes

```txt
Animar en directa una caminata: sin contactos aprobados, la continuidad deriva. La pierna
repetida de Miles vino de un generador que no siguio los contactos: el mismo defecto, por
otra via.
Suavizar antes de aprobar el blocking.
Exportar una copia de la primera pose como ultimo cuadro: en bucle es una pausa.
Animar un salto como un clip fijo: no responde a un techo ni a una caida larga.
Cargar una clave por cuadro "para tener control": se pierde el control.
```

---

## Fuentes

- `59_The_Illusion_of_Life` — los dos métodos.
- `60_The_Animators_Survival_Kit` — claves, pasajes e intermedios; las poses de la caminata.
- `61_Game_Anim` — clips de juego partidos para responder al estado.
- `68_Apuntes_de_catedra_Animacion_2D_3D` — blocking, clave e intermedio; menos claves.
- `RA-011_Locomocion_por_apoyos` — los contactos y las poses por acción.
