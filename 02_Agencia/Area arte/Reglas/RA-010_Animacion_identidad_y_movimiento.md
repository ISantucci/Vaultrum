# RA-010 — Animacion: identidad y movimiento son dos criterios

**Insumo:** el trabajo de animacion de Miles con Codex (caminata, salto, saludo, pulsar un boton, tutorial WASD) y el `Manual del animador de Vaultrum` que salio de esas correcciones, integrado el 2026-09-25. Las situaciones de abajo las pidio o las corrigio el owner en sesion; los ejemplos numericos son puntos de partida, no resultados medidos en Miles.
**Estado:** Vigente.

> **Una animacion tiene que conservar al personaje, comunicar la accion y funcionar bajo control del jugador.** Una imagen atractiva no prueba que un ciclo este bien, ni que el recurso este listo para el motor.

## Lo que paso, y la regla que dejo

| Situacion en Miles | Lo que enseno |
|---|---|
| un ciclo de caminata correcto estilizo de mas al personaje | movimiento e identidad son criterios independientes |
| el personaje tenia que ser bajito y rellenito, y el 3D salio demasiado obeso | los adjetivos solos dejan margen de mas |
| el saludo tenia que ser con UNA mano | se fija que miembro hace la accion, y que hace el otro |
| se pidio un salto con brazos abiertos y salio un golpe | saltar y atacar comparten despegue y son acciones distintas |
| pulsar un boton necesitaba la mano abierta | el contacto necesita forma de mano y destino claros |
| el texto del tutorial se genero con signos de apertura | el texto es contenido exacto, no una decision del generador |

## Regla 1 — La identidad se fija antes de animar

Se elige **un** archivo como referencia maestra y se registra su version. No se mezclan versiones automaticamente: el owner puede aprobar el movimiento de una y las proporciones de otra.

Se mide sobre la referencia, en vez de inventar medidas: alto total, ancho de cabeza, ancho de torso, largo de piernas y linea de suelo. Si el estilo admite deformacion expresiva, se anota cuanto puede variar cada parte y en que momentos.

Para Miles, como intencion visual: cuerpo bajito y compacto, cabeza grande y piernas cortas —ni figura esbelta ni abdomen exagerado—; rulos oscuros definidos, rostro reconocible, barba corta; buzo negro, pantalon oscuro, zapatillas negras con blanco; misma paleta, grosor de contorno, escala y orientacion en todos los cuadros.

## Regla 2 — Una correccion es local

```txt
"mas corta la zancada"     conservar cara, ropa, camara y proporciones
"menos ancho el torso"     conservar apoyos y tiempos ya aprobados
```

Una familia de problemas por iteracion: primero mecanica, despues proporciones, despues detalle. Si se corrigen varias cosas juntas, se enumeran para poder verificar cada una. Es la misma regla que el Modo Encargo ya tiene para las imagenes —*"mantene todo igual y cambia solo X"*—, aplicada a una secuencia: pedir tres cosas a la vez es rehacer la animacion, y el personaje deriva.

## Regla 3 — Los adjetivos se traducen a condiciones visibles

"Fluido", "chiquito", "con fuerza" no identifican ninguna causa. El feedback tiene cuatro partes:

```txt
donde + que ocurre + que deberia ocurrir + que conservar
```

| Ambiguo | Accionable |
|---|---|
| no queda fluido | en 08 -> 01 la cadera salta hacia arriba; corregi esa transicion conservando los contactos |
| camina raro | en 05 vuelve a adelantarse I; deberia contactar D |
| parece correr | acorta la zancada y elimina el vuelo; conserva la flexion visible de rodillas |
| cambiaste al personaje | la cabeza es mas chica respecto del torso que en la referencia; restaura esa proporcion |
| se hace invisible | en la reproduccion desaparece el cuadro 06; revisa alfa, recorte e importacion antes de redibujar |
| el saludo esta mal | solo saluda la mano derecha anatomica; el brazo izquierdo queda relajado |
| sobra blanco | acerca el texto a WASD y reduce el ancho sin recortar la palabra mas larga |

## Regla 4 — Los doce principios, con su control de juego

Nomenclatura segun la introduccion de Adobe a los doce principios. Los usos y los controles son de este registro, no citas de esa fuente.

```txt
compresion y estiramiento   aterrizaje, rebote, UI. CONTROL: la cabeza no cambia de tamano
                            para siempre; deformar el dibujo no obliga a deformar el collider
anticipacion                aviso de ataque enemigo, carga, salto. CONTROL: una preparacion
                            larga en el salto del JUGADOR se siente como retraso
puesta en escena            la pose se entiende en silueta, a la camara y escala reales.
                            En UI, una sola tecla reclama atencion por vez
pose a pose / directa       locomocion y contactos: pose a pose. Primero contacto I y D
                            aprobados; ocho dibujos sueltos no aseguran continuidad
continuacion y superposicion   pelo, mangas, equipo. CONTROL: lo accesorio no oculta que
                            el jugador ya puede volver a actuar
entradas y salidas suaves   CONTROL: no suavizar todo; un impacto puede llegar abrupto, y
                            suavizar el dibujo no cambia la fisica del controlador
arcos                       CONTROL: un arco lindo no justifica atravesar el suelo o el boton
accion secundaria           mirar el boton antes de tocarlo. CONTROL: no se vuelve protagonista
timing                      CONTROL: cuadros de animacion no son cuadros de simulacion.
                            Ocho imagenes pueden durar 0.8 s en un juego a 60 FPS
exageracion                 CONTROL: exagerar la rodilla no obliga a alargar la zancada.
                            Se exagera lo que comunica, sin cambiar la categoria de la accion
dibujo solido               seguir articulaciones y masas aunque una pierna quede oculta.
                            No reasignar la identidad de las piernas al cruzarse
atractivo                   CONTROL: no es embellecer ni adelgazar. Sigue siendo el mismo personaje
```

## Verificacion

Lo mecanico lo mide `animacion.py` sobre los cuadros que vuelven: mismo lienzo, alto de la silueta estable contra la mediana (**escala**) y ningun cuadro con una familia de colores que el primero no tiene (**paleta**). Una pose que cambia la silueta a proposito —el brazo arriba del saludo, el apice del salto— sube la tolerancia con `--tol-escala`, y el `ART` lo declara.

Lo que no es mecanico se juzga **contra la referencia maestra**, con los cuadros numerados al lado y a la misma escala: que el personaje sea el mismo, que la accion se lea en silueta, que el miembro que actua sea el pedido. Se dice como juicio, no como medicion.

## Fuentes

- [Adobe: 12 Principles of Animation](https://www.adobe.com/creativecloud/animation/discover/principles-of-animation.html) — nomenclatura de los principios.
- Historial de trabajo de Miles: pedidos y correcciones del owner sobre caminata, proporciones, salto, saludo, interaccion, transparencia y tutorial WASD.
