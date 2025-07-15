@echo off
:: Caminho relativo para o executável
set EXE=limpeza.exe

:: Verifica se está sendo executado como admin
net session >nul 2>&1
if %errorlevel% == 0 (
    echo [✓] Executando como administrador...
    %EXE%
) else (
    echo [!] Solicitando permissões de administrador...
    powershell -Command "Start-Process '%EXE%' -Verb runAs"
)
exit
