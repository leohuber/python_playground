import select
import sys
import threading
import time
from pathlib import Path

import sounddevice as sd
from pedalboard.io import AudioFile, AudioStream  # type: ignore[attr-defined]

mp3_quality = "V6"  # V0 (highest quality) to V9 (lowest quality)

project_root = (Path(__file__).resolve().parent / "../../").resolve()
MP3_OUTPUT_FILENAME = project_root / ".tmp" / "output.mp3"

print("Available input devices:")
device_list = []
devices = sd.query_devices()
for dev in devices:
    if dev["max_input_channels"] > 0:
        device_list.append(dev["name"])
        print(f"Device {len(device_list) - 1}: {dev['name']}")

while True:
    try:
        selected_index = int(input("Select device index: "))
        if 0 <= selected_index < len(device_list):
            input_device_name = device_list[selected_index]
            break
        else:
            print("Invalid index. Please select a valid device index.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# Open up an audio stream:
# Open an audio stream from the microphone, process the audio with a pedalboard,
# and write the processed audio to a file.
with (
    AudioStream(
        input_device_name=input_device_name,  # Guitar interface
    ) as stream,
    AudioFile(
        MP3_OUTPUT_FILENAME,
        "w",
        stream.sample_rate,
        stream.num_input_channels,
        quality=mp3_quality,
    ) as audio_file,
):
    # Set up the pedalboard for processing
    """
    stream.plugins = Pedalboard([
        Compressor(threshold_db=-50, ratio=25),
        Gain(gain_db=30),
        Chorus(),
        Phaser(),
        Reverb(room_size=0.25),
    ])
    """

    # Use a separate thread to listen for the user pressing enter.
    stop_event = threading.Event()

    def wait_for_input() -> None:
        start_time = time.time()
        print("Press enter to stop streaming and writing the file ...")
        while True:
            elapsed = int(time.time() - start_time)
            minutes = elapsed // 60
            seconds = elapsed % 60
            print(f"\rRecording ({minutes}m {seconds}s) ... Press enter to stop streaming and writing the file ...", end="", flush=True)
            if sys.stdin in select.select([sys.stdin], [], [], 1)[0]:
                sys.stdin.readline()
                break
        stop_event.set()
        stop_event.set()

    threading.Thread(target=wait_for_input, daemon=True).start()

    # Continuously read audio blocks and write them to the file until input is received.
    while not stop_event.is_set():
        audio_buffer = stream.read()
        audio_file.write(audio_buffer)

# The live AudioStream is now closed, and audio has stopped.
