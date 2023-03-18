from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

from frontpagecamera import Ui_FrontWindow

class Main(QMainWindow, Ui_FrontWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.Scenario1.clicked.connect(self.OpenWindow1)
        #self.PushButton2.clicked.connect(self.OpenWindow2)

    def OpenWindow1(self):
        self.QtStack.setCurrentIndex(1)

    def OpenWindow2(self):
        self.QtStack.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()
    sys.exit(app.exec_())