## Proposito

Esta rama reune los problemas y las soluciones de rendimiento de la interfaz.

No existe para prohibir animaciones de UI.
No existe para reducir la cantidad de elementos en pantalla.
No existe para tratar la UI como un detalle que se optimiza al final.

Existe porque la UI es un sistema de performance propio, con costo en los dos procesadores a la vez.

---

## Idea central

La UI no se clasifica solamente como CPU ni solamente como GPU.

```txt
CPU    actualizacion
       layout
       rebuilds
       generacion de texto
       input
       raycasts

GPU    transparencias
       imagenes
       mascaras
       overdraw
       grandes superficies
```

Por eso tiene rama propia. Meterla adentro de CPU dejaria afuera el overdraw; meterla adentro de GPU dejaria afuera los rebuilds.

Y hay un segundo motivo, que es de diseño y no de tecnica: la UI existe para comunicar. Una optimizacion de UI que rompe la comunicacion no es una optimizacion, es una perdida.

---

## El problema de fondo

Casi todos los costos de UI salen de la misma raiz:

```txt
la UI se actualiza porque tecnicamente puede
en vez de actualizarse cuando tiene algo que comunicar
```

La diferencia conceptual es:

```txt
Polling          Push / event-driven

¿Cambio?         Cambio → actualizar
¿Cambio?
¿Cambio?
¿Cambio?
```

Una barra de vida que se redibuja sesenta veces por segundo para mostrar el mismo numero no esta comunicando sesenta veces: esta trabajando sesenta veces.

---

## Cuando usar esta rama

Usar UI cuando:

```txt
el frame empeora al abrir una pantalla o un menu
el HUD actualiza texto todos los frames
una lista larga se reconstruye al scrollear
hay caida al mostrar inventarios, tiendas o tablas
el costo aparece con paneles translucidos superpuestos
el profiler muestra layout o rebuild dominando
```

---

## Como debe usar esta rama una IA

Antes de tocar UI, una IA debe separar tres preguntas:

```txt
¿Cada cuanto se actualiza?     → frecuencia
¿Cuanto se reconstruye?        → alcance del rebuild
¿Cuanta pantalla cubre?        → costo de fragmentos
```

Son tres problemas distintos con tres soluciones distintas. Bajar la frecuencia no arregla un rebuild de jerarquia entera, y separar canvas no arregla un panel translucido que cubre toda la pantalla.

Y antes de sacar algo, la pregunta obligatoria:

```txt
¿Que deja de saber el jugador si esto no esta?
```

---

## Problemas incluidos

### [[UI actualizada innecesariamente]]

La UI hace trabajo sin que el dato haya cambiado.

Consultar cuando el costo sea constante aunque no pase nada en pantalla.

### [[Canvas rebuild]]

Cuando cambia una parte, se reconstruye informacion de elementos que casi nunca cambian.

Consultar cuando el costo escale con el tamaño de la jerarquia y no con lo que se modifico.

---

## Soluciones incluidas

### [[UI orientada a eventos]]

El dueño del dato avisa que cambio; la UI reacciona en vez de preguntar.

Consultar cuando la UI consulte estado todos los frames.

### [[Separar canvas por frecuencia de cambio]]

Agrupar lo que cambia junto y separar lo que casi nunca cambia, para acotar el alcance del rebuild.

Consultar cuando un solo elemento dinamico este arrastrando a toda una pantalla estatica.

---

## Como se conecta con otras ramas

```txt
Diagnostico             CPU Usage muestra UI; Frame Debugger muestra sus pasadas
Fundamentos             valor perceptual por costo aplica aca mas que en ningun lado
CPU                     layout, rebuilds, generacion de texto y raycasts
GPU                     transparencias, mascaras, overdraw y grandes superficies
Memoria                 el texto que se regenera por frame genera basura
Patrones transversales  Early Exit y Active Set aplican a listas y paneles
```

---

## Criterio de uso

La UI no debe actualizarse porque tecnicamente puede.

Debe actualizarse cuando necesita comunicar:

```txt
cambio
estado
consecuencia
disponibilidad
exito
error
```

Eso favorece de forma natural una arquitectura basada en eventos, y no al reves: la arquitectura de eventos no es una tecnica de optimizacion que se aplica a la UI, es la forma que toma la UI cuando se la piensa como comunicacion.

Hay excepciones legitimas y conviene tenerlas escritas: barras animadas, timers, minimapas y medidores continuos si necesitan actualizacion sostenida. Bajarles la frecuencia rompe la lectura.

---

## Regla final

La UI se optimiza haciendola trabajar cuando tiene algo que decir.

```txt
¿Cambio el dato?
→ si no, no hay nada que dibujar
→ si si, dibujar solo lo que cambio
```
