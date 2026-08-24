---
tipo: fundamento
estado: En estudio
mision: EST-006_Mision_Lote_Biblioteca_Agosto26
profundiza: transversal de proceso
cruza: 19_Playful_Production_Process, 03_Definicion_de_terminado, 04_Playbook_de_diseno, 01_Loop_de_experiencia
---

# Fundamento 17 — Scope, prototipado y cierre

> Cubre el control del alcance como estructura de proceso: el verbo único, los prototipos por pregunta, el presupuesto de contenido, la vertical slice, el orden de recorte y el protocolo de cierre. **No** cubre gestión de equipos, contratos, publishing ni marketing. Tampoco cubre estimación de costos económicos.
> **IP:** conceptos destilados + cita. Nunca texto verbatim con copyright.

## Índice del libro
1. Qué es y por qué se rompe si falta
2. El modelo — verbo único, prototipos, presupuesto, slice, recorte, cierre
3. Baseline numérico
4. Patrones que funcionan
5. Antipatrones
6. Cómo se verifica
7. CHECKLIST
8. Aplicación · Límites · Fuentes

## Qué es y por qué se rompe si falta
El alcance no se controla con voluntad. Todos los devs que abandonaron un proyecto de tres años tenían disciplina; lo que no tenían era estructura. La fuerza de voluntad decide qué hacés hoy; la estructura decide qué es posible en seis meses, y gana siempre la estructura.

Un dev solo tiene un problema específico: no hay nadie que le diga que no. No hay productor que corte el feature, no hay fecha externa, no hay presupuesto que se agote de golpe. El proyecto no muere: se estira hasta volverse un pasatiempo triste. La señal no es dramática, es aburrida: pasan tres meses y no hay una build nueva que alguien más pueda jugar.

Terminar no es cuestión de talento. Es una habilidad separada del diseño y de la programación, que se entrena terminando cosas chicas primero. El dev que terminó cinco juegos de un mes está mucho mejor preparado para el juego de un año que el que lleva un año en el mismo prototipo.

## El modelo

**Capa 1 — El verbo único.** Si no podés describir el juego en una oración con un verbo principal, todavía no tenés juego: tenés una lista de deseos. El verbo es lo que el jugador hace 500 veces por sesión.

```txt
  ✔  "Saltás entre plataformas que desaparecen cuando las pisás."     1 verbo
  ✔  "Ordenás cajas en una estantería antes de que se caiga todo."    1 verbo
  ✘  "Un juego de exploración con crafteo, combate táctil, base
      building y narrativa ramificada en un mundo procedural."        0 verbos, 5 sistemas

  Test: tapá todo menos el verbo. ¿Sigue siendo un juego jugable?
  Si la respuesta es "no, le falta X", entonces X era el verbo real.
```

**Capa 2 — Un prototipo, una pregunta.** El prototipo no "avanza el juego": responde una pregunta y después se tira. Si no sabés qué pregunta responde, no es un prototipo, es el juego empezado sin pensar.

| Prototipo | Pregunta que responde | Duración | Criterio de éxito | Qué se tira |
|---|---|---|---|---|
| **Gris (feel)** | ¿Se siente bien mover esto? | 2–5 días | Divertido moverse en una sala vacía | Todo el arte (no había) |
| **Comprensión** | ¿Lo entiende sin que le expliques? | 3–7 días | 4 de 5 testers juegan 2 min sin ayuda | La UI provisoria |
| **Diversión** | ¿Lo vuelve a jugar sin que se lo pidas? | 1–2 semanas | ≥1 tester pide "otra" | Los sistemas que nadie usó |
| **Viabilidad técnica** | ¿Corre? ¿Es implementable solo? | 2–4 días | 60 fps con N entidades en hardware objetivo | El código entero, siempre |

El orden importa: **feel → comprensión → diversión → viabilidad**. Si el prototipo gris falla, ningún arte lo salva y toda la producción posterior es dinero tirado.

**Capa 3 — El presupuesto de contenido.** Este es el modelo que más proyectos salva, porque convierte la fantasía en aritmética. Baseline para un dev solo con **25–30 horas reales de producción por semana** (no 40: reuniones, build, bugs, admin y vida existen).

