# VFX

## Qué hace Vaultrum acá

Especifica un efecto —un impacto, una explosión, un brillo de recolección, polvo al aterrizar— y verifica lo que vuelve: que se lea, que dure lo que tiene que durar y que no cueste más píxeles de los que paga.

## El pedido de un efecto

Un efecto sin propósito tapa el juego. Antes de pedirlo, cinco datos:

```txt
que comunica     el golpe conecto, se junto algo, algo va a explotar
cuanto dura      en cuadros o segundos, dentro del tiempo del gameplay
que tamano tiene en pantalla, a la distancia de juego
sobre que fondo  el real (Color en contexto)
cuanto puede     particulas y area de pixeles transparentes: el costo de un efecto es
costar           sobre todo overdraw
```

## El timing de un efecto

Un efecto es energía que aparece y se disipa. Como punto de partida:

```txt
el impacto     llega de golpe: el primer cuadro ya es el pico
la expansion   rapida
la disipacion  mas lenta que la expansion, y no tapa lo que viene despues
```

Es `09 - Timing` y `10 - Exageracion` aplicados a algo que no tiene cuerpo (`66_Elemental_Magic`).

## Con qué opera la IA

```txt
en Blender     particulas y simulaciones por Python, y renders a cuadros para un efecto
               2D (Blender por MCP)
por cuadros    un flipbook pedido a un generador sigue el circuito de Sprites y animacion 2D
en un motor    la especificacion de arriba, para que el sistema de particulas del motor la
               implemente; la IA verifica contra ella
```

## Qué verifica

```txt
se mide     duracion; cuantos cuadros tapa a la figura que importa; area de pixeles
            transparentes que cubre (el costo esta en Overdraw y transparencias, del Core)
se juzga    si se lee lo que tiene que comunicar
```

## Cómo pedírselo

```txt
"Efecto de <evento> para <juego>: comunica <que>, dura <tiempo>, ocupa <tamano>,
 sobre <fondo>, presupuesto <particulas / area>."
```

## Lo que no hace

No decide si el evento necesita un efecto: la cadena de feedback la diseña Game Design y su canal UI/UX.
