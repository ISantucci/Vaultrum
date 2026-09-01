#requires -version 5
<#
    Observer Vaultrum - capa IA Operativa

    Canal entre el productor (la conversacion donde se decide) y los ejecutores
    que tienen manos (Claude Code en esta maquina). El productor deja una orden
    en ordenes/, el observer la ejecuta parado en el proyecto, y la salida
    vuelve a resultados/.

    POR QUE ESTE ARCHIVO NO TIENE RUTAS FIJAS
    La primera version traia "D:\git\Vaultrum" y "D:\git\Project-Forge" como
    defaults. Eso hace que la herramienta funcione en la maquina donde se
    escribio y en ninguna otra: en otra PC el mismo repo vive en otro lado y el
    observer arranca apuntando a una carpeta que no existe. Es exactamente el
    defecto que skills.bat ya habia resuelto -- se ubica solo, y verifica que
    esta parado en un Vaultrum de verdad buscando 00_START_HERE.md.

    Aca se aplica la misma regla:
      - la bandeja sale de donde vive ESTE archivo ($PSScriptRoot);
      - la raiz del vault se busca hacia arriba, por 00_START_HERE.md;
      - el proyecto NO se adivina: es un dato de esta maquina, y vive en
        proyecto.local.txt (que no se versiona, igual que .owner.local.json).

    Y la otra regla del Core, `La superficie del ejecutor`: antes de gastar una
    ejecucion se comprueba que se PUEDE ejecutar -- que claude existe, que el
    proyecto existe, que se puede escribir el resultado. Y lo que falla vuelve
    como FALLO, no como nota al pie: por eso el resultado guarda el exit code.

    Codigos de salida:
      1  la bandeja no esta dentro de un Vaultrum (falta 00_START_HERE.md)
      2  no hay proyecto declarado, o la ruta declarada no existe
      3  el ejecutor pedido no esta en el PATH de esta consola
      4  no se puede escribir en resultados/
      5  el ejecutor pedido no tiene perfil de invocacion declarado
#>
[CmdletBinding()]
param(
    [string]$Bandeja   = '',
    [string]$Proyecto  = '',
    [int]   $Intervalo = 5,
    [string]$Permisos  = 'acceptEdits',
    [string]$Ejecutor  = 'claude',
    [switch]$Continuar
)

$ErrorActionPreference = 'Stop'

function Fallar([string]$mensaje, [string[]]$detalle, [int]$codigo) {
    Write-Host ''
    Write-Host "  [X] $mensaje" -ForegroundColor Red
    foreach ($d in $detalle) { Write-Host "      $d" -ForegroundColor DarkGray }
    Write-Host ''
    exit $codigo
}

# --- 1. donde estoy -----------------------------------------------------------
# $PSScriptRoot es la carpeta de este .ps1. Si alguien lo corre por dot-sourcing
# raro y queda vacio, se cae a la carpeta actual antes de rendirse.
if (-not $Bandeja) { $Bandeja = $PSScriptRoot }
if (-not $Bandeja) { $Bandeja = (Get-Location).Path }
if (-not (Test-Path -LiteralPath $Bandeja)) {
    Fallar "No existe la bandeja: $Bandeja" @() 1
}
$Bandeja = (Resolve-Path -LiteralPath $Bandeja).Path

# La raiz del vault se busca hacia arriba, no se declara. Mismo criterio que
# skills.bat: 00_START_HERE.md es la firma de un Vaultrum.
$Raiz = $null
$dir  = Get-Item -LiteralPath $Bandeja
while ($dir -ne $null) {
    if (Test-Path -LiteralPath (Join-Path $dir.FullName '00_START_HERE.md')) {
        $Raiz = $dir.FullName
        break
    }
    $dir = $dir.Parent
}
if (-not $Raiz) {
    Fallar 'Esto no parece estar dentro de un Vaultrum.' @(
        "Busque 00_START_HERE.md desde: $Bandeja",
        'Corre observer.bat desde 04_IA Operativa\Herramientas\bandeja\ del vault.'
    ) 1
}

