@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"

rem ============================================================================
rem  Vaultrum - instalador de skills            RQ-007.7 . Portabilidad
rem ----------------------------------------------------------------------------
rem  Las skills VIVEN en su area. Eso es lo que las hace parte del sistema.
rem  Este script las SINCRONIZA a los dos directorios donde los asistentes las
rem  descubren solos. No es una mudanza: es una copia, y la fuente sigue siendo
rem  el area.
rem
rem      02_Agencia\Area X\Skills\vaultrum-X\SKILL.md      <-- la fuente
rem              |
rem              +--> .claude\skills\vaultrum-X\           Claude Code
rem              +--> .agents\skills\vaultrum-X\           Codex, Cursor, Zed, Copilot
rem
rem  Es idempotente: corrlo todas las veces que quieras.
rem  Las copias NUNCA se editan a mano. Se edita el area y se vuelve a correr.
rem ============================================================================

echo.
echo  VAULTRUM - instalador de skills
echo  ===============================
echo.

if not exist "00_START_HERE.md" (
  echo  [ERROR] Esto no parece la raiz de Vaultrum.
  echo          Corre skills.bat desde la carpeta que contiene 00_START_HERE.md
  echo.
  pause
  exit /b 1
)

rem --- destinos: se regeneran enteros para que un borrado en el area se propague
for %%T in (".claude\skills" ".agents\skills") do (
  if exist "%%~T" rmdir /s /q "%%~T"
  mkdir "%%~T" >nul 2>&1
)

set /a N=0
for /r "%CD%" %%F in (SKILL.md) do (
  set "SRC=%%~dpF"
  echo !SRC! | findstr /i /c:"\.claude\\" /c:"\.agents\\" /c:"\.git\\" >nul
  if errorlevel 1 (
    for %%D in ("!SRC!.") do set "NAME=%%~nxD"
    robocopy "!SRC!." ".claude\skills\!NAME!" /E /NJH /NJS /NP /NDL /NFL /NC /NS >nul
    robocopy "!SRC!." ".agents\skills\!NAME!" /E /NJH /NJS /NP /NDL /NFL /NC /NS >nul
    set /a N+=1
    echo   [ok] !NAME!
  )
)

rem --- marca de generado, para que nadie edite las copias
for %%T in (".claude\skills" ".agents\skills") do (
  >"%%~T\_GENERADO_NO_EDITAR.txt" echo Generado por skills.bat desde 02_Agencia\Area *\Skills\ y las capas 03/04/05.
  >>"%%~T\_GENERADO_NO_EDITAR.txt" echo Editar aca no cambia el sistema: se pisa en la proxima corrida.
  >>"%%~T\_GENERADO_NO_EDITAR.txt" echo Para cambiar una skill, edita su fuente en el area y volve a correr skills.bat.
)

echo.
echo   %N% skills sincronizadas a .claude\skills y .agents\skills
echo.

rem --- presupuesto de contexto: lo unico que queda residente es el frontmatter.
rem     Claude Code topea 1536 caracteres por description; Codex 8000 en total.
where powershell >nul 2>&1
if errorlevel 1 goto :fin

echo   Presupuesto de contexto (solo name + description quedan residentes):
powershell -NoProfile -Command ^
  "$t=0; $mx=0; $bad=@();" ^
  "Get-ChildItem -Path .claude\skills -Recurse -Filter SKILL.md | ForEach-Object {" ^
  "  $c=Get-Content $_.FullName -Raw;" ^
  "  if($c -match (?ms)^description:\s*\"(.*?)\"\s*$){ $d=$Matches[1].Length; $t+=$d;" ^
  "    if($d -gt $mx){$mx=$d}; if($d -gt 1536){$bad+=$_.Directory.Name} } };" ^
  "Write-Host (     total residente : {0} chars  (tope Codex 8000) -f $t);" ^
  "Write-Host (     la mas larga    : {0} chars  (tope Claude Code 1536) -f $mx);" ^
  "if($bad.Count -gt 0){ Write-Host      [AVISO] pasan el tope:  $bad } else { Write-Host      [ok] ninguna pasa el tope };" ^
  "if($t -gt 8000){ Write-Host      [AVISO] el total pasa el tope de Codex }"

:fin
echo.
rem ---------------------------------------------------------------------------
rem  Gate de cierre: .git\hooks NO viaja en un clone, asi que el hook se instala
rem  aca desde su fuente versionada. Sin esto, un clone no tiene gate.
set "HOOK_SRC=02_Agencia\Area arquitectura\Herramientas\pre-commit"
if exist ".git" if exist "%HOOK_SRC%" (
  if not exist ".git\hooks" mkdir ".git\hooks"
  copy /y "%HOOK_SRC%" ".git\hooks\pre-commit" >nul
  echo   [ok] gate de cierre instalado en .git\hooks\pre-commit
)

echo   Listo. Abri una sesion nueva para que el asistente las descubra.
echo.
endlocal
