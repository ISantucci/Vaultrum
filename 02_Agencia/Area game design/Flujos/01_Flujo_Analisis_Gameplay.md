## Propósito

Transformar un `RQ` jugable en un encuadre de diseño: qué experiencia se busca y qué debe sentir el jugador, antes de definir reglas.

---

## Entrada del flujo

- `RQ-XXX.n` jugable del Área de Producción.

Si el `RQ` no es jugable o está mal definido, el flujo no avanza: se deriva (a Programación si es infraestructura, a Producción si falta alcance).

---

## Transformación que realiza

- Parte del Core: consulta identidad, principios y conocimiento aplicable (principio 1).
- Interpreta la intención jugable del requerimiento.
- Define el objetivo del sistema en términos de juego.
- Describe la experiencia esperada y el feeling buscado.
- Marca riesgos de diseño e información faltante.

---

## Salida esperada / formato

```txt
## Requerimiento (RQ-XXX.n)
## Objetivo del sistema (en términos de juego)
## Experiencia esperada / feeling
## Qué debe sentir el jugador
## Riesgos de diseño
## Información faltante
## Base para el diseño de sistema
```

---

## Criterios de aceptación

- La intención jugable está entendida.
- El objetivo del sistema es claro en términos de experiencia.
- Los riesgos y faltantes están visibles.

---

## Condiciones para avanzar

Avanza al `02_Flujo_Diseno_Sistema` cuando la experiencia buscada está clara.
No avanza si el `RQ` no es jugable o falta información crítica.

---

## Qué debe evitar

No define reglas, estados ni parámetros. No entra en implementación.

---

## Resultado final

Un encuadre de diseño transferible que le permite al Diseñador de Sistema trabajar sobre una experiencia clara.
