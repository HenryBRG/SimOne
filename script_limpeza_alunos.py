import os
import shutil
import subprocess
import getpass
import ctypes
from pathlib import Path
from datetime import datetime

LOG_FILE = Path(__file__).parent / "log_limpeza.txt"

def log(msg):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {msg}")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {msg}\n")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def fechar_processos(processos):
    for proc in processos:
        subprocess.run(["taskkill", "/f", "/im", proc], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def limpar_navegadores():
    user = getpass.getuser()
    
    navegadores = {
        "Chrome": Path(f"C:/Users/{user}/AppData/Local/Google/Chrome/User Data"),
        "Edge": Path(f"C:/Users/{user}/AppData/Local/Microsoft/Edge/User Data"),
        "Firefox": Path(f"C:/Users/{user}/AppData/Roaming/Mozilla/Firefox/Profiles"),
    }

    fechar_processos(["chrome.exe", "msedge.exe", "firefox.exe"])

    for nome, caminho in navegadores.items():
        if caminho.exists():
            log(f"🧽 Limpando perfis do {nome}")
            try:
                shutil.rmtree(caminho, ignore_errors=True)
                log(f"✅ Perfis do {nome} removidos com sucesso.")
            except Exception as e:
                log(f"❌ Erro ao limpar {nome}: {e}")

def limpar_pastas_temp():
    user = getpass.getuser()
    pastas = [
        Path(f"C:/Users/{user}/AppData/Local/Temp"),
        Path(f"C:/Windows/Temp"),
        Path(f"C:/Users/{user}/Downloads"),
    ]
    for pasta in pastas:
        if pasta.exists():
            log(f"🧼 Limpando: {pasta}")
            for item in pasta.glob("*"):
                try:
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir():
                        shutil.rmtree(item, ignore_errors=True)
                except Exception as e:
                    log(f"❌ Erro ao remover {item}: {e}")

def remover_arquivos_lixo():
    user_path = Path(f"C:/Users/{getpass.getuser()}")
    extensoes = ['*.tmp', '*.log', '*.bak']
    for ext in extensoes:
        for file in user_path.rglob(ext):
            try:
                file.unlink()
                log(f"🗑️ Removido: {file}")
            except Exception as e:
                log(f"❌ Erro ao remover {file}: {e}")

def remover_programas_bloat(adware_list):
    for prog in adware_list:
        try:
            subprocess.run(["wmic", "product", "where", f"name like '%{prog}%'", "call", "uninstall", "/nointeractive"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            log(f"📦 Tentando remover: {prog}")
        except Exception as e:
            log(f"❌ Erro ao tentar remover {prog}: {e}")

def main():
    if not is_admin():
        log("❌ Esse script precisa ser executado como administrador.")
        input("Pressione Enter para sair...")
        return

    log("🧹 INÍCIO DA LIMPEZA")

    limpar_navegadores()
    limpar_pastas_temp()
    remover_arquivos_lixo()
    remover_programas_bloat(["McAfee", "WildTangent", "ByteFence", "Opera", "Avast", "AVG"])

    log("✅ LIMPEZA FINALIZADA!")
    input("Pressione Enter para fechar...")

if __name__ == "__main__":
    main()
