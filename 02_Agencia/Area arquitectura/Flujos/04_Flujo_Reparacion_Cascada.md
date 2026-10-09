## Propósito

Aplicar la corrección mínima que devuelve el grafo a la ley, sobre lo que el informe de auditoría marcó.

---

## Entrada del flujo

- Un informe del `03_Flujo_Auditoria_Grafo` con la lista de fuera de ley y de notas sin camino.
- Aprobación del owner para tocar archivos.

Sin informe no hay reparación: no se repara sobre una impresión.

---

## Transformación que realiza

En este orden, de menor a mayor riesgo:

```txt
1. frontmatter        → texto plano                   (Ley 6)
2. celdas de tabla    → texto plano                   (Ley 6)
3. mitad de frase     → backticks                     (Ley 4)
4. tabla-registro     → cascada ## [[Hijo]]           (Ley 1)
5. saltos de nivel    → backticks o el indice justo   (Ley 2)
6. cruces de capa     → al puente, y declarado        (Ley 5)
7. notas sin camino   → colgadas de su indice         (corolario)
```

Cada paso se corre completo y se vuelve a medir antes de pasar al siguiente.

---

## Salida esperada / formato

```txt
## Reparaciones aplicadas
   paso — archivos tocados — links afectados
## Reparaciones que requieren decisión
   índice faltante / renombre / algo del Core
## Antes / después
   links totales, sin camino, fuera de ley, links por KB
```

---

## Criterios de aceptación

- Ninguna nota cambió lo que dice: solo dónde caen sus links.
- Ningún archivo del Core modificado sin aprobación explícita.
- Cada link convertido a backtick sigue nombrando lo mismo que nombraba.
- Ninguna reparación dejó una nota sin camino que antes lo tenía.

---

## Condiciones para avanzar

Avanza al `05_Flujo_Validacion_Pureza` cuando los siete pasos se corrieron o se declararon fuera de alcance.
No avanza si quedó una reparación aplicada a medias.

---

## Qué debe evitar

No borra notas. No renombra archivos por su cuenta. No inventa índices para colgar algo que no tiene lugar: eso se pregunta.

---

## Resultado final

El vault con la forma corregida y la lista de lo que quedó pendiente de decisión.
