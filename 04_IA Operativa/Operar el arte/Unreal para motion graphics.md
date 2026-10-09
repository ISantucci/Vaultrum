# Unreal para motion graphics

## Qué hace Vaultrum acá

Animación de interfaz y motion graphics en Unreal: widgets de UMG con sus estados y transiciones, y las piezas de Motion Design. Es lo que el owner está trabajando en la cátedra (animar widgets, transiciones, el menú principal animado).

**Hoy Unreal no está conectado a Vaultrum.** Esta nota dice cómo se conectaría, y qué hace la IA mientras tanto. Unreal no figura en el mapa de superficies de `07_Despacho de ejecucion`: entra cuando un caso real lo use, no antes.

## Con qué podría operar la IA, en orden

```txt
1  el plugin MCP oficial    experimental desde Unreal 5.8: un servidor MCP dentro del
   (76)                     editor, por HTTP local. Es la via directa
2  Python del editor (77)   scripts que crean y cambian assets. No todo lo de UMG esta
                            expuesto: se verifica antes de prometer
3  Remote Control (78)      leer y cambiar propiedades en vivo, por HTTP
4  sin conexion             la IA escribe la especificacion exacta y el owner la arma en
                            el editor. Es el modo de hoy
```

## Cómo se pone en marcha

Para la vía 1, en la PC del owner:

```txt
1  habilitar el plugin de Model Context Protocol en el editor y reiniciarlo
2  verificar que el servidor quedo escuchando en su direccion local
3  registrar ese servidor MCP en la app de escritorio de Claude de esa PC
4  vincular la conversacion a la PC: las herramientas aparecen con el prefijo del puente
```

Los pasos exactos dependen de la versión, y el plugin es experimental: la ficha `76_Unreal_MCP_Plugin` tiene la página oficial. Para la vía 2 hace falta el plugin de scripting con Python del editor (`77_Unreal_Python_Editor_Scripting`).

## Cómo opera sin conexión

La IA entrega una **tabla de pistas** que se arma tal cual en el editor de animación del widget:

```txt
elemento    propiedad      desde -> hasta    inicio    duracion   curva                 evento
Logo        opacidad       0 -> 1            0.00 s    0.30 s     llega frenando        al abrir
Logo        escala         0.9 -> 1.0        0.00 s    0.30 s     overshoot leve        al abrir
Boton 1     traslacion Y   +20 -> 0          0.08 s    0.20 s     llega frenando        al abrir
Boton 2     traslacion Y   +20 -> 0          0.16 s    0.20 s     llega frenando        al abrir
```

Propiedades permitidas: **traslación, escala, rotación y opacidad del render**. Nunca tamaño ni márgenes del layout (`Motion graphics y UI`).

Y la revisión de lo que vuelve: un video del owner a 60 cuadros por segundo, contra la tabla, con **un cuadro de tolerancia**: a 60 cuadros, 0.08 s son 4.8 cuadros, y ningún video cae justo ahí. Si la precisión importa, los tiempos de la tabla se escriben en múltiplos de 1/60.

## Cómo pedírselo

```txt
"Anima <widget> de <pantalla>: estados <lista>, entrada <utilitaria / contextual /
 dramatica>, escalonado <s> entre elementos, la dispara <evento>. Entregame la tabla
 de pistas."
```

## Qué verifica y con qué

Con conexión, lee las pistas del widget —propiedades, claves, tiempos, curvas— y las compara con la tabla. Sin conexión, compara el video contra la tabla cuadro por cuadro. El criterio de lo que se compara está en `Motion graphics y UI`.

## Lo que no hace

No programa la lógica del juego en Unreal: eso es el Área de Programación. No decide qué estados tiene una pantalla ni qué comunica: eso es UI/UX.
