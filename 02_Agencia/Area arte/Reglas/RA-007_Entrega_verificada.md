# RA-007 - Entrega con contrato: nombres, cotas medibles y verificacion del archivo

**Insumo:** pedido del owner, figura humana en `.glb` con nombres de malla exactos e
innegociables. **Estado:** Vigente.

## Regla 1 - el contrato del cliente manda sobre la convencion interna

`RA-004` dice que todo objeto lleva el prefijo de su asset (`Voyage_Techo`). Este
pedido exige `cabeza`, `pecho`, `biceps`... **sin prefijo**, porque son las claves con
las que el owner va a pintar cada musculo.

```txt
Convencion interna   ordena el .blend
Contrato de entrega  ordena el archivo que sale
Cuando chocan, gana el contrato -- y el choque se declara.
```

## Regla 2 - una especificacion medible se AJUSTA, no se afirma

El pedido decia **1,75 m y 75 kg**. Las dos son medibles y ninguna se declaro a ojo:

```txt
altura  ->  z maximo de la malla                      = 1.7500 m   exacto
masa    ->  volumen x densidad corporal (1050 kg/m3)  = 75.00 kg   ajustado
```

La masa no se estima: se **resuelve**. El volumen escala con el cuadrado del factor
transversal, asi que el factor sale de una raiz, se aplica y se vuelve a medir.

```txt
K = sqrt( (75 / 1050) / V_medido )
```

Tres pasadas hicieron falta, y cada una la disparo una medicion, no una impresion:

```txt
1. seccion eliptica         62.3 L -> 65.4 kg   (13% liviano)
2. superelipse (exp 0.80)   66.0 L              +6% de area por seccion
3. K transversal 1.0407     71.4 L -> 75.00 kg  clavado
```

**Lo que ninguna cota captura, hay que medirlo aparte.** Con la masa clavada, el
bideltoideo dio 0.520 m: razon 0.297 de la altura contra 0.26-0.28 de un atletico
delgado. Se angosto de z=1.12 para arriba y la masa se recupero en PROFUNDIDAD, no
en ancho. Despues el torax/cintura daba 0.90 (recto): se afino la cintura y se abrio
el torax con un factor por altura.

```txt
                 medido      referencia atletico delgado
altura           175.0 cm    -
masa              75.00 kg   -
bideltoideo       48.7 cm    razon 0.278  (0.26-0.28)   OK
torax             92.4 cm    90-98                      OK
cintura           75.6 cm    73-80                      OK
cadera            96.6 cm    92-98                      OK
muslo             53.0 cm    50-56                      OK
pantorrilla       39.6 cm    36-38                      2 cm de mas
cintura/torax     0.818      0.80-0.85                  OK
```

**Truco de escalado que vale registrar:** un factor que depende SOLO de la altura
-`f(z)` aplicado a x e y- no rompe ninguna luz de junta, porque las dos piezas de
cada junta comparten la misma z y se escalan igual. Permite reesculpir la silueta sin
volver a resolver las 66 colisiones.

## Regla 3 - el .glb se verifica LEYENDO el .glb

No alcanza con que el exportador no tire error. Dos defectos reales aparecieron solo
al parsear el archivo, y los dos habrian arruinado la entrega:

```txt
1. "core.001"  Las mallas de la construccion ANTERIOR quedaron huerfanas en
               bpy.data con el nombre exacto tomado. Las nuevas salieron con
               sufijo .001 y el contrato de nombres se rompio en silencio.
               -> purgar mallas con users == 0 ANTES de renombrar.

2. "Cube"      El Cube de la escena por defecto seguia SELECCIONADO en su propia
               view layer, en OTRA escena. El exportador con use_selection lo
               levanto igual. -> deseleccionar en TODAS las view layers del archivo.
```

Ninguno se ve en Blender. Los dos se ven leyendo el binario.

## Que se verifica en un .glb (sin decodificar el binario)

El chunk JSON del `.glb` ya trae todo: nombres, contadores y el bounding box de cada
malla en `accessors[].min/max`.

```txt
[ ] meshes y nodes == la lista exacta pedida, sin faltantes ni sobrantes
[ ] animations / skins / cameras / images == 0
[ ] materials == los declarados
[ ] bbox Y: pies en 0.0 y altura exacta
[ ] bbox X centrado en 0
[ ] orientacion: centro Z de "pecho" NEGATIVO y el de "espalda" POSITIVO -> mira a -Z
[ ] triangulos y tamano contra el limite del pedido
```

El eje es la trampa silenciosa: Blender exporta con **+Y arriba**, y la conversion es
`(x, y, z)_blender -> (x, z, -y)_gltf`. **Para que la figura mire a -Z en el .glb hay
que modelarla mirando a +Y en Blender.** Se comprueba con las dos piezas que ya
existen: el pecho tiene que quedar en Z negativo y la espalda en Z positivo.

## Regla 4 - la banda horizontal miente sobre un miembro inclinado

Medir un perimetro juntando los vertices dentro de `|z - z0| < tol` funciona en el
torso y **falla en un brazo en pose A**: la banda toma dos anillos a distinta altura de
un cilindro inclinado y el ancho sale inflado.

```txt
brazo medido por banda horizontal   38.5 cm   (falso)
brazo por su anillo real            34.7 cm
```

Sobre un miembro inclinado se mide **en el plano del anillo**, no en el plano del piso.
