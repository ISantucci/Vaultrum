## Definicion

Separar canvas por frecuencia de cambio es agrupar la interfaz segun cada cuanto se modifica cada elemento, no segun donde aparece en pantalla.

La idea principal es:

```txt
UI estatica
→ un lote que casi nunca se reconstruye

UI altamente dinamica
→ un lote que se reconstruye seguido
```

El criterio de agrupacion es uno solo:

```txt
¿Cada cuanto cambia este elemento?
```

No es la ubicacion en pantalla.

No es la jerarquia visual del diseño.

No es la pertenencia a un mismo panel.

Dos elementos que se ven pegados pueden pertenecer a lotes distintos, y dos elementos alejados pueden compartir lote si comparten frecuencia.

---

## Que problema ayuda a prevenir

Ayuda con:

```txt
Canvas rebuild de alcance excesivo.
Costo de UI desproporcionado respecto de lo que cambia.
Frame time mayor con el HUD activo.
Picos regulares producidos por timers o contadores.
Costo que crece al agregar decoracion que nunca cambia.
```

Lo que ataca es el alcance, no la frecuencia.

```txt
Antes:
un elemento cambia
→ se reconstruye la interfaz entera

Despues:
un elemento cambia
→ se reconstruye solo el lote dinamico
```

---

## Como funciona

Cada Canvas prepara su propio lote de dibujo.

Cuando algo dentro de un Canvas cambia, el trabajo de reconstruccion queda contenido dentro de ese Canvas.

```txt
Canvas A cambia
→ se reconstruye A
→ B y C quedan intactos
```

El procedimiento es directo.

```txt
1. Listar los elementos de la interfaz.
2. Anotar cada cuanto cambia cada uno.
3. Agrupar por frecuencia parecida.
4. Dar un Canvas a cada grupo.
5. Medir antes y despues.
```

Una clasificacion suficiente para empezar:

```txt
Nunca cambia
→ fondos, marcos, separadores, titulos fijos.

Cambia por evento
→ dinero, vida, oleada, estado de botones.

Cambia por frame
→ timers, barras interpoladas, medidores continuos.
```

Tres grupos suelen alcanzar.

Un cuarto grupo debe justificarse con una medicion, no con una intuicion.

---

## Como aplicarlo en videojuegos

Aplicaciones tipicas:

```txt
HUD de combate.
Barras de vida y de energia.
Contadores de recursos.
Timers y cuentas regresivas.
Indicadores de progreso.
Minimapas.
Paneles de estado persistentes.
```

Ejemplo en un Tower Defense:

```txt
Canvas estatico
    marco del HUD
    fondo del panel inferior
    iconos de las torres
    titulo de la wave

Canvas por evento
    dinero
    vida de la base
    numero de oleada

Canvas continuo
    timer de la proxima oleada
    barra de progreso de la wave
```

El timer avanza todos los frames, pero ahora arrastra unicamente su propio lote.

```txt
Antes:
el timer mantiene sucio el HUD completo.

Despues:
el timer mantiene sucio un lote de dos elementos.
```

El marco decorativo pasa a costar una vez y despues deja de aparecer en el perfil.

---

## Relacion con arquitectura

Se relaciona con:

```txt
UI orientada a eventos.
Separacion de responsabilidades.
Frecuencia de actualizacion como criterio de diseño.
Composicion de la escena de interfaz.
```

Conviene que la estructura de canvas sea explicita y este documentada.

```txt
Cada Canvas
→ un proposito
→ una frecuencia
→ un responsable claro
```

Una interfaz sana mantiene esa separacion visible.

```txt
Si un elemento nuevo se agrega al HUD,
la pregunta previa es a que lote pertenece.
```

