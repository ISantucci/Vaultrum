@echo off
cd /d "%~dp0"

rem ============================================================================
rem  Vaultrum - instalador del entorno          RQ-007.7 . Portabilidad
rem  Sincroniza las skills a los dos directorios de descubrimiento, instala el
rem  gate de cierre, prepara la bandeja y VERIFICA que el entorno pueda trabajar.
rem  Envoltorio. La logica vive en un solo lugar y es la misma en las tres
rem  plataformas:  02_Agencia\Area arquitectura\Herramientas\instalar_skills.py
rem  Este .bat solo elige el interprete, PROPAGA EL CODIGO DE SALIDA y espera.
rem ============================================================================

set "SCRIPT=02_Agencia\Area arquitectura\Herramientas\instalar_skills.py"
set "RC=1"

if not exist "00_START_HERE.md" goto :no_raiz
if not exist "%SCRIPT%" goto :no_script

python --version >nul 2>&1
if not errorlevel 1 goto :con_python
py --version >nul 2>&1
if not errorlevel 1 goto :con_py
goto :no_python

:con_python
python "%SCRIPT%" "%CD%" %*
set "RC=%ERRORLEVEL%"
goto :fin

:con_py
py "%SCRIPT%" "%CD%" %*
set "RC=%ERRORLEVEL%"
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

:fin
echo.
if not "%RC%"=="0" echo  [!] El instalador termino con codigo %RC%.
rem  El pause es para que la ventana no se cierre sola con doble clic, pero NO
rem  se traga el codigo: quien lo llame desde un script recibe el de verdad.
pause
exit /b %RC%
