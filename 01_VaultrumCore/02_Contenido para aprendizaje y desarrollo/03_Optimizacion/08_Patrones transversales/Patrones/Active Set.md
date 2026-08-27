## Definicion

Active Set es la separacion entre los objetos que existen y los objetos que se actualizan.

No todo lo que existe tiene que pertenecer al conjunto que trabaja este frame.

```txt
Todos los objetos
≠
objetos activos y relevantes
```

Ejemplo directo:

```txt
1000 NPC existentes
150 activos
```

Los otros 850 siguen existiendo, conservan su estado y pueden volver al conjunto en cualquier momento.

Lo que no hacen es consumir tiempo de frame mientras no aportan.

```txt
Existir
≠
actualizarse
```

El patron no pertenece a un recurso ni a un subsistema.

Aparece en IA, en fisica, en animacion, en audio, en particulas y en rendering.

---

## Que problema ayuda a prevenir

Ayuda con:

```txt
Costo que crece con la cantidad de entidades creadas.
Update ejecutado sobre objetos que nadie percibe.
Fisica simulada lejos de cualquier jugador.
Animacion evaluada fuera de camara.
Audio procesado a distancias irrelevantes.
Spikes al poblar el nivel.
```

Y previene una trampa de diagnostico muy frecuente.

```txt
Sintoma:
el comportamiento individual parece barato,
pero el sistema entero es caro.

Causa:
se esta ejecutando sobre demasiadas entidades.
```

Actualizar solo lo relevante suele pesar muchisimo mas que microoptimizar el comportamiento individual.

```txt
Bajar 20% el costo de cada NPC
sobre 1000 NPC
```

rinde bastante menos que:

```txt
pasar de 1000 NPC actualizados
a 150
```

---

## Como funciona

El sistema mantiene dos cosas distintas.

```txt
Registro completo
→ todo lo que existe y su estado

Conjunto activo
→ lo que se procesa este frame
```

La pertenencia al conjunto se decide con un criterio explicito.

```txt
Distancia al jugador o a la camara.
Estado de la entidad.
Visibilidad.
Relevancia de gameplay.
Pertenencia a una zona o encuentro activo.
```

Esos criterios se combinan.

```txt
Lejos y sin relevancia
→ fuera del set

Lejos pero persiguiendo al jugador
→ dentro del set

Cerca pero desactivado por diseño
→ fuera del set
```

La revision de pertenencia tambien cuesta.

```txt
Revisar el set cada frame
→ el chequeo se vuelve el costo
```

Por eso conviene revisarlo con menor frecuencia que el propio update, o revisarlo por eventos.

```txt
Entra al set
→ por evento o por revision periodica

Sale del set
→ con histeresis, nunca con el mismo umbral con el que entro
```

Sin histeresis, una entidad parada sobre el umbral entra y sale todos los frames.

---

## Como aplicarlo en videojuegos

En IA:

```txt
NPC fuera de la zona activa
→ no evalua percepcion ni decisiones
```

En fisica:

```txt
Cuerpo lejano y en reposo
→ fuera de la simulacion activa
```

En animacion:

```txt
Personaje fuera de camara
→ no evalua el grafo de animacion
```

En particulas:

```txt
Emisor fuera de relevancia
→ deja de emitir y de simular
```

Ejemplo en un Tower Defense:

```txt
Registro completo
    todos los enemigos de la oleada, incluidos los que faltan aparecer

Conjunto activo
    enemigos ya spawneados y todavia vivos

Conjunto activo de torres
    torres con al menos un enemigo dentro de su rango
```

Ese ultimo conjunto suele ser el mas rentable.

```txt
Antes:
30 torres buscan objetivo todos los frames.

Despues:
solo las torres con enemigos en rango buscan objetivo.
```

En un mapa largo, la mayoria de las torres no tiene nada que hacer durante buena parte de la oleada.

---

## Relacion con arquitectura

Se relaciona con:

```txt
Batch processing.
Separacion model view.
Un sistema que administra muchas entidades.
Culling entendido como evitar trabajo que no contribuye.
```

