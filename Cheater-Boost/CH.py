import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import urllib.request
import webbrowser  # Para abrir sites no navegador

# Função para baixar um script (exemplo)
def baixar_script():
    url = "https://pastebin.com/raw/EXEMPLO"  # coloque a URL do script real
    nome_arquivo = "script.lua"
    try:
        urllib.request.urlretrieve(url, nome_arquivo)
        messagebox.showinfo("Sucesso", f"{nome_arquivo} baixado!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao baixar: {e}")

# Função que encontra o RobloxPlayerBeta.exe automaticamente
def encontrar_roblox():
    roblox_path = os.path.expandvars(r"%LOCALAPPDATA%\Roblox\Versions")
    try:
        for pasta in os.listdir(roblox_path):
            caminho_possivel = os.path.join(roblox_path, pasta, "RobloxPlayerBeta.exe")
            if os.path.isfile(caminho_possivel):
                return caminho_possivel
    except Exception as e:
        return None
    return None

# Função para iniciar Roblox usando a busca automática
def iniciar_roblox():
    caminho = encontrar_roblox()
    if caminho:
        subprocess.Popen([caminho])
        messagebox.showinfo("Launcher", "Roblox is open")
    else:
        messagebox.showerror("Erro", "Executável do Roblox não encontrado.")

# Função para atualizar (exemplo)
def atualizar_booster():
    messagebox.showinfo("Atualizar", "no updates.")

# Função para abrir logs (exemplo)
def abrir_logs():
    logs_path = "logs.txt"
    if os.path.exists(logs_path):
        os.startfile(logs_path)
    else:
        messagebox.showwarning("Logs", "no logs")

# Função para abrir o site Xeno
def abrir_xeno():
    url = "https://www.xeno.onl/"
    webbrowser.open(url)

# Criação da janela principal
janela = tk.Tk()
janela.title("Cheater boost by GiGXxX4")
janela.geometry("400x350")  # Aumentei um pouco a altura para caber o novo botão
janela.configure(bg="#1e1e1e")  # fundo escuro

# Se quiser usar um ícone, descomente a linha abaixo e coloque o caminho do seu arquivo .ico
# janela.iconbitmap('seu_icone.ico')

# Título no topo
titulo = tk.Label(janela, text="Cheater Boost", font=("Segoe UI", 18, "bold"), fg="red", bg="#1e1e1e")
titulo.pack(pady=10)

# Botões vermelhos com fonte branca
botao_baixar = tk.Button(janela, text="download script", bg="red", fg="white", font=("Segoe UI", 12, "bold"), command=baixar_script)
botao_baixar.pack(pady=8, ipadx=10, ipady=5)

botao_iniciar = tk.Button(janela, text="open Roblox", bg="red", fg="white", font=("Segoe UI", 12, "bold"), command=iniciar_roblox)
botao_iniciar.pack(pady=8, ipadx=10, ipady=5)

botao_atualizar = tk.Button(janela, text="update Booster", bg="red", fg="white", font=("Segoe UI", 12, "bold"), command=atualizar_booster)
botao_atualizar.pack(pady=8, ipadx=10, ipady=5)

botao_logs = tk.Button(janela, text="open Logs", bg="red", fg="white", font=("Segoe UI", 12, "bold"), command=abrir_logs)
botao_logs.pack(pady=8, ipadx=10, ipady=5)

botao_xeno = tk.Button(janela, text="Abrir Xeno", bg="red", fg="white", font=("Segoe UI", 12, "bold"), command=abrir_xeno)
botao_xeno.pack(pady=8, ipadx=10, ipady=5)

# Rodapé
rodape = tk.Label(janela, text="© GiGXxX4 2025", font=("Segoe UI", 9), fg="gray", bg="#1e1e1e")
rodape.pack(side="bottom", pady=10)

janela.mainloop()
