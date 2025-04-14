# AI YouTube Video Automation

This project automatically generates two AI-based YouTube videos daily and schedules them for upload at 11 AM IST.

## Features
- Random topic selection from 9 themes
- Voiceover using pyttsx3
- Text-based video generation
- Auto-scheduling for YouTube uploads

## Setup

1. Install requirements:
```
pip install -r requirements.txt
```

2. Run the script:
```
python main.py
```

> To integrate with YouTube API, replace the `upload.py` logic with authenticated YouTube Data API v3 upload code.