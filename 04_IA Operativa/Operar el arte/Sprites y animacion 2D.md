# Sprites y animación 2D

## Qué hace Vaultrum acá

Corre el circuito entero de una animación por cuadros: escribe el encargo, mide lo que vuelve, arma el paquete de entrega y lo lleva al motor. Es la animación que el sistema ya produjo de verdad: Miles.

## El circuito

```txt
1  el encargo      lo escribe el Area de Arte con las doce lineas del Modo Encargo de
                   su skill. Lo corre el generador que diga 07_Despacho (Codex, para
                   secuencias)
2  la medicion     lo que vuelve se mide ANTES de mirarlo:
                   animacion.py <carpeta> --gif <preview.gif> [--in-place]
3  la revision     lo que el instrumento no ve —que pierna apoya, si es el mismo
                   personaje— sobre la plancha numerada, contra la referencia maestra
4  el paquete      cuadros PNG, hoja, GIF hecho DESDE los PNG, plancha de contactos y
                   manifiesto (RA-012, regla 7)
5  el motor        en la web, la hoja y su CSS o JS; en Unreal, los cuadros como sprites
                   armados en un flipbook; el filtrado de pixel art, por textura
```

El criterio de cada paso no se repite acá: está en `RA-010`, `RA-011` y `RA-012` del Área de Arte, y los principios en el Core (`Principios de animacion`).

## Lo que la IA opera

```txt
animacion.py         lienzo, alfa real, cuadros vacios, recortes, escala, paleta,
                     linea de apoyo, enlace del loop y GIF
el manifiesto        lo escribe: version de la referencia, celda, pivot, orden,
                     duracion por cuadro, loop, eventos
la memoria           cuadros x resolucion x bytes, antes de pedir (Sprites en memoria)
```

## Cómo pedírselo

```txt
pedir      "Que Codex anime <accion> de <personaje>: para <uso en el juego>, camara
            <lateral>, in-place, <N> poses."  -> el Area escribe el encargo
medir      "Medi la secuencia de <carpeta> contra su GIF, in-place."
exportar   "Arma el paquete de <accion> v<N> y dejalo listo para <motor>."
```

## Lo que no hace

No genera los cuadros: los genera el taller externo. No dice "listo para juego" si solo se comprobó la vista previa: declara el nivel de validación alcanzado (`RA-012`, regla 6).
