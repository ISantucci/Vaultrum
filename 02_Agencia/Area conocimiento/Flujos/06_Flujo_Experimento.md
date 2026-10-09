## Propósito — Caso 3: Branch experimental

Se arranca una idea que quizás es un avance, sin certeza de que sirva. Este flujo la evalúa: si sirve, genera candidatos; si no, se descarta sin tocar el Core.

---

## Entrada del flujo

Una branch experimental —prueba de una técnica, mecánica o enfoque no confirmado— derivada por el `03_Flujo_Cosecha`.

---

## Transformación que realiza

- El Cosechador evalúa el resultado del experimento contra el criterio de cosecha.
- ¿Aportó algo reutilizable y confirmado? ¿O quedó en intento?
- Decide: promover o descartar.

```txt
Experimento cerrado
   ↓
¿Sirve y es reutilizable?
   ├── Sí → genera candidatos → sigue el `05_Flujo_Aprendizaje_Branch`
   └── No → branch descartada → cero al Core
```

---

## Salida esperada

```txt
## Experimento de <branch>
## Resultado (sirvió / no sirvió)
## Aprendizaje confirmado (si hay)
## Decisión: promover a merge / descartar
```

---

## Criterios de aceptación

- La evaluación es honesta: un experimento fallido se descarta sin culpa.
- Solo se promueve lo confirmado y reutilizable.
- Descartar no deja rastro en el Core.

---

## Qué debe evitar

No mergear un experimento no confirmado. No guardar el intento fallido en el Core "por si acaso". No confundir una prueba con criterio establecido.

---

## Resultado final

O el experimento se confirma y entra al flujo de aprendizaje, o se descarta limpio. El Core solo recibe lo que probó servir.
