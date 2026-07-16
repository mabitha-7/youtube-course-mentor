from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id)

    text = " ".join([item.text for item in transcript])

    return text