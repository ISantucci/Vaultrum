## Definicion

Culling consiste en descartar trabajo que no va a contribuir al resultado.

En rendering aparece en dos formas clasicas.

```txt
Frustum culling:
¿esta dentro del volumen visible de la camara?
│
├── No → descartar
└── Si → continuar
```

```txt
Occlusion culling:
¿esta completamente tapado por algo opaco?
│
├── Si → descartar
└── No → continuar
```

Son preguntas distintas. Un objeto puede estar dentro de la camara y aun asi no aportar un solo pixel.

```txt
Camara → pared → objeto
```

Pero la definicion util para Vaultrum es mas amplia:

```txt
si no contribuye
→ no se procesa
```

Culling no es un sistema de rendering. Es la version binaria del mismo criterio que sostiene LOD.

---

## Que problema ayuda a prevenir

Ayuda principalmente con:

```txt
Costo de vertices y geometria
Costo de fragmentos y shaders
Sombras costosas
Draw calls innecesarios
Trabajo de CPU sobre entidades irrelevantes
```

Y con una familia de problemas que no son graficos:

```txt
Enemigos extremadamente lejanos actualizandose.
Particulas fuera de relevancia.
Animaciones que nadie ve.
Audio de fuentes lejanas.
IA razonando fuera de actividad.
```

El principio de fondo es uno solo:

```txt
eliminar trabajo invisible para el jugador
```

---

## Como funciona

El patron es siempre filtrar barato antes de ejecutar caro.

```txt
Prueba barata de descarte
↓
conjunto reducido
↓
trabajo caro solo sobre lo que queda
```

Frustum culling usa una prueba geometrica simple contra un volumen. Es barata y suele venir resuelta por el motor.

Occlusion culling es otra cosa:

```txt
Necesita saber que tapa a que.
Necesita datos precalculados o consultas en runtime.
Tiene costo propio.
Tiene complejidad propia.
```

Por eso su rendimiento depende mucho de la escena:

```txt
Interiores, pasillos, ciudad densa
→ mucha oclusion real
→ aporta bastante.

Mundo abierto sin obstruccion
→ poca oclusion real
→ puede costar mas de lo que ahorra.
```

Culling de logica funciona igual, pero el criterio deja de ser la camara:

```txt
¿Esta activo?
¿Esta cerca?
¿Puede afectar al jugador ahora?
¿Cambia algo si no lo actualizo este frame?
```

---

## Como aplicarlo en videojuegos

En un Tower Defense el mapa suele verse casi entero, asi que el frustum culling aporta poco y el culling de logica aporta mucho.

Sobre lo visual:

```txt
Decoracion fuera del recorrido
→ descartada por frustum.

Props detras del edificio central
→ candidatos a occlusion culling.

Efectos de disparo fuera de pantalla
→ no se emiten.
```

Sobre la simulacion, que es donde esta el ahorro real:

```txt
Enemigo en la ultima curva del recorrido
→ solo avanza por el camino.

Enemigo dentro del rango de una torre
→ simulacion completa.

Torre sin enemigos en rango
→ no busca objetivo cada frame.
```

Un ejemplo concreto de conjunto activo:

```txt
Antes:
300 enemigos vivos
→ 300 busquedas de objetivo por frame.

Despues:
300 enemigos vivos
→ 30 dentro de rango de alguna torre
→ 30 busquedas.
```

El HUD de dinero, vida y wave se actualiza cuando el dato cambia, no cuando la camara lo mira.

El caso de la torre sin enemigos en rango es el ejemplo de Active Set, que es donde esta desarrollado. Lo que decide cual de las dos respuestas corresponde es una sola pregunta:

```txt
¿Puede dejar de hacerlo sin que se note?   → sale del conjunto activo
¿Tiene que seguir haciendolo, mas lento?   → baja de frecuencia o de precision
```

Culling se ocupa del primer caso: trabajo que no contribuye y por eso directamente no se hace.

---

## Relacion con arquitectura

Culling necesita que exista alguien capaz de responder si algo es relevante. Eso es una decision de arquitectura, no de rendering.

```txt
todos los objetos
≠
objetos activos y relevantes
```

Se apoya en:

