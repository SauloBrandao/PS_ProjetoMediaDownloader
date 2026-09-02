import yt_dlp

def baixar_mp4(url: str) -> None:
    opcoes = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",

        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])


def baixar_mp3(url: str) -> None:
    opcoes = {
        "format": "bestaudio/best",
        "noplaylist": True,

        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ]
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])
