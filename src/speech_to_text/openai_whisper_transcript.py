import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Print the environment variable OPENAPI_KEY and exit
openapi_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

project_root = Path(__file__).resolve().parents[1]
WAVE_FILENAME = project_root + "/.tmp/output.mp3"

audio_path = Path(WAVE_FILENAME)
with audio_path.open("rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
    )

print(transcription.text)
