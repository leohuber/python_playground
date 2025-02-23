from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Print the environment variable OPENAPI_KEY and exit
openapi_key = os.getenv("OPENAI_API_KEY")
print(f"OPENAI_API_KEY: {openapi_key}")

client = OpenAI()

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
WAVE_FILENAME = project_root + "/.tmp/recording.wav"

audio_file= open(WAVE_FILENAME, "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)

print(transcription.text)