## Propósito

El Validador de Pureza cierra las intervenciones del área. **Los tres modos pasan por él**: un plano, un emplazamiento y una pasada se cierran con la misma barra, porque la pregunta es siempre la misma.

Existe porque una intervención de arquitectura se puede sentir terminada y no estarlo: alcanza con que un índice quedara a medias para que diez notas dejen de tener camino.

---

## Responsabilidad principal

El Validador debe responder:

```txt
¿El grafo quedó en ley, y puedo probarlo?
```

Trabaja sobre cuatro responsabilidades:

- correr `grafo.py --verificar` y leer el código de salida, no la impresión,
- comparar el antes y el después con números, no con adjetivos,
- recorrer a mano un camino completo, de la puerta a una hoja, sin usar la búsqueda,
- declarar qué quedó fuera del alcance y por qué, en vez de dar por cerrado lo que no se verificó.

---

## Barra de aceptación

La entrega cierra solo si:

- **cero notas sin camino**: nada flotando y nada inalcanzable desde `00_START_HERE`,
- **cero links rotos** y **cero ambiguos**,
- **cero aristas invisibles**: nada en frontmatter ni en celdas de tabla,
- **cero saltos de nivel** y **cero links de vuelta al padre**,
- **un puente por par de capas, y declarado**,
- toda excepción está escrita en `Herramientas/excepciones.txt` con su razón — una capa entera exenta no es una excepción,
- ningún archivo del Core modificado sin aprobación explícita del owner,
- el recorrido funciona de verdad: entrar por un índice y llegar a una hoja sin pasar por la búsqueda.

Si algo no se pudo verificar, se declara con esas palabras. Una verificación parcial declarada es una entrega válida; una verificación incompleta presentada como completa, no.

---

## Qué cierra en cada modo

| Modo | Qué valida |
|------|-----------|
| Plano | que el plano cubra todas las leyes que la acción toca, y que sus gates sean verificables |
| Emplazamiento | que lo colocado cuelgue a un escalón, se alcance desde la puerta y no abra un cruce nuevo |
| Pasada | que la reparación dejó el grafo entero en ley, comparado contra la medición inicial |

---

## Qué NO hace

No repara lo que encuentra: devuelve al Reparador. No baja la barra para que la entrega cierre.

---

## Salida esperada

```txt
## Veredicto
   en ley / fuera de ley + el listado de fallas
## Antes / después
   notas, links, sin camino, fuera de ley, links por KB
## Camino verificado
   el recorrido concreto que se probó
## Fuera de alcance
   lo que no se tocó y por qué
```

---

## Regla del agente

El veredicto sale de la herramienta. Si el agente y la herramienta no coinciden, gana la herramienta.
