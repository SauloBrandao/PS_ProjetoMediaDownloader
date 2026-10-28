import threading

import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
from urllib.parse import urlparse
from downloader.downloader import baixar_mp4, baixar_mp3

# Funções
#------------------------------------------------------------------------------------------------
pasta_downloads = Path.home() / "Downloads"

# Função de Seleção de Pasta
def selecionar_pasta(): # — > criando função para selecionar diretório
    caminho = filedialog.askdirectory()

    if caminho: # — > validando se existe ou não
        caminho_destino.set(caminho)

# Função de iniciar ‘Download’
def iniciar_download(pasta: str): # — > Criando Função para iniciar ‘Downloads' e criar Threads
    url = url_entrada.get() # -> pegando url inserida

    if formato.get() == "MP3":
        threading.Thread( # -> Thread do MP3
            target=baixar_mp3,
            args=(url,pasta, atualizar_progresso),
            daemon=True
        ).start()

    else:
        threading.Thread( # -> Thread do MP4
            target=baixar_mp4,
            args=(url,pasta, atualizar_progresso, download_concluido),
            daemon=True
        ).start()

# Função de Atualizar Barra de progresso
def atualizar_progresso(valor):
    def atualizar():
        barra_de_progresso.set(valor)
        progresso_atual.set(valor)

        if valor > 0.1 and (valor < 1.0):
            status.configure(text="Baixando")

    app.after(0, atualizar)

def download_concluido():
    def atualizar():
        status.configure(text="Concluído")
        messagebox.showinfo(
            title="Download Cocluído",
            message="O arquivo foi baixado com sucesso."
        )
        barra_de_progresso.set(0)
        status.configure(text="Aguardando")

    app.after(0, atualizar)

# Função para validar url inserida
def validar_url(url:str):
    resultado = urlparse(url)
    return resultado.scheme in ("http", "https") and bool(resultado.netloc)

# Função para validar o ‘download’
def validar_download():
    url = url_entrada.get().strip()

    if not url:
        messagebox.showerror(
            title="Erro",
            message="Selecione uma URL"
        )
        return

    if not validar_url(url):
        messagebox.showerror(
            title="Erro",
            message="A URL informada é inválida."
        )
        return

    iniciar_download(caminho_destino.get())
#--------------------------------------------------------------------------------------------
# Interface do CustomTkinter
# Header
ctk.set_appearance_mode("system")

app = ctk.CTk()
app.geometry("500x600")
app.title("Custom Media Downloader - By Saulo")
app.resizable(False, False)
app.iconbitmap("../conteudo/imagens/media_downloader_icon.ico")

titulo = ctk.CTkLabel( # -> Titulo do Software
    app,
    text="Custom Media Downloader \n"
         "Feito por Saulo",
    font=ctk.CTkFont(family="Indie Flower", size=30),
)
titulo.pack(pady=30)

#--------------------------------------------------------------------------------------------
# Entradas e Botões
# Entrada do URL
url_entrada = ctk.CTkEntry(
    app,
    width=450,
    placeholder_text="Cole o link do vídeo",
    font=ctk.CTkFont(family="Indie Flower")
)
url_entrada.pack(pady=10)
caminho_destino = ctk.StringVar(value=str(pasta_downloads))

# Exibição de Caminho para ‘Download’
exibicao_caminho = ctk.CTkEntry(
    app,
    width=450,
    font=ctk.CTkFont(family="Indie Flower"),
    textvariable=caminho_destino
)
exibicao_caminho.pack(pady=10)
exibicao_caminho.configure(state="disabled")

# Seletor de Caminho
botao_pasta = ctk.CTkButton(
    app,
    text="Selecionar pasta",
    hover=True,
    hover_color="Red",
    fg_color="Grey",
    font=ctk.CTkFont("Indie Flower",weight = "bold",size=20),
    command=selecionar_pasta
)
botao_pasta.pack(padx=20, pady=20)

# Seletor de Formato
formato = ctk.CTkSegmentedButton(
    app,
    values=["MP4", "MP3"],
    selected_color="Red",
    selected_hover_color="Red",
    unselected_color="Grey",
    font=ctk.CTkFont(family="Indie Flower", weight="bold")
)
formato.set("MP4")
formato.pack(pady=10)

# Botão de iniciar de ‘Download’
botao_download = ctk.CTkButton(
    app,
    text="Baixar",
    hover=True,
    hover_color="Red",
    fg_color="Grey",
    font=ctk.CTkFont("Indie Flower",weight = "bold",size=20),
    command=lambda: validar_download()
)
botao_download.pack(pady=20)

barra_de_progresso = ctk.CTkProgressBar(
    app,
    width=100,
    height=20,
    progress_color="Red",
    orientation="horizontal",
)
barra_de_progresso.pack(pady=20)
barra_de_progresso.set(0)

progresso_atual = ctk.DoubleVar(value=0)
status = ctk.CTkLabel(
    app,
    text="Aguardando",
    font=ctk.CTkFont("Indie Flower", weight="bold", size=20),
)
status.pack(pady=20)

app.mainloop()
