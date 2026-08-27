## Definicion

Son dos estrategias distintas que responden a la misma pregunta: cuando conviene pagar un trabajo que hay que pagar igual.

Carga distribuida:

```txt
mucho trabajo ahora
↓
trabajo repartido en el tiempo
```

Precarga:

```txt
trabajo que hara falta despues
↓
hecho antes, en un momento menos critico
```

Una reparte el costo. La otra lo adelanta. Ninguna lo elimina.

Y esa es la aclaracion central:

```txt
distribuir no elimina trabajo
```

Solo cambia:

```txt
cuando se hace
durante cuanto tiempo
como afecta la experiencia
```

Todo lo demas de esta nota se apoya en eso.

---

## Que problema ayuda a prevenir

Ayuda principalmente con:

```txt
Freeze por carga en runtime
Spikes al aparecer contenido nuevo
Stutters en transiciones
Tirones al abrir interfaces por primera vez
Picos de instanciacion masiva
```

El caso que ataca siempre tiene la misma forma:

```txt
frame normal
→ carga
→ freeze
→ frame normal
```

Y la observacion que habilita la solucion:

```txt
El trabajo era necesario.
El momento no lo era.
```

---

## Como funciona

La carga distribuida corta una operacion grande en partes que caben en el presupuesto del frame.

```txt
Antes:
Frame X → 60 objetos.

Despues:
Frame X   → 10
Frame X+1 → 10
Frame X+2 → 10
...
```

El trabajo total puede seguir siendo el mismo. Lo que baja es el pico.

La precarga adelanta el trabajo a una ventana donde el jugador no esta midiendo la respuesta del juego.

```txt
Ventanas baratas:
carga inicial
menu
transicion entre niveles
pausa
momentos sin presion.
```

El criterio para elegir entre una y otra:

```txt
¿Se sabe de antemano que hara falta?
→ Si → precarga.
→ No → carga distribuida.

¿Se necesita completo de inmediato?
→ Si → precarga.
→ No → carga distribuida.
```

Muchas veces se combinan: se precarga lo previsible y se distribuye lo que aparece durante el juego.

---

## Como aplicarlo en videojuegos

En un Tower Defense el momento critico es el comienzo de la wave.

Precarga de lo previsible:

```txt
Al cargar el mapa
→ se conocen los tipos de enemigo de todas las waves
→ se cargan sus assets
→ ninguna wave paga la primera aparicion.
```

Distribucion de lo masivo:

```txt
Antes:
La wave instancia 300 enemigos en un frame.

Despues:
6 tandas de 50 a lo largo de seis frames.
```

Y el detalle que suele resolver el caso mas molesto:

```txt
Panel de compra de torres
→ construido al cargar el mapa
→ oculto hasta que el jugador lo abre.
```

El escalonamiento no es solo tecnico. Una oleada que entra por tandas se lee mejor que trescientos enemigos apareciendo de golpe.

El HUD de dinero, vida y wave no entra en esto: es liviano y tiene que estar listo desde el primer frame.

---

## Relacion con arquitectura

Las dos estrategias necesitan lo mismo: saber de antemano que va a hacer falta.

```txt
Contenido declarado
→ se puede precargar.

Contenido descubierto en runtime
→ solo se puede distribuir.
```

Lo que ayuda:

```txt
Definiciones de wave con sus tipos de enemigo.
Manifiestos de contenido por nivel.
Un punto unico de carga por contexto.
Spawners que aceptan un ritmo, no una cantidad.
Sistemas que toleran contenido incompleto por unos frames.
```

Ese ultimo punto es el que mas se subestima. Distribuir significa que durante unos frames el mundo esta a medias, y el resto del juego tiene que aguantar eso sin romperse.

Conviene distinguir esta nota de distribucion temporal del trabajo. Las dos reparten trabajo en varios frames, las dos usan el mismo diagrama de tandas y las dos cargan la misma advertencia: distribuir no elimina trabajo. El deslinde esta en que se reparte.

```txt
Precarga y carga distribuida
→ trabajo de carga de contenido: assets, instanciacion, preparacion de escena.

Distribucion temporal del trabajo
→ trabajo recurrente de simulacion: rutas, percepcion, targeting, sensores.
```

