# Bandeja - capa IA Operativa

Canal entre el productor (chat de Cowork) y los ejecutores (Claude Code en Windows).
Patron observer: el productor publica una orden, el observer la escucha y la ejecuta,
el resultado vuelve al buzon.

## Como se arranca

En una consola de PowerShell, una vez por sesion de trabajo:

    cd "D:\git\Vaultrum\04_IA Operativa\Herramientas\bandeja"
    .\observer.ps1

Parametros opcionales:
    -Proyecto  "D:\git\Project-Forge"   carpeta donde corre claude (default)
    -Intervalo 5                          segundos entre chequeos
    -Permisos  acceptEdits                modo de permisos de Claude Code
    -Continuar                            mantiene el contexto entre ordenes

Para cortar: Ctrl+C, o crear el archivo stop.txt en esta carpeta.

## Como funciona

    ordenes/     el productor deja aca los .md  -> el observer los toma en orden alfabetico
    procesadas/  la orden se mueve aca apenas empieza a ejecutarse (no se repite nunca)
    resultados/  <nombre>.result.md con la salida completa
    log.txt      una linea por orden: cuando, cual, cuanto tardo

## Reglas

- Una orden = un archivo .md autocontenido. El ejecutor no ve la conversacion del chat.
- El productor no escribe ordenes destructivas (push, delete, reset) sin acuerdo previo
  en el chat. La bandeja es texto plano: siempre se puede leer antes de que corra.
- Si el observer no esta corriendo, las ordenes se acumulan y se ejecutan al arrancarlo.
