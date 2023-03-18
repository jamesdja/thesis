import sys
import frontpage
import mappage
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        frontpage.Ui_FrontWindow()
        #self.Scenario1.clicked.connect(self.action1)

class screen2(QtWidgets.QDialog):
    def __init__(self):
        super(screen2, self).__init__()
        mappage.Ui_mappage()

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget
mainwindow = MainWindow()
screen2 = screen2()
widget.addWidget(mainwindow)
widget.addWidget(screen2)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")


