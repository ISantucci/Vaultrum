---
tipo: fuente
titulo: "Apuntes de cátedra — Animación 2D/3D"
autores: el owner de Vaultrum (apuntes propios de cursada)
editorial: inédito — apuntes personales
anio: 2026 (clases del 03-08, 10-08, 31-08 y 21-09)
estado: Estudiado
mision: EST-020_Mision_Mapa_Territorio_Arte
temas: motion design de interfaz, transiciones, escalonado, microanimaciones, curvas de interpolación, keyframes e intermedios, blocking, principios avanzados en 2D, personalidad en el movimiento
apunta_a: Curvas e interpolacion · 04 - Pose a pose y accion directa · 09 - Timing · Personalidad en el movimiento · Motion graphics y UI · Sprites y animacion 2D
---

# Fuente 68 — Apuntes de cátedra de Animación 2D/3D

> **Fuente propia.** Apuntes que el owner tomó cursando la materia en 2026. No es material de los docentes ni texto de terceros: el repo es público y lo que entra es lo que el owner escribió.
> Se destiló entero en `TL-012`. Esta ficha registra **qué trajo cada clase y adónde fue**, para que una idea del Core se pueda rastrear hasta la clase de la que salió.

## Cita

Owner de Vaultrum (2026). *Apuntes de la materia Animación 2D/3D.* Cinco archivos: `12_principios`, `Animacion_2D_3D_03-08-26`, `Animacion_2D_3D_10-08-26`, `Animacion_2D_3D_31-08-26`, `Animacion_2D_3D_21-09-26`. Inédito.

## Qué trae, clase por clase

```txt
03-08   dos definiciones: motion graphics y blocking
10-08   LA CLASE DENSA: motion design de interfaz en Unreal. Que hace buena a una
        interfaz, escalonado con tiempos, microanimaciones, la cadena de feedback
        del dano, los estados de un boton, tres tipos de transicion, las cuatro
        interpolaciones, keyframe e intermedio, y una regla tecnica: no animar
        size ni margins
31-08   animacion 2D avanzada: exageracion, arcos, follow through, overlapping,
        accion secundaria, ciclo de caminata; exportar a UE5; y la frase de la
        clase: la personalidad empieza en como se mueve
21-09   una linea: interpolacion Bezier libre para el eje Z
12_principios   un solo item escrito: compresion y estiramiento
```

**Lo que no trae, dicho con la misma honestidad:** dos de los cinco archivos tienen una línea, y el de los doce principios tiene uno. La materia los recorre; el apunte todavía no. Los doce se completaron con `59_The_Illusion_of_Life`, `60_The_Animators_Survival_Kit` y `61_Game_Anim`.

## Adónde fue cada idea

| Idea del apunte | Clase | Nota destino |
|---|---|---|
| motion graphics como animación de elementos gráficos | 03-08 | `Motion graphics y UI` |
| blocking: la forma más básica de animar | 03-08 | `04 - Pose a pose y accion directa` |
| la animación como sucesión de imágenes; keyframe e intermedio | 10-08 | `Principios de animacion`, `04 - Pose a pose y accion directa` |
| a menos claves, más fácil de manipular; se ajusta moviendo claves y curvas | 10-08 | `Curvas e interpolacion`, `Claves por tipo de animacion` |
| lineal, ease in / ease out, overshoot, constante | 10-08 | `Curvas e interpolacion` |
| el ritmo: lento frustra, rápido no se entiende | 10-08 | `09 - Timing` |
| transición utilitaria, contextual y dramática | 10-08 | `09 - Timing`, `Motion graphics y UI` |
| qué aparece, qué desaparece, qué se mueve, qué llama la atención, qué queda estático | 10-08 | `03 - Puesta en escena`, `Motion graphics y UI` |
| escalonado 0 · 0.08 · 0.16 s | 10-08 | `Motion graphics y UI` |
| microanimaciones: +5% de escala, opacidad breve, shake de pocos cuadros | 10-08 | `10 - Exageracion`, `Motion graphics y UI` |
| daño → flash → barra → shake → sonido | 10-08 | `Motion graphics y UI` |
| botón: default → hover → pressed → feedback | 10-08 | `Motion graphics y UI` |
| cambios inmediatos, siempre con una animación de por medio | 10-08 | `02 - Anticipacion`, `Motion graphics y UI` |
| los textos primero y por encima | 10-08 | `Motion graphics y UI` |
| la información la dispara un evento, en el momento | 10-08 | `Motion graphics y UI` |
| no animar size ni margins | 10-08 | `Motion graphics y UI` |
| exageración, arcos, follow through, overlapping, acción secundaria | 31-08 | sus cinco notas en `Principios de animacion` |
| la personalidad empieza en cómo se mueve | 31-08 | `Personalidad en el movimiento` |
| exportar para UE5 | 31-08 | `Sprites y animacion 2D` |
| Bezier libre para un solo canal | 21-09 | `Curvas e interpolacion` |

## Lo que se corrigió sin borrarlo

**Ease in y ease out.** El apunte describe el *in* como la mitad donde la velocidad aumenta y el *out* como la que desacelera. Es correcto en el vocabulario del software, y es el **opuesto** del vocabulario de la animación tradicional, donde *slow in* es frenar al **llegar** a una pose. Los dos nombres conviven y se cruzan. `Curvas e interpolacion` deja la regla: en Vaultrum una curva se describe **por lo que hace la velocidad** —arranca lento, llega frenando— y el nombre del software se usa solo junto con la herramienta.

**Motion graphics.** El apunte la define como animación de la tipografía *y los sonidos*. El sonido acompaña y sincroniza, pero no es lo que se anima: la nota habla de elementos gráficos —tipografía, formas, interfaz— sincronizados con sonido.

## Límites declarados

Son apuntes de cursada: registran lo que el owner anotó, no la clase entera. Donde un apunte es una línea, la nota destino no se apoya en él más que para la línea.
