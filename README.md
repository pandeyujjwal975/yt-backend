Bilkul Ujjwal, yah raha ek simple aur clean README.md ka code format:

# yt-backend

FastAPI backend to download YouTube videos using yt-dlp.

## Features

- Download YouTube videos (supports Shorts)
- POST API endpoint
- Easy Render deployment

## API Endpoint

**POST** `/download`

**Request:**
```json
{
  "url": "https://youtube.com/shorts/your-video-url"
}

Response:

{
  "message": "Download completed!"
}

Setup Instructions

1. Install Dependencies

pip install -r requirements.txt

2. Run Locally

uvicorn main:app --reload

Deploy on Render

1. Push to GitHub


2. Go to https://render.com


3. Create new Web Service


4. Connect your repo


5. Render detects render.yaml and auto deploys



License

MIT License

Author
Ujjwal Pandey
