---
tipo: fuente
titulo: "Real-Time Collision Detection"
autores: Christer Ericson
editorial: Morgan Kaufmann / Elsevier
anio: 2004
estado: Estudiado (destilada — alimentó 02_Colision_y_consulta_espacial)
mision: EST-009_Mision_Fuentes_Huerfanas
temas: detección de colisiones, tests geométricos, colisión continua vs discreta, tunneling, estructuras de aceleración
apunta_a: 01_Pong (table-stake 2) · Área de Programación · 10_Input_y_respuesta
---

# Fuente 54 — Real-Time Collision Detection

> Libro-fuente externo. Entra por un motivo puntual y verificable: **el libro de Pong nombra un fallo y la Biblioteca no tenía ninguna fuente que lo resuelva.**
> **IP:** conceptos + cita, nunca texto verbatim con copyright.

## Cita

Ericson, C. (2004). *Real-Time Collision Detection*. Morgan Kaufmann / Elsevier. ISBN 978-1-55860-732-3.

## Qué es (marco aprendido)

El tratado de referencia sobre detección de colisiones en tiempo real: tests geométricos primitiva por primitiva, volúmenes envolventes y cuál conviene según el caso, estructuras de aceleración espacial, y la distinción que decide todo lo demás — **colisión discreta contra colisión continua**.

La discreta pregunta "¿estos dos objetos se solapan *ahora*?" y por eso falla cuando algo se mueve más de su propio tamaño en un frame: el objeto aparece de un lado y reaparece del otro sin haber tocado nada. Eso es **tunneling**. La continua pregunta "¿se cruzaron *entre* este frame y el anterior?", que es la pregunta correcta y la que cuesta más.

## Por qué le sirve a Vaultrum (a qué apunta)

`01_Pong` —el único libro del estante de Juegos, y el que ya alimentó `TL-003`— declara en su tabla de table-stakes:

> *"El fallo #1 de todo Pong implementado a las apuradas es el tunneling. Una pelota que atraviesa la paleta rompe el Pilar 5 (justicia): el jugador hizo bien y perdió igual."*

La Biblioteca nombraba el fallo y **no tenía una sola fuente que explicara cómo se resuelve**. Esta es esa fuente. Y el problema escala: a mayor velocidad de pelota —que es exactamente lo que la aceleración de `RQ-001.2` y `RQ-002.3` produce— más probable el tunneling.

## Límites declarados

Es un libro técnico denso y anterior a los motores actuales. Para Vaultrum se destila la **distinción discreta/continua y cuándo hace falta cada una**, no la implementación de estructuras de aceleración, que Unity ya resuelve.

## Estado y próximos pasos

- **Estudiado**, destilada en `EST-013` → `02_Colision_y_consulta_espacial`.
- El circuito se cerró: `01_Pong` nombraba el tunneling como su fallo número uno, `EST-009` catalogó la fuente que lo resuelve, y `EST-013` la destiló. Entre el fallo nombrado y el mecanismo escrito pasaron tres misiones.
- **Lo que se tomó:** la distinción discreta/continua, la condición exacta del tunneling, y la asimetría de la fase ancha (falsos positivos sí, falsos negativos jamás).
- **Lo que sigue sin destilar:** los tests geométricos primitiva por primitiva y las estructuras de aceleración. El motor los resuelve; el criterio de costo ya es del Core.
