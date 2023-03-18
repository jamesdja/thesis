import cv2
import time

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    start_time = time.time()
    check, frame = cam.read()
    #print(check)
    #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('video',frame)
    key = cv2.waitKey(1)
    print('FPS {:.1f}'.format(1 / (time.time() - start_time)))

    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()