Cuando esa pregunta no se hace, la separacion se degrada sola en pocas semanas de trabajo.

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
CPU
Frame Budget
Sistema de UI
```

Reduce:

```txt
Cantidad de elementos involucrados en cada rebuild.
Costo de layout sobre jerarquias grandes.
Regeneracion de geometria que nadie modifico.
```

Aumenta:

```txt
Cantidad de lotes de dibujo.
Cantidad de draw calls.
Cantidad de batches enviados por frame.
```

Ese aumento es el precio de la separacion y es medible.

```txt
Menos trabajo de reconstruccion
↔
mas trabajo de envio
```

La separacion conviene mientras el primer termino baje mas de lo que sube el segundo.

---

## Cuando conviene usarlo

Conviene cuando:

```txt
Hay un HUD persistente con elementos de frecuencias muy distintas.
Hay decoracion fija conviviendo con elementos animados.
Hay timers, barras o medidores continuos.
El costo de UI no baja aunque cambie poca informacion.
El costo crece al agregar elementos que nunca cambian.
La medicion muestra rebuilds sobre jerarquias grandes.
```

Casos claros:

```txt
HUD de combate con marco decorativo.
Barra de progreso dentro de un panel de estado.
Contador de tiempo sobre un fondo elaborado.
```

---

## Cuando NO conviene usarlo

No conviene cuando:

```txt
La interfaz es pequeña y ya es barata.
Todos los elementos cambian con frecuencia parecida.
El juego esta limitado por envio de dibujo y no por reconstruccion.
No hay medicion que sostenga la separacion.
La interfaz aparece un instante y desaparece.
```

Y hay un limite explicito:

```txt
Separar por frecuencia
≠
un Canvas por elemento
```

Un Canvas por elemento es el otro extremo.

```txt
Un Canvas por elemento
→ casi ningun rebuild compartido
→ muchos lotes
→ mas draw calls
→ mas batches
→ mas complejidad de escena
```

Eso cambia un problema por otro.

---

## Trade-offs

Ventajas:

```txt
Rebuilds acotados a lo que realmente cambia.
Costo de UI proporcional al cambio.
Decoracion que deja de pagarse por frame.
Perfil de interfaz mas facil de leer.
```

Costos:

```txt
Mas draw calls y mas batches.
Mas objetos en la escena de interfaz.
Mas decisiones de estructura al agregar elementos.
Orden de dibujo que hay que administrar entre canvas.
Riesgo de sobreseparacion.
```

El balance se decide midiendo, no contando canvas.

---

## Riesgos de aplicarlo mal

Riesgos:

```txt
Crear un Canvas por elemento.
Separar por ubicacion en pantalla en vez de por frecuencia.
Separar sin medir el estado previo.
Dejar elementos animados dentro del lote estatico.
Romper el orden de dibujo y superponer paneles mal.
Duplicar componentes de interfaz al reorganizar.
No revisar la clasificacion cuando cambia el diseño.
```

Ejemplo de aplicacion incorrecta:

```txt
Decision:
separar el HUD en canvas superior, medio e inferior.

Resultado:
el timer sigue conviviendo con el marco decorativo,
porque estan en la misma zona de pantalla.
```

La separacion existe, pero el criterio fue el equivocado y el problema sigue.

---

## Checklist de implementacion

```txt
¿Se midio el costo de UI antes de separar?
¿Se listo cada cuanto cambia cada elemento?
¿La agrupacion sigue frecuencia y no ubicacion?
¿Quedo algun elemento animado en el lote estatico?
¿Quedo decoracion fija en el lote dinamico?
¿Cuantos canvas quedaron y por que cada uno?
¿Se justifica el cuarto grupo con una medicion?
¿Subieron los draw calls y cuanto?
¿Bajo el costo de rebuild mas de lo que subio el envio?
¿El orden de dibujo sigue siendo correcto?
¿La estructura queda clara para quien agregue un elemento nuevo?
¿Se midio despues?
```

---

## Regla final

La interfaz se agrupa por como cambia, no por como se ve.

```txt
Mismo ritmo, mismo lote.
Ritmos distintos, lotes distintos.
Un lote por elemento no es separar: es fragmentar.
```
