## Definicion

Canvas rebuild es el trabajo que realiza Unity para reconstruir la informacion de dibujo de un Canvas cuando algo dentro de su jerarquia cambia.

Un Canvas no dibuja elementos sueltos: prepara un lote a partir de todo lo que contiene.

Si una parte de ese contenido cambia, la informacion asociada puede tener que rehacerse.

```txt
Un elemento cambia
→ el Canvas queda marcado como sucio
→ se recalcula informacion de la jerarquia
→ se regenera geometria
→ se vuelve a preparar el envio de dibujo
```

Conviene diferenciar dos reconstrucciones distintas.

```txt
Rebuild de layout
→ recalcula posicion y tamaño
→ lo disparan cambios de estructura, de texto,
  de tamaño o componentes de layout
```

```txt
Rebuild de geometria y batch
→ regenera vertices, colores y agrupacion de dibujo
→ lo disparan cambios visuales: color, sprite,
  relleno, alpha, texto
```

El costo no depende solamente de que elemento cambio.

Depende de cuanta jerarquia queda involucrada en ese cambio.

---

## Responsabilidad de esta nota

No existe para pedir que la UI cambie lo menos posible.
No existe para repetir que la UI no deberia actualizarse sin motivo.
No existe para prohibir barras, contadores o animaciones de interfaz.
No existe para convertir la cantidad de Canvas en una metrica.

Su responsabilidad es explicar el mecanismo del rebuild y el costo por jerarquia:

```txt
¿Cuanta UI se reconstruye cuando cambia un solo elemento?
```

El foco esta en la relacion entre cambio y alcance:

```txt
que dispara el rebuild
que tipo de rebuild dispara
cuanta jerarquia arrastra
cuantas veces por segundo ocurre
cuanto de ese trabajo cae en CPU y cuanto en GPU
```

La nota hermana sobre UI actualizada innecesariamente trata la frecuencia con la que la interfaz trabaja sin motivo.

Esta trata el alcance del trabajo cuando la actualizacion si tiene motivo.

---

## Sintomas

Sintomas comunes:

```txt
Costo de UI que no baja aunque cambie poca informacion.
Frame time mayor con el HUD activo.
Spikes al abrir o cerrar paneles grandes.
Costo que crece al agregar elementos que nunca cambian.
Picos regulares asociados a un contador o un timer.
```

Un sintoma muy caracteristico:

```txt
Se agrega un marco decorativo al HUD.
Nadie lo toca durante la partida.
El costo de UI sube igual.
```

Esa es la firma del problema: el costo dejo de ser proporcional al cambio.

---

## Que parte del software suele causarlo

Suele aparecer en:

```txt
HUD unico que contiene toda la interfaz.
Canvas raiz con decenas o cientos de hijos.
Paneles ocultos que siguen dentro de la misma jerarquia.
Layouts anidados varios niveles.
Listas largas con contenido dinamico.
Barras interpoladas cuadro a cuadro.
```

Ejemplo problematico:

```csharp
private void Update()
{
    hpBar.fillAmount = Mathf.Lerp(hpBar.fillAmount, target, 0.2f);
}
```

La barra vive dentro del Canvas que contiene todo el HUD.

Cada frame que cambia el relleno, ese lote debe regenerarse.

Version que acota el alcance:

```csharp
private void Update()
{
    float next = Mathf.Lerp(hpBar.fillAmount, target, 0.2f);

    if (Mathf.Abs(next - hpBar.fillAmount) < 0.001f)
        return;

    hpBar.fillAmount = next;
}
```

Sigue habiendo rebuild mientras el valor cambia, y deja de haberlo cuando la animacion termina.

---

## Que parte del hardware o runtime afecta

La UI no es solo CPU ni solo GPU.

Costos del lado CPU:

```txt
Actualizacion de componentes.
Layout.
Rebuilds.
Generacion de texto.
Input y raycasts de interfaz.
Preparacion de batches y draw calls.
```

Costos del lado GPU:

```txt
Transparencias.
Imagenes.
Mascaras.
Overdraw.
Grandes superficies de pantalla cubiertas.
```

El rebuild pertenece principalmente al lado CPU, pero cambia lo que la GPU termina dibujando.

```txt
Rebuild
→ nueva geometria y nueva agrupacion
→ posible cambio en cantidad de draw calls
→ posible cambio en overdraw
```

Por eso el diagnostico no puede detenerse en una sola de las dos ramas.

---

## Como detectarlo

Se detecta observando que cambia, con que frecuencia y cuanta jerarquia arrastra.

Buscar especialmente:

```txt
Un solo Canvas conteniendo toda la interfaz.
Elementos dinamicos mezclados con elementos estaticos.
Textos de longitud variable que disparan layout.
Listas que se reconstruyen enteras.
Elementos ocultos con alpha en vez de desactivados.
```

Preguntas practicas:

```txt
¿Que elemento dispara el rebuild?
¿Es rebuild de layout o de geometria?
¿Cuantos elementos quedan dentro del mismo lote?
¿Cuantos de esos elementos cambian realmente?
¿El costo crece al agregar elementos que no cambian?
```

La ultima pregunta separa este problema de una UI que simplemente se actualiza de mas.

---

## Herramientas de deteccion

Herramientas utiles:

```txt
Unity Profiler
CPU Usage
Timeline
Frame Debugger
Logs de diagnostico
```

