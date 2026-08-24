## Propósito

Verificar que la reparación dejó el grafo en ley, y dejar registrada la pasada como `ARQ`.

---

## Entrada del flujo

- Un vault ya reparado por el `02_Flujo_Reparacion_Cascada`.
- El informe previo, para poder comparar antes y después.

---

## Transformación que realiza

- Corre `grafo.py --verificar` y lee el código de salida.
- Compara contra la medición inicial: links totales, flotando, fuera de ley, densidad por KB.
- Recorre a mano un camino completo — de un índice de capa hasta una hoja — para confirmar que la navegación funciona de verdad y no solo en los números.
- Escribe el `ARQ-XXX` en `Salidas/` y lo registra en el índice.

---

## Salida esperada / formato

```txt
## Veredicto
   en ley / fuera de ley + fallas
## Antes / después
   notas, links, flotando, fuera de ley, links por KB, por capa
## Camino verificado
   el recorrido concreto que se probó
## Fuera de alcance
   lo que no se tocó y por qué
```

---

## Criterios de aceptación

- Cero flotando, cero rotos, cero ambiguos, cero aristas invisibles fuera del Core.
- El recorrido probado llega a destino sin usar la búsqueda.
- Lo no verificado está declarado con esas palabras.

---

## Condiciones para avanzar

Cierra la pasada cuando el veredicto es *en ley* o cuando lo que falta está declarado y aprobado por el owner.
Vuelve al `02_Flujo_Reparacion_Cascada` si el veredicto es *fuera de ley*.

---

## Qué debe evitar

No repara lo que encuentra. No baja la barra para poder cerrar. No declara verificado lo que no corrió.

---

## Resultado final

Un `ARQ` registrado que dice con números en qué estado quedó el grafo.