| Unidad de contenido | Horas por unidad | Minutos de juego que genera |
|---|---|---|
| Nivel 2D simple (tiles + encuentros) | 8–16 h | 3–5 min |
| Nivel 3D (blockout + pase de arte + audio) | 30–60 h | 4–8 min |
| Enemigo nuevo (IA + arte + anim + audio) | 20–40 h | — (multiplica variedad) |
| Arma / habilidad nueva | 8–20 h | — |
| Jefe | 60–120 h | 5–10 min |
| Cutscene de 30 s | 15–40 h | 0.5 min |
| Sistema nuevo (inventario, diálogo, crafteo) | 40–120 h | 0 min de contenido |

```txt
   RATIO DE CONTENIDO (dev solo, full-time, contenido pulido)

     2D simple        5 – 15 min / semana
     3D               2 –  6 min / semana
     Sistémico / proc  20 – 60+ min / semana   (el contenido lo genera el sistema)

   ARITMÉTICA QUE DUELE:
     querés 6 h de juego en 3D  ->  360 min / 4 min por semana  =  90 semanas
     + 30% de cierre            ->  ~117 semanas  =  2 años y 3 meses

   Salidas posibles (elegí una, conscientemente):
     a) bajar la duración objetivo    (6 h -> 90 min)
     b) cambiar a contenido sistémico (procedural, roguelite, sandbox)
     c) bajar el nivel de pulido      (estilizado barato, sin cutscenes)
     d) aceptar los 2 años            (con los ojos abiertos, no por default)
```

**Capa 4 — Vertical slice honesta.** Una rebanada de 3–10 minutos del juego a calidad final absoluta: arte, audio, UI, feel, guardado, todo. Honesta significa que no hay nada truqueado para la demo. Sirve para dos cosas: probar que sabés cómo se ve el producto terminado, y medir cuánto cuesta realmente producir un minuto de tu juego. Ese número, multiplicado por la duración objetivo, es tu calendario real. Se hace **antes** de producir contenido en masa, nunca después.

**Capa 5 — El orden del recorte.** Cuando hay que cortar (siempre hay que cortar), el orden no es negociable.

```txt
   SE CORTA PRIMERO  ┌─ 1. Cantidad de contenido   (12 niveles -> 7)
                     │  2. Variedad                (5 enemigos -> 3)
                     │  3. Sistemas secundarios    (crafteo, diálogos)
                     │  4. Modos y extras          (NG+, coleccionables)
                     │  5. Alcance narrativo       (cutscenes -> texto)
                     │  6. Fidelidad de arte       (estilizado, menos anim)
   SE CORTA ÚLTIMO   └─ 7. Pulido del core loop    (NUNCA)

   Un juego corto y pulido se publica. Un juego largo y crudo se abandona.
```

**Capa 6 — El cierre como fase.** El cierre no es "los últimos días": es el 30% del calendario, reservado desde el principio.

```txt
  CONCEPTO   PROTOTIPOS   PRODUCCIÓN                CIERRE
  |---5%---|----15%-----|----------50%-----------|--------30%--------|
                                                 ▲        ▲      ▲   ▲
                                    feature freeze  content lock  |  gold
                                    (nada nuevo)    (nada de       bug bar
                                                     contenido)   (solo P0/P1)
```

**Feature freeze:** al 70% del calendario. Desde ahí, ninguna funcionalidad nueva; solo terminar y pulir lo que existe.
**Content lock:** al 85%. Ningún nivel, enemigo o asset nuevo. Se congela para poder testear un juego que no cambia.
**Bug bar:** al 90%. Solo crashes, softlocks y bloqueantes. Todo bug cosmético conocido va a una lista y se publica igual.

**Capa 7 — La lista NO.** Un documento vivo, en el mismo repo que el diseño, con todo lo que decidiste no hacer y por qué. No es un cementerio: es la evidencia de que el alcance está bajo control. Si en un mes no agregaste ninguna entrada, el scope no se está gestionando, está creciendo.

## Baseline numérico

