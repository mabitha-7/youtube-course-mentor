from youtube_utils import get_transcript
from rag_utils import split_text
from vector_store import store_chunks

video_id = "aircAruvnKk"

transcript = get_transcript(video_id)

chunks = split_text(transcript)

count = store_chunks(chunks)

print(f"{count} chunks stored successfully!")