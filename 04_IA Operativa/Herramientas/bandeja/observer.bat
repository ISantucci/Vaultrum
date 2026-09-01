@echo off
setlocal
title Observer Vaultrum
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0observer.ps1" %*
if errorlevel 1 (
    echo.
    echo El observer termino con error. Revisa el mensaje de arriba.
    pause
)
