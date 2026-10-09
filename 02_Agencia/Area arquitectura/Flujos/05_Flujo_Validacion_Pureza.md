## Propósito

Verificar que la intervención dejó el grafo en ley, y dejarla registrada como `ARQ` con su modo declarado.

Cierra los tres modos. Un plano, un emplazamiento y una pasada pasan por acá antes de darse por terminados.

---

## Entrada del flujo

- Una intervención terminada: un plano entregado, un emplazamiento colocado, o un vault ya reparado por el `04_Flujo_Reparacion_Cascada`.
- La medición previa, para poder comparar antes y después.

---

## Transformación que realiza

- Corre `grafo.py --verificar` y lee el código de salida.
- Compara contra la medición inicial: links totales, sin camino, fuera de ley, densidad por KB.
- Recorre a mano un camino completo — de la puerta hasta una hoja — para confirmar que la navegación funciona de verdad y no solo en los números.
- Escribe el `ARQ-XXX` en `Salidas/`, con su **modo** declarado, y lo registra en el índice.

---

## Salida esperada / formato

```txt
## Modo
   Plano / Emplazamiento / Pasada
## Veredicto
   en ley / fuera de ley + fallas
## Antes / después
   notas, links, sin camino, fuera de ley, links por KB
## Camino verificado
   el recorrido concreto que se probó
## Fuera de alcance
   lo que no se tocó y por qué
```

---

## Criterios de aceptación

- Cero notas sin camino, cero rotos, cero ambiguos, cero aristas invisibles, cero saltos, un puente por par de capas.
- Toda excepción está escrita en `Herramientas/excepciones.txt` con su razón.
- El recorrido probado llega a destino sin usar la búsqueda.
- Lo no verificado está declarado con esas palabras.

---

## Condiciones para avanzar

Cierra la intervención cuando el veredicto es *en ley* o cuando lo que falta está declarado y aprobado por el owner.
Vuelve al `04_Flujo_Reparacion_Cascada` si el veredicto es *fuera de ley*.

---

## Qué debe evitar

No repara lo que encuentra. No baja la barra para poder cerrar. No declara verificado lo que no corrió.

---

## Resultado final

Un `ARQ` registrado que dice, con su modo y con números, en qué estado quedó el grafo.
