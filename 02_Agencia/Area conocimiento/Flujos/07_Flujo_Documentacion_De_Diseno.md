## Propósito — Documentar un diseño por decisiones

Convertir ideas, conversaciones y decisiones de desarrollo en documentación **clara, trazable y aprobable**, reduciendo la incertidumbre hasta el nivel necesario para tomar la siguiente decisión o construir la siguiente prueba — y no más.

No es un flujo de producción de documentos. El método se probó fuera de Vaultrum: con él se escribió la documentación del próximo tower defense del owner en ChatGPT Cowork, y el owner lo trajo para que el sistema documente igual. Lo que funcionó allá es lo que este flujo fija acá.

```txt
el objetivo no es completar una biblioteca
es que el proyecto avance sin perder contexto, intención ni trazabilidad
```

---

## Entrada del flujo

Uno de tres casos:

```txt
un área escribe un documento con decisiones abiertas   el cuaderno y el TL de Producción,
                                                       un GDS con reglas y excepciones sin cerrar
el owner trae documentación hecha afuera               por ejemplo, los documentos de diseño de un
                                                       proyecto escritos en ChatGPT Cowork
el owner quiere documentar una idea antes de           visión, alcance, núcleo, sistemas: el
prototiparla                                           material que después se vuelve TL, RQ y GDS
```

**La autoría sigue siendo del área dueña del tema.** Visión, alcance y decisiones del proyecto son de Producción; reglas, sistemas y balance, de Game Design. Este flujo pone el método; el documento lo firma quien es dueño de lo que dice.

---

## Transformación que realiza

### A — Leer antes de preguntar

Identifica la fase real del proyecto, lee las fuentes vigentes —el cuaderno, los artefactos de la cadena, los documentos que el owner trajo— y lista qué ya está decidido, qué se contradice y qué bloquea. **No vuelve a preguntar lo que ya está confirmado.** Sale con el alcance de la sesión y la primera pregunta útil.

### B — Un mapa, y un solo documento activo

El índice del proyecto dice en menos de un minuto: fase, hito, documentos existentes con su estado y versión, cuál está activo, la última decisión relevante, qué bloquea y cómo se sigue. En Vaultrum ese índice **ya existe: es el cuaderno del proyecto**. Los documentos que no hacen falta para el hito actual quedan pospuestos a propósito, y se dice.

### C — Descubrimiento guiado: una decisión por vez

Por cada tema:

```txt
1. una pregunta concreta
2. dos a cuatro opciones excluyentes, cada una con su consecuencia en una frase:
   qué permite · qué cuesta o arriesga · qué cambia en alcance, experiencia o implementación
3. una recomendada, cuando la hay, con su criterio visible:
   objetivo · fase · recursos y plazo · riesgo a validar · decisiones ya aprobadas · dependencias
4. siempre la opción de responder otra cosa
5. la respuesta, reescrita como regla verificable
6. la pregunta que esa respuesta habilita, y las dependencias que toca
```

**Una sola pregunta principal por turno** cuando las respuestas se condicionan entre sí: la respuesta temprana cambia las preguntas de después. **En tanda** cuando son independientes, usan el mismo criterio y traen default recomendado —que es exactamente la regla de las tandas del relevamiento de Producción— o cuando el owner pide acelerar. Las dos reglas son la misma: lo que no se puede agrupar es lo que depende.

Orden de descubrimiento:

```txt
objetivo -> experiencia deseada -> alcance -> regla general -> excepciones
-> interacción con otros sistemas -> feedback -> valores provisionales
-> métricas y validación -> criterio de terminado
```

Preguntas que no se hacen: las que ya están respondidas, las demasiado abiertas cuando hay opciones claras, las técnicas antes de la intención, las numéricas antes de la función, las confirmaciones de lo explícito, varias dependientes juntas, opciones falsas donde una es absurda, y precisión final sobre algo que todavía hay que prototipar.

### D — Cada respuesta con su estado

```txt
Confirmado    el responsable lo aprobó explícitamente          = "declarado" del cuaderno
Delegado      el responsable autorizó elegir con la recomendación
Provisional   se usa para construir o probar; cambia con evidencia
Supuesto      se usa porque falta información; hay que validarlo  (incluye lo "inferido")
Pendiente     todavía no hay respuesta suficiente               = "faltante" del cuaderno
Reemplazado   una decisión posterior lo dejó sin vigencia
```

**Una frase escrita con seguridad no convierte un supuesto en una decisión.** Y un "Aprobado" que viene de un documento hecho afuera entra como Confirmado; un "Aprobado para prueba", como Provisional.

### E — Borrador completo, no fragmentos

Incorpora todo lo confirmado; separa reglas de ejemplos; pone cada excepción junto a la regla que modifica; marca lo provisional; deja visibles los pendientes reales; usa tablas para comparaciones exactas y diagramas solo si aclaran un flujo; termina con criterios de aceptación.

### F — Coherencia antes de pedir aprobación

Contra la visión y el alcance vigentes; términos, nombres y cantidades iguales en todo el documento; reglas y excepciones compatibles; ninguna decisión inventada; impacto sobre otros documentos identificado.

### G — Aprobación y propagación

