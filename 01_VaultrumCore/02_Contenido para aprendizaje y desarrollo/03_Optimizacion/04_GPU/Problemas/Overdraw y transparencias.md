## Definicion

Overdraw ocurre cuando el mismo pixel de la pantalla se dibuja varias veces durante un frame.

La GPU no sabe de antemano que una capa va a quedar tapada. Dibuja lo que se le mando, en el orden en que se le mando.

```txt
fondo
→ particula transparente
→ otra particula
→ UI transparente
```

Aunque al final se ve un solo pixel, la GPU proceso ese lugar varias veces.

La idea principal es:

```txt
muchas capas
× muchos pixeles
=
costo de GPU que no se ve en pantalla
```

Las transparencias son el caso tipico porque la GPU necesita combinar resultados. Un opaco escribe y tapa. Uno transparente lee lo que ya estaba, lo mezcla y escribe de nuevo.

Casos habituales:

```txt
Particulas.
Humo.
Vegetacion.
UI.
Efectos.
```

Y el dato que mas cuesta aceptar:

```txt
Una particula enorme puede tener muy pocos vertices
y aun asi ser carisima por cantidad de fragmentos.
```

Menos poligonos no significa menos GPU.

---

## Responsabilidad de esta nota

Esta nota no existe para prohibir transparencias.

Esta nota no existe para reducir particulas por reflejo.

Esta nota no existe para llevar el overdraw a cero.

Esta nota no existe para explicar el pipeline grafico completo.

Existe para diagnosticar un caso concreto: el frame se encarece porque el mismo espacio de pantalla se procesa muchas veces.

Su responsabilidad es ayudar a responder:

```txt
¿Cuantas veces se esta pintando el mismo lugar?
```

El foco no esta en la cantidad de objetos. Esta en:

```txt
cuanta pantalla cubre cada capa
cuantas capas se apilan
si esas capas necesitan ser transparentes
si el jugador percibe cada una de ellas
```

---

## Sintomas

Sintomas comunes:

```txt
Caida al aparecer explosiones o efectos.
Caida al acercar la camara a un efecto.
Caida al mirar hacia el humo o las particulas.
Bajar la resolucion mejora bastante.
El costo sube sin subir la cantidad de objetos.
La escena se ve simple y rinde mal.
```

Un patron muy caracteristico:

```txt
Particula lejos y chica
→ casi no cuesta.

La misma particula cerca y cubriendo pantalla
→ cuesta mucho mas.
```

El costo no cambio porque cambio el objeto. Cambio porque cambio cuanta pantalla ocupa.

---

## Que parte del software suele causarlo

Suele aparecer en:

```txt
Sistemas de particulas.
Efectos de impacto y explosion.
Humo, polvo y niebla.
Vegetacion con alpha.
Paneles y fondos translucidos de UI.
Decals superpuestos.
Indicadores en el piso.
Sprites grandes en 2D.
```

El patron tecnico habitual:

```txt
material transparente
+ quad grande
+ muchas instancias
+ superpuestas
```

---

## Que parte del hardware o runtime afecta

Afecta principalmente:

```txt
GPU
Fragment processing
Fill rate
Ancho de banda de memoria
```

Cada capa transparente implica leer, combinar y escribir en el buffer de color.

Tambien afecta indirectamente:

```txt
CPU
```

cuando las transparencias obligan a ordenar por profundidad y rompen agrupaciones de dibujado.

Pesa mas en hardware con poco ancho de banda.

---

## Como detectarlo

La prueba mas directa es bajar la resolucion de render y observar el frame.

```txt
Bajar resolucion
→ mejora mucho
→ el limite esta del lado de los pixeles.

Bajar resolucion
→ casi no cambia
→ buscar en geometria, draw calls o CPU.
```

Otras dos pruebas baratas: apagar las particulas y volver a medir, y acercar o alejar la camara del efecto sin tocar nada mas.

Preguntas practicas:

```txt
¿El costo aparece solo con efectos en pantalla?
¿Escala con el tamaño en pantalla o con la cantidad?
¿Cuantas capas hay en el peor caso?
¿Hay UI translucida sobre toda la pantalla?
¿Hay opacos dibujados y despues tapados?
¿Rinde bien mirando al vacio?
```

---

## Herramientas de deteccion

Herramientas utiles:

```txt
→ Frame debugger
→ Stats window
→ Unity Profiler
→ Vistas de debug de overdraw del motor
→ Herramientas de GPU profiling del fabricante
```

Que mirar:

```txt
Orden de dibujado.
Cola de render transparente.
Passes sobre la misma zona.
Materiales con blending.
Tamaño en pantalla de cada efecto.
GPU frente a CPU.
```

Recorrer el frame paso a paso convierte el overdraw en algo visible.

---

## Soluciones posibles

Soluciones candidatas dentro de la rama GPU:

```txt
LOD
Culling
Draw calls y batching
Texturas y mipmaps
```

Soluciones especificas del problema:

