## Patrón: Contextos - Proyecto nuevo vs. Existente

Este es un patrón estándar reutilizable en Vaultrum que aparece en múltiples modos.

**Validado en**: Productor, Documentador, Programador, Technical Game Designer.

---

## Descripción del patrón

Cuando un modo se activa, su comportamiento depende del **contexto del proyecto**.

Hay dos contextos fundamentales que requieren enfoques distintos:

1. **Proyecto nuevo** (desde cero)
2. **Proyecto existente** (ya tiene estructura, decisiones, sistemas)

El modo debe tener preguntas, criterios de acción y resultados diferentes para cada contexto.

---

## Contexto: Proyecto nuevo

**Pregunta clave**: ¿Qué es lo mínimo necesario para validar la dirección?

### Características

- No hay decisiones previas
- El sistema es exploratorio
- El riesgo es sobre-arquitecturar temprano
- El objetivo es validar rápido, iterar

### Preguntas específicas

Cada modo debe responder:

```txt
¿Cuál es la idea/objetivo central?
¿Qué ya existe? (si algo)
¿Qué está decidido?
¿Qué todavía es exploratorio?
¿Qué necesita documentarse/definirse AHORA?
¿Qué sería prematuro?
¿Qué permite validar la idea?
```

### Resultado esperado

- Estructura mínima viable
- Criterios iniciales
- Primeras decisiones
- Plan de próximos pasos
- Claridad sobre qué falta

### Anti-patrón

Crear arquitectura completa. Documentar todo. Definir sistemas que no se usan.

---

## Contexto: Proyecto existente

**Pregunta clave**: ¿Qué se respeta de lo ya hecho y qué se mejora puntualmente?

### Características

- Hay decisiones previas que deben respetarse
- El riesgo es romper coherencia existente
- El objetivo es mejorar sin rediseñar
- No se debe proponer empezar de cero salvo razón fuerte

### Preguntas específicas

Cada modo debe responder:

```txt
¿Qué existe actualmente?
¿Qué criterios ya se usan?
¿Qué problema específico hay AHORA?
¿Qué parte del proyecto afecta?
¿Hay algo similar ya implementado?
¿Se puede reutilizar o adaptar?
¿Qué se debe tocar?
¿Qué no se debe tocar?
¿Cuál es el cambio mínimo que resuelve?
¿Cómo se valida sin romper lo existente?
```

### Resultado esperado

- Propuesta compatible
- Análisis de impacto
- Plan incremental
- Claridad sobre riesgos
- Validación de coherencia

### Anti-patrón

Proponer refactors globales. Reescribir todo. Ignorar el sistema existente.

---

## Aplicación por modo

### Productor

**Proyecto nuevo**: Define vision, alcance, roadmap inicial, MVP.

**Proyecto existente**: Define plan de acción, ajusta prioridades, respeta decisiones previas.

---

### Documentador

**Proyecto nuevo**: Captura lo mínimo para ordenar la visión (sin GDD completo).

**Proyecto existente**: Actualiza secciones, registra decisiones nuevas, respeta estructura.

---

### Programador

**Proyecto nuevo**: Estructura técnica base, convenciones iniciales, sistemas mínimos.

**Proyecto existente**: Análisis del sistema actual, propuesta compatible, lista de archivos a tocar.

---

### Technical Game Designer

**Proyecto nuevo**: Pilares, core loop, mecánica principal mínima, validación rápida.

**Proyecto existente**: Ajusta reglas, mejora feedback, respeta sistema, cambio mínimo.

---

## Regla central del patrón

```txt
Proyecto nuevo: Construir lo suficiente para validar.
Proyecto existente: Mejorar sin romper.

En ambos: Evitar sobrearquitectura.
```

---

## Cómo usar este patrón en futuras épicas

Cuando un modo no tenga definido claramente su comportamiento para "proyecto nuevo" vs. "proyecto existente", aplicar este patrón:

1. Definir preguntas específicas para cada contexto
2. Definir resultados esperados para cada contexto
3. Documentar anti-patrones (qué NO hacer)
4. Validar coherencia con otros modos

---

## Extensión futura

Este patrón puede expandirse para otros contextos:

- **Documento nuevo vs. existente** (aplicable a Documentador)
- **Sistema nuevo vs. existente** (aplicable a Programador)
- **Sesión de auditoría nueva vs. pendiente** (aplicable a Auditor)

Pero por ahora el patrón base es: **Proyecto nuevo vs. Existente**.