$ordenes    = Join-Path $Bandeja 'ordenes'
$resultados = Join-Path $Bandeja 'resultados'
$procesadas = Join-Path $Bandeja 'procesadas'
foreach ($d in @($ordenes, $resultados, $procesadas)) {
    if (-not (Test-Path -LiteralPath $d)) { New-Item -ItemType Directory -Path $d | Out-Null }
}

# --- 2. contra que proyecto corro ---------------------------------------------
# Una ruta relativa se resuelve contra la carpeta que CONTIENE al vault: los
# proyectos son hermanos del vault, no hijos (nada se escribe adentro de Vaultrum).
function Resolver-Proyecto([string]$ruta) {
    $ruta = $ruta.Trim().Trim('"')
    if (-not $ruta) { return '' }
    if (-not [System.IO.Path]::IsPathRooted($ruta)) {
        $ruta = Join-Path (Split-Path -Parent $Raiz) $ruta
    }
    return [System.IO.Path]::GetFullPath($ruta)
}

$configProyecto = Join-Path $Bandeja 'proyecto.local.txt'
$origenProyecto = 'parametro -Proyecto'
if (-not $Proyecto -and (Test-Path -LiteralPath $configProyecto)) {
    $linea = Get-Content -LiteralPath $configProyecto |
             Where-Object { $_.Trim() -ne '' -and -not $_.TrimStart().StartsWith('#') } |
             Select-Object -First 1
    if ($linea) {
        $Proyecto = $linea
        $origenProyecto = 'proyecto.local.txt'
    }
}
if (-not $Proyecto) {
    Fallar 'No se contra que proyecto ejecutar las ordenes.' @(
        'Es un dato de ESTA maquina, no del repo. Dos formas:',
        '',
        "  1) crea $configProyecto con la ruta del proyecto adentro",
        '  2) o pasala al arrancar:  .\observer.bat -Proyecto "C:\ruta\al\proyecto"',
        '',
        'Una ruta sin unidad se toma como hermana del vault.'
    ) 2
}
$Proyecto = Resolver-Proyecto $Proyecto
if (-not (Test-Path -LiteralPath $Proyecto)) {
    Fallar "No existe la carpeta del proyecto: $Proyecto" @("(declarada en: $origenProyecto)") 2
}

# --- 3. superficie: puedo ejecutar de verdad? ---------------------------------
# El ejecutor se resuelve por nombre y no esta cableado: la bandeja despacha a
# Claude Code por defecto, y una orden puede pedir otro con "Ejecutor: <nombre>".
# El nombre se valida contra un patron simple ANTES de buscarlo: una orden es
# texto plano que puede escribir cualquiera, y de ahi no sale una ruta ni un
# argumento suelto. Si el binario no esta, la orden vuelve en FALLO de
# superficie y no se ejecuta nada -- que es lo correcto, no un bug.
# CADA EJECUTOR SE INVOCA DISTINTO, Y ESO SE DECLARA ACA
#
# La primera version resolvia el ejecutor por nombre y le pasaba SIEMPRE los
# flags de Claude Code. Con "Ejecutor: codex" eso ejecutaba
#   codex -p --permission-mode acceptEdits
# que no es como se invoca codex. El test no lo vio porque el ejecutor falso
# ignoraba sus argumentos: probaba el ruteo, no la invocacion.
#
# Ahora un ejecutor sin perfil NO se despacha, aunque este en el PATH. La lista
# de perfiles es la unica autoridad de como se llama a cada uno, y agregar un
# ejecutor es agregar su perfil -- no basta con instalarlo.
#
#   claude   claude -p --permission-mode <modo> [--continue]     prompt por stdin
#   codex    codex exec - --sandbox <read-only|workspace-write>  prompt por stdin
#            `exec -` es la forma oficial de que stdin SEA el prompt.
#            Fuente: developers.openai.com/codex -> Non-interactive mode.
#
# El modo de permisos se declara una vez en vocabulario de Claude (-Permisos) y
# se traduce por ejecutor: no se le pide al owner que sepa dos vocabularios.
function Perfil-Ejecutor([string]$nombre, [string]$permisos, [bool]$continuar) {
    $escribe = @('acceptEdits', 'bypassPermissions', 'acceptAll') -contains $permisos
    switch ($nombre) {
        'claude' {
            $a = @('-p', '--permission-mode', $permisos)
            if ($continuar) { $a += '--continue' }
            return @{ args = $a; continuidad = $true }
        }
        'codex' {
            $caja = if ($escribe) { 'workspace-write' } else { 'read-only' }
            return @{ args = @('exec', '-', '--sandbox', $caja); continuidad = $false }
        }
    }
    return $null
}

