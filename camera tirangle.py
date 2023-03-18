import cv2
import cvzone
import numpy as np
import time

# specify the three vertices of the triangle
pt1 = (100, 100)
pt2 = (300, 100)
pt3 = (200, 300)

# initialize the position of the horizontal line
line_pos = 50

# load the PNG image
img = cv2.imread('signright.png', cv2.IMREAD_UNCHANGED)
#img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

#foreground = np.ones((100,100,3),dtype='uint8')*255

img = cv2.resize(img,(0,0), None, 0.3,0.3)

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
    if time.time() // 2 == 0:
        line_pos += 1

    # overlay the PNG image onto the current frame
    alpha = 0.5  # transparency level of the PNG image
    x_offset = 50  # horizontal offset of the PNG image from the left edge
    y_offset = 50  # vertical offset of the PNG image from the top edge
    #'frame[y_offset:y_offset + img.shape[0], x_offset:x_offset + img.shape[1]] = cv2.addWeighted('
        #'frame[y_offset:y_offset + img.shape[0], x_offset:x_offset + img.shape[1]], 1 - alpha, img, alpha, 0)'
    #frame = cv2.addWeighted(frame, 0.4, img, 0.1, 0)
    #frame = cv2.addWeighted(frame[0:480, 0:480, :], alpha, foreground[0:100, 0:100, :], 1 - alpha, 0)

    hf, wf, cf = img.shape
    hb, wb, cb = frame.shape
    frame = cvzone.overlayPNG(frame, img, [0,hb-hf] )

    # display the resulting image
    cv2.imshow("Triangle", frame)

    # wait for key press to exit
    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()