from pedalboard import Pedalboard, Chorus, Compressor, Gain, Reverb, Phaser
from pedalboard.io import AudioStream, AudioFile
import threading
import pyaudio
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
MP3_OUTPUT_FILENAME = project_root + "/.tmp/output.mp3"

p = pyaudio.PyAudio()

print("Available input devices:")
device_list = []
for i in range(p.get_device_count()):
    device_info = p.get_device_info_by_index(i)
    if device_info['maxInputChannels'] > 0:
        device_list.append(device_info['name'])
        print(f"Device {len(device_list)-1}: {device_info['name']}")

selected_index = int(input("Select device index: "))
input_device_name = device_list[selected_index]

p.terminate()


# Open up an audio stream:
# Open an audio stream from the microphone, process the audio with a pedalboard,
# and write the processed audio to a file.
with AudioStream(
    input_device_name=input_device_name,  # Guitar interface
) as stream, AudioFile(
    MP3_OUTPUT_FILENAME,
    "w",
    stream.sample_rate,
    stream.num_input_channels,
    quality='V8'
) as audio_file:
    # Set up the pedalboard for processing
    stream.plugins = Pedalboard([
        Compressor(threshold_db=-50, ratio=25),
        Gain(gain_db=30),
        Chorus(),
        Phaser(),
        Reverb(room_size=0.25),
    ])

    # Use a separate thread to listen for the user pressing enter.
    stop_event = threading.Event()
    def wait_for_input():
        input("Recording... Press enter to stop streaming and writing the file...")
        stop_event.set()
    threading.Thread(target=wait_for_input, daemon=True).start()

    # Continuously read audio blocks and write them to the file until input is received.
    while not stop_event.is_set():
        audio_buffer = stream.read()
        audio_file.write(audio_buffer)
# AudioStream and AudioFile are now closed and the file "output.wav" has been written.

# The live AudioStream is now closed, and audio has stopped.