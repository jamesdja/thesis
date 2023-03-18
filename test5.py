import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMainWindow, QPushButton
import cv2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create buttons
        self.button1 = QPushButton("Camera 1", self)
        self.button2 = QPushButton("Camera 2", self)
        self.button3 = QPushButton("Camera 3", self)
        self.button4 = QPushButton("Camera 4", self)
        self.button1.clicked.connect(self.open_camera_1)
        self.button2.clicked.connect(self.open_camera_2)
        self.button3.clicked.connect(self.open_camera_3)
        self.button4.clicked.connect(self.open_camera_4)

        # Set layout
        self.button1.move(50, 50)
        self.button2.move(150, 50)
        self.button3.move(250, 50)
        self.button4.move(350, 50)

        self.setGeometry(300, 300, 500, 150)
        self.setWindowTitle("Main Window")
        self.show()

    def open_camera_1(self):
        self.camera_window = CameraWindow(0)
        self.camera_window.show()

    def open_camera_2(self):
        self.camera_window = CameraWindow(1)
        self.camera_window.show()

    def open_camera_3(self):
        self.camera_window = CameraWindow(2)
        self.camera_window.show()

    def open_camera_4(self):
        self.camera_window = CameraWindow(3)
        self.camera_window.show()

class CameraWindow(QDialog):
    def __init__(self, camera_index):
        super().__init__()

        self.camera_index = camera_index
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.close)
        self.label = QLabel(self)

        # Create a timer to update the frame
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

        # Set layout
        self.label.move(10, 10)
        self.back_button.move(10, 400)
        self.setGeometry(100, 100, 800, 450)
        self.setWindowTitle("Camera {}".format(self.camera_index))

        self.capture = cv2.VideoCapture(0)

    def update_frame(self):
        # Get video frame

        ret, frame = self.capture.read()

        # Convert the image from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Get image dimensions
        height, width, channel = frame.shape

        # Create QImage from frame
        image = QImage(frame, width, height, channel * width, QImage.Format_RGB888)

        # Set pixmap
        self.label.setPixmap(QPixmap.fromImage(image))

    def closeEvent(self, event):
        self.timer.stop()
        self.capture.release()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())