Que mirar:

```txt
Costo de rebuild de layout.
Costo de rebuild de geometria.
Cantidad de rebuilds por frame.
Cantidad de batches de UI.
Costo con HUD activo contra HUD desactivado.
```

Si la diferencia entre HUD activo y HUD desactivado es grande y la interfaz casi no cambia, el problema es de alcance y no de frecuencia.

---

## Soluciones posibles

Soluciones candidatas:

```txt
Separar canvas por frecuencia de cambio.
Sacar los elementos animados del lote estatico.
Evitar layouts automaticos donde la posicion es fija.
Reservar tamaño para textos de longitud variable.
Actualizar solo el elemento afectado de una lista.
Desactivar paneles en vez de dejarlos con alpha cero.
```

Ejemplo:

```txt
Antes:
un unico Canvas con marco, fondo, dinero, vida, wave y botones.

Despues:
un Canvas con marco y fondo,
otro Canvas con dinero, vida y wave.
```

---

## Trade-offs

Reducir rebuilds casi siempre implica reorganizar la interfaz.

```txt
Separar canvas
→ reduce el alcance de cada rebuild
→ aumenta draw calls y batches.

Evitar layouts automaticos
→ reduce recalculos
→ obliga a posicionar a mano.

Reservar tamaño de texto
→ evita layout por cambio de longitud
→ resta flexibilidad al diseño.

Reducir frecuencia de animaciones
→ menos rebuilds
→ posible perdida de suavidad percibida.
```

Ninguna de estas decisiones se justifica sola.

Se justifican contra una medicion previa.

---

## Ejemplo en videojuegos

En un Tower Defense el HUD suele contener:

```txt
Dinero.
Vida de la base.
Oleada actual.
Timer de la proxima oleada.
Marco decorativo.
Botones de torres.
```

De esa lista, casi nada cambia durante la partida.

```txt
Cambia seguido:
dinero, vida, timer.

Casi nunca cambia:
marco, fondo, iconos, layout general.
```

Si todo vive en el mismo Canvas, el timer alcanza para mantener el lote sucio de forma permanente.

```txt
Timer avanza cada frame
→ Canvas sucio cada frame
→ se regenera geometria del HUD completo
→ incluido el marco que nunca cambia
```

El trabajo util es un puñado de digitos.

El trabajo real abarca la interfaz entera.

---

## Como guia el diagnostico

Esta nota guia el diagnostico cuando el costo de UI no es proporcional a lo que cambia.

Flujo recomendado:

```txt
Sintoma:
costo alto de UI con poca informacion cambiando.

Sospecha:
rebuilds de alcance excesivo.

Medicion:
Profiler / CPU Usage / Frame Debugger / HUD activo contra HUD desactivado.

Dato esperado:
rebuilds frecuentes sobre jerarquias grandes.

Problema confirmado:
un cambio pequeño arrastra una reconstruccion grande.

Solucion candidata:
separar por frecuencia de cambio y acotar el alcance.
```

La pregunta clave es:

```txt
¿El costo del cambio es proporcional al cambio?
```

---

## Errores comunes al intentar solucionarlo

Errores comunes:

```txt
Crear un Canvas por elemento.
Reducir rebuilds y disparar draw calls sin medirlo.
Suponer que el problema es GPU porque se ve en pantalla.
Ocultar paneles con alpha cero y creer que dejan de costar.
Eliminar feedback visual en vez de acotar su alcance.
```

Ejemplo de mala solucion:

```txt
Problema:
un timer mantiene sucio el HUD completo.

Decision:
cada widget del HUD pasa a tener su propio Canvas.

Resultado:
menos rebuild por lote,
mas batches, mas draw calls y mas complejidad.
```

Cambiar un problema por otro no es optimizar.

---

## Hacia donde seguir

Si todavia no se midio si el frame esta limitado por CPU o por GPU:

→ [[Diagnostico]]

Si hace falta entender el presupuesto que la interfaz esta gastando:

→ [[Fundamentos]]

Si el costo cae del lado de preparacion, layout y envio de dibujo:

→ [[CPU]]

Si el costo cae del lado de transparencias, overdraw y superficie cubierta:

→ [[GPU]]

Si el patron util es agrupar por frecuencia de cambio y acotar alcance:

→ [[Patrones transversales]]

Notas relacionadas dentro de esta rama:

```txt
UI actualizada innecesariamente
Separar canvas por frecuencia de cambio
```

---

## Checklist de diagnostico

```txt
¿Que elemento dispara el rebuild?
¿Es rebuild de layout o de geometria?
¿Cuantos elementos comparten ese Canvas?
¿Cuantos de esos elementos cambian de verdad?
¿Hay elementos estaticos dentro de un lote dinamico?
¿Hay layouts automaticos donde la posicion es fija?
¿Hay textos de longitud variable disparando layout?
¿Hay paneles ocultos que siguen en la jerarquia?
¿El costo crece al agregar elementos que no cambian?
¿Cuanto del costo es CPU y cuanto es GPU?
¿Se midio antes y despues?
```

---

## Regla final

Un cambio pequeño no deberia costar como un cambio grande.

```txt
El rebuild no se paga por elemento que cambia.
Se paga por jerarquia involucrada.
Acotar la jerarquia es acotar el costo.
```
