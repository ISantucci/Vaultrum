## Proposito

Esta subcarpeta reune criterios para definir condiciones que afectan como se interpreta, recorre o valida un mapa logico.

No existe para explicar algoritmos completos.
No existe para decidir comportamientos de NPC.
No existe para reemplazar la representacion del mapa.
No existe para convertir cada mapa en un sistema complejo.

Existe para responder:

```txt
¿Que reglas afectan por donde se puede, conviene o no conviene pasar?
```

---

## Idea central

Un mapa logico no siempre se reduce a:

```txt
se puede pasar
no se puede pasar
```

Tambien puede incluir condiciones como:

```txt
se puede pasar pero cuesta mas
se puede pasar pero es peligroso
esta bloqueado hasta cierto evento
se desbloquea durante la partida
conviene menos que otra ruta
solo algunos agentes pueden pasar
```

Estas reglas no son el mapa completo.

Son informacion adicional que otros sistemas pueden consultar.

---

## Responsabilidad de esta subcarpeta

Esta subcarpeta debe explicar reglas que afectan el uso del espacio.

Su responsabilidad incluye:

```txt
costos
zonas navegables
zonas bloqueadas
mapas con costos
rutas alternativas
desbloqueo de caminos
condiciones de disponibilidad
criterios de validez espacial
```

No es responsabilidad principal de esta subcarpeta explicar:

```txt
percepcion del NPC
ataque
huida
patrullaje
algoritmos de pathfinding completos
movimiento fisico
arquitectura completa de NPC
```

Las reglas de mapa alimentan sistemas consumidores.

No reemplazan esos sistemas.

---

## Como usar esta subcarpeta

Usar esta subcarpeta cuando el problema sea:

```txt
un camino cuesta mas que otro
una zona no se puede atravesar
una ruta se desbloquea despues
el mapa cambia durante la partida
el pathfinding debe preferir ciertos caminos
un nodo o conexion tiene penalizacion
hay rutas alternativas que dependen de condiciones
```

Ejemplos:

```txt
Una puerta bloquea el paso hasta conseguir una llave.
→ Desbloqueo de caminos.

Una zona de barro penaliza el movimiento.
→ Costos.

Un camino corto es peligroso y uno largo es seguro.
→ Mapas con costos.

Una oleada desbloquea un nuevo camino.
→ Desbloqueo de caminos / Rutas alternativas.
```

---

## Flujo recomendado

El flujo sano para trabajar reglas de mapa es:

```txt
1. Identificar que condicion afecta al espacio.
2. Definir si la condicion bloquea, permite, penaliza o habilita.
3. Definir si aplica a nodo, conexion, zona, celda o ruta.
4. Definir si es fija o dinamica.
5. Exponer la informacion para sistemas consumidores.
6. Validar que la regla no rompa la navegacion.
7. Debuggear visualmente si corresponde.
```

Las reglas de mapa no reemplazan al algoritmo.

Lo alimentan.

---

## [[Costos]]

Define valores que indican que tan caro, dificil, riesgoso o conveniente es usar una parte del mapa.

Usar esta nota cuando la navegacion no deba depender solo de distancia.

Pregunta principal:

```txt
¿Este punto, zona o conexion deberia ser mas o menos conveniente que otro?
```

---

## [[Mapas con costos]]

Explica como integrar costos dentro de una representacion de mapa.

Usar esta nota cuando el mapa necesita exponer valores que sistemas consumidores puedan interpretar.

Pregunta principal:

```txt
¿Como represento un mapa donde no todos los caminos valen lo mismo?
```

---

## [[Zonas navegables y bloqueadas]]

Define espacios que pueden o no pueden ser usados por un sistema de navegacion.

Usar esta nota cuando el mapa necesita distinguir areas validas e invalidas.

Pregunta principal:

```txt
¿Que partes del mapa se pueden usar y cuales no?
```

---

## [[Rutas alternativas]]

Define la existencia de mas de un camino posible entre puntos relevantes.

Usar esta nota cuando el diseño del mapa ofrece opciones de recorrido.

Pregunta principal:

```txt
¿Existen varios caminos posibles y que diferencia hay entre ellos?
```

---

## [[Desbloqueo de caminos]]

Define como una ruta, nodo, conexion o zona pasa de no disponible a disponible durante la partida.

Usar esta nota cuando el mapa cambia por progreso, eventos, oleadas, llaves u objetivos.

Pregunta principal:

```txt
¿Cuando y por que una parte del mapa pasa a estar disponible?
```

---

## Relacion con representacion de mapa

Las reglas de mapa necesitan una estructura sobre la cual aplicarse.

Pueden aplicarse sobre:

```txt
nodos
conexiones
grillas
celdas
zonas
rutas
waypoints
```

La direccion correcta es:

```txt
Representacion de mapa
→ define estructura.

Reglas de mapa
→ agregan condiciones sobre esa estructura.

Sistema consumidor
→ interpreta esas condiciones.
```

---

## Relacion con navegacion y pathfinding

Las reglas de mapa pueden afectar el calculo de rutas.

Ejemplo:

```txt
Un nodo bloqueado
→ no se incluye.

Una conexion cara
→ se evita si hay opcion mejor.

Una ruta desbloqueada
→ pasa a estar disponible.

Un costo dinamico
→ modifica la decision del algoritmo.
```

Pero la regla no calcula la ruta por si sola.

La regla expone informacion.

El sistema de navegacion o pathfinding la consume.

---

## Criterio para una IA

Antes de proponer reglas de mapa, una IA debe responder:

```txt
¿Que condicion espacial existe?
¿Bloquea, habilita, penaliza o modifica?
¿Sobre que estructura aplica?
¿Es fija o dinamica?
¿Quien actualiza la regla?
¿Quien consume la regla?
¿Como se valida?
¿Que costo tecnico tiene?
¿Una solucion mas simple alcanza?
```

No debe agregar reglas solo porque el sistema parece mas completo.

---

## Errores que esta subcarpeta ayuda a evitar

```txt
tratar todos los caminos como iguales cuando no lo son
meter reglas de mapa dentro del NPC
usar costos sin explicar que representan
bloquear rutas sin criterio de diseño
crear rutas alternativas que no afectan gameplay
no actualizar pathfinding cuando cambia el mapa
confundir zona bloqueada con zona cara
duplicar reglas entre varias clases
```

---

## Criterio de links

Los links deben respetar la direccion de dependencia.

```txt
Reglas de mapa
→ pueden llamar a estructuras base cuando necesitan explicar sobre que aplican.

Estructuras base
→ no deben explicar todas las reglas que podrian usarlas.

Sistemas consumidores
→ llaman a reglas cuando las interpretan.
```

Regla:

```txt
El consumidor llama al proveedor.
El proveedor no explica todos sus consumidores.
```

---

## Regla final

Las reglas de mapa no mueven al NPC.

No deciden comportamiento.

No calculan solas la ruta.

Definen condiciones sobre el espacio.

```txt
Mapa
→ define estructura

Reglas
→ definen condiciones

Sistema consumidor
→ interpreta y ejecuta
```