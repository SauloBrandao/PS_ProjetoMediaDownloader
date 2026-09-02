import yt_dlp
from pathlib import Path

def baixar_mp4(url: str,  pasta: str) -> None:
    opcoes = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "outtmpl": str(
            Path(pasta) / "%(title)s.%(ext)s"
        ),
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])


def baixar_mp3(url: str, pasta: str) -> None:
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
        )
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])
