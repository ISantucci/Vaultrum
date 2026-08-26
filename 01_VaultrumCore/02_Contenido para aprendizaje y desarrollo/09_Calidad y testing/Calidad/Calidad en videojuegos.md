## Que es

Verificar un juego no es verificar software con graficos. Hay diferencias estructurales que rompen los supuestos del testing clasico.

```txt
estado continuo    no hay pantallas discretas: hay un mundo que evoluciona cuadro a cuadro
tiempo real        el mismo caso da distinto si se hace medio segundo antes
entrada analogica  no es "click": es direccion, intensidad, duracion y combinacion
fisica             el resultado depende de posiciones y velocidades imposibles de enumerar
no determinismo    aleatoriedad, concurrencia, tiempos de carga, hardware
contenido masivo   cientos de items, niveles, dialogos, cada uno con su propio defecto posible
jugador adversario nadie hace lo que el diseno esperaba, y algunos lo rompen a proposito
```

La consecuencia practica: **el caso escrito paso a paso cubre menos superficie que en software de gestion**, y la exploracion con criterio pesa mucho mas.

---

## Las dimensiones a verificar

Cada una falla distinto y ninguna se cubre con las otras.

| Dimension | Que se verifica | Falla tipica |
|---|---|---|
| Jugabilidad | reglas, estados, combinaciones, interrupciones | una habilidad usada durante una transicion deja al personaje sin control |
| Progresion | avance, desbloqueos, objetivos, no retorno | un objetivo se completa dos veces y la mision queda trabada |
| Guardado | guardar, cargar, autoguardado, versiones, corrupcion | una partida vieja no abre despues de una actualizacion |
| Entrada | teclado, mando, raton, reasignacion, desconexion | desconectar el mando en pausa deja el menu sin foco |
| Interfaz | navegacion, foco, escalado, estados vacios y de error | una resolucion 16:10 corta el boton de confirmar |
| Rendimiento | cuadros por segundo, memoria, carga, picos, estabilidad | el pico aparece recien a los 40 minutos de sesion |
| Audio | mezcla, disparadores, silencios, corte al pausar | el sonido de un enemigo muerto sigue sonando |
| Visual | materiales, iluminacion, nivel de detalle, artefactos | una malla desaparece a cierta distancia de camara |
| Nivel | colisiones, atascos, aparicion, disparadores, atravesado | se puede salir del escenario saltando en una esquina |
| Plataforma | requisitos de la tienda o consola, permisos, suspension | suspender la consola durante el guardado corrompe la partida |
| Accesibilidad | tamano de texto, contraste, remapeo, subtitulos, opciones | el estado critico se comunica solo por color |
| Idioma | textos, cortes, caracteres, formato de numeros y fechas | el aleman rompe el ancho de todos los botones |
| Red | latencia, perdida, reconexion, desincronizacion | dos clientes ven resultados distintos del mismo golpe |
| Economia | precios, monedas, limites, explotaciones | un ciclo de compra y venta genera dinero infinito |

Ninguna entrega necesita las catorce. Lo que si se necesita es **decidir cuales aplican y decirlo**, porque una dimension que nadie nombro es una dimension que nadie probo.

---

## Dos confusiones caras

### Playtesting no es control de calidad

```txt
QA           el sistema hace lo que dice hacer?        se responde con una prueba
playtesting  a esta persona le sirve, entiende, disfruta?   se responde observando personas
```

Quien verifica puede detectar **friccion observable** —el jugador no encuentra la salida, repite el mismo error, no ve el aviso— y es informacion valiosa. Pero comprension, preferencia, diversion y percepcion se miden con metodo de investigacion de usuario, con personas que no construyeron el juego.

Usar uno en lugar del otro sale caro en las dos direcciones: pedirle diversion a un pase de pruebas, o dar por probado un sistema porque a tres personas les gusto.

### Que funcione en el editor no dice nada de la build

Es la trampa mas repetida del desarrollo con motor. La build de destino difiere en casi todo lo que puede fallar:

```txt
rendimiento real y presupuesto de memoria
rutas de archivos y permisos de escritura
serializacion y datos guardados
recorte de codigo y recursos no incluidos
API de graficos y capacidades del dispositivo
servicios de plataforma
tiempos de carga sobre almacenamiento real
```

Verificar en el editor es una **verificacion parcial**, valida y declarable como tal. No habilita a decir que funciona.

---

## Guardado y progresion: la matriz minima

Es la dimension que produce el dano irreversible, porque el jugador no puede volver atras.

```txt
partida nueva
guardar y cargar en el mismo momento
autoguardado
sobrescribir
guardar durante y despues de un evento critico
varias ranuras
partida corrupta o faltante: que hace el juego
partida de la version anterior en la version nueva
actualizacion o contenido descargable encima de una partida existente
conflicto entre nube y local, si existe
cambio de usuario o cierre de sesion, si existe
almacenamiento lleno o fallo de escritura, si se puede simular
```

Regla: **cualquier cambio en la estructura de datos guardados obliga a probar la migracion desde la version anterior.** Sin eso, la actualizacion borra progresos.

---

## El modelo de certificacion como forma mental

Las plataformas grandes verifican en un orden que conviene copiar aunque no se publique en ninguna:

```txt
1. build candidata limpia e identificable
2. validacion del paquete
3. verificacion de build (humo): vale la pena probar esto?
4. solo si paso: pase completo
5. verificacion de requisitos aplicables
6. decision, con la informacion necesaria para poder repetirla
```

Lo valioso no es el tramite: es el orden. **Primero se comprueba que la build es testeable, despues se gastan horas en probarla.** Un pase profundo sobre una build rota consume un dia y no produce informacion util.

Y el corolario que se paga caro cuando se ignora: **nunca se valida una entrega contra una version que puede cambiar.** Si la build se puede recompilar y ser otra, el resultado de la prueba no significa nada. Version congelada, o no hay verificacion.

---

## Regla final

```txt
Un juego no falla como falla el software: falla en el estado que nadie enumero,
en el momento que nadie cronometro y en la maquina que nadie tenia.

Por eso el criterio pesa mas que la lista de casos.
```
