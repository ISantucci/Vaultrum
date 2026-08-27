## Índice de intervenciones de arquitectura (ARQ)

Registro de todo lo que el Área de Arquitectura hace sobre la forma del vault.

Cada `ARQ-XXX` declara su **modo** y queda con lo que se midió, lo que se hizo y en qué estado quedó el grafo.

---

## Los tres modos

| Modo | Qué registra | Cuándo |
|------|--------------|--------|
| Plano | el procedimiento en cascada que se le entregó a otra área | antes de que esa área toque la forma |
| Emplazamiento | dónde se ubicó contenido nuevo y qué índices se tocaron | cuando entra material al vault |
| Pasada | una medición con su reparación y su verificación | cuando hay que corregir lo que ya está |

Un `ARQ` declara un solo modo. Si una intervención empezó como plano y terminó reparando, son dos `ARQ`: el plano falló o la ejecución se desvió, y eso hay que poder leerlo separado.

---

## Regla de numeración

`ARQ-001`, `ARQ-002`, … en orden de ejecución. Una intervención por número, sin subíndices: la arquitectura no se fracciona por sistema. Un `ARQ` se corre entero o acotado a una capa, y eso se declara adentro.

Los `ARQ` **no cuelgan de la columna vertebral de numeración de la Agencia**: no son un eslabón de la cadena de producción, son intervenciones sobre el vault mismo.

---

## Registro

El listado de intervenciones vive en `00_Registro_arq`, que no se versiona.

Una intervencion entra al registro recien cuando paso por el `05_Flujo_Validacion_Pureza`. Una reparacion sin verificacion no es una intervencion: es un cambio suelto.