```txt
Active Set
Broad phase antes de narrow phase
Early exit
Particiones espaciales
Estados que habilitan solo lo necesario
```

Un sistema central que decide quien participa es mucho mas facil de perfilar que doscientos objetos que se auto excluyen con reglas propias.

```txt
Registro y desregistro explicitos
→ el conjunto activo es un dato observable.
```

Si nadie puede listar que se esta actualizando, tampoco se puede saber que se dejo de actualizar.

---

## Relacion con hardware/runtime

Afecta principalmente:

```txt
GPU
CPU
Ancho de banda
```

El reparto depende del tipo de culling:

```txt
Frustum culling
→ evita preparacion y dibujado.

Occlusion culling
→ evita fragmentos y passes
→ agrega costo de decision.

Culling de logica
→ evita CPU
→ no toca la GPU.
```

Conviene recordar que la prueba misma cuesta:

```txt
Costo de la prueba
×
cantidad de candidatos
×
frecuencia
```

Un culling caro sobre miles de objetos cada frame puede consumir mas de lo que descarta.

---

## Cuando conviene usarlo

Conviene cuando:

```txt
Hay mucho contenido fuera de camara.
La escena tiene oclusion real y estable.
Existen muchas entidades simuladas.
Buena parte de esas entidades no afecta nada.
El conjunto relevante es mucho menor que el total.
El costo se midio y crece con la cantidad.
```

Casos claros:

```txt
Mundos grandes con camara local.
Interiores con muros.
Multitudes.
Sistemas de audio ambiental.
IA numerosa.
```

---

## Cuando NO conviene usarlo

No conviene cuando:

```txt
Casi todo esta siempre visible.
Hay pocos objetos.
La escena no tiene obstruccion real.
El criterio de descarte cuesta mas que el trabajo.
El sistema depende de simulacion continua.
No hay problema medido.
```

Y hay un caso donde directamente no debe aplicarse:

```txt
Logica que sostiene el estado del juego.
```

Si un enemigo deja de avanzar porque la camara no lo mira, eso no es culling. Es un bug.

---

## Trade-offs

```txt
Frustum culling
→ barato y automatico
→ aporta poco con camara amplia.

Occlusion culling
→ mucho ahorro en escenas cerradas
→ costo de datos, autoria y runtime.

Culling de logica
→ gran ahorro de CPU
→ riesgo de romper simulacion.

Conjunto activo explicito
→ control y visibilidad
→ mas ciclo de vida que mantener.

Umbrales agresivos
→ mas ahorro
→ mas artefactos y saltos.
```

---

## Riesgos de aplicarlo mal

Riesgos comunes:

```txt
Cullear logica que si importa aunque no se vea.
Enemigos que se congelan fuera de camara.
Estados que no avanzan y quedan desincronizados.
Audio que corta de golpe.
Objetos que aparecen tarde al girar la camara.
Volumenes de culling mal ajustados a la malla.
Occlusion culling sobre geometria que se mueve.
Prueba de descarte mas cara que el descarte.
```

Ejemplo:

```txt
Antes:
El enemigo lejano deja de actualizarse.

Problema:
Tampoco avanza por el recorrido.

Resultado:
La wave nunca termina y el jugador no entiende por que.
```

La pregunta correcta no es si se ve. Es si contribuye.

---

## Checklist de implementacion

```txt
¿El problema fue medido?
¿Cuanto contenido queda realmente fuera de camara?
¿La escena tiene oclusion real?
¿Cuanto cuesta la prueba de descarte?
¿Sobre cuantos candidatos corre y con que frecuencia?
¿Que sistemas se apagan y cuales siguen vivos?
¿El estado de gameplay avanza igual con el objeto cullado?
¿Se probo girando la camara rapido?
¿Aparecen objetos tarde o parpadeando?
¿Los volumenes de culling coinciden con la geometria?
¿El conjunto activo se puede inspeccionar?
¿Se midio despues del cambio?
```

---

## Regla final

Culling no significa dejar de dibujar. Significa dejar de trabajar en lo que no cambia nada.

```txt
Si el jugador no lo percibe
y el juego no depende de eso,
no hace falta calcularlo.
Si el juego depende de eso,
no era culling.
```
