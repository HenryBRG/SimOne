# SimOne



🧹 SCRIPT DE LIMPEZA



📌 OBJETIVO:
-----------------------------------
Este script foi criado para realizar uma LIMPEZA COMPLETA nos notebooks dos alunos de forma rápida e automatizada, direto de um pendrive. Ele remove contas logadas em navegadores, apaga arquivos inúteis e desinstala programas desnecessários.


-------------------------------
✅ O QUE O SCRIPT FAZ
-------------------------------

1. FECHA NAVEGADORES:
   - Chrome
   - Edge
   - Firefox

2. REMOVE PERFIS DE USUÁRIO DOS NAVEGADORES:
   - Apaga dados salvos, histórico, extensões e CONTA LOGADA

3. LIMPA PASTAS TEMPORÁRIAS:
   - C:\Users\[usuário]\AppData\Local\Temp
   - C:\Windows\Temp
   - C:\Users\[usuário]\Downloads

4. REMOVE ARQUIVOS INÚTEIS:
   - Arquivos com extensões: `.tmp`, `.log`, `.bak`

5. DESINSTALA PROGRAMAS DESNECESSÁRIOS:
   - McAfee
   - WildTangent
   - ByteFence
   - Opera
   - Avast
   - AVG

6. GERA UM ARQUIVO DE LOG:
   - `log_limpeza.txt` (no mesmo local do executável)
   - Mostra tudo o que foi feito, com horário

-------------------------------
🚀 COMO USAR
-------------------------------

1. Copie o arquivo `script_limpeza_alunos.exe` e o `README.txt` para um pendrive
2. Plugue o pendrive no notebook do aluno
3. Clique com o botão direito no `script_limpeza_alunos.exe` e escolha **"Executar como administrador"**
4. Aguarde o processo — ele mostrará tudo no console
5. Ao final, o log será salvo automaticamente

⚠️ IMPORTANTE:
- O script só funciona com permissão de administrador
- Não precisa instalar nada (é um arquivo `.exe`)
- Os navegadores serão reiniciados e saem das contas logadas

-------------------------------
📝 LOG DE AÇÕES (EXEMPLO)
-------------------------------

[10:15:32] 🧹 INÍCIO DA LIMPEZA
[10:15:34] 🧽 Limpando perfis do Chrome
[10:15:35] ✅ Perfis do Chrome removidos com sucesso.
[10:15:36] 🧽 Limpando perfis do Edge
[10:15:37] ✅ Perfis do Edge removidos com sucesso.
[10:15:38] 🧽 Limpando perfis do Firefox
[10:15:39] ✅ Perfis do Firefox removidos com sucesso.
[10:15:40] 🧼 Limpando: C:\Users\Aluno\AppData\Local\Temp
[10:15:42] 🧼 Limpando: C:\Windows\Temp
[10:15:44] 🧼 Limpando: C:\Users\Aluno\Downloads
[10:15:46] 🗑️ Removido: C:\Users\Aluno\arquivo1.tmp
[10:15:47] 📦 Tentando remover: McAfee
[10:15:48] 📦 Tentando remover: Avast
[10:15:49] ✅ LIMPEZA FINALIZADA!
