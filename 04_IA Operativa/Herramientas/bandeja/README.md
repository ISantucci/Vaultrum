# Bandeja - capa IA Operativa

Canal entre el productor (chat de Cowork) y los ejecutores (Claude Code en Windows).
Patron observer: el productor publica una orden, el observer la escucha y la ejecuta,
el resultado vuelve al buzon.

## Como se arranca

El observer se ubica solo: no hay rutas escritas adentro. Sale de donde vive el
archivo, y busca la raiz del vault hacia arriba por `00_START_HERE.md`, igual que
`skills.bat`. Lo unico que no puede adivinar es **contra que proyecto** corre, y
eso es un dato de cada maquina.

Una sola vez por maquina, crear `proyecto.local.txt` en esta carpeta con la ruta
adentro (no se versiona, igual que `.owner.local.json`):

    C:\Users\<vos>\Documents\GitHub\Project-Forge

Una ruta sin unidad se toma como **hermana del vault** — `Project-Forge` a secas
alcanza si el proyecto es vecino de `Vaultrum/`.

Despues, doble clic en `observer.bat`, o desde una consola parada en esta carpeta:

    .\observer.bat

Parametros opcionales (van los dos, al .bat y al .ps1):

    -Proyecto  "C:\ruta\al\proyecto"   pisa proyecto.local.txt en esta corrida
    -Bandeja   "C:\otra\bandeja"       correr el observer sobre otra bandeja
    -Intervalo 5                       segundos entre chequeos
    -Permisos  acceptEdits             modo de permisos de Claude Code
    -Continuar                         mantiene el contexto entre ordenes

Para cortar: Ctrl+C, o crear el archivo `stop.txt` en esta carpeta.

## Como funciona

    ordenes/     el productor deja aca los .md  -> el observer los toma en orden alfabetico
    procesadas/  la orden se mueve aca apenas empieza a ejecutarse (no se repite nunca)
    resultados/  <nombre>.result.md con el estado, el proyecto y la salida completa
    log.txt      una linea por orden: cuando, cual, cuanto tardo, como termino

Una orden puede declarar su propio proyecto con una linea `Proyecto: <ruta>` en las
primeras diez lineas. Sirve cuando hay mas de un proyecto en vuelo y la orden tiene
que ir a uno que no es el default de la maquina.

## La superficie se verifica antes, no despues

Antes de la primera orden, el observer comprueba que **puede** ejecutar: que `claude`
esta en el PATH, que la carpeta del proyecto existe, y que puede escribir en
`resultados/`. Si algo no da, corta con un codigo y no gasta la ejecucion.

    1  la bandeja no esta dentro de un Vaultrum (falta 00_START_HERE.md)
    2  no hay proyecto declarado, o la ruta declarada no existe
    3  'claude' no esta en el PATH de esta consola
    4  no se puede escribir en resultados/

Y lo que falla vuelve como **fallo**, no como nota al pie: el resultado guarda el
`Estado` con el exit code del ejecutor, y el log tambien. Criterio del Core:
`La superficie del ejecutor`.

## Reglas

- Una orden = un archivo .md autocontenido. El ejecutor no ve la conversacion del chat.
- El productor no escribe ordenes destructivas (push, delete, reset) sin acuerdo previo
  en el chat. La bandeja es texto plano: siempre se puede leer antes de que corra.
- Si el observer no esta corriendo, las ordenes se acumulan y se ejecutan al arrancarlo.
- `ordenes/`, `procesadas/`, `resultados/`, `log.txt` y `proyecto.local.txt` son runtime:
  no se versionan. La herramienta si. Las carpetas las crea `instalar_skills.py`.
