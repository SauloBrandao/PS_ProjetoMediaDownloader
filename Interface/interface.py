import customtkinter as ctk
from downloader import downloader as dlp_mp4

ctk.set_appearance_mode("system")

app = ctk.CTk()
app.geometry("600x400")
app.title("Custom Media Downloader - By Saulo")

titulo = ctk.CTkLabel( # -> Titulo do Sofware
    app,
    text="Custom Media Downloader \n"
         "Feito por Saulo",
    font=ctk.CTkFont(family="Indie Flower", size=30),
)
titulo.pack(pady=30) # -> espaço padrão 30 px

entrada_url = ctk.CTkEntry(
    app,
    width=450,
    placeholder_text="Cole o link do vídeo",
    font=ctk.CTkFont(family="Indie Flower")
)
entrada_url.pack(pady=10) # -> padrão é 10 px

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

def baixar():
    url = entrada_url.get()
    dlp_mp4.baixar_mp4(url)

botao_download = ctk.CTkButton(
    app,
    text="Baixar",
    hover=True,
    hover_color="Red",
    fg_color="Grey",
    font=ctk.CTkFont("Indie Flower", weight = "bold", size=20),
    command=baixar()
)
botao_download.pack(pady=20)

app.mainloop()