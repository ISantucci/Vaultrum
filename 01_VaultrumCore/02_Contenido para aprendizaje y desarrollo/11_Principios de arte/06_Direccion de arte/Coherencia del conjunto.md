## Definición

La **coherencia del conjunto** es que todos los assets de un juego parezcan del mismo juego: la misma mano, la misma luz, la misma densidad, el mismo movimiento.

Es la única propiedad del arte que **no se puede juzgar asset por asset**.

---

## Idea central

```txt
cada asset aprobado por separado     puede dar un conjunto incoherente
el conjunto aprobado junto           obliga a cada asset a parecerse a sus vecinos
```

El goblin cerró en ley las leyes de la malla —1, 2 y 3— y trajo diez materiales nuevos contra los treinta que ya había. Ningún instrumento de malla lo vio, porque el color no es una ley de la malla. Es el caso que creó la silla del `05_Guardian_Visual`: **la única que mira el conjunto y no la pieza**.

---

## Qué se mira

```txt
paleta               los colores nuevos que trae cada asset
densidad de detalle  un asset muy detallado entre assets simples se ve de otro juego
densidad de textura  los pixeles de textura por metro: uno nitido al lado de uno borroso
escala               todos contra la dimension maestra
grosor de linea      si el estilo tiene contorno
estilizacion         todos en el mismo lugar de la escala
movimiento           los mismos dibujos por segundo, la misma dosis de exageracion
```

---

## Especificación para videojuegos

```txt
un asset nuevo entra contra sus vecinos   no contra una muestra suelta
se mira en una alineacion                 todos los assets juntos, a escala, en el
                                          ambiente real: una "line-up"
el conjunto se mide en cada cierre        antes de cerrar un ART-XXX (gate de Conjunto)
```

---

## Cómo se juzga

```txt
se mide     censo de paleta del conjunto (arte.paleta()), escalas contra la dimension
            maestra, costo en pantalla del set completo (arte.presupuesto()): el gate de
            Conjunto del Area de Arte
se juzga    la line-up: si parecen del mismo juego
```

---

## Errores comunes

```txt
Aprobar cada asset en su propia escena.
Sumar un asset de una libreria externa sin pasarlo por la paleta y la densidad.
Medir el conjunto recien al final, cuando ya hay cuarenta assets que corregir.
```

---

## Fuentes

- `62_Color_and_Light` — luz y color como unidad de una imagen.
- `64_Creating_Characters_with_Personality` — la line-up de un elenco.
- Área de Arte: ley 5, `05_Guardian_Visual`, Modo Pasada y el gate de Conjunto.
