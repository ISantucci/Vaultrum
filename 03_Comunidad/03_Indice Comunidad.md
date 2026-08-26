## Propósito

La Comunidad es la capa **pública** de Vaultrum. Se ocupa de dos cosas que son la misma vista desde los dos lados: cómo entra alguien de afuera al proyecto, y cómo sale el proyecto hacia afuera.

Hasta hace poco solo hacía lo primero: era un conjunto de documentos de gobernanza. Ahora también **trabaja**. Comparte estructura con la Escuela —tiene `Agentes/`, `Flujos/`, `Salidas/` y su skill— porque también es un lugar donde se produce algo. Lo que produce son las publicaciones del sistema.

No existe para sumar contenido sin dirección. Existe para proteger la coherencia de Vaultrum mientras permite crecimiento abierto.

---

## Sobre qué trabaja esta capa

El criterio que separa las capas de Vaultrum es **sobre qué trabajan**:

```txt
Agencia    produce el proyecto del usuario
Escuela    produce conocimiento para el sistema
Comunidad  produce la cara pública del sistema, y cuida quién la construye con él
```

Por eso las salidas `PUB` no cuelgan de la columna vertebral de numeración de la Agencia: una publicación no es un eslabón de la cadena de producción.

---

## Responsabilidad de esta sección

Debe ayudar a responder:

```txt
¿Cómo se puede contribuir?
¿Qué criterios debe respetar una contribución?
¿Qué tipo de contenido se acepta y cuál no corresponde?
¿Cómo se gobierna el proyecto?
¿Qué límites legales y de marca existen?
¿Qué se contó ya hacia afuera, y qué falta contar?
¿Quién aportó, y está registrado?
```

La Comunidad no reemplaza a VaultrumCore. Define cómo se cuida, se expande y se muestra el proyecto.

---

## [[00_Archivo|El Archivo]]

El corazón de la capa, y su equivalente a la Biblioteca de la Escuela: lo que el sistema ya mostró hacia afuera, y el registro de quién lo construye con él.

Guarda las fichas de lo publicado —que fijan el piso de cada corrida nueva— y la gestión del leaderboard. Sin Archivo, cada publicación arranca de cero y repite la anterior.

---

## Sub-agentes de la capa

### [[01_Analista_De_Avance]]

Rol ancla. Lee lo que cambió desde la última ficha del Archivo y decide **si hay post**. No hay post es una respuesta válida.

### [[02_Redactor]]

Convierte el informe en el texto publicable, en español e inglés, sin agregar una sola afirmación que el informe no traiga.

### [[03_Director_De_Imagen]]

Define qué imágenes lleva el post y escribe el pedido con la precisión suficiente para que se saquen de una sola vez. No genera imágenes.

### [[04_Validador_Publicacion]]

Rastrea cada afirmación hasta el archivo que la prueba, comprueba que las imágenes estén en disco y emite el veredicto. Es el último paso antes de lo único que no se puede deshacer.

---

## Flujos de la capa

### [[01_Flujo_Lectura_De_Avance]]

Leer el período contra el piso del Archivo y decidir si hay post.

### [[02_Flujo_Redaccion]]

Convertir el informe en el texto, en los dos idiomas.

### [[03_Flujo_Pedido_De_Capturas]]

Definir qué se ve y dejar el pedido escrito.

### [[04_Flujo_Validacion_Publicacion]]

Verificar afirmaciones, números e imágenes, y emitir el veredicto.

---

## Salidas de la capa

### [[00_Indice_pub]]

El registro de las publicaciones preparadas. Cada `PUB-XXX` es un post listo para publicar, con el informe que lo justifica y la verificación que lo respalda.

---

## Skill ejecutable

La capa corre como la skill **`vaultrum-contenido`**, con fuente versionada en `03_Comunidad/Skills/vaultrum-contenido/SKILL.md`. Es lo que convierte estos documentos en una máquina: sin ella son el manual.

Su único disparador es el **pedido del owner**. La Comunidad no sale a publicar sola.

---

## [[Sistema de contribucion]]

Explica el sistema general de contribución de Vaultrum. Sirve para entender cómo se evalúan aportes y qué responsabilidad debe cumplir cada contribución.

---

## [[CONTRIBUTING]]

Documento práctico para personas que quieran contribuir al proyecto. Sirve como guía directa de participación.

---

## [[GOVERNANCE]]

Documento de gobernanza del proyecto. Sirve para explicar cómo se toman decisiones y cómo se protege la dirección de Vaultrum.

---

## [[License_Notice]]

Aclara el criterio de licencia del proyecto y la necesidad del archivo `LICENSE` oficial en raíz.

---

## [[Trademark]]

Aclara el uso del nombre, identidad y marca Vaultrum.

---

## [[CONTRIBUTORS]]

Registro visible del scoreboard comunitario de Vaultrum. El criterio con el que se mantiene vive en el Archivo.

---

## Regla final

La Comunidad existe para permitir crecimiento sin perder criterio.

Contribuir no es agregar más. Contribuir es mejorar Vaultrum respetando su responsabilidad.

Y mostrar no es vender: lo que esta capa publica tiene que poder señalar el archivo que lo prueba.
