from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QProgressBar, QPushButton, QVBoxLayout
import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time

from threading import *
import sounddevice as sd

class ThreadStatusBar(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)

    def run(self):
        cnt = 0
        while cnt < 100:
            cnt += 1
            time.sleep(0.05)
            self.change_value.emit(cnt)

class ThreadRecorder(QThread):
    def run(self):
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

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 ProgressBar"
        self.top = 200
        self.left = 500
        self.width = 300
        self.height = 100
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        # self.progressbar.setOrientation(Qt.Vertical)
        self.progressbar.setMaximum(100)
        self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey;border-radius:8px;padding:1px}"
                                       "QProgressBar::chunk {background:green}")
        # qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white);
        # self.progressbar.setStyleSheet("QProgressBar::chunk {background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white); }")
        # self.progressbar.setTextVisible(False)
        vbox.addWidget(self.progressbar)
        self.button = QPushButton("Start Progressbar")
        self.button.clicked.connect(self.startrecord)
        #self.button.clicked.connect(self.record)

        self.button.setStyleSheet('background-color:grey')
        vbox.addWidget(self.button)
        self.setLayout(vbox)
        self.show()

    def startrecord(self):
        #self.thread1 = ThreadStatusBar()
        #self.thread1.change_value.connect(self.setProgressVal)
        self.thread2 = ThreadRecorder()
        self.thread2.change_value.connect(self.threadrecord)

        #self.thread1.start()
        self.thread2.start()

        #self.thread1.join()
        #self.thread2.join()

    def setProgressVal(self, val):
        self.progressbar.setValue(val)

    def threadrecord(self, val):
        record()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())