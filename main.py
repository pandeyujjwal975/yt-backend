from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import yt_dlp

# Create a FastAPI instance
app = FastAPI()

# Allow frontend requests from any origin (you can restrict this to your frontend URL later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a request model with a single field: URL
class URLRequest(BaseModel):
    url: str

# Define a POST endpoint to handle video download
@app.post("/download")
def download_video(data: URLRequest):
    try:
        # Set options for downloading the best quality video
        ydl_opts = {
            "format": "best",
            "outtmpl": "%(title)s.%(ext)s"  # Save as video title + extension
        }

        # Use yt_dlp to download the video from the given URL
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([data.url])

        # Return success message
        return {"message": "Download completed!"}
    except Exception as e:
        # Return error message if something goes wrong
        return {"message": f"Error: {str(e)}"}
