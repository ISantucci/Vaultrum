## Proposito

Esta seccion organiza los comportamientos que un NPC puede ejecutar dentro del juego.

Un comportamiento representa una accion, modo o respuesta concreta.

```txt
Decision
→ elige comportamiento.

Comportamiento
→ ejecuta una intencion.

Movimiento / combate / interaccion
→ resuelven partes concretas si hace falta.
```

---

## Contenido de esta seccion

```txt
Patrullaje
Persecucion
Ataque
Huida
```

---

## [[Patrullaje]]

Comportamiento de recorrido, rutina o control de zona.

Sirve para NPCs que deben moverse entre puntos, cubrir un espacio o simular vigilancia.

---

## [[Persecucion]]

Comportamiento de acercamiento hacia un objetivo, una amenaza o una ultima posicion conocida.

---

## [[Ataque]]

Comportamiento ofensivo que permite ejecutar una accion de daño, presion o amenaza.

---

## [[Huida]]

Comportamiento evasivo que permite alejarse de una amenaza, buscar seguridad o reposicionarse.

---

## Regla de navegacion

```txt
Comportamientos
→ linkea a sus comportamientos directos.

Cada comportamiento
→ desarrolla su accion concreta.

Los comportamientos
→ no deben linkear hermanos por cercania.
```

---

## Regla final

```txt
Un comportamiento no es toda la IA.

Es una accion organizada que el NPC puede ejecutar cuando corresponde.
```