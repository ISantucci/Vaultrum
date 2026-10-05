## Definición

**Compresión y estiramiento** (*squash and stretch*): deformar un objeto mientras se mueve para mostrar su peso, su material y su velocidad, **conservando el volumen**.

Es el primero de la lista de Thomas y Johnston y el que la cátedra del owner anotó primero. El ejemplo de siempre: la pelota que se aplasta al tocar el piso y se estira en la caída.

---

## Idea central

```txt
volumen constante     si se aplasta en alto, se ensancha en ancho. La relacion depende
                      de las dimensiones:
                      2D   se conserva el area:    ancho = 1 / alto     0.8 -> 1.25
                      3D   se conserva el volumen: cada eje horizontal = 1 / raiz(alto)
                                                   0.8 -> 1.12 en X y en Y
lo que comunica       el MATERIAL (goma se deforma mucho, piedra nada), la VELOCIDAD
                      (estira en el cuadro mas rapido, a lo largo de la trayectoria) y
                      el IMPACTO (aplasta en el contacto)
```

Si el volumen no se conserva, no se lee deformación: se lee que el objeto **creció**.

---

## Especificación para videojuegos

```txt
el collider no se deforma    deformar el dibujo no obliga a deformar el collider. La caja
                             de colision la fija el gameplay, y un collider que se aplasta
                             en el aterrizaje cambia la fisica del salto
vuelve al reposo             en pocos cuadros. La cabeza no cambia de tamano para siempre:
                             un personaje que queda deformado cambio de identidad (`RA-010`, antes de `TL-012`)
la dosis la da el material   un personaje de madera no se estira. La dosis se escribe en la
                             guia de estilo y vale para todo el elenco
se puede hacer por codigo    escalar el sprite o el transform en el aterrizaje es barato y
                             responde al instante. En 3D por rig pide huesos que escalen o
                             formas clave; una escala no uniforme en un hueso padre se
                             propaga a todos sus hijos
UI                           el "pressed" de un boton es una compresion: una escala de 0.95
                             que vuelve
```

---

## Cómo se juzga

```txt
se mide     el alto de la silueta contra la mediana de la secuencia: animacion.py lo mide
            y marca el cuadro que se aparta. Un cuadro que deforma a proposito sube la
            tolerancia con --tol-escala, y el ART lo declara
            en motor: que el collider no cambie en el cuadro de impacto
se juzga    si el material se lee, contra la referencia maestra
```

---

## Errores comunes

```txt
Estirar sin compensar el ancho: se ve que crece.
Dejar deformacion residual: el ultimo cuadro no vuelve a la forma de reposo.
Aplicarlo a todo: el elenco entero parece de goma.
Deformar tambien el collider "para que coincida".
Estirar fuera de la direccion del movimiento.
```

---

## Ejemplo en videojuegos

Aterrizaje del jugador en un juego 2D: uno o dos cuadros de compresión (alto 0.8, ancho 1.25; en 3D, 1.12 en cada eje horizontal) y vuelta al reposo; despegue: un cuadro de estiramiento en el sentido del salto. El collider no se entera. Los números son un punto de partida para un estilo caricaturesco; un estilo realista los acerca a 1.

---

## Fuentes

- `59_The_Illusion_of_Life` — el principio y su regla de volumen.
- `60_The_Animators_Survival_Kit` — la pelota y sus variantes.
- `61_Game_Anim` — la deformación que no toca la colisión.
- `68_Apuntes_de_catedra_Animacion_2D_3D` — el primer principio anotado.
- `RA-010_Animacion_identidad_y_movimiento`, con su tabla de control previa a `TL-012` — la cabeza que no cambia de tamaño.
