@echo off
echo Tornando o usuário Fundhas um administrador...
net localgroup Administradores Fundhas /add
if %errorlevel%==0 (
    echo ✅ Fundhas agora é administrador.
    timeout /t 3 >nul
    echo Saindo da sessão para aplicar alterações...
    shutdown /l
) else (
    echo ❌ Ocorreu um erro ao tentar promover Fundhas.
    pause
)
