import random
from upload import schedule_video_upload
from generator import create_ai_video

TOPICS = [
    "Business ideas in India",
    "Global education",
    "Anime updates and recaps",
    "World news headlines",
    "Motivational quotes",
    "Cricket-focused sports",
    "Health tips and yoga",
    "Untold world history",
    "Facts about the universe",
]

def select_topics(n=2):
    return random.sample(TOPICS, n)

if __name__ == "__main__":
    topics = select_topics()
    for topic in topics:
        print(f"Creating video for: {topic}")
        video_path = create_ai_video(topic)
        schedule_video_upload(video_path, topic)