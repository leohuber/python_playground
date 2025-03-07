from pathlib import Path

from pedalboard.io import AudioFile  # type: ignore[attr-defined]

# Path to the MP3 file
file_path = (Path(__file__).parent / "../../.tmp/output.mp3").resolve()

# Check if the file exists
if not file_path.is_file():
    raise FileNotFoundError(file_path)

# Open the MP3 file and analyze it
with AudioFile(str(file_path)) as f:
    print(f"Sample rate: {f.samplerate}")
    print(f"Number of channels: {f.num_channels}")
    print(f"Duration: {f.duration} seconds")
