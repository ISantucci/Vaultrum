# RA-012 — Secuencia, alfa y entrega: una vista previa no es un recurso listo

**Insumo:** las animaciones y el tutorial WASD de Miles con Codex. El personaje tuvo transparencias y desapariciones; se pidio un mini GIF para revisar; el tutorial tenia demasiado blanco y se iba a usar sobre violeta; se pidieron cuatro estados y uno neutro. Integrado desde el `Manual del animador de Vaultrum` el 2026-09-25.
**Estado:** Vigente.

## Lo que paso

```txt
hubo transparencias y desapariciones     la causa puede estar en el dibujo, el alfa, el recorte,
                                          un cuadro vacio, el indice de celda o la importacion
se pidio un mini GIF                      la revision necesita movimiento, no solo una plancha
el tutorial se usaria sobre violeta       el contexto visual es parte del encargo
cuatro estados y uno sin texto            una animacion tambien es una coleccion de estados
```

## Regla 1 — Una hoja generada es una propuesta, no una secuencia

Una hoja de sprites generada por IA no garantiza identidad entre cuadros, grilla exacta, alfa correcto ni anatomia consistente. Para continuidad estricta se trabaja sobre dibujos controlados o un rig, y se corrigen cuadros puntuales.

## Regla 2 — El lienzo es uno, y el pivot no se mueve

```txt
dimension de celda y pivot constantes      NO se recentra cada pose por su caja visible
margen para manos, pies, pelo y efectos    en la pose mas amplia, no en la media
```

## Regla 3 — Transparencia real, revisada sobre el fondo real

```txt
un damero dibujado NO es transparencia
probar sobre fondo claro, oscuro y el fondo del juego   buscar huecos, halos y restos opacos
no borrar a ciegas un color compartido                   fondo, ropa, ojos y piel lo comparten
pixel art de pixel duro     escalado entero y filtrado apropiado
ilustracion suavizada       conservar el borde previsto
                            no mezclar las dos politicas sin intencion
atlas                       padding y extrusion acordados con el motor
```

## Regla 4 — Una desaparicion se diagnostica en orden, no se redibuja

```txt
1  el PNG afectado       tiene contenido? tiene alfa? esta recortado?
2  la secuencia exportada   esta el cuadro, en su orden, con su indice?
3  la reproduccion en el motor   visibilidad animada, logica de estados
```

Redibujar antes de mirar el alfa es arreglar el lugar equivocado.

## Regla 5 — El GIF es revision, no fuente

Se conserva una secuencia fuente **sin perdida**. El GIF limita color y transparencia: sirve para mirar el movimiento en bucle, y **se construye desde los mismos PNG** de la entrega. Nunca al reves.

## Regla 6 — Cuatro niveles de validacion, y se dice cual se alcanzo

```txt
propuesta visual        se ve bien en la vista previa
secuencia validada      los cuadros pasan animacion.py y la revision de apoyos
exportacion validada    el paquete esta completo y el manifiesto dice lo que hay
integracion comprobada  se probo dentro del motor: velocidad, eventos, interrupciones
```

**Nunca se afirma "listo para juego" si solo se comprobo la vista previa.**

## Regla 7 — El paquete de entrega

```txt
personaje/accion/v003/
  frames/accion_01.png ... accion_08.png
  accion_sheet.png
  accion_preview.gif          sale de frames/, no al reves
  accion_contactos.png        la plancha numerada, con los apoyos marcados
  accion.json                 el manifiesto
  README.md
```

El manifiesto declara: version de la referencia, orientacion, tamano de celda, pivot y su convencion de coordenadas, orden de cuadros, duracion por cuadro, loop, eventos, estados de entrada y salida, y si hay root motion o desplazamiento dibujado.

Para 3D se suman rig, pesos, acciones separadas, escala, ejes y exportacion. Un modelo de partes editables sirve para disenar y no prueba buena deformacion: **el rig se valida con poses antes de producir los clips**.

## Regla 8 — Una animacion de UI es un conjunto de estados

El caso WASD dejo la especificacion completa: burbuja estilo comic, WASD a la izquierda y texto a la derecha, 490 x 222 px con exterior transparente, borde violeta oscuro, superficie lavanda, tecla activa turquesa oscuro elegido contra el fondo violeta real; recorrido W -> A -> S -> D, una tecla activa por estado; texto literal *Arriba!, Izquierda!, Abajo!, Derecha!* con signo solo al final, por pedido del owner; cuatro PNG activos y uno neutro sin texto ni tecla; GIF de revision de 2 s en bucle, 500 ms por tecla.

```txt
el GIF muestra una demostracion      NO detecta teclas: si el tutorial reacciona al
                                     jugador, se usan los estados con la logica del juego
traducciones                         reservar el lugar de la palabra mas larga; una
                                     fuente comun a todos los estados, no un tamano por palabra
composicion                          se revisa al tamano real de uso, no en la plancha
```

## Verificacion

`animacion.py <carpeta> --gif <preview.gif>` mide lo mecanico de la entrega:

```txt
cuadros   existen, se leen y comparten lienzo
alfa      canal alfa real, transparencia presente, y no un damero dibujado
vacio     ningun cuadro sin pixeles opacos
recorte   ninguna silueta tocando el borde del lienzo
gif       los mismos cuadros que la carpeta, y la duracion del ciclo
```

Eso alcanza para declarar **secuencia validada** en lo mecanico. **Exportacion validada** exige ademas el manifiesto completo, y **integracion comprobada** exige el motor: velocidad y apoyos, eventos en el contacto, inicio, interrupcion, cambio de direccion y salida, y un salto que responda a suelo, caida y techo reales.

## Fuentes

- [Godot: 2D sprite animation](https://docs.godotengine.org/en/stable/tutorials/2d/2d_sprite_animation.html) — reproduccion de cuadros sueltos y de regiones de una hoja.
- Historial de trabajo de Miles: transparencias, mini GIF, tutorial WASD y sus estados.
