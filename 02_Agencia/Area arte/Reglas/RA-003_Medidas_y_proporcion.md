# RA-003 — Medidas reales y proporcion entre assets

**Insumo:** dictado del owner, sesion 2026-09-01: *"es importante siempre usar bien medidas por si se exporta a un proyecto"*. Aplicado en la torre de arqueras.
**Estado:** Vigente.

## La regla

> Un asset se modela en **metros reales desde el primer vertice**, no se escala al final. Y su tamano no se elige en abstracto: **se elige contra un asset que ya existe en el mundo.**

Escalar al exportar rompe las normales, los modificadores y la fisica. Modelar en la escala equivocada y corregir despues es la misma deuda con un turno de demora.

## Contrato de export

```txt
1. Unidades          metros. El numero que se ve en Blender es el del motor.
2. Origen del asset  en el suelo, en el centro de la planta -> (0,0,0)
3. Transform limpio  scale (1,1,1) y rotation (0,0,0) APLICADOS en cada objeto
4. Ancla             la pieza que toca el piso es el padre (RA-001)
5. Bounding box      se declara: X x Y x Z en metros
```

El punto 3 es el que mas se olvida: una pieza rotada en el objeto (no en la malla) llega al motor con un transform que el importador puede interpretar distinto. Se verifica en una linea:

```python
sucios = [o.name for o in col.objects
          if tuple(round(v,4) for v in o.scale) != (1,1,1)
          or any(abs(a) > 1e-4 for a in o.rotation_euler)]
```

## Como se fija la proporcion

No con una tabla de tamanos ideales: **con el asset vecino y una razon funcional.**

```txt
Arbol           4.50 m   el asset de referencia, ya existia
Torre arqueras  6.47 m   1.44x el arbol
Fogata          0.93 m   0.21x el arbol
```

La torre no mide 6.47 m porque "6.47 queda bien". Mide eso porque **la plataforma esta a 3.97 m**: una arquera parada ahi tiene los ojos a ~5.6 m, por encima de la copa del arbol (4.50 m). El arma dispara sobre el bosque. La altura sale de la funcion, y el total sale de sumarle baranda y techo.

Ese es el metodo: **fijar primero la cota que la funcion exige, y derivar el resto.**

## Medidas de la torre (registro)

```txt
altura total              6.474 m
plataforma (cota util)    3.974 m
bounding box              2.90 x 2.90 x 6.474 m
cimiento                  octogono, 2.90 m de diametro,  h 0.40
fuste                     octogono, 2.60 -> 1.84 m diam, h 3.148  (conicidad 29%)
cornisa                   octogono invertido, vuela 0.20 m
plataforma                cuadrado 2.60 x 2.60 x 0.24
parapeto                  0.58 m de alto  (media altura: cubre y deja tirar)
postes                    4 x 0.18 x 0.18 x 1.248
techo                     piramide 2.90 x 2.90, h 1.25, vuela 0.15 sobre el deck
puerta                    0.78 x 1.40, apoyada sobre una cara real del fuste
separacion entre piezas   2 mm en cada junta apilada
```

## Criterio de silueta (juicio, no medicion)

Tres decisiones que hacen que se lea como torre defensiva y no como casita:

```txt
1. La piedra se afina hacia arriba (29%)   -> peso abajo, permanencia
2. La madera VUELA sobre la piedra         -> linea de sombra que separa los dos
                                              materiales, y es la matacan real
3. El techo es mas alto que ancho          -> "torre", no "choza"
```

El vuelo de la cornisa y el del techo son la misma herramienta usada dos veces: **cada cambio de material se marca con un vuelo, no con un cambio de color solo.**

Los 2 mm de junta son la unica concesion: a esta escala no se ven, y hacen que RA-002 (cero interpenetracion) se pueda verificar en una estructura apilada, donde caras coincidentes darian cruce.

## Verificacion

```txt
transform_sucio      []                      -> las 14 piezas limpias
bbox_m               [2.9, 2.9, 6.474]
base_z_m             0.0                     -> apoyada en el piso, no flotando
veredicto RA-002     EN LEY                  -> 95 caras, 133 verts, 0 cruces,
                                                0 interiores, 0 no-manifold,
                                                0 normales invertidas
```
