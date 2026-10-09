## Definición

**Exageración**: llevar una pose, una acción o una expresión más allá de lo real para que se lea con claridad. No es distorsionar: es **hacer evidente lo que ya estaba**.

---

## Idea central

```txt
lo realista, a escala de pantalla, no se lee
lo exagerado se lee, si se exagera lo que comunica
```

Un juego muestra a su personaje chico, lejos y en movimiento. Lo que en primer plano es sutil, a 60 px es invisible. Por eso en un juego exagerar es casi siempre **legibilidad**, no estilo.

---

## Especificación para videojuegos

```txt
se exagera lo que comunica     exagerar la rodilla no obliga a alargar la zancada (`RA-010`, antes de `TL-012`)
sin cambiar la categoria       una caminata exagerada sigue siendo caminata; si gana vuelo,
                               paso a ser carrera
sin cambiar la identidad       exagerar no es redisenar: Miles salio estilizado de mas en un
                               ciclo correcto
la dosis minima suele alcanzar la catedra lo dejo con numeros: un +5% de escala, un cambio
                               breve de opacidad, un desplazamiento chico, un temblor de
                               pocos cuadros. Es suficiente para que algo llame la atencion
                               (microanimaciones)
la dosis es del estilo         cuanto se exagera se escribe en la guia de estilo y vale
                               para todo el elenco
```

---

## Cómo se juzga

```txt
se mide     que la exageracion no cambie el tamano del personaje: escala de la silueta
            estable contra la mediana (animacion.py), con la tolerancia declarada en los
            cuadros que deforman a proposito
se juzga    a escala real y contra la referencia maestra: si se lee, y si sigue siendo el
```

---

## Errores comunes

```txt
Exagerar todo: nada destaca.
Exagerar la parte que no comunica.
Cambiar la categoria de la accion.
Corregir una pose exagerada cambiando proporciones del personaje.
Una microanimacion tan grande que ya es una animacion.
```

---

## Fuentes

- `59_The_Illusion_of_Life` — el principio.
- `61_Game_Anim` — legibilidad a distancia de juego.
- `68_Apuntes_de_catedra_Animacion_2D_3D` — exageración en 2D avanzada y las microanimaciones.
- `RA-010_Animacion_identidad_y_movimiento`, con su tabla de control previa a `TL-012` — la rodilla, la zancada y el personaje estilizado de más.
