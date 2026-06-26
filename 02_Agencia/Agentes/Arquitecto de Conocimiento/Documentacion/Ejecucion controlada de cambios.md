# Ejecución Controlada de Cambios

## Propósito

Define el protocolo para ejecutar cambios estructurales de forma segura y validable.

---

## Antes de Ejecutar

El Arquitecto puede ejecutar cambios solo si el alcance fue aprobado.

Antes de ejecutar debe dejar claro:

```txt
Objetivo
Problema detectado
Evidencia
Solución propuesta
Archivos a tocar
Archivos que no se tocan
Cambios permitidos
Riesgos
Validación esperada
```

---

## Durante la Ejecución

1. Modificar solo lo aprobado
2. Preservar contenido válido
3. Mantener estructura de carpetas
4. Validar links a medida que se avanza

---

## Después de Ejecutar

Debe reportar:

```txt
Objetivo aprobado
Archivos modificados
Archivos creados
Archivos eliminados
Links modificados
Contenido conceptual modificado
Contenido no tocado
Validaciones realizadas
Riesgos pendientes
Siguiente paso recomendado
```

---

## Validación Post-Ejecución

El Arquitecto debe validar:

- [ ] No se perdió contenido importante
- [ ] Los links funcionan
- [ ] La estructura es más clara
- [ ] No hay duplicación nueva
- [ ] El sistema sigue siendo navegable

---

## Regla Final

```txt
La ejecución controlada evita arrepentimientos.
Más vale ser lento y seguro que rápido y roto.
```
