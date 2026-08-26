import customtkinter as ctk

ctk.set_appearance_mode("system")

app = ctk.CTk()
app.geometry("600x400")
app.title("Custom Media Downloader - By Saulo")

# Criando fonte
fonte = ctk.CtkFont(family="")

titulo = ctk.CTkLabel(
    app,
    text="Custom Media Downloader",
    font=("Arial", 20),
)
titulo.pack(pady=30)

url_entry = ctk.CTkEntry(
    app,
    width=450,
    placeholder_text="Cole o link do vídeo"
)
url_entry.pack(pady=10)



app.mainloop()