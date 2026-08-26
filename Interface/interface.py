import customtkinter as ctk

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

url_entry = ctk.CTkEntry(
    app,
    width=450,
    placeholder_text="Cole o link do vídeo",
    font=ctk.CTkFont(family="Indie Flower")
)
url_entry.pack(pady=10) # -> padrão é 10 px

formato = ctk.CTkSegmentedButton(
    app,
    values=["MP4", "MP3"],
    font=ctk.CTkFont(family="Indie Flower", weight="bold")
)
formato.set("MP4")
formato.pack(pady=10)

botao_download = ctk.CTkButton(
    app,
    text="Baixar",
    font=ctk.CTkFont("Indie Flower", weight = "bold", size=20)
)
botao_download.pack(pady=20)

app.mainloop()