El patron necesita un dueño claro del conjunto.

```txt
Un sistema
→ conoce el registro completo
→ decide la pertenencia
→ recorre solo el conjunto activo
```

Cuando cada entidad decide sola si actualizarse, el chequeo se paga igual en todas.

```txt
Update que empieza preguntando si corresponde actualizar
→ ya se pago el callback
```

Sacar la decision afuera es lo que convierte el patron en un ahorro real.

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
CPU
Frame Budget
```

Puede afectar tambien:

```txt
GPU
Memoria
```

porque las entidades inactivas suelen dejar de generar geometria, particulas o comandos de dibujo, y porque el registro completo sigue ocupando memoria.

Ese ultimo punto es el trade-off central:

```txt
Menos tiempo de frame
↔
memoria residente que no se libera
```

El objeto inactivo sigue vivo.

Lo que se ahorra es su tiempo, no su espacio.

---

## Cuando conviene usarlo

Conviene cuando:

```txt
Existen muchas mas entidades de las que importan a la vez.
El costo escala con la cantidad creada.
Hay un criterio claro de relevancia.
El jugador no percibe lo que ocurre fuera del set.
La cantidad de entidades varia mucho durante la partida.
```

Casos claros:

```txt
Mundos grandes con poblacion distribuida.
Oleadas numerosas.
Sistemas de particulas ambientales.
Fauna, trafico y NPC de ambientacion.
```

---

## Cuando NO conviene usarlo

No conviene cuando:

```txt
Casi todas las entidades son relevantes al mismo tiempo.
La cantidad total es baja.
El estado fuera del set debe seguir evolucionando.
El criterio de relevancia no se puede definir con claridad.
La revision de pertenencia cuesta mas que el update evitado.
```

Y hay un limite duro:

```txt
Simulacion que el jugador espera que siga ocurriendo
→ economia, produccion, timers, progresion
```

Si un sistema debe avanzar aunque nadie lo mire, no puede salir del set sin mas.

Puede bajar su frecuencia, o puede recuperar el tiempo perdido al reactivarse.

---

## Trade-offs

Ventajas:

```txt
Costo proporcional a lo relevante y no a lo creado.
Mucho margen sin tocar el comportamiento individual.
Sistemas que escalan mejor con la poblacion.
Ahorro medible en un solo lugar.
```

Costos:

```txt
Memoria residente de lo que existe pero no corre.
Logica de entrada y salida del conjunto.
Riesgo de comportamiento visible al reactivar.
Estado congelado que puede quedar desactualizado.
```

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Sacar del set algo que el jugador si estaba mirando.
Umbral unico de entrada y salida.
Revisar la pertenencia todos los frames.
Congelar sistemas que debian seguir avanzando.
Reactivar sin reconciliar el estado.
Criterio basado solo en distancia.
```

Ejemplo de riesgo real:

```txt
Un enemigo sale del set por distancia mientras persigue al jugador.

Resultado:
queda quieto a la vista,
y vuelve a moverse recien cuando el jugador se acerca.
```

Ese es el riesgo central del patron: lo que se cae del set deja de comportarse como el jugador espera.

El criterio de pertenencia es una decision de diseño antes que una decision tecnica.

---

## Checklist de implementacion

```txt
¿Cuantas entidades existen y cuantas importan a la vez?
¿Cual es el criterio de pertenencia?
¿Interviene algo mas que la distancia?
¿Quien decide la pertenencia?
¿Cada cuanto se revisa?
¿Hay histeresis entre entrar y salir?
¿Que pasa con el estado mientras la entidad esta fuera?
¿Hay sistemas que deban avanzar igual?
¿Se reconcilia el estado al reactivar?
¿El jugador puede notar la salida del set?
¿Cuanta memoria queda ocupada por lo inactivo?
¿Se midio antes y despues?
```

---

## Regla final

Existir no da derecho a consumir tiempo de frame.

```txt
El costo deberia seguir a lo relevante,
no a lo creado.
Y lo que sale del set no puede dejar de tener sentido.
```
