## Proposito

Esta carpeta agrupa presets reutilizables para crear NPCs de forma mas rapida, consistente y mantenible.

Un preset es un molde operativo.

No es una regla universal.

Sirve como punto de partida para implementar un tipo de NPC frecuente sin volver a pensar toda la arquitectura desde cero.

```txt
Necesidad de NPC
→ buscar preset existente
→ adaptar sistemas necesarios
→ descartar lo que no aplica
→ implementar
→ validar
→ registrar variante si aporta valor
```

---

## Responsabilidad

La responsabilidad de esta carpeta es guardar moldes concretos de NPCs.

Debe ayudar a responder:

```txt
que tipo de NPC necesito
que preset se parece mas
que sistemas usa
que sistemas no necesita
como se comporta
como se valida
que puedo copiar
que debo adaptar
que errores evitar
```

---

## Contenido de esta seccion

```txt
[[NPC pasivo de interaccion]]
[[NPC patrullero simple]]
[[NPC patrullero con variedad]]
[[NPC de sigilo]]
[[NPC agresivo directo]]
[[NPC evasivo]]
[[NPC con ataques variados]]
[[NPC tactico simple]]
```

---

## [[NPC pasivo de interaccion]]

Molde para NPCs que existen principalmente para dialogar, vender, entregar informacion o iniciar una interaccion.

Ejemplos:

```txt
comerciante
personaje de quest
guia estatico
NPC narrativo
```

---

## [[NPC patrullero simple]]

Molde para NPCs que recorren puntos o zonas con un patron claro.

Ejemplos:

```txt
guardia basico
enemigo de pasillo
camara movil
```

---

## [[NPC patrullero con variedad]]

Molde para NPCs que patrullan sin repetir siempre el mismo recorrido.

Usa variedad controlada mediante pesos, memoria o condiciones de validez.

Ejemplos:

```txt
guardia que revisa zonas
NPC con rutina menos mecanica
enemigo que alterna puntos de interes
```

---

## [[NPC de sigilo]]

Molde para NPCs que deben detectar al jugador de forma justa y legible.

Ejemplos:

```txt
guardia de stealth
camara de seguridad
enemigo que investiga ruidos
```

---

## [[NPC agresivo directo]]

Molde para enemigos que detectan al jugador y lo presionan de forma clara.

Ejemplos:

```txt
zombie
criatura hostil
enemigo de arena
enemigo melee simple
```

---

## [[NPC evasivo]]

Molde para NPCs que evitan peligro, huyen o buscan seguridad.

Ejemplos:

```txt
civil
animal
enemigo debil
NPC que busca sobrevivir
```

---

## [[NPC con ataques variados]]

Molde para NPCs que necesitan alternar ataques sin perder control de diseño.

Ejemplos:

```txt
boss
enemigo elite
mago
enemigo tactico ofensivo
```

---

## [[NPC tactico simple]]

Molde para NPCs que toman decisiones segun contexto, pero sin llegar a una IA compleja.

Ejemplos:

```txt
enemigo que alterna ataque y cobertura
aliado que ayuda o se retira
enemigo que evalua distancia
```

---

## Como usar esta carpeta

Cuando se necesite crear un NPC:

```txt
1. Definir el rol del NPC.
2. Buscar el preset mas parecido.
3. Leer cuando usarlo y cuando no.
4. Revisar sistemas necesarios.
5. Revisar sistemas opcionales.
6. Descartar sistemas que no aplican.
7. Adaptar datos al juego.
8. Implementar.
9. Validar en gameplay.
10. Registrar variante si aporta valor.
```

Regla:

```txt
Primero buscar molde existente.
Despues adaptar.
Recien despues crear algo nuevo.
```

---

## Como crear un nuevo preset

Crear un nuevo preset cuando:

```txt
aparece un tipo de NPC repetible
la combinacion de sistemas puede reutilizarse
la solucion ya fue validada o tiene criterio claro
el NPC representa un caso comun
el preset ahorraria decisiones futuras
```

No crear preset cuando:

```txt
el caso es demasiado especifico
todavia no se valido
solo cambia un valor menor
ya existe un preset parecido
la diferencia es solo estetica
la solucion no se repetiria
```

---

## Formato recomendado para cada preset

Cada preset debe respetar una estructura operativa.

```txt
Definicion
Rol de gameplay
Cuando usarlo
Cuando no usarlo
Sistemas necesarios
Sistemas opcionales
Sistemas que NO necesita
Flujo de comportamiento
Estructura recomendada
Datos necesarios
Variantes posibles
Costos de implementacion
Costos de optimizacion
Validacion
Errores comunes
Criterio para una IA
Checklist
Regla final
```

---

## Autonutricion de presets

Esta carpeta puede crecer a partir de proyectos reales.

Flujo:

```txt
1. Se implementa un NPC real.
2. Se valida que funciona.
3. Se detecta si la solucion es reutilizable.
4. Se compara con presets existentes.
5. Si encaja, se agrega como variante.
6. Si no encaja y es reutilizable, se crea nuevo preset.
7. Se documenta que sistemas usa y que problema resolvio.
```

Regla:

```txt
Los presets no se agregan por cantidad.

Se agregan cuando reducen decisiones futuras y aumentan reutilizacion.
```

---

## Criterio para una IA

Cuando una IA trabaje con esta carpeta debe:

```txt
buscar presets antes de inventar soluciones
elegir el preset mas parecido al rol pedido
adaptar, no copiar ciegamente
descartar sistemas innecesarios
mantener separacion de responsabilidades
no crear presets para casos triviales
proponer nuevo preset solo si hay reutilizacion real
registrar variantes utiles
respetar navegacion waterfall
```

---

## Regla final

```txt
Un preset no reemplaza el criterio.

Lo acelera cuando el problema ya tiene un molde confiable.
```