# 🧹 SimOne — Script de Limpeza Avançada (Versão Final)

---

## 📌 OBJETIVO

O **SimOne** é um script criado para **limpar completamente os notebooks dos alunos** da escola técnica, de forma rápida e automatizada, diretamente de um pendrive.  
Ele **remove arquivos inúteis**, **desinstala programas desnecessários**, **desloga contas**, **organiza a área de trabalho** e **restaura o ambiente limpo para o próximo aluno**.

---

## ✅ O QUE O SCRIPT FAZ

### 1. Fecha Navegadores:
- Chrome  
- Edge  
- Firefox  

---

### 2. Remove Perfis de Navegadores:
- Apaga dados de usuário (cookies, histórico, senhas, cache)
- **Remove contas logadas** nos navegadores

---

### 3. Limpa Pastas Temporárias:
- `C:\\Users\\Fundhas\\AppData\\Local\\Temp`  
- `C:\\Windows\\Temp`  
- `C:\\Users\\Fundhas\\Downloads`  

---

### 4. Apaga Arquivos Inúteis:
- Arquivos com extensões `.tmp`, `.log`, `.bak`  
- Busca recursivamente dentro da pasta `C:\\Users\\Fundhas`

---

### 5. Remove Pastas Desconhecidas de `AppData\\Local`:
- Apaga todas as pastas **exceto** uma lista segura com 22 pastas essenciais  
  (ex: `Microsoft`, `Google`, `Lenovo`, `Packages`, etc.)

---

### 6. Limpa Diretórios Pessoais:
- Apaga todos os arquivos das pastas:
  - `Documentos`  
  - `Imagens`  
  - `Vídeos`  

---

### 7. Limpa e Organiza a Área de Trabalho:
- Remove **todos os arquivos** da Área de Trabalho  
- Mantém apenas os **atalhos autorizados**, como:
  - Lixeira  
  - Scratch 3  
  - VLC  
  - AutoCAD 2024  
  - LibreOffice  
  - Microsoft Edge  
  - etc.  
- Reorganiza os atalhos restantes automaticamente

---

### 8. Remove Programas Indesejados:
- Tenta desinstalar automaticamente:
  - McAfee  
  - WildTangent  
  - ByteFence  
  - Opera  
  - Avast  
  - AVG  

---

### 9. Gera Log de Limpeza:
- `log_limpeza.txt` salvo ao lado do executável  
- Mostra cada ação com horário e status

---

## ⚙️ PROCEDIMENTO PARA REMOVER CONTA MICROSOFT

A remoção da conta Microsoft conectada **não é automática** (por limitações do sistema).  
Por isso, um processo **manual e controlado** é utilizado:

### Scripts envolvidos:
- `elevar_fundhas.bat`: Torna o usuário `Fundhas` administrador temporariamente  
- `rebaixar_fundhas.bat`: Retorna o `Fundhas` para conta padrão

### Etapas manuais:

1. No usuário **Fundhas**, execute `elevar_fundhas.bat`  
2. O script faz o logout da conta, logo após entre novamente em **Fundhas**.
3. Agora com acesso total às configurações:
   - Vá em: ⚙️ Configurações > Contas > E-mail e contas  
   - Remova a conta Microsoft vinculada  
4. Depois, execute `rebaixar_fundhas.bat`  
   - Isso impede que o aluno continue com privilégios de administrador  

---

## 🧪 COMO USAR

1. Copie os arquivos abaixo para um pendrive:
   - `script_limpeza_alunos.exe`  
   - `elevar_fundhas.bat`  
   - `rebaixar_fundhas.bat`   
2. No notebook do aluno:
   - Execute `elevar_fundhas.bat` pelo **usuário Fundhas**
   - Reinicie e entre no **usuário Fundhas**
3. Remova a conta Microsoft (se existir)
4. Execute `script_limpeza_alunos.exe` como administrador
5. Ao final, execute `rebaixar_fundhas.bat`
6. Pronto! Máquina limpa e segura para o próximo uso

---

## 📝 EXEMPLO DE LOG

[10:15:32] 🧹 INÍCIO DA LIMPEZA
[10:15:34] 🧽 Limpando perfis do Chrome
[10:15:35] ✅ Perfis do Chrome removidos com sucesso.
[10:15:40] 🧼 Limpando: C:\Users\Fundhas\AppData\Local\Temp
[10:15:44] 🧼 Limpando: C:\Windows\Temp
[10:15:47] 🧼 Limpando: C:\Users\Fundhas\Downloads
[10:15:50] 🗑️ Arquivo removido: C:\Users\Fundhas\arquivo1.tmp
[10:15:53] 🧹 Limpando AppData\Local
[10:15:55] 🧹 Removendo atalho: Discord.lnk
[10:15:58] 📦 Tentando remover: Avast
[10:16:00] ✅ LIMPEZA FINALIZADA!

yaml
Mostrar sempre detalhes

Copiar

---


## 🛡️ IMPORTANTE

- Script exige permissão de administrador  
- Ideal para rodar direto do pendrive  
- **Não requer instalação** nem internet

---


📦 Feito por **Gustavo Henrique Braga**  
🎓 Projeto aplicado para suporte técnico em ambiente escolar 