## Problema

El frame cae cuando hay muchos objetos de una misma familia en pantalla, aunque cada uno por separado sea barato.

## Área

GPU (procesamiento de vértices), con CPU si el skinning o la preparación de la geometría se resuelven del lado del procesador.

## Síntoma observable

```txt
el juego anda bien con pocos enemigos y cae con la oleada completa
bajar la resolucion casi no cambia nada
el contador de triangulos del frame sube con la cantidad de instancias
```

## Causa técnica

El costo de la geometría no es el del asset: es el de **todas sus instancias visibles**, por cada pasada que las procesa.

```txt
caras en pantalla  =  caras del asset  x  instancias simultaneas maximas  x  pasadas

pasadas  =  1 (camara)  +  cada mapa de sombra que la toca  (+ una pasada previa de
            profundidad, si el render la usa). Una luz con una sola sombra: 2. Una
            sombra en cascadas suma una por cascada; una luz puntual, hasta seis
```

```txt
goblin             817 caras
oleada             20 goblins a la vez
en pantalla        16.340 caras
con una sombra     32.680 procesadas
```

El conteo de caras de un asset, solo, no dice si es caro. Por eso la ley 4 del Área de Arte mide **en pantalla** y no en el archivo.

## Detección

```txt
contador de triangulos y vertices del frame (Stats en Unity, stat de render en Unreal)
comparar el frame con la oleada completa contra el frame con una sola instancia
arte.presupuesto(escena, familia): caras x instancias, antes de que exista el juego
```

## Diagnóstico

Se distingue de un problema de fragmentos con la prueba cruzada de `Costo de vertices y geometria`: bajar resolución no mejora; bajar la densidad de las mallas sí. Si mejora al bajar resolución, el problema son los píxeles y reducir caras no compra nada.

## Solución

```txt
presupuesto por familia      antes del primer asset: cuantas caras puede tener un
                             enemigo que aparece veinte veces (Modo Escala)
niveles de detalle           version completa cerca, reducida lejos (LOD)
caras a la silueta           reducir el interior, no el contorno (Low poly)
menos sombras                que solo proyecten sombra las instancias cercanas
instanciado                  dibujar las instancias iguales en una llamada
el diseno                    a veces la respuesta es menos instancias: es una decision
                             de Game Design, no del arte
```

## Trade-off

```txt
menos caras        silueta menos definida
LOD                saltos visibles al cambiar de nivel
sin sombra lejos   la escena pierde anclaje
```

## Validación

Comparar el frame con la oleada completa antes y después, con el mismo contador. El presupuesto de la familia se cumple **en pantalla**, no en el archivo.
