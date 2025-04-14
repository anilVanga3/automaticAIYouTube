import os
from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip
import pyttsx3

def create_ai_video(topic):
    audio_filename = f"audio_{topic[:10]}.mp3"
    video_filename = f"video_{topic[:10]}.mp4"

    engine = pyttsx3.init()
    engine.save_to_file(f"This video is about {topic}. Stay tuned for more!", audio_filename)
    engine.runAndWait()

    clip = TextClip(f"{topic}", fontsize=70, color='white', size=(720, 1280))
    clip = clip.set_duration(10).set_position('center')

    audio = AudioFileClip(audio_filename)
    video = CompositeVideoClip([clip]).set_audio(audio)
    video.write_videofile(video_filename, fps=24)

    return video_filename