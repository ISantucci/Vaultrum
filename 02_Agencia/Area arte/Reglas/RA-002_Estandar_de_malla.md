# RA-002 — Estandar de malla low poly

**Insumo:** observado en la sesion 2026-09-01, sobre tres iteraciones del mismo arbol dirigidas por el owner.
**Estado:** Vigente, con una parte declarada como juicio.

## La regla

> Low poly no es "pocas caras". Es **pocas caras y ninguna cara de mas**: nada escondido adentro, nada dado vuelta, nada que se cruce.

## Las cinco condiciones

```txt
1. Polycount declarado        se dice el numero, no "es liviano"
2. Cero geometria interior    ninguna cara queda tapada dentro de otra pieza
3. Cero interpenetracion      dos piezas se tocan, no se atraviesan
4. Normales hacia afuera      todas, sin excepcion
5. Malla manifold             sin aristas sueltas ni bordes abiertos
```

## Como se verifica (instrumento, no ojo)

El owner no acepta "se ve bien". Cada condicion tiene una medicion que corre en Python dentro de Blender:

```txt
polycount          len(me.polygons) · len(me.vertices)
caras interiores   toda arista de la cara con mas de 2 caras vinculadas  -> debe dar 0
interpenetracion   BVHTree.overlap() entre cada par de objetos           -> debe dar []
normales           bmesh.calc_volume(signed=True) > 0                    -> uno por objeto
manifold           edges con is_manifold == False                        -> debe dar 0
```

El volumen con signo es la prueba barata de las normales: si una cara quedo invertida, el signo se va a negativo. No requiere mirar la escena.

## El truco de la separacion sin hueco

Para que dos piezas **se toquen sin atravesarse**, no se calcula la posicion: se relaja.

```txt
1. Se colocan interpenetradas a proposito
2. Se empujan de a 1 cm en la direccion que las separa
3. Se corta en el primer paso donde BVHTree.overlap() devuelve []
```

Ese primer paso es el contacto exacto. Convergio en 86 iteraciones sobre el arbol.

## El intercambio que hay que declarar

```txt
boolean union      silueta organica, fundida     PERO genera ngons en las costuras
piezas apoyadas    cero ngons, malla limpia      PERO se ve como racimo de bloques
```

Medido sobre el mismo arbol: fusionado dio 97 caras con **43 ngons**; separado dio 100 caras con **cero ngons**. El owner eligio separado. **Cual de los dos estilos prefiere en general todavia no esta dicho** — una eleccion no es una regla.

## Parametros observados

```txt
escala        metros reales (arbol: 4.5 m de alto)
origen        en la base del asset, en (0,0,0)
shading       flat
materiales    uno por familia de superficie (Corteza, Follaje), no uno por objeto
primitivas    icoesfera subdivision 1 (20 caras) · cono de 5-6 lados
```

## Lo que no esta medido

Si el estandar se sostiene al exportar a un motor: los ngons habria que triangular, y eso no se probo. **Juicio, no medicion.**
