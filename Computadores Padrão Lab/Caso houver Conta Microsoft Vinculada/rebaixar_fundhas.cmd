@echo off
echo Removendo Fundhas do grupo de administradores...
net localgroup Administradores Fundhas /del
if %errorlevel%==0 (
    echo ✅ Fundhas agora é um usuário padrão.
    timeout /t 3 >nul
    echo Saindo da sessão para aplicar alterações...
    shutdown /l
) else (
    echo ❌ Ocorreu um erro ao tentar remover Fundhas do grupo de administradores.
    pause
)
