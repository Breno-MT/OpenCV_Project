import numpy as np
import cv2 as cv
 
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera or camera was not found.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # You can set width and height to your prefence using the code below
    # ret = cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
    # ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Our operations on the frame come here
    # color = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    color = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
    # Display the resulting frame
    cv.imshow('frame', color)
    if cv.waitKey(1) == ord('q'):
        break


# Print some informations about WIDTH and HEIGHT
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
