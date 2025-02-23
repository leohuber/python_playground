from openai import OpenAI
import os
client = OpenAI()

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
WAVE_FILENAME = project_root + "/.tmp/recording.wav"

audio_file= open(WAVE_FILENAME, "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)

print(transcription.text)