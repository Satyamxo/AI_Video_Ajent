from dotenv import load_dotenv
load_dotenv()
from utils.audio_processor import process_input
from core.transcriber import transcribe_all




source = "https://youtu.be/gZQqBhL7yBg?si=AXZzNU67T4YL2Q9a"
language = "hinglish"

chunks = process_input(source)
transcript = transcribe_all(chunks, language=language)


print("\n===transcript===\n")
print(transcript)