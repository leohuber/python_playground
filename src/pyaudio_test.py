import pyaudio
import wave
import threading
 
audio = pyaudio.PyAudio()

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"

device_info = audio.get_default_input_device_info()

print("Default input device info:")
print(device_info)

max_channels = device_info.get('maxInputChannels')
if max_channels > 1:
    CHANNELS = 2
    print("Two channels available")
else:
    CHANNELS = 1
    print("Only one channel available")

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)

def record():
    print("recording...")
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