Una wave que entra escalonada es carga distribuida. Los mismos enemigos recalculando ruta por turnos, una vez que ya existen, es distribucion temporal.

Se apoya directamente en el ciclo de vida de recursos: precargar sin liberar despues es como no haber controlado nada.

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
Almacenamiento
CPU
Memoria
Main Thread
Frame Budget
```

El intercambio es explicito:

```txt
Precarga
→ menor spike futuro
→ mayor memoria residente anticipada.

Carga distribuida
→ frame estable
→ el contenido tarda mas en estar completo.
```

Y una precision util:

```txt
Distribuir baja el pico.
No baja el total.
El tiempo de CPU sigue ahi, repartido.
```

En almacenamiento lento la precarga rinde mucho mas, porque la espera de lectura no se puede partir en pedazos chicos.

---

## Cuando conviene usarlo

Conviene precargar cuando:

```txt
Se sabe con certeza que hara falta.
Existe una ventana barata para hacerlo.
El contenido se usa poco despues.
Hay memoria disponible.
El spike se midio y molesta.
```

Conviene distribuir cuando:

```txt
Aparecen muchos objetos juntos.
El trabajo se puede cortar en partes.
El sistema tolera contenido incompleto un momento.
El total es aceptable y el pico no.
```

---

## Cuando NO conviene usarlo

No conviene cuando:

```txt
No hay spike medido.
El trabajo ya cabe en el presupuesto del frame.
El contenido se necesita completo de inmediato.
La memoria es el recurso critico.
El contenido es impredecible.
La ventana de precarga tampoco existe.
```

Y hay un abuso que merece nombre propio:

```txt
Precargar todo por las dudas
es el camino directo
a un problema de memoria.
```

Cambiar un freeze de medio segundo por una carga inicial de dos minutos y memoria al limite no es una optimizacion. Es mudar el problema de rama.

---

## Trade-offs

```txt
Precarga
→ menor spike futuro
→ mayor memoria residente anticipada.

Carga distribuida
→ frame estable
→ contenido incompleto por unos frames.

Precarga amplia
→ gameplay sin cortes
→ carga inicial mas larga.

Tandas mas chicas
→ pico mas bajo
→ el contenido tarda mas en aparecer.

Contenido preparado y oculto
→ apertura instantanea
→ memoria ocupada sin uso.
```

Los dos ejes son memoria y tiempo. Nunca se ganan los dos.

---

## Riesgos de aplicarlo mal

Riesgos comunes:

```txt
Precargar todo el juego al iniciar.
Precargar y no liberar nunca.
Cortar en tandas tan chicas que el contenido llega tarde.
Distribuir trabajo que se necesitaba completo.
Romper la logica de wave por aparicion escalonada.
Suponer que distribuir reduce el costo total.
Cambiar un freeze por una carga inicial insoportable.
No medir la memoria despues del cambio.
```

Ejemplo:

```txt
Antes:
Freeze al empezar cada wave.

Decision:
Precargar los enemigos de las cincuenta waves al abrir el mapa.

Resultado:
Sin freeze, con carga inicial larguisima
y memoria al limite en plataformas chicas.
```

Otro caso:

```txt
La wave se instancia en tandas de dos.
El conteo de enemigos vivos se lee antes de terminar.
La wave se da por completada con enemigos en camino.
```

Distribuir mal no solo se ve. Rompe reglas.

---

## Checklist de implementacion

```txt
¿El spike fue medido?
¿Que trabajo cae en ese frame?
¿Se sabe de antemano que contenido hara falta?
¿Existe una ventana barata para adelantarlo?
¿Cuanta memoria agrega la precarga?
¿Lo precargado se libera al salir del contexto?
¿El trabajo se puede cortar en partes?
¿Que tamaño de tanda cabe en el presupuesto?
¿El juego tolera contenido incompleto unos frames?
¿La logica de gameplay resiste la aparicion escalonada?
¿La carga inicial sigue siendo aceptable?
¿Se midieron frame y memoria despues del cambio?
```

---

## Regla final

Precargar y distribuir no hacen que el trabajo desaparezca. Eligen cuando molesta menos.

```txt
El costo total no baja.
Lo que baja es el pico.
Y lo que sube, casi siempre,
es la memoria.
```
