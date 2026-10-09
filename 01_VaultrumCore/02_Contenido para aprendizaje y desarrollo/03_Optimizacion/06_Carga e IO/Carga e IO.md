## Proposito

Esta rama reune los problemas y las soluciones de carga, almacenamiento y entrada/salida.

No existe para acortar pantallas de carga a cualquier costo.
No existe para precargar todo por las dudas.
No existe para tratar Addressables como una optimizacion automatica.

Existe porque el rendimiento de un juego no es solamente su frame rate, y porque el peor momento de muchos juegos no es cuando corren: es cuando cargan.

---

## Idea central

El rendimiento tambien incluye:

```txt
startup
pantallas de carga
transiciones
streaming
stutters por carga
```

Un juego puede tener un frame time excelente y aun asi sentirse mal:

```txt
frame normal
→ carga
→ freeze
→ frame normal
```

Ese freeze no aparece en el promedio de FPS y arruina el momento igual. Casi siempre es la misma causa: mucho trabajo resuelto de golpe en un momento en el que el jugador esta esperando una respuesta.

---

## Las dos palancas

Esta rama tiene solo dos movimientos, y los dos son sobre el eje del tiempo:

```txt
mover el trabajo mas tarde y repartido    → carga distribuida
mover el trabajo mas temprano             → precarga
```

Y una advertencia que vale para los dos:

```txt
distribuir no elimina trabajo
```

Solo cambia cuando se hace, durante cuanto tiempo y como afecta la experiencia. La cuenta total sigue siendo la misma.

---

## Cuando usar esta rama

Usar Carga e IO cuando:

```txt
hay un freeze al entrar a una zona
hay un freeze la primera vez que aparece un tipo de enemigo o efecto
la transicion entre escenas corta el ritmo
el startup es largo
el juego tironea mientras carga contenido en streaming
el primer disparo del arma nueva cuesta y los siguientes no
```

Ese ultimo sintoma es el mas facil de confundir con un problema de gameplay: no lo es, es una carga.

---

## Como debe usar esta rama una IA

Antes de proponer una solucion, una IA debe poder decir:

```txt
¿Que se esta cargando?
¿Cuando se carga?
¿Se puede cargar antes, en un momento menos critico?
¿Se puede repartir en varios frames?
¿Se puede no cargarlo todavia?
¿Cuanta memoria residente agrega la solucion?
¿Cuando se libera?
```

Una IA no debe razonar asi:

```txt
Hay assets pesados.
→ Addressables.
```

Debe razonar asi:

```txt
Freeze al entrar a la zona norte.
→ Timeline: un unico frame de 900 ms con carga de assets.
→ ¿que assets? ¿son de esa zona?
→ candidatas: precargar durante la transicion, o repartir la carga.
→ trade-off: memoria residente anticipada.
→ validar entrando a la misma zona en las mismas condiciones.
```

---

## Problemas incluidos

### [[Freeze por carga en runtime]]

Trabajo de carga resuelto de golpe en medio del gameplay, que corta el frame aunque el rendimiento habitual sea bueno.

Consultar cuando el corte coincida con entrar a una zona, abrir una pantalla o ver algo por primera vez.

---

## Soluciones incluidas

### [[Precarga y carga distribuida]]

Las dos formas de mover el trabajo en el tiempo, con sus intercambios contra memoria y contra latencia.

Consultar cuando ya se sepa que se carga y falte decidir cuando.

### [[Addressables como metodologia de optimizacion]]

Carga bajo demanda y contenido direccionable, con su gestion de grupos y su riesgo de cargar en el peor momento.

Consultar cuando haga falta controlar que contenido esta cargado y cuando.

### [[Assetmanager como optimizacion|AssetManager]]

Una capa unica de acceso a assets, con cache, conteo de referencias y precarga o descarga por contexto.

Consultar cuando el gameplay este hablando directo con el sistema de carga.

---

## Lo que esta rama le debe a Memoria

Las dos palancas de esta rama se pagan en memoria:

```txt
mayor memoria residente anticipada
↔
menor spike futuro
```

Precargar mejora las transiciones y empeora la memoria. Cargar tarde mejora la memoria y empeora las transiciones. No hay una opcion universal: hay un presupuesto de memoria y un momento del juego donde el corte se nota mas.

Por eso lo que se precarga tambien tiene que tener escrito cuando se libera. Un sistema que solo sabe cargar termina siendo un problema de memoria con otro nombre.

---

## Como se conecta con otras ramas

```txt
Diagnostico    Timeline muestra el frame del freeze; Memory Profiler muestra que quedo cargado
Fundamentos    el trade-off loading contra memoria es uno de los seis basicos
Memoria        el ciclo Load, Use, Release es de alla y esta rama lo usa entero
CPU            instanciar lo cargado tambien cuesta, y ese costo es de CPU
GPU            texturas y meshes recien cargados ocupan VRAM
```

---

## Criterio de uso

El objetivo no es que no haya cargas.

El objetivo es que las cargas ocurran donde el jugador las tolera:

```txt
tolera esperar        al arrancar el juego
tolera esperar        entre niveles
tolera poco           al abrir un menu
no tolera             en combate
```

Una carga bien ubicada puede ser mas larga que una mal ubicada y molestar menos.

---

## Regla final

Distribuir no elimina trabajo.

Elige cuando dolerlo.

```txt
¿Que se carga?
¿Cuando?
¿Quien lo libera?
```
