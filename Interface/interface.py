import threading

import customtkinter as ctk
from tkinter import filedialog
from serviços.downloader.downloader import baixar_mp4

def inificar_download(): # -> Criando Thread para evitar que o tkinter crashe
    url = url_entrada.get()

    threading.Thread(
        target=baixar_mp4,
        args=(url,),
        daemon=True
    ).start()

def selecionar_pasta(): # -> criando função para selecionar diretorio
    caminho = filedialog.askdirectory()

    if caminho:
        print(caminho)


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
    command=inificar_download
)
botao_download.pack(pady=20)

botao_pasta = ctk.CTkButton(
    app,
    text="Selecionar pasta",
    command=selecionar_pasta
)
botao_pasta.pack(padx=20, pady=20)

app.mainloop()