El documento se presenta completo, con las decisiones sensibles y los pendientes resumidos. Estado y versión cambian **solo después** de la aprobación. Después: se actualiza el registro de decisiones del cuaderno, se corrigen los documentos que consumían la decisión —o se marcan `Requiere revisión`— y se conserva el rastro de lo reemplazado.

**Un documento tiene un solo propietario por tema.** La visión es de la visión; la cantidad de niveles, del alcance; el daño numérico, del balance. Los demás lo citan, no lo redefinen. Es la ley 6 de la documentación —no se dice dos veces— aplicada a decisiones.

### H — Cuándo se deja de documentar

Si las incertidumbres que quedan solo se resuelven jugando, midiendo o prototipando, se recomienda el prototipo y se define: el riesgo que se quiere validar, el alcance mínimo y lo excluido, los valores provisionales, **la instrumentación mínima —que es un `MET` del Área de Métricas si la pregunta es sobre lo que hace el jugador—** y el criterio para continuar, iterar o descartar. Eso es preproducción técnica: no autoriza la producción completa.

---

## Números y balance

Antes de asignar un valor: la función del elemento, las relaciones a preservar, la duración objetivo, la unidad de comparación, el resultado esperado y la condición que mostraría que el valor está mal. Un documento de balance previo al prototipo trae valores iniciales, fórmulas, supuestos, casos de referencia, **métricas a registrar, umbrales de corrección** y las variables que tienen que quedar configurables.

**La precisión matemática no es evidencia de diversión ni de equilibrio.** Un cálculo coherente puede producir una mala experiencia; por eso los valores son Provisionales hasta que un prototipo diga otra cosa.

---

## Cambios y contradicciones

```txt
jerarquía de fuentes   1 la decisión explícita más reciente del responsable
                       2 el documento propietario vigente y aprobado
                       3 el registro de decisiones y reemplazos
                       4 los documentos que consumen esa decisión
                       5 borradores y notas
                       6 inferencias de quien documenta
```

Ante dos fuentes que se contradicen, no se elige en silencio la más cómoda: se identifica el propietario, la versión más reciente y si hay un reemplazo registrado. **Si la contradicción cambia alcance, costo, experiencia o arquitectura, se frena el cierre y se pide la decisión.**

Una idea que mejora la experiencia y excede el alcance no se descarta en silencio: queda como contenido futuro, con la condición que permitiría reconsiderarla. Y entre documento e implementación, no se supone que el código tiene razón ni que el documento la tiene: se registra la discrepancia hasta saber si el cambio fue deliberado.

Lo que describe el mundo —mercado, plataformas, legislación, precios, herramientas externas, accesibilidad— se investiga en fuente primaria, con fecha de consulta, y separado de la decisión interna. Una tendencia de mercado no es una obligación de diseño.

---

## Salida esperada / formato

Todo documento de diseño empieza así:

```txt
# Proyecto — Documento NN
## Nombre del documento
Estado:                 En descubrimiento / Borrador / En revisión / Aprobado /
                        Aprobado para prueba / Requiere revisión / Reemplazado
Versión:                0.x mientras no está aprobado · 1.0 la primera aprobada ·
                        1.1 ajustes que preservan la intención · 2.0 un cambio central
Fecha de actualización: AAAA-MM-DD, con el motivo
Documento propietario de: los temas que gobierna
Objetivo:               el resultado que tiene que permitir
```

Y su cuerpo, tan corto como sea posible y tan completo como sea necesario: propósito, alcance, fuera de alcance, principios, reglas confirmadas, excepciones y dependencias, valores, pendientes, métricas o validación, criterios de aceptación.

Nombres de archivo con prefijo numérico, minúsculas y guiones bajos, un tema por archivo, **nunca `final`, `final_v2` ni `nuevo_definitivo`**: se conserva el archivo y sube la versión interna.

---

## Criterios de aceptación

- el propósito está claro, y el alcance separado de lo excluido,
- cada decisión confirmada es verificable, y los supuestos y provisionales están marcados,
- las excepciones están junto a sus reglas,
- los pendientes son reales y accionables,
- no contradice la visión ni el alcance, y respeta al propietario de cada tema,
- el destinatario puede actuar sin inventar decisiones esenciales,
- el nivel de detalle corresponde a la fase,
- estado, versión y fecha están al día, y el registro de decisiones del cuaderno refleja el cambio,
- el siguiente paso está escrito.

---

## Qué debe evitar

Aprobar en nombre del responsable sin delegación. Ocultar pendientes para que el documento parezca completo. Inventar fechas, responsables o capacidades. Expandir el alcance. Convertir ideas futuras en compromisos. Escribir especificaciones técnicas definitivas sin participación técnica. Seguir preguntando cuando una prueba informa más. Generar todos los documentos antes de que hagan falta. Sobrescribir lo aprobado sin registrar el cambio. Tratar una recomendación como evidencia. Llenar la conversación de metodología: el método se ve en la calidad del documento, no en la charla.

---

## Resultado final

Un documento que alguien puede usar para decidir, construir o probar mañana, con cada decisión en su estado, un solo dueño por tema, y el camino a la próxima pregunta escrito. Y cuando escribir deja de informar, la recomendación de ir a probar.
