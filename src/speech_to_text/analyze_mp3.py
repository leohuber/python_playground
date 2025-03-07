import os

from pedalboard.io import AudioFile

# Path to the MP3 file
file_path = os.path.join(os.path.dirname(__file__), "../../.tmp/output.mp3")

# Check if the file exists
if not os.path.isfile(file_path):
    raise FileNotFoundError(f"The file {file_path} does not exist.")

# Open the MP3 file and analyze it
with AudioFile(file_path) as f:
    print(f"Sample rate: {f.samplerate}")
    print(f"Number of channels: {f.num_channels}")
    print(f"Duration: {f.duration} seconds")