| Parámetro / criterio | Baseline sugerido | Por qué |
|---|---|---|
| Duración del primer juego terminado | ≤3 meses full-time / ≤6 part-time | Terminar es la habilidad que se está entrenando |
| Verbo único | 1 oración, ≤15 palabras, 1 verbo | Si no entra, el concepto no está cerrado |
| Sistemas nuevos por proyecto | ≤3 | Cada sistema son 40–120 h que no producen contenido |
| Prototipo gris | ≤5 días | Si a los 5 días no se siente bien, cambiá o cortá |
| Vertical slice | 3–10 min a calidad final, ≤15% del contenido | Alcanza para medir el costo por minuto |
| Reserva de cierre | 30% del calendario (nunca <25%) | Es la parte que siempre se subestima |
| Multiplicador de estimación | ×1.6 sobre tu estimación optimista; ×2 si el sistema es nuevo para vos | Sesgo de planificación, medido en tu propio historial |
| Horas reales de producción | 25–30/sem full-time · 8–12/sem part-time | Las otras horas existen igual |
| Contenido pulido por semana | 2–6 min (3D) · 5–15 min (2D) | Base de toda la aritmética de calendario |
| Feature freeze | Al 70% del calendario | Deja tiempo real para terminar lo empezado |
| Content lock | Al 85% | Testear un blanco móvil no sirve |
| Entradas nuevas en la lista NO | ≥1 por semana | Métrica directa de gestión de alcance |
| Cadencia de build jugable | ≥1 por semana | Sin build no hay proyecto, hay repositorio |
| Jugado por alguien externo | ≥1 vez por mes | Es la única fuente de verdad |
| Bug bar de release | 0 crashes · 0 softlocks · ≤5 cosméticos conocidos | Perfecto no existe; publicable sí |
| Alarma de proyecto eterno | >2 refactors del core en 3 meses, o >6 semanas sin build jugable | Señal temprana y objetiva |
| Ratio de backlog | Tareas cerradas / tareas creadas por semana ≥1 | Debajo de 1, el final se aleja cada semana |

## Patrones que funcionan

- **El verbo único.** Escribí la oración, pegala arriba del documento de diseño, y evaluá cada feature preguntando si sirve al verbo. *Cuándo:* antes de escribir una línea de código. *Costo:* te obliga a matar ideas que querés; es exactamente para eso.
- **Prototipo por pregunta con fecha de corte.** Una pregunta, una fecha, y el compromiso explícito de tirar el código. *Cuándo:* cada incertidumbre grande. *Costo:* disciplina de borrar trabajo que funciona; es la habilidad más difícil de la lista.
- **Presupuesto invertido.** Partís de la fecha de release y calculás cuánto contenido entra, en vez de partir del contenido y estimar la fecha. *Cuándo:* al pasar de prototipo a producción. *Costo:* el juego resultante es más chico que tu fantasía, y por eso existe.
- **Vertical slice honesta.** Una rebanada a calidad final antes de producir en masa. *Cuándo:* después de que el prototipo de diversión pasó. *Costo:* 2–6 semanas que se sienten como no avanzar, y que evitan rehacer 30 niveles.
- **La lista NO.** Documento vivo de cortes con fecha y motivo. *Cuándo:* desde el día uno. *Costo:* 20 minutos por semana.
- **Timebox de rescate.** Si un feature pasa el doble de su estimación, se degrada a la versión simple o se corta. Decisión tomada de antemano, no en el momento de frustración. *Cuándo:* siempre. *Costo:* ninguno; el costo es no tenerlo.
- **Congelar hacia atrás.** Freeze escalonado (features → contenido → bugs) en vez de un único "ya está". *Cuándo:* último 30%. *Costo:* requiere haber reservado ese 30%.
- **El juego chico primero.** Terminar y publicar algo del tamaño de un `01_Pong` antes del proyecto grande. *Cuándo:* si nunca terminaste nada. *Costo:* 2–4 semanas que parecen desvío y son la inversión más rentable del proyecto grande.
- **Definición de terminado por entregable.** Cada tarea tiene su criterio de cierre escrito antes de empezarla. *Cuándo:* siempre. Ver [[03_Definicion_de_terminado]].

## Antipatrones

| Antipatrón | Síntoma observable |
|---|---|
| El refactor eterno | Tres meses sin una sola feature jugable nueva |
| El prototipo que se volvió el juego | No podés tocar nada sin romper otra cosa; el "prototipo" tiene 8 meses |
| Scope creep por playtest | Cada comentario de cada tester se convirtió en una tarea del backlog |
| El motor propio | Semana 20 y todavía estás escribiendo el sistema de partículas |
| Arte primero | Assets hermosos de un juego que nadie confirmó que sea divertido |
| El pitch que crece | El elevator pitch pasó de 1 oración a 4 en seis meses |
| Terminar el 90% dos veces | Llevás cuatro meses "casi terminando" |
| No hay fecha | No podés responder "¿cuándo?" ni con un rango de tres meses |
| Cortar el cierre | El 30% de pulido se lo comió el retraso de producción |
| Contenido sin slice | Produjiste 20 niveles y ahora hay que rehacerlos todos |

