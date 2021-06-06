from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

import sys
import time

import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()

        super(MainWindow, self).__init__(parent)

        self.button1 = QPushButton(self)
        self.button1.setText("Record")
        self.button1.move(64, 32)
        self.button1.clicked.connect(self.record)

        self.button2 = QPushButton(self)
        self.button2.setText("Play")
        self.button2.move(164, 32)
        self.button2.clicked.connect(self.play)

        # set the title
        self.setWindowTitle("Python")

        # setting  the geometry of window
        self.setGeometry(60, 60, 600, 400)

        # setting status bar message
        self.statusBar().showMessage("this is status bar")

        # creating a label widget
        self.label_1 = QLabel("Status Bar", self)

        # moving position
        self.label_1.move(100, 100)

        # setting up the border
        self.label_1.setStyleSheet("border :5px solid blue;")

        # resizing label
        self.label_1.resize(80, 100)

        # show all the widgets
        #self.setGeometry(50, 50, 320, 200)
        self.show()

    def record(self):
        # Press the green button in the gutter to run the script.
        # Sampling frequency
        freq = 44100

        # Recording duration
        duration = 5

        # Start recorder with the given values of
        # duration and sample frequency

        print("start recording")
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

        # time.sleep(3)

        # Record audio for the given number of seconds
        sd.wait()
        # self.status("end recording")
        print("end recording")

        # This will convert the NumPy array to an audio
        # file with the given sampling frequency
        write("recording0.wav", freq, recording)

    def play(self, name):
        print("play sound")
        playsound("recording0.wav")
        print("end")

        result = "Hi " + name
        self.output.configure(text=result)

        print(result)

if __name__ == '__main__':
    App = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    sys.exit(App.exec_())