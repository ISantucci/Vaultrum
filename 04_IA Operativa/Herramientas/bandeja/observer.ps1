#requires -version 5
[CmdletBinding()]
param(
    [string]$Bandeja  = "D:\git\Vaultrum\04_IA Operativa\Herramientas\bandeja",
    [string]$Proyecto = "D:\git\Project-Forge",
    [int]$Intervalo   = 5,
    [string]$Permisos = "acceptEdits",
    [switch]$Continuar
)

$ErrorActionPreference = "Stop"

$ordenes    = Join-Path $Bandeja "ordenes"
$resultados = Join-Path $Bandeja "resultados"
$procesadas = Join-Path $Bandeja "procesadas"
foreach ($d in @($Bandeja, $ordenes, $resultados, $procesadas)) {
    if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d | Out-Null }
}

$claude = Get-Command claude -ErrorAction SilentlyContinue
if (-not $claude) {
    Write-Host "[X] No encontre 'claude' en el PATH de esta consola." -ForegroundColor Red
    Write-Host "    Instala Claude Code o abri la consola donde el comando exista." -ForegroundColor Red
    exit 1
}
if (-not (Test-Path $Proyecto)) {
    Write-Host "[X] No existe la carpeta del proyecto: $Proyecto" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "=== Observer Vaultrum ===" -ForegroundColor Cyan
Write-Host "  bandeja  : $Bandeja"
Write-Host "  proyecto : $Proyecto"
Write-Host "  claude   : $($claude.Source)"
Write-Host "  permisos : $Permisos    continuar: $($Continuar.IsPresent)"
Write-Host "  Ctrl+C para cortar, o crea stop.txt en la bandeja."
Write-Host ""

while ($true) {
    $stop = Join-Path $Bandeja "stop.txt"
    if (Test-Path $stop) {
        Write-Host "stop.txt encontrado. Cierro." -ForegroundColor Yellow
        Remove-Item $stop -Force
        break
    }

    $pendientes = @(Get-ChildItem -Path $ordenes -Filter *.md -File -ErrorAction SilentlyContinue | Sort-Object Name)

    foreach ($orden in $pendientes) {
        $nombre = [IO.Path]::GetFileNameWithoutExtension($orden.Name)
        $inicio = Get-Date
        Write-Host ""
        Write-Host ("[{0}] ejecutando {1}" -f $inicio.ToString("HH:mm:ss"), $orden.Name) -ForegroundColor Green

        $texto = Get-Content -Path $orden.FullName -Raw -Encoding UTF8
        Move-Item -Path $orden.FullName -Destination (Join-Path $procesadas $orden.Name) -Force

        $argumentos = @("-p", "--permission-mode", $Permisos)
        if ($Continuar) { $argumentos += "--continue" }

        Push-Location $Proyecto
        try {
            $salida = ($texto | & claude @argumentos 2>&1 | Out-String)
        } catch {
            $salida = "ERROR ejecutando claude: $_"
        } finally {
            Pop-Location
        }

        $segundos = [int]((Get-Date) - $inicio).TotalSeconds
        $encabezado = "# Resultado de $($orden.Name)`r`nFecha: $((Get-Date).ToString('yyyy-MM-dd HH:mm:ss'))  |  Duracion: ${segundos}s`r`n`r`n---`r`n`r`n"
        Set-Content -Path (Join-Path $resultados "$nombre.result.md") -Value ($encabezado + $salida) -Encoding UTF8
        Add-Content -Path (Join-Path $Bandeja "log.txt") -Value ("{0}  {1}  {2}s" -f $inicio.ToString("yyyy-MM-dd HH:mm:ss"), $orden.Name, $segundos)

        Write-Host ("      listo en ${segundos}s -> resultados\$nombre.result.md") -ForegroundColor Green
    }

    Start-Sleep -Seconds $Intervalo
}
