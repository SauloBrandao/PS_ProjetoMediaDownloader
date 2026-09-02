import threading

import customtkinter as ctk
from tkinter import filedialog
from serviços.downloader.downloader import baixar_mp4, baixar_mp3

# Funções
#------------------------------------------------------------------------------------------------
def inificar_download(pasta: str): # -> Criando Função para iniciar Downloads e criar Threads
    url = url_entrada.get() # -> pegando url inserida

    if formato.get() == "MP3":
        threading.Thread( # -> Thread do MP3
            target=baixar_mp3,
            args=(url,pasta),
            daemon=True
        ).start()

    else:
        threading.Thread( # -> Thread do MP4
            target=baixar_mp4,
            args=(url,pasta),
            daemon=True
        ).start()

def selecionar_pasta(): # -> criando função para selecionar diretorio
    global pasta_destino # -> criando variavel global para armazenar pasta destino

    caminho = filedialog.askdirectory()

    if caminho: # -> validando se existe ou não
        pasta_destino = caminho

#------------------------------------------------------------------------------------------
# Interface do CustomTkinter
ctk.set_appearance_mode("system")

app = ctk.CTk()
app.geometry("600x400")
app.title("Custom Media Downloader - By Saulo")

titulo = ctk.CTkLabel( # -> Titulo do Software
    app,
    text="Custom Media Downloader \n"
         "Feito por Saulo",
    font=ctk.CTkFont(family="Indie Flower", size=30),
)
titulo.pack(pady=30) # -> espaço padrão 30 px

url_entrada = ctk.CTkEntry(
    app,
    width=450,
    placeholder_text="Cole o link do vídeo",
    font=ctk.CTkFont(family="Indie Flower")
)
url_entrada.pack(pady=10) # -> padrão é 10 px

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

botao_download = ctk.CTkButton(
    app,
    text="Baixar",
    hover=True,
    hover_color="Red",
    fg_color="Grey",
    font=ctk.CTkFont("Indie Flower",weight = "bold",size=20),
    command=lambda: inificar_download(pasta_destino),
)
botao_download.pack(pady=20)

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

app.mainloop()
