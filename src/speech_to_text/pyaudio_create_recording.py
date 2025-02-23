import pyaudio
import wave
import threading
import os
 
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
