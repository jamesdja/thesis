import cv2
import numpy as np
import time

# specify the three vertices of the triangle
pt1 = (100, 100)
pt2 = (300, 100)
pt3 = (200, 300)

# initialize the position of the horizontal line
line_pos = 50

# Read logo and resize
logo = cv2.imread(r'C:\Users\danie\Projects\thesis\signright.png')
size = 100
logo = cv2.resize(logo, (size, size))


# Create a mask of logo
img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)


# open the webcam
cap = cv2.VideoCapture(0)

while True:
    # read a frame from the webcam
    ret, frame = cap.read()

    # draw the triangle by connecting the vertices
    cv2.line(frame, pt1, pt2, (0, 255, 0), 3)
    cv2.line(frame, pt2, pt3, (0, 255, 0), 3)
    cv2.line(frame, pt3, pt1, (0, 255, 0), 3)

    # draw the horizontal line
    cv2.line(frame, (0, line_pos), (frame.shape[1], line_pos), (255, 0, 0), 2)

    # update the position of the horizontal line every second
    if int(time.time() % 2) == 0:
        line_pos += 1

    # overlay the PNG image onto the current frame
    # Region of Image (ROI), where we want to insert logo
    roi = frame[-size-10:-10, -size-10:-10]
  
    # Set an index of where the mask is
    roi[np.where(mask)] = 0
    roi += logo

    # display the resulting image
    cv2.imshow("Triangle", frame)

    # wait for key press to exit
    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()