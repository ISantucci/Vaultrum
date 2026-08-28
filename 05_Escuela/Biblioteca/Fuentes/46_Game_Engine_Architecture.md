---
tipo: fuente
titulo: "Game Engine Architecture"
autores: Jason Gregory
editorial: CRC Press / A K Peters
anio: 2018 (3ª ed.)
estado: Estudiado (destilada parcialmente — alimentó 01_Bucle_de_simulacion, 02_Colision_y_consulta_espacial, 03_Matematica_del_movimiento)
mision: EST-009_Mision_Fuentes_Huerfanas
temas: arquitectura de motor, subsistemas, gameplay foundation, bucle principal, memoria, herramientas
apunta_a: Área de Programación · 10_Input_y_respuesta
---

# Fuente 46 — Game Engine Architecture

> Libro-fuente externo. **Primer libro del estante para el Área de Programación**, que hasta ahora se apoyaba solo en documentación de motor del estante de Documentación real.
> **IP:** conceptos + cita, nunca texto verbatim con copyright.

## Cita

Gregory, J. (2018). *Game Engine Architecture* (3ª ed.). CRC Press / A K Peters. ISBN 978-1-138-03545-4.

## Qué es (marco aprendido)

El tratado completo de cómo está hecho un motor por dentro, escrito por un programador de Naughty Dog. Recorre la pila entera: capa de plataforma, gestión de memoria, sistema de recursos, render, animación, colisión y física, y la **gameplay foundation layer** — la capa donde viven las entidades, los componentes y el bucle de actualización.

Su valor para quien **usa** un motor en vez de escribirlo: explica *por qué* Unity o Godot están organizados como están. Un `Update` por frame, un sistema de componentes, un pipeline de assets y un ciclo de vida de escena dejan de ser convenciones arbitrarias y pasan a ser decisiones con razones que se pueden discutir.

## Por qué le sirve a Vaultrum (a qué apunta)

El Área de Programación consume `RQ` y `GDS` y produce `SOL` + `EJ`, apoyándose en los documentos de motor del cuarto estante (patrones de Unity, ScriptableObjects, guías oficiales). Todos esos son **específicos de un motor**. Este libro da la base agnóstica debajo, que es lo que permite decidir cuándo una recomendación de Unity es un principio y cuándo es una particularidad de Unity.

## Límites declarados

Es un libro de motores AAA y de 1000+ páginas. Se destila la **estructura de subsistemas y el ciclo de vida del frame**, no la implementación de render ni de animación, que no tienen consumidor en Vaultrum hoy.

## Estado y próximos pasos

- **Estudiado**, destilada parcialmente en la misión `EST-012` / `EST-013` / `EST-014`.
- El estante que esta ficha pedía **existe**: `ARQ-022_La_frontera_del_material_tecnico` lo abrió como quinto estante, `Construcción`. Esta ficha lo había anticipado — *"la Biblioteca todavía no tiene estante ni criterio para fundamentos de programación"*— y era correcta.
- **Lo que se tomó:** el marco de los tres relojes y el ciclo de vida del frame (`01_Bucle_de_simulacion`), el lugar del subsistema de colisión (`02`), la interpolación dentro del frame (`03`).
- **Lo que sigue sin destilar:** memoria, sistema de recursos, render, animación. Ninguno tiene consumidor en Vaultrum hoy; `EST-011` los ubica en la lista priorizada.
