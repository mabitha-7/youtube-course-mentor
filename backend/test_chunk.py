from youtube_utils import get_transcript
from rag_utils import split_text
video_id = "aircAruvnKk"
transcript = get_transcript(video_id)
chunks = split_text(transcript)
print("Total Chunks:", len(chunks))
print("\nFirst Chunk:\n")
print(chunks[0])