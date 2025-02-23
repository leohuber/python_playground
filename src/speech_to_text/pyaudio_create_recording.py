import pyaudio
import wave
import threading
import os
from pedalboard import Pedalboard
from pedalboard.io import AudioFile
 
audio = pyaudio.PyAudio()

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
WAVE_OUTPUT_FILENAME = project_root + "/.tmp/recording.wav"

device_info = audio.get_default_input_device_info()

print("Default input device name:", device_info.get('name'))
print("Default input device rate:", device_info.get('defaultSampleRate'))
print("Default input device max input channels:", device_info.get('maxInputChannels'))
print("-----------------------------")
print("")

max_channels = device_info.get('maxInputChannels')
if max_channels > 1:
    CHANNELS = 2
else:
    CHANNELS = 1

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)

def record():
    print("Starting Recording ...")
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as waveFile:
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        
        while recording:
            data = stream.read(CHUNK)
            waveFile.writeframes(data)
    print("finished recording")

def wait_for_key():
    global recording
    input("Press Enter to stop recording...\n")
    recording = False

recording = True
record_thread = threading.Thread(target=record)
key_thread = threading.Thread(target=wait_for_key)

record_thread.start()
key_thread.start()

record_thread.join()
key_thread.join()

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

# Load the recorded WAV file
with AudioFile(WAVE_OUTPUT_FILENAME) as f:
    audio = f.read(f.frames)
    samplerate = f.samplerate

# Create an empty Pedalboard (no effects)
board = Pedalboard([])

# Process the audio (this doesn't change it, since the board is empty)
processed_audio = board(audio, samplerate)

# Save the processed audio to an MP3 file
mp3_output_filename = WAVE_OUTPUT_FILENAME.replace('.wav', '.mp3')
with AudioFile(mp3_output_filename, 'w', samplerate, processed_audio.shape[0]) as f:
    f.write(processed_audio)

print(f"MP3 file saved as {mp3_output_filename}")