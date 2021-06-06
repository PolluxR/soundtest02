# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import required module

import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound

def record(self, name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


    # Press the green button in the gutter to run the script.
    # Sampling frequency
    freq = 44100

    # Recording duration
    duration = 5

    # Start recorder with the given values of
    # duration and sample frequency

    print ("start recording")
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()
    print ("end recording")

    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write("recording0.wav", freq, recording)

    print ("play sound")
    playsound("recording0.wav")
    print("end")

    result = "Hi " +  name
    self.output.configure(text=result)

    print (result)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/