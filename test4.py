import sys
from camerapage import Ui_ARWindow
from PyQt5 import QtCore, QtGui, QtWidgets


app = QtWidgets.QApplication(sys.argv)
ARWindow = QtWidgets.QMainWindow()
ui = Ui_ARWindow()
ui.setupUi(ARWindow)
ARWindow.show()
sys.exit(app.exec_())