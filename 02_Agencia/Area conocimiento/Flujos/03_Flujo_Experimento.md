## Propósito — Caso 3: Branch experimental

Se arranca una idea que quizás es un avance en algo, sin certeza de que sirva. Este flujo la evalúa: si sirve, genera commits; si no, se descarta sin tocar el Core.

---

## Entrada del flujo

- Una branch experimental (prueba de una técnica, mecánica o enfoque no confirmado).

---

## Transformación que realiza

- El Encargado de Commits evalúa el resultado del experimento contra el criterio de commit.
- ¿Aportó algo reutilizable y confirmado? ¿O quedó en intento?
- Decide: promover o descartar.

```
Experimento cerrado
   ↓
¿Sirve y es reutilizable?
   ├── Sí → genera commits → sigue el [[02_Flujo_Aprendizaje_Branch]]
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
- Descartar no deja rastro en el Core (principio 11).

---

## Qué debe evitar

No mergear un experimento no confirmado. No guardar el intento fallido en el Core "por si acaso". No confundir una prueba con criterio establecido.

---

## Resultado final

O el experimento se confirma y entra al flujo de aprendizaje (caso 2), o se descarta limpio. El Core solo recibe lo que probó servir.
