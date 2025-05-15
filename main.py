from fastapi import FastAPI
from pydantic import BaseModel
import yt_dlp

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/download")
def download_video(data: URLRequest):
    try:
        ydl_opts = {
            "format": "best",
            "outtmpl": "%(title)s.%(ext)s"
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([data.url])
        return {"message": "Download completed!"}
    except Exception as e:
        return {"message": f"Error: {str(e)}"}