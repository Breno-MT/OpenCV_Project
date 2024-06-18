import numpy as np
import cv2 as cv
 
# It can be any format supported.:
# In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
# In Windows: DIVX (More to be tested and added)
# In OSX: MJPG (.mp4), DIVX (.avi), X264 (.mkv).
cap = cv.VideoCapture('path/to/video')
 
while cap.isOpened():
    # You can change it the frame if you want by using.: ret = cap.set(cv.CAP_PROP_FRAME_WIDTH, 320) or
    # ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 320)
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    color = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)

    cv.imshow('frame', color)

    # If it is too less, video will be very fast and if it is too high,
    # video will be slow (That's a way you can display videos in slow motion).
    # 25 milliseconds will be OK in normal cases.    
    if cv.waitKey(25) == ord('q'):
        break
 
cap.release()
cv.destroyAllWindows()