function Resolver-Ejecutor([string]$nombre) {
    $nombre = $nombre.Trim().Trim('"')
    if ($nombre -notmatch '^[A-Za-z][\w.-]*$') { return $null }
    return Get-Command $nombre -ErrorAction SilentlyContinue
}

if (-not (Perfil-Ejecutor $Ejecutor $Permisos $Continuar.IsPresent)) {
    Fallar "No tengo perfil de invocacion para '$Ejecutor'." @(
        'Un ejecutor sin perfil no se despacha, aunque este instalado: no se',
        'inventa como se lo llama. Perfiles declarados: claude, codex.'
    ) 5
}
$cmdEjecutor = Resolver-Ejecutor $Ejecutor
if (-not $cmdEjecutor) {
    Fallar "No encontre '$Ejecutor' en el PATH de esta consola." @(
        'Instala el ejecutor, o abri la consola donde el comando exista.'
    ) 3
}
$prueba = Join-Path $resultados '.superficie.tmp'
try {
    Set-Content -LiteralPath $prueba -Value 'ok' -Encoding UTF8
    Remove-Item -LiteralPath $prueba -Force
} catch {
    Fallar "No puedo escribir en $resultados" @(
        'Una orden que corre y no puede dejar su resultado vuelve como exito vacio.'
    ) 4
}

Write-Host ''
Write-Host '=== Observer Vaultrum ===' -ForegroundColor Cyan
Write-Host "  vault    : $Raiz"
Write-Host "  bandeja  : $Bandeja"
Write-Host "  proyecto : $Proyecto   ($origenProyecto)"
Write-Host "  ejecutor : $Ejecutor -> $($cmdEjecutor.Source)"
Write-Host "  permisos : $Permisos    continuar: $($Continuar.IsPresent)"
Write-Host '  Ctrl+C para cortar, o crea stop.txt en la bandeja.'
Write-Host ''

