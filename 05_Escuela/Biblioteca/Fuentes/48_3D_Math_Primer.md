---
tipo: fuente
titulo: "3D Math Primer for Graphics and Game Development"
autores: Fletcher Dunn & Ian Parberry
editorial: A K Peters / CRC Press
anio: 2011 (2ª ed.)
licencia: nivel B — descatalogado; texto completo publicado libre por los autores en gamemath.com
estado: Estudiado (destilada parcialmente — alimentó 03_Matematica_del_movimiento: vectores y producto punto; matrices y quaternions siguen sin destilar)
mision: EST-009_Mision_Fuentes_Huerfanas
temas: vectores, matrices, transformaciones, espacios de coordenadas, rotación, cuaterniones
apunta_a: Área de Programación · VaultrumWorld (mundo isométrico) · 11_Camara_y_encuadre
url: https://gamemath.com/book/
---

# Fuente 48 — 3D Math Primer for Graphics and Game Development

> Libro-fuente externo, **descatalogado y publicado libre por sus autores**. Texto completo consultable sin costo.
> **IP:** conceptos + cita, nunca texto verbatim con copyright.

## Cita

Dunn, F. & Parberry, I. (2011). *3D Math Primer for Graphics and Game Development* (2ª ed.). A K Peters / CRC Press. ISBN 978-1-56881-723-1. Texto completo: https://gamemath.com/book/ (consultado 2026-08-26).

## Qué es (marco aprendido)

La introducción de referencia a la matemática que un juego 3D necesita, escrita para programadores y no para matemáticos: vectores y sus operaciones con **interpretación geométrica** antes que algebraica, matrices como transformaciones, espacios de coordenadas y cómo se pasa de uno a otro, rotación y las tres formas de representarla (Euler, matriz, cuaternión) con sus trampas.

Su aporte pedagógico es el orden: primero qué significa geométricamente, después cómo se calcula. Es lo que permite depurar un bug de transformación razonando en vez de probando signos.

## Por qué le sirve a Vaultrum (a qué apunta)

`VaultrumWorld` pasó a **3D isométrico con WASD** en `TL-006`, y `Pong3D` ya trabaja en 3D. Todo lo que sea posicionar la cámara, convertir input de pantalla a dirección de mundo, o entender por qué una rotación se comporta raro, sale de acá. La Biblioteca no tenía ni una fuente de matemática.

## Nota de licencia

**Nivel B.** El libro está fuera de catálogo y los autores publicaron el texto completo en su sitio. Se cita y se referencia; la Biblioteca no lo aloja.

## Estado y próximos pasos

- **Estudiado**, destilada **parcialmente** en `EST-014` → `03_Matematica_del_movimiento`.
- **Lo que se tomó:** vectores con interpretación geométrica, la separación posición/desplazamiento, normalización y sus trampas, el producto punto en sus tres usos.
- **Lo que NO se tomó, y es deliberado:** matrices, espacios de coordenadas, rotación y cuaterniones — o sea, todo lo 3D. `Pong3D` y `VaultrumWorld` lo van a necesitar; hoy no lo necesitan. Queda como la próxima misión del estante de Construcción, declarada en los límites del libro `03`.
- Sigue siendo además fuente de consulta directa: texto completo libre y a mano cuando aparece el problema.
