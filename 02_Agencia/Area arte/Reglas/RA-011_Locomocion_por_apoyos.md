# RA-011 — Locomocion por apoyos: cada pierna se sigue por separado

**Insumo:** la caminata de Miles con Codex. Dos correcciones del owner: la caminata **repetia la misma pierna**, y otra version **parecia correr**. Integrado desde el `Manual del animador de Vaultrum` el 2026-09-25.
**Estado:** Vigente.

## Lo que paso

```txt
dos movimientos parecidos no son dos apoyos alternados   -> la misma pierna, dos veces
una caminata no se define por la velocidad                -> zancada larga + vuelo = carrera
```

Las dos se veian bien en la vista previa. Las dos se ven mal apenas se sigue un pie cuadro por cuadro.

## Regla 1 — Los miembros se nombran por anatomia

**I = izquierda del personaje. D = derecha del personaje.** Cerca o lejos de camara son descripciones adicionales, no sustitutos. Durante la revision se pueden usar marcas de color temporales que no van en la entrega.

## Regla 2 — El ciclo se aprueba por contactos, y despues se intercala

Esquema de trabajo de ocho poses para una caminata convencional —no es obligacion de usar ocho cuadros ni tiempos iguales—:

```txt
01  contacto I     I llega adelante; D termina atras
02  descenso I     se acepta el peso sobre I; la pelvis baja un poco
03  paso D         D cruza junto al apoyo I; rodilla flexionada
04  elevacion I    I impulsa; D avanza hacia el proximo contacto
05  contacto D     D llega adelante; I termina atras
06  descenso D     se acepta el peso sobre D
07  paso I         I cruza junto al apoyo D
08  elevacion D    D impulsa; I prepara el contacto 01
```

En una caminata siempre hay algun apoyo, y suele haber doble apoyo en los cambios. Una carrera incorpora **vuelo**, y ademas cambia postura, impulso y energia: no es la caminata reproducida mas rapido.

## Regla 3 — La revision sigue un pie, despues el otro

```txt
1  seguir el pie I por todos los cuadros; despues el D
2  cada uno pasa por avance, contacto, apoyo y salida
3  la rodilla se lee sin alargar el paso de mas
4  oposicion de brazos y piernas, si el estilo la pide
5  08 -> 01: continuidad de posicion y de direccion
6  NO exportar una copia de 01 como ultimo cuadro: en bucle es una pausa
7  probar con el desplazamiento real del juego, para ver si patina
```

## Regla 4 — In-place o root motion, y quien mueve al personaje

**In-place**: el ciclo no se desplaza; lo mueve el juego. En un ciclo in-place el pie apoyado **retrocede respecto del cuerpo**, y eso no es patinaje: tiene que quedar quieto respecto del mundo al sumarle el avance del personaje.

```txt
primera referencia   velocidad ~= distancia recorrida por ciclo / duracion del ciclo
despues              se ajusta mirando los contactos, no la formula
```

**Root motion**: el desplazamiento de la raiz de la animacion conduce al personaje. Elegirlo es coordinar animacion y movimiento; no se suma por accidente al desplazamiento del controlador. Ver la documentacion de Epic sobre root motion.

## Regla 5 — Cada accion trae sus poses y su control

```txt
idle             base · respiracion · regreso       no deriva, no cambia de tamano, se interrumpe
saludo 1 mano    levantar · saludo · bajar          el otro brazo NO repite el gesto
correr           apoyos alternos · impulso · vuelo  no es una caminata acelerada
                 · recepcion
salto brazos     preparacion · despegue · ascenso   brazos legibles; aterriza con el contacto real
abiertos         · apice · caida · aterrizaje
golpe arriba     preparacion · extension · impacto  puno sobre la cabeza; alcance compatible
                 · recuperacion                     con la hitbox
agacharse        entrada · pose sostenida · salida  pies anclados; cambio de collider acordado
pulsar boton     aproximar · palma abierta          la mano llega sin atravesar; el EVENTO
                 · contacto · retirada              ocurre en el contacto
dano             impacto · reaccion · recuperacion  recuperacion visual != fin de invulnerabilidad
```

**Saltos de duracion variable:** ascenso, caida y aterrizaje separados, no un clip fijo. Un techo puede cortar el ascenso antes del apice, y el animador tiene que saberlo.

**Combate:** preparacion, actividad y recuperacion se acuerdan con Game Design, igual que cancelaciones y prioridades. El momento de dano **se documenta como evento**; no se deduce de la pose mas extendida.

## Verificacion

`animacion.py <carpeta> --in-place` mide lo mecanico de un ciclo de caminata o de idle: la **linea de apoyo** no deriva entre cuadros, el **ultimo cuadro no repite al primero**, y el **enlace ultimo -> primero** no salta mas que un paso tipico del ciclo. Una carrera tiene fase aerea y no se mide con `--in-place`.

Que la pierna que apoya en 05 sea la D no lo puede decir ningun instrumento de pixeles. Se verifica a mano siguiendo un pie y despues el otro, sobre la plancha numerada, y se escribe como juicio.

## Fuentes

- [Epic Games: Root Motion](https://dev.epicgames.com/documentation/en-us/unreal-engine/root-motion-in-unreal-engine) — movimiento derivado de la raiz.
- Historial de trabajo de Miles: la caminata que repetia la pierna y la que parecia correr.
