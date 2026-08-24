## Propósito

Transformar un diagnóstico técnico en una **solución técnica validada** (`SOL-XXX.n`), SOLID, expansible y coherente con el proyecto y el Core, aprobada antes de ejecutar. Es el gate del área.

---

## Entrada del flujo

- Diagnóstico técnico del [[01_Flujo_Analisis_Tecnico]].
- Conocimiento del Core aplicable ya identificado.

Si el diagnóstico no trae contexto real suficiente, no avanza: vuelve al Analista.

---

## Transformación que realiza

- Define la arquitectura de la solución (clases, servicios, managers, datos).
- Aplica separación de responsabilidades: estructura / algoritmo / consumidor.
- Decide qué patrones y criterios del Core se usan y por qué.
- Define parámetros configurables (no hardcodear gameplay/balance).
- Lista archivos a tocar/crear y alternativas descartadas.
- Verifica la numeración disponible antes de asignar `SOL-XXX.n`.

---

## Verificación de numeración

`SOL-XXX.n` hereda el número base y la subnumeración del `RQ-XXX.n` que resuelve. Revisar [[00_Indice_soluciones]] antes de registrar. No inventar numeración.

---

## Salida esperada / formato

```txt
## SOL-XXX.n — Título
## Requerimiento asociado (RQ-XXX.n / GDS-XXX.n / LDS-XXX.n / UXS-XXX.n)
## Solución propuesta (arquitectura)
## Separación de responsabilidades
## Conocimiento del Core aplicado
## Parámetros configurables (Unity)
## Archivos a tocar / crear
## Alternativas descartadas
## Riesgos
## Criterios de validación
## ¿Apruebo este alcance para ejecutar?
```

---

## Criterios de aceptación

- La solución cumple el requerimiento con la menor complejidad razonable.
- Aplica SOLID y separación de responsabilidades.
- Usa el conocimiento del Core cuando corresponde.
- No hardcodea valores de gameplay/balance.
- Queda expansible y mantenible.
- Tiene `SOL-XXX.n` asignado y linkeado a su `RQ`.

---

## Condiciones para avanzar

Avanza al [[03_Flujo_Ejecucion]] **solo con aprobación explícita del alcance**.
No avanza sin OK. Si el diagnóstico era insuficiente, rebota al Analista.

---

## Qué debe evitar

No escribe la implementación final. No inventa arquitectura si ya hay una sana. No crea managers/capas por gusto. No propone refactors grandes para problemas chicos.

---

## Resultado final

Una `SOL-XXX.n` registrable y aprobada, lista para ejecutarse sin reinterpretar.
