# Prompteo

Promptear en Vaultrum es pedirle a una IA con criterio: contexto suficiente, objetivo claro, límites explícitos y salida esperada definida. Un buen prompt operativo se parece a un buen requerimiento.

---

## Anatomía de un prompt operativo vaultrumita

```
Contexto      → qué hay, desde qué parte del Core se parte
Objetivo      → qué se quiere lograr, no cómo
Límites       → qué NO hacer, qué no tocar, alcance
Salida esperada → formato y criterio de "listo"
```

Esto no es nuevo: es la misma estructura que ya usan las salidas de las áreas (un RQ, un SOL, un GDS). Las áreas ya promptean bien; esta nota lo hace explícito.

---

## Las skills son prompts

Cada `SKILL.md` de un área es un prompt operativo persistente. Cuando se escribe o ajusta una skill, aplica todo lo de acá: contexto, objetivo, límites, salida, y cuidado de tokens (breve y autocontenido).

---

## Dar Vaultrum de contexto sin saturar

Dar el vault entero de contexto es caro e innecesario (ver `01_Cuidado de tokens`). En cambio:

```
Cargar el índice de la capa/área que aplica
→ desde ahí, seguir solo los links necesarios
→ incluir el Core puntual que el problema requiere
→ no arrastrar secciones que no se van a usar
```

Partir del Core (principio 1) no significa cargar todo el Core: significa cargar el criterio que aplica.

---

## Señales de buen y mal prompt

Buen prompt:

```
Parte del Core que corresponde
Objetivo claro y acotado
Límites explícitos
Salida definida
Token-eficiente (no infla contexto)
```

Mal prompt:

```
Pide "mejorá esto" sin objetivo
No declara límites
Carga contexto de más
No dice cómo se ve "terminado"
Invita a inventar fuera del Core
```

---

## Regla final

Un prompt operativo no pide magia. Pide una acción concreta, con criterio Vaultrum, dentro de un presupuesto de tokens.
