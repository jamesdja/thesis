import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import time

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.VBL = QVBoxLayout()
        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)
        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        Capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        Capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        while self.ThreadActive:
            start_time = time.time()
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                FlippedImage = cv2.line(FlippedImage, (0,0), x, 0, 5)
                if x[1] < 720:
                    x[0] = x[0] + 20
                    x[1] = x[1] + 20
                else:
                    x[0] = 0
                    x[1] = 0
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(1920, 1080, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
                print('FPS {:.1f}'.format(1 / (time.time() - start_time)))
    def stop(self):
        self.ThreadActive = False
        self.quit()


x = [0, 0]

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())