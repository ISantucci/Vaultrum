# Operar el arte

Cómo opera la IA las herramientas de arte, y **cómo se le pide** a Vaultrum un trabajo de arte para que lo haga bien a la primera.

No decide **dónde** corre el trabajo —qué superficie, qué modelo, qué ejecutor—: eso es `07_Despacho de ejecucion`, y esta nota no lo repite. Contesta lo que viene después: una vez que el trabajo corre ahí, cómo lo opera la IA, con qué lo verifica y qué tiene que traer el pedido.

No enseña a modelar ni a animar. El criterio de oficio está en el Core (`Principios de arte`), su precio en `Optimizacion` (rama `Arte`), y las leyes medidas en el Área de Arte. Lo que entra acá de "manual para humanos" es lo único que hace falta para que la herramienta **ande**: qué abrir, qué prender, qué conectar.

---

## Cómo se pide arte a Vaultrum

Un pedido de arte que sale bien trae cinco cosas. Las que falten, el Área de Arte las pregunta antes de empezar, porque cada una que falta es una vuelta más con el generador o con el DCC.

```txt
QUE          el asset o la accion, con su nombre en el proyecto
PARA QUE     el hecho del juego que lo pide: que hace, cuantas veces aparece, desde
             que camara se ve
CANON        la referencia aprobada: el archivo, no la descripcion
LIMITES      lo que ya esta decidido: escala, presupuesto, paleta, cuadros de gameplay
ACEPTACION   como se va a saber que esta bien: que se mide y que juzga el owner
```

```txt
mal     "haceme un enemigo que se vea amenazante"
bien    "el enemigo de oleada de TowerDefense: aparece hasta 20 a la vez, camara
         a 30° sobre la horizontal, familia 'terrestre', mitad A cerrada. Que se distinga
         del goblin en silueta. Te paso el bloqueo aprobado."
```

Y Vaultrum contesta siempre con tres cosas antes de hacer: **en qué modo entra el Área de Arte**, **qué va a medir con instrumento** y **qué va a quedar como juicio del owner**.

---

## Las herramientas

### [[Blender por MCP]]

Cómo modela, verifica y renderiza la IA en Blender a través del servidor MCP conectado a la PC del owner, con las reglas de costo que ya se midieron.

### [[Unreal para motion graphics]]

Cómo podría operar la IA Unreal para animar interfaces y motion graphics, qué hay que prender para que lo haga, y qué hace mientras no está conectado.

---

## Los temas

### [[Legibilidad]]

Cómo mide la IA si algo se lee: silueta, valor, daltonismo y tamaño real en pantalla. El principio está en el Core; acá está el procedimiento.

### [[Rigging y skinning]]

Cómo arma y verifica la IA un esqueleto y sus pesos, y cómo se le pide la prueba de poses antes de animar.

### [[Texturizado UV y materiales]]

Cómo despliega la IA las UV, mide la densidad de textura y asigna materiales desde la paleta.

### [[Sprites y animacion 2D]]

Cómo corre la IA el circuito de una animación por cuadros: el encargo, la medición de lo que vuelve y la exportación al motor.

### [[Motion graphics y UI]]

Cómo se especifica una interfaz animada para que la IA la pueda construir y verificar: estados, transiciones, escalonado, curvas. Salió de la clase del 10 de agosto del owner.

### [[VFX]]

Cómo se pide un efecto y qué verifica la IA de lo que vuelve: lectura, duración y costo de píxeles.
