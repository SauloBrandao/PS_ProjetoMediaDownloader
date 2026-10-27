import yt_dlp
from pathlib import Path

def baixar_mp4(url: str,  pasta: str, progresso_resposta) -> None:
    opcoes = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "outtmpl": str(
            Path(pasta) / "%(title)s.%(ext)s"
        ),
        "progress_hooks": [
            lambda d: progresso_download(d, progresso_resposta),
        ],
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])


def baixar_mp3(url: str, pasta: str, progresso_resposta) -> None:
    opcoes = {
        "format": "bestaudio/best",
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": str(
            Path(pasta) / "%(title)s.%(ext)s"
        ),
        "progress_hooks": [
            lambda d: progresso_download(d, progresso_resposta),
        ],
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])

def progresso_download(d, resposta):
    if d["status"] == "downloading":
        baixado = d.get("downloaded_bytes", 0)

        total = (
            d.get("total_bytes")
            or d.get("total_bytes_estimate")
        )

        if total:
            progresso = baixado / total
            resposta(progresso)


