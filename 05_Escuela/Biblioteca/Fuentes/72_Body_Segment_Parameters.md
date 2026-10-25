---
tipo: fuente
titulo: "Body segment parameters (cuaderno de BMClab)"
autores: Marcos Duarte (BMClab, Universidade Federal do ABC)
editorial: cuaderno Jupyter público en GitHub
anio: vivo (consultado 2026-10-05)
estado: Estudiado
mision: EST-024_Mision_Morfologia_del_movimiento
temas: masa y centro de masa por segmento: tablas de Dempster vía Winter y de de Leva, y cómo se calcula el centro de masa del cuerpo
apunta_a: 03_Masa_centro_de_masa_y_equilibrio
---

# Fuente 72 — Body segment parameters (cuaderno de BMClab)

> Fuente externa catalogada y estudiada en `EST-024`, destilada en `03_Masa_centro_de_masa_y_equilibrio`.
> **IP:** conceptos + cita, nunca texto verbatim con copyright.

## Cita

Duarte, M. *Body segment parameters*. BMClab, UFABC. https://github.com/BMClab/BMC/blob/master/notebooks/BodySegmentParameters.ipynb — reproduce la tabla 4.1 de Winter, D. A. (2009), *Biomechanics and Motor Control of Human Movement* (4ª ed., Wiley), a partir de Dempster (1955), y la tabla de de Leva, P. (1996), *Journal of Biomechanics* 29(9), 1223–1230.

## Qué es (marco aprendido)

1. **Dos modelos de segmentos, no uno.** Dempster midió cadáveres de varones mayores; de Leva ajustó a Zatsiorsky y Seluyanov, que midieron personas jóvenes vivas de los dos sexos. Difieren en cuánto pesan muslo, tronco y cabeza, y en dónde empieza y termina cada segmento.
2. **El centro de masa del cuerpo se calcula**: cada segmento aporta su fracción de masa ubicada a una fracción fija de su largo, y el total es el promedio ponderado.
3. **No se mezclan filas de tablas distintas**, porque los segmentos no se definen igual.

## Por qué le sirve a Vaultrum

Es la tabla que necesita cualquier cálculo del centro de masa de una pose, y la única fuente abierta encontrada que reproduce las dos tablas clásicas completas.

## Límites declarados

Es material de curso, no un artículo. La licencia del repositorio no se verificó; se usa como lectura de las tablas publicadas, que son las que se citan.

## Estado

**Estudiado**: alimentó `03_Masa_centro_de_masa_y_equilibrio` en `EST-024`.