# --- 4. el loop ---------------------------------------------------------------
while ($true) {
    $stop = Join-Path $Bandeja 'stop.txt'
    if (Test-Path -LiteralPath $stop) {
        Write-Host 'stop.txt encontrado. Cierro.' -ForegroundColor Yellow
        Remove-Item -LiteralPath $stop -Force
        break
    }

    $pendientes = @(Get-ChildItem -LiteralPath $ordenes -Filter *.md -File -ErrorAction SilentlyContinue | Sort-Object Name)

    foreach ($orden in $pendientes) {
        $nombre = [System.IO.Path]::GetFileNameWithoutExtension($orden.Name)
        $inicio = Get-Date
        $texto  = Get-Content -LiteralPath $orden.FullName -Raw -Encoding UTF8

        # Una orden puede declarar su propia superficie con una linea
        # "Proyecto: <ruta>" en las primeras 10 lineas. Si no, corre en el
        # proyecto por defecto de esta maquina.
        $destino = $Proyecto
        $cabecera = (($texto -split "`r?`n") | Select-Object -First 10) -join "`n"
        $m = [regex]::Match($cabecera, '(?im)^\s*(?:<!--\s*)?proyecto\s*:\s*(.+?)\s*(?:-->)?\s*$')
        if ($m.Success) { $destino = Resolver-Proyecto $m.Groups[1].Value }

        # ...y su ejecutor. Queda registrado en el log aunque sea el de siempre:
        # sin esa columna, despacho.py puede contar cuantas ejecuciones hubo
        # pero no a quien fueron, que es justo la pregunta del criterio.
        $nombreEjec = $Ejecutor
        $cmdOrden   = $cmdEjecutor
        $me = [regex]::Match($cabecera, '(?im)^\s*(?:<!--\s*)?ejecutor\s*:\s*(.+?)\s*(?:-->)?\s*$')
        if ($me.Success) {
            $nombreEjec = $me.Groups[1].Value.Trim()
            $cmdOrden   = Resolver-Ejecutor $nombreEjec
        }
        $perfil = Perfil-Ejecutor $nombreEjec $Permisos $Continuar.IsPresent

        Write-Host ''
        Write-Host ("[{0}] ejecutando {1}" -f $inicio.ToString('HH:mm:ss'), $orden.Name) -ForegroundColor Green
        if ($destino -ne $Proyecto)   { Write-Host "      proyecto declarado en la orden: $destino" -ForegroundColor DarkGray }
        if ($nombreEjec -ne $Ejecutor) { Write-Host "      ejecutor declarado en la orden: $nombreEjec" -ForegroundColor DarkGray }

        # Se mueve ANTES de ejecutar: una orden no se repite nunca, ni aunque
        # la corrida muera a la mitad.
        Move-Item -LiteralPath $orden.FullName -Destination (Join-Path $procesadas $orden.Name) -Force

        if (-not (Test-Path -LiteralPath $destino)) {
            $salida = "FALLO de superficie: la orden declara el proyecto '$destino' y esa carpeta no existe.`r`nNo se ejecuto nada."
            $codigo = 2
        } elseif (-not $cmdOrden) {
            $salida = "FALLO de superficie: la orden declara el ejecutor '$nombreEjec' y no esta en el PATH de esta consola.`r`nNo se ejecuto nada."
            $codigo = 3
        } elseif (-not $perfil) {
            $salida = "FALLO de superficie: no tengo perfil de invocacion para '$nombreEjec'.`r`nEsta en el PATH, pero no se inventa como se lo llama. Perfiles declarados: claude, codex.`r`nNo se ejecuto nada."
            $codigo = 5
        } elseif ($Continuar -and -not $perfil.continuidad) {
            # Declarar y frenar. Correr sin continuidad seria devolver un
            # resultado distinto del pedido y avisarlo al pie, que es
            # exactamente el fallo que se disfraza de exito.
            $salida = "FALLO de superficie: la corrida pide -Continuar y el perfil de '$nombreEjec' no sostiene contexto entre ordenes.`r`nSacale -Continuar, o mandala al ejecutor que si lo sostiene.`r`nNo se ejecuto nada."
            $codigo = 5
        } else {
            $argumentos = $perfil.args
            Push-Location -LiteralPath $destino
            try {
                $salida = ($texto | & $cmdOrden.Name @argumentos 2>&1 | Out-String)
                $codigo = $LASTEXITCODE
            } catch {
                $salida = "ERROR ejecutando ${nombreEjec}: $_"
                $codigo = 1
            } finally {
                Pop-Location
            }
        }
        if ($null -eq $codigo) { $codigo = 0 }

        # El estado va en el resultado y en el log. Un ejecutor que no pudo
        # hacer algo lo reporta como FALLO, no como nota al pie.
        $estado   = if ($codigo -eq 0) { 'OK' } else { "FALLO (exit $codigo)" }
        $segundos = [int]((Get-Date) - $inicio).TotalSeconds
        $encabezado = @(
            "# Resultado de $($orden.Name)",
            '',
            "Estado: $estado  |  Duracion: ${segundos}s  |  Fecha: $((Get-Date).ToString('yyyy-MM-dd HH:mm:ss'))",
            "Proyecto: $destino",
            "Ejecutor: $nombreEjec",
            '',
            '---',
            '',
            ''
        ) -join "`r`n"
        Set-Content -LiteralPath (Join-Path $resultados "$nombre.result.md") -Value ($encabezado + $salida) -Encoding UTF8
        # Formato del log, que es lo que lee despacho.py:
        #   <fecha> <hora>  <orden>  <ejecutor>  <seg>s  <estado>
        Add-Content -LiteralPath (Join-Path $Bandeja 'log.txt') -Value ("{0}  {1}  {2}  {3}s  {4}" -f $inicio.ToString('yyyy-MM-dd HH:mm:ss'), $orden.Name, $nombreEjec, $segundos, $estado)

        $color = if ($codigo -eq 0) { 'Green' } else { 'Red' }
        Write-Host ("      $estado en ${segundos}s -> resultados\$nombre.result.md") -ForegroundColor $color
    }

    Start-Sleep -Seconds $Intervalo
}
