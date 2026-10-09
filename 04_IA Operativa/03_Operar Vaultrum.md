# Operar Vaultrum

Cómo una IA debe operar el vault cuando lo tiene de contexto. Es el manual mínimo de conducta, alineado con la identidad y los principios del Core.

---

## Reglas de operación

```
1. Partir del Core (principio 1) — el criterio sale del Core, no de ocurrencias.
2. Cargar por índices — leer el índice que aplica y seguir solo lo necesario (cuidado de tokens).
3. No inventar (principio 2) — usar conocimiento real; si no está en el Core, decirlo.
4. Declarar límites (principio 9) — si el problema excede el Core, marcarlo, no aparentar certeza.
5. Validar antes de ejecutar (principio 10) — entender problema y objetivo antes de producir.
6. No repetir el Core — referenciar, no duplicar (cuidado de tokens + principio 6).
7. Separar responsabilidades — usar el área/capa que corresponde, no absorber roles.
```

---

## Flujo de una IA operando Vaultrum

```
Pedido
→ identificar qué capa/área aplica
→ cargar su índice (no todo el vault)
→ traer el criterio puntual del Core
→ trabajar dentro de ese criterio
→ declarar límites si el Core no alcanza
→ producir la salida en el formato esperado
```

---

## Qué NO debe hacer una IA operando Vaultrum

```
Cargar el vault entero sin necesidad
Inventar patrones o teoría fuera del Core
Repetir contenido que ya vive en el Core
Aparentar certeza sin base
Absorber responsabilidades de otras áreas
Producir sin entender el objetivo
```

---

## Reglas de git (política del repositorio)

Operar el vault incluye tocar su repositorio, y eso tiene límites duros. **No son de ningún área**: son conducta de quien opera, igual que las reglas de arriba. Vivían en el Área de Conocimiento por un accidente de su metáfora —se llamaba *control de versiones* y se le colgó el control de versiones literal— y ahí no tenían nada que ver con el conocimiento.

```
1. A `main` integra SOLO la persona. La IA nunca mergea ni pushea a main.
2. Trabajando sobre `main`, no se crean branches nuevas ni se commitea antes
   de que exista una implementación.
3. Se puede stagear, commitear y pushear la branch de trabajo. Eso es el
   seguro de vida: que el trabajo hecho no se pierda.
4. Ante la duda sobre tocar el árbol de git, la IA se detiene y le pasa la
   decisión a la persona.
```

**Cuándo se commitea un proyecto** no lo decide quien opera: lo declara el Área de Producción con el `VE` en Cerrado. La verificación previa —si lo hecho está bien— es del **Área de Control de Calidad**: su `QA` en GO o CONDITIONAL GO es lo que habilita al `VE` a cerrar. El gate de forma corre solo en `.git/hooks/pre-commit` y es del Área de Arquitectura: un commit que deja el grafo fuera de ley no entra.

El commit es además el intervalo del Pass GC: ver `04_Pass GC de contexto`.

---

## Regla final

Vaultrum no reemplaza el criterio de la IA: le da una base. La IA opera mejor cuando parte del Core, gasta tokens con cuidado y declara lo que no sabe.
