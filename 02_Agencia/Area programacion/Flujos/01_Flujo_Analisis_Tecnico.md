## Propósito

Transformar un requerimiento (`RQ` + `GDS`, y `LDS`/`UXS` si existen) en un diagnóstico técnico basado en el proyecto real y el conocimiento del Core, para que el diseño de solución no se construya sobre suposiciones.

---

## Entrada del flujo

- `RQ-XXX.n` del Área de Producción.
- `GDS-XXX.n` del Área de Game Design, si el requerimiento es jugable.
- Acceso al proyecto real.

Si el `RQ` es ambiguo o no existe, el flujo no avanza: se deriva a Producción.

---

## Transformación que realiza

- Interpreta el requerimiento en términos técnicos.
- Lee los archivos relevantes del proyecto.
- Detecta sistemas, managers y convenciones existentes.
- Evalúa reutilizar / extender / crear.
- Identifica el conocimiento del Core aplicable (SOLID, patrones, managers, optimización, estructuras, algoritmos, IA).
- Marca riesgos, dependencias e información faltante.

---

## Salida esperada / formato

```txt
## Requerimiento y specs (RQ-XXX.n / GDS-XXX.n / LDS-XXX.n / UXS-XXX.n)
## Sistema existente relevante
## Reutilizable / extensible
## Conocimiento del Core aplicable
## Riesgos y dependencias
## Información faltante
## Base para el diseño de solución
```

---

## Criterios de aceptación

- El requerimiento fue entendido en términos técnicos.
- Se leyó el proyecto real (no se asumió arquitectura).
- Se identificó qué se reutiliza y qué conocimiento del Core aplica.
- Riesgos y faltantes están visibles.

---

## Condiciones para avanzar

Avanza al [[02_Flujo_Diseno_Solucion]] cuando hay contexto real suficiente para diseñar.
No avanza si el requerimiento sigue ambiguo o falta información crítica: se marca y se deriva.

---

## Qué debe evitar

No propone solución final. No escribe código. No copia teoría del Core.

---

## Resultado final

Un diagnóstico técnico transferible que le permite al Diseñador de Solución trabajar sin reanalizar desde cero.
