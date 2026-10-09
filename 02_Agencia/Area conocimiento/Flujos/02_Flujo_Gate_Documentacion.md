## Propósito — Modo Gate

Medir un artefacto contra su contrato antes de darlo por cerrado. Corre **solo**, sin que nadie se acuerde de pedirlo: es lo único que evita que un artefacto se cierre incompleto porque quien lo escribió no notó lo que faltaba.

Un gate que no se puede verificar mecánicamente no es un gate, es una intención.

---

## Entrada del flujo

Un artefacto que su área da por terminado, o una carpeta de artefactos al cerrar una entrega.

---

## Transformación que realiza

```txt
`documentacion.py <ruta> --verificar`
   ↓
   ├── exit 0 → el artefacto cierra. El área sigue.
   └── exit 1 → el Validador lee el informe
                 ↓
                 ├── falla de ley        → rebota al área dueña con el hallazgo
                 ├── excepción legítima  → se declara en excepciones.txt, con razón
                 └── tipo sin contrato   → no falla el artefacto: falta el contrato
```

Cuando el rebote es de forma y no de criterio, dispara el `01_Flujo_Copiloto` en vez de devolver una lista.

---

## Salida esperada

```txt
## Medición — artefactos leídos / tipos / fallas por ley
## Fuera de ley — archivo, ley, detalle
## Excepciones declaradas — con su razón
## Fuera del alcance de la herramienta — dicho como juicio
## Cierre — Cerrado / Ajustar (a quién rebota) / Pausado (qué falta)
```

---

## Criterios de aceptación

- El veredicto sale de correr la herramienta, no de leer el artefacto a ojo.
- Cada excepción tiene su razón escrita. Una excepción sin razón es un agujero.
- Lo que la herramienta no prueba está separado y no cuenta como falla.
- Un tipo sin contrato se reporta como contrato faltante, no como artefacto malo.

---

## Qué debe evitar

No fallar un artefacto por una ley que la herramienta no puede probar. No reparar el artefacto ajeno. No dejar pasar una falla "porque se entiende igual": el gate existe para el que llega después.

---

## Resultado final

Un artefacto cerrado con número, o un rebote con el hallazgo concreto y el área a la que le corresponde.
