import sys

from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('...')

        self.lineEdit = QLineEdit()
        self.setCentralWidget(self.lineEdit)

        self.lineEdit.textEdited.connect(self.updateStatusBar)

    def updateStatusBar(self, string):
        self.statusBar.showMessage(string)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())