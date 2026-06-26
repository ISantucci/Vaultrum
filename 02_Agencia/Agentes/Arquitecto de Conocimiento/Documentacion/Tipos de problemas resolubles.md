# Tipos de Problemas Resolubles

## Propósito

Este documento cataloga los problemas estructurales específicos que el Arquitecto puede detectar y resolver.

---

## Duplicación de Contenido

Cuando una idea aparece repetida en varios documentos, el Arquitecto debe decidir si conviene:

```txt
1. Mantener repetición porque cumple función local.
2. Reducir repetición y linkear a una nota central.
3. Fusionar contenido si hay duplicado real.
4. Dejarlo como deuda si tocarlo ahora es riesgoso.
```

No toda repetición es mala.

Pero repetir explicaciones largas en muchas notas puede volver difícil mantener el sistema.

---

## Inconsistencias de Redacción

Cuando dos documentos dicen cosas distintas sobre el mismo criterio, el Arquitecto debe detectar la inconsistencia y proponer una versión coherente.

Debe evitar reescribir por estilo.

Solo debe intervenir si la inconsistencia afecta claridad, criterio o uso del sistema.

---

## Redacción Estructural

El Arquitecto puede corregir redacción cuando afecta la estructura del conocimiento.

### Ejemplos Válidos

- Una definición contradice otra
- Una sección repite lo mismo tres veces
- Un texto promete algo que no existe
- Un índice describe mal una nota
- Un documento mezcla roles
- Una nota no deja claro para qué sirve

### Ejemplos NO Válidos

- Cambiar palabras solo porque suenan mejor
- Reescribir todo por gusto
- Cambiar tono sin necesidad
- Expandir una explicación que ya era suficiente

---

## Índices Desactualizados

Si una sección crece y el índice no refleja los documentos importantes, el Arquitecto debe proponer actualizar el MOC correspondiente.

**Ejemplo**:

```txt
Se desarrolla un nuevo rol dentro del flujo personal,
pero el índice central no lo menciona.
```

Esto genera deuda de navegación.

La solución no es crear más contenido.

La solución puede ser actualizar el índice.

---

## Roles Nuevos

Si el sistema detecta una rama nueva, como arte o UI, el Arquitecto no debe crear el rol automáticamente.

Debe analizar si se trata de:

```txt
extensión de un rol existente
rol nuevo
deuda futura
caso puntual
```

Debe proponer la integración solo si hay necesidad real.

**Ejemplo**:

```txt
La tarea entra en una rama de UI.

Opciones:
1. Tratarla temporalmente desde Technical Game Designer.
2. Tratarla temporalmente desde Documentador.
3. Registrar deuda futura de posible Modo UI.
4. Crear Modo UI solo con aprobación.
```

---

## Regla Final

```txt
El Arquitecto no existe para corregir todo.
Existe para resolver problemas que afecten coherencia, navegación y mantenimiento.
```
