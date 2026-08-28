@echo off
cd /d "%~dp0"

rem ============================================================================
rem  Vaultrum - instalador de skills            RQ-007.7 . Portabilidad
rem ----------------------------------------------------------------------------
rem  Esto es un envoltorio. La logica vive en un solo lugar, en Python, y es la
rem  misma en Windows, macOS y Linux:
rem      02_Agencia\Area arquitectura\Herramientas\instalar_skills.py
rem
rem  La version anterior de este .bat implementaba la sincronizacion a mano y
rem  tenia un defecto que no avisaba: borraba los dos destinos ANTES de copiar,
rem  y el nombre de la skill se le resolvia al de una carpeta ancestro. Borraba
rem  las once skills y despues copiaba el repo entero dentro de .claude\skills\,
rem  recursivamente. Desde afuera parecia que no hacia nada.
rem ============================================================================

set "SCRIPT=02_Agencia\Area arquitectura\Herramientas\instalar_skills.py"

if not exist "00_START_HERE.md" goto :no_raiz
if not exist "%SCRIPT%" goto :no_script

python --version >nul 2>&1
if not errorlevel 1 goto :con_python
py --version >nul 2>&1
if not errorlevel 1 goto :con_py
goto :no_python

:con_python
python "%SCRIPT%" "%CD%" %*
goto :fin

:con_py
py "%SCRIPT%" "%CD%" %*
goto :fin

:no_raiz
echo.
echo  [ERROR] Esto no parece la raiz de Vaultrum.
echo          Corre skills.bat desde la carpeta que contiene 00_START_HERE.md
goto :fin

:no_script
echo.
echo  [ERROR] No encuentro %SCRIPT%
goto :fin

:no_python
echo.
echo  [ERROR] No encontre Python en el PATH ^(probe "python" y "py"^).
echo          Instalalo desde python.org y volve a correr esto.

:fin
echo.
pause
