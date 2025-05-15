# yt-backend

FastAPI backend to download YouTube videos using yt-dlp.

---

## Features

- Download YouTube videos (including Shorts)
- Simple POST API
- Easy deployment on Render

---

## API Usage

### Endpoint

POST /download

### Request Body

{ "url": "https://youtube.com/shorts/your-video-url" }

### Response

{ "message": "Download completed!" }

---

## Setup Instructions

### 1. Install Dependencies

pip install -r requirements.txt

### 2. Run Locally

uvicorn main:app --reload

---

## Deploy on Render

1. Push this project to GitHub  
2. Visit: https://render.com  
3. Create a new Web Service  
4. Connect your GitHub repo  
5. Render will auto-detect `render.yaml` and deploy your app

---

## License

MIT License

---

## Author

Ujjwal Pandey
