## Que es

La calidad de un analisis no puede superar la calidad de su telemetria. Esta nota dice que se instrumenta, como se nombra, que contexto lleva, como se verifica antes de creerle a un tablero y que no se recolecta nunca.

El principio que la ordena entera:

```txt
minima instrumentacion suficiente
  se instrumenta solo lo necesario para
    medir el objetivo
    diagnosticar las fallas razonables
    validar la calidad del dato
```

No se instrumenta cada click "por las dudas". Menos eventos es menos costo, menos cardinalidad, menos complejidad, mas privacidad y tableros que se leen.

---

## El presupuesto depende de la fase

En las fases donde rige el playtest —prototipo, produccion, testing— el tope lo fija el libro `13_Playtesting_y_validacion` de la Biblioteca, que es el dueno de ese territorio: **diez eventos activos como maximo, uno por pregunta de diseno**, en CSV local con id de sesion anonimo. Esta nota no lo pisa: lo aplica.

Cuando el producto pasa a soft launch o a lanzamiento, el presupuesto cambia porque cambia la pregunta, y el plan de medicion lo declara con su razon. Pasar de diez eventos a sesenta no es una evolucion natural: es una decision que se escribe.

---

## Categorias de eventos

```txt
sesion           session_start · session_end
progresion       start · fail · complete
recurso          source · sink
negocio          purchase · refund · transaction_validated
anuncios         impression · click · rewarded_completion
diseno/custom    interacciones con features · decisiones del jugador · pasos de tutorial
error/rendim.    crash · exception · FPS · memoria · tiempo de carga · latencia
```

---

## Diseno de un evento

Un evento representa **una accion o un cambio de estado relevante**, y lleva los parametros que la pregunta necesita:

```txt
mission_completed
  mission_id · world_id · difficulty · attempts · duration_seconds · player_level
```

Nombres consistentes, descriptivos, versionables, sin informacion personal y **sin valores dinamicos dentro del nombre**:

```txt
bien   level_completed    con  level_id = forest_03
mal    level_completed_forest_03_2026_09_25_user_12345
```

El segundo convierte cada partida en un evento distinto: ningun tablero puede agruparlos y ningun analisis puede contarlos.

---

## Cardinalidad

La cantidad de valores distintos que puede tomar un nombre o un parametro. Duele en rendimiento, costo, tableros e interpretabilidad.

No se meten como categorias: timestamps, coordenadas crudas, ids procedurales, texto libre, ids de usuario en el nombre del evento. Se agrupa cuando es razonable: una coordenada se vuelve una zona, un tiempo se vuelve un rango.

---

## Contexto minimo de cada evento

Segun el stack, se captura o se deriva:

```txt
timestamp del evento · id de jugador PSEUDONIMO · id de sesion · version del juego
· plataforma · build · entorno (dev / test / prod) · grupo de experimento
· contexto de progresion
```

Sin la version y el entorno, un evento de una build de prueba contamina los datos de la real, y la contaminacion parece un cambio de comportamiento.

---

## Cliente o servidor

Lo sensible al fraude se valida del lado del servidor cuando hay infraestructura: compras, recompensas valiosas, resultados competitivos, grants de moneda. Las compras usan validacion de recibo cuando se puede. Un evento de cliente es una declaracion del cliente, y el cliente puede mentir.

---

## Verificar el evento antes de creerle al tablero

```txt
dispara                      dispara una sola vez
en el momento correcto       con los parametros correctos y del tipo correcto
en el entorno correcto       con la version correcta
no duplica                   no se pierde
source y sink con su signo   la transaccion con su moneda y su precio
identidad consistente        de jugador y de sesion
el consentimiento se respeta
```

Esta verificacion la ejecuta quien verifica lo construido —Calidad— contra criterios que escribe quien disena la medicion. Un tablero sobre eventos sin verificar es un informe sobre el comportamiento del codigo de telemetria.

---

## Observar el pipeline

Una anomalia de telemetria **parece** un cambio de comportamiento. Se vigila:

```txt
volumen de eventos · eventos invalidos · eventos faltantes · duplicados
· cambios de esquema · picos y caidas bruscas · huecos por version
· contaminacion entre entornos
```

Si el DAU cae 40% el mismo dia que salio una version, la primera hipotesis no es el jugador: es el evento.

---

## Privacidad por diseno

```txt
minimizacion de datos · limitacion de proposito · consentimiento cuando corresponde
· opt-out cuando corresponde · mecanismo de borrado · politica de retencion
· acceso restringido · nada de datos personales sin necesidad legitima
```

Las obligaciones dependen de la jurisdiccion, la audiencia, la edad, la plataforma y el SDK. Este criterio **no reemplaza una revision legal**. En cualquier SDK de analytics —Unity Analytics, GameAnalytics u otro— el consentimiento, los eventos automaticos, los limites de cardinalidad y la sintaxis se verifican contra su documentacion vigente antes de implementar: los conceptos de esta nota son agnosticos de proveedor, los detalles del proveedor no.

---

## Regla final

```txt
Cada evento justifica su existencia con una pregunta.

Un evento sin pregunta es costo.
Un evento sin verificar es una opinion del codigo.
Un evento con datos personales que nadie necesitaba es un riesgo que alguien firmo sin leer.
```
