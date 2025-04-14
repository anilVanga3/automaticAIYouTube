import datetime

def schedule_video_upload(video_path, topic):
    print(f"Uploading {video_path} for topic '{topic}' at 11:00 AM IST...")
    # Here you would use YouTube API for actual upload
    print(f"Upload scheduled successfully for {datetime.datetime.now().date()}")