## Cómo se verifica

- **Test del verbo.** Decile la oración a alguien que no sabe nada del proyecto. Si te pide aclaraciones, el concepto no está cerrado.
- **Test de la build semanal.** ¿Existe un ejecutable de esta semana que alguien pueda abrir y jugar sin vos? Si no, el proyecto no está en producción.
- **Test del tercero.** Alguien juega 10 minutos mientras vos mirás en silencio. La regla es no hablar: cada vez que sentís la urgencia de explicar algo, anotá qué era. Esa lista es tu backlog de claridad.
- **Costo por minuto medido.** Después de la vertical slice, dividí las horas invertidas por los minutos de juego producidos. Multiplicá por la duración objetivo. Ese número es tu calendario real, no el que tenías en la cabeza.
- **Burn de scope.** Cada semana anotá tareas creadas vs tareas cerradas. Cuatro semanas seguidas con ratio <1 significan que el proyecto se está alejando, no acercando.
- **Extrapolación de fecha.** Anotá el % de contenido terminado y la fecha. Trazá la recta. Si el resultado te sorprende, ya tenés el dato que estabas evitando.

## CHECKLIST

```txt
[ ] El juego se describe en 1 oracion de <=15 palabras con 1 verbo principal
[ ] Hay <=3 sistemas nuevos en todo el proyecto
[ ] Cada prototipo tiene escrita su pregunta y su fecha de corte
[ ] El prototipo gris paso: mover al personaje en una sala vacia es divertido
[ ] El prototipo de comprension paso: 4 de 5 testers jugaron 2 min sin ayuda
[ ] Existe vertical slice de 3-10 min a calidad final, sin trucos de demo
[ ] El costo por minuto de juego esta medido, no estimado
[ ] La duracion objetivo sale de la aritmetica del presupuesto de contenido
[ ] Todas las estimaciones tienen multiplicador x1.6 (x2 si el sistema es nuevo)
[ ] El 30% final del calendario esta reservado para cierre y esta protegido
[ ] Existe fecha de feature freeze (70%) y de content lock (85%) en el calendario
[ ] Existe la lista NO y se le agrego algo en las ultimas 2 semanas
[ ] Hay build jugable de esta semana que un tercero puede abrir
[ ] Alguien externo jugo el juego en el ultimo mes
[ ] El orden de recorte esta escrito y acordado con vos mismo antes de la crisis
[ ] Ratio tareas cerradas/creadas >=1 en las ultimas 4 semanas
[ ] Bug bar definido: 0 crashes, 0 softlocks, lista de cosmeticos conocidos
[ ] Existe una fecha de release escrita, aunque sea un rango de un mes
```

## Aplicación · Límites · Fuentes

**Aplicación (Unity, dev solo).** Mantené el prototipo en un proyecto separado del juego: si comparten repo, el código de prototipo termina en producción y el "tiralo" no ocurre nunca. Automatizá la build desde el día uno —un script que genere el ejecutable con un click— porque la fricción de buildear es la causa número uno de que no haya build semanal. El documento del verbo único, la lista NO y el presupuesto de contenido viven en el repo, versionados, no en la cabeza. En el tracker, una etiqueta `post-release` que absorba todo lo que llegue después del feature freeze: la idea no se pierde, pero tampoco entra. Y guardá el log de horas reales por tarea durante el primer mes: tu multiplicador personal de estimación es mucho más útil que el ×1.6 genérico.

**Límites.** Este libro asume un dev solo o un equipo de 2–3 personas, autofinanciado, sin fecha externa impuesta. No cubre planificación con publisher, hitos contractuales, ni coordinación de equipos donde el problema deja de ser el alcance y pasa a ser la comunicación. Los ratios de contenido son baseline sugerido a partir de estructura de trabajo típica: medí los tuyos en la primera vertical slice y reemplazalos, porque los tuyos son los únicos que importan.

**Fuentes.** `19_Playful_Production_Process` · `03_Game_Design_Workshop` · `02_Art_of_Game_Design` · `16_Advanced_Game_Design` · `13_Elements_of_Game_Design` · `08_Designing_Games`
**Cruces.** `03_Definicion_de_terminado` (el criterio de cierre por entregable que este libro presupone) · `04_Playbook_de_diseno` · `01_Loop_de_experiencia` (el loop es lo último que se recorta) · `05_Fundamentos_de_experiencia_ludica` · `01_Pong` (el juego chico como entrenamiento de cierre)
