# Rigging y skinning

## Qué hace Vaultrum acá

Arma el esqueleto de un personaje (rigging), asigna cuánto sigue cada vértice a cada hueso (skinning, pesos) y lo **verifica con poses antes de que exista un solo clip**. Es la frase de `RA-012` —*el rig se valida con poses antes de producir los clips*— convertida en procedimiento.

## Con qué opera la IA

En Blender, por MCP (`Blender por MCP`), con Python:

```txt
esqueleto     una armadura con nombres que espejan (.L / .R) para poder simetrizar
pesos         asignacion automatica como punto de partida, despues normalizar y
              limitar las influencias por vertice al tope de la plataforma
exportacion   solo los huesos que deforman; sin huesos "hoja" extra que agregan
              algunos exportadores; ejes y escala verificados en el archivo entregado
```

## Lo que se verifica por script, sin mirar

```txt
huesos                cuantos, contra el presupuesto de la familia (Huesos e influencias)
influencias           maximo por vertice, contra el tope
vertices sin peso     ninguno: un vertice sin peso se queda atras al moverse
suma de pesos         1 en cada vertice
simetria              los pesos de I y D se espejan
```

## La prueba de poses

Antes de animar, el personaje se lleva a las poses extremas que la animación va a pedir, y en cada una se corre `arte.malla()` sobre la malla **deformada**:

```txt
poses      brazo arriba, rodilla al maximo, torso girado, las del encargo (el saludo
           con una mano, el agachado)
se mide    solapes (un accesorio que atraviesa es un solape real, RA-009), espesor
se juzga   si el volumen se sostiene, sobre los renders de las poses
```

Si falla, se corrige **antes** de animar. Si la causa es topología, no se tapa con pesos (`Topologia para deformar`).

## Cómo pedírselo

```txt
"Rigueá <personaje> para <motor>: presupuesto <N> huesos, <K> influencias por vertice.
 Poses de prueba: <lista>. Entregame los numeros del rig y los renders de las poses."
```

## Lo que no hace

No fija el presupuesto de huesos: sale del costo en pantalla y lo decide el Optimizador del área. No anima: produce el rig que se va a animar.
