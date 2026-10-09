## Definición

La **proporción** es la relación de tamaño entre las partes de un personaje: cabeza contra cuerpo, piernas contra torso. La **estilización** es cuánto se aleja esa proporción de la real.

```txt
iconico ... caricaturesco ... estilizado ... realista
mas iconico     mas facil de leer y de identificarse con el
mas realista    mas detalle, y mas facil de caer en lo raro
```

Bancroft ordena los diseños en una escala que va de lo icónico a lo realista. McCloud explica por qué lo icónico identifica más: cuanto más simple la cara, más gente se ve en ella.

---

## Idea central

**La proporción es la identidad.** Se puede cambiar la pose, la ropa, la expresión; si cambia la proporción, es otro personaje.

```txt
los adjetivos no alcanzan    "bajito y rellenito" salio obeso: el adjetivo deja margen
                             de mas (RA-010)
se mide sobre la referencia  alto total, ancho de cabeza, ancho de torso, largo de
                             piernas, linea de suelo. La proporcion se escribe en numeros,
                             o en cabezas: "tres cabezas de alto"
```

---

## Especificación para videojuegos

```txt
la proporcion sirve a la camara   un personaje visto chico y de lejos necesita cabeza y
                                  manos grandes para leer gesto y direccion
la estilizacion es del elenco     todos en el mismo lugar de la escala; un personaje
                                  realista entre caricaturas se ve de otro juego
corregir no es restilizar         una correccion es local: "menos ancho el torso"
                                  conserva todo lo demas (RA-010, regla 2)
el generador estiliza de mas      un generador de imagen tiende al cliche: mas alto,
                                  mas esbelto, mas "lindo". El ancla del canon va primero
                                  en el encargo
```

---

## Cómo se juzga

```txt
se mide     las proporciones de la referencia maestra contra cada version: son medidas.
            En una secuencia, la escala de la silueta contra la mediana (animacion.py)
se juzga    en que lugar de la escala quiere estar el juego: es direccion de arte
```

---

## Errores comunes

```txt
Describir un personaje con adjetivos y aprobarlo a ojo.
Corregir la proporcion de una pose cambiando la del personaje.
Mezclar niveles de estilizacion en el mismo elenco.
Dejar que una version nueva "mejore" la proporcion del canon.
```

---

## Fuentes

- `64_Creating_Characters_with_Personality` — la escala de estilización.
- `51_Understanding_Comics` — lo icónico y la identificación.
- `RA-010_Animacion_identidad_y_movimiento` — Miles, los adjetivos y la corrección local.