```txt
Reducir cantidad de particulas.
Reducir tamaño de cada particula.
Reducir lifetime de los efectos.
Recortar el area vacia de la textura.
Ajustar la geometria al contenido del sprite.
Evitar apilar efectos en el mismo lugar.
Usar opaco cuando la transparencia no aporta.
Reducir capas de UI translucida.
Limitar efectos simultaneos.
```

Y desde otras ramas:

```txt
UI orientada a eventos
Object pool como optimizacion
Reducir frecuencia de actualizacion
```

Ejemplo:

```txt
Antes:
Cada impacto crea 4 particulas grandes superpuestas.

Despues:
1 particula bien diseñada con la misma lectura visual.
```

Otro ejemplo:

```txt
Antes:
Panel de pausa translucido sobre toda la pantalla, con el juego dibujandose detras.

Despues:
Fondo opaco o congelado, sin seguir dibujando la escena completa.
```

---

## Trade-offs

```txt
Menos particulas
→ menos overdraw
→ menos impacto visual.

Particulas mas chicas
→ menos fragmentos
→ efecto menos vistoso.

Material opaco
→ mas barato
→ bordes menos suaves.

Geometria ajustada al sprite
→ menos pixeles vacios
→ mas trabajo de arte.

Limitar efectos simultaneos
→ techo de costo previsible
→ picos menos espectaculares.
```

El efecto visual es feedback. Optimizar overdraw no deberia borrar la respuesta del juego.

---

## Ejemplo en videojuegos

En un Tower Defense:

```txt
Explosiones al morir cada enemigo.
Efectos de disparo en cada torre.
Rango de torre dibujado en el piso.
Niebla ambiental sobre el mapa.
HUD translucido con dinero, vida y wave.
```

Con una wave grande:

```txt
30 enemigos mueren juntos
→ 30 explosiones superpuestas
→ sobre la niebla
→ sobre los rangos en el piso
→ debajo del HUD translucido
```

El mismo pixel del centro puede terminar procesado seis o siete veces, con la misma cantidad de triangulos que hace un segundo.

Una solucion sana:

```txt
Explosion mas chica y mas corta.
Un solo rango de torre visible por vez.
Niebla mas liviana.
Fondo de HUD opaco donde no aporta ver a traves.
```

---

## Como guia el diagnostico

Flujo recomendado:

```txt
Sintoma:
caida al aparecer efectos o al acercar la camara.

Sospecha:
overdraw por capas transparentes.

Medicion:
bajar resolucion y comparar.

Dato esperado:
mejora clara al bajar resolucion.

Confirmacion:
Frame debugger muestra muchas capas sobre la misma zona.

Solucion candidata:
reducir cantidad, tamaño o duracion de las capas.
```

La pregunta clave es:

```txt
¿Cuantas veces se pinta el mismo pixel y cuantas de esas veces se perciben?
```

---

## Errores comunes al intentar solucionarlo

```txt
Bajar poligonos cuando el problema es de pixeles.
Eliminar efectos en vez de ajustarlos.
Reducir particulas sin medir si eran la causa.
Pasar todo a opaco y romper la lectura visual.
Ignorar la UI translucida.
Medir en una escena que no es el peor caso.
No volver a medir despues.
```

Ejemplo de mala solucion:

```txt
Problema:
El juego cae en las explosiones.

Solucion:
Se sacan las explosiones.

Resultado:
El frame mejora y el jugador deja de entender que mato al enemigo.
```

Se optimizo el numero y se rompio el feedback.

---

## Hacia donde seguir

Si hace falta entender por que el costo esta en los pixeles:

→ [[Fundamentos]]

Si hace falta confirmar que el frame esta limitado por GPU:

→ [[Diagnostico]]

Si la UI translucida aparece como sospechosa:

→ [[UI]]

Si las particulas ademas se crean y destruyen todo el tiempo:

→ [[CPU]]

Si las texturas de los efectos son enormes:

→ [[Memoria]]

Si el efecto se instancia al cargar una wave:

→ [[Carga e IO]]

Herramientas para confirmar:

```txt
→ Frame debugger
→ Stats window
→ Unity Profiler
```

Notas hermanas de esta rama:

```txt
→ Fill rate y resolucion
→ Costo de fragmentos y shaders
→ Post processing pesado
```

---

## Checklist de diagnostico

```txt
¿El costo aparece solo con efectos en pantalla?
¿Bajar resolucion mejora mucho el frame?
¿El costo escala con el tamaño en pantalla?
¿Cuantas capas hay en el peor caso?
¿Las particulas se superponen entre si?
¿La textura tiene mucha area vacia?
¿La geometria del sprite esta ajustada?
¿Hay UI translucida sobre toda la pantalla?
¿Hay opacos dibujados y despues tapados?
¿Se probo apagando las particulas?
¿Se reviso el frame paso a paso?
¿Se mantiene el feedback del jugador?
¿Se comparo antes y despues?
```

---

## Regla final

El overdraw no se mide en objetos. Se mide en capas sobre el mismo lugar.

```txt
Un objeto con pocos vertices
puede cubrir media pantalla.
La GPU no cobra por triangulo.
Cobra por pixel procesado.
```
