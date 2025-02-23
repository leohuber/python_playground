import pyaudio

audio = pyaudio.PyAudio()

print(audio.get_default_input_device_info())
