import cv2 as cv
import sys

# you can make it basically convert any type of img to the one you want
# e.g: you can put a path to a jpg and then save it as png, webp or whatever you want
img = cv.imread(cv.samples.findFile("path/to/image"))
 
if img is None:
    sys.exit("Could not read or find the image.")
 
cv.imshow("Display window", img)
k = cv.waitKey(0)
 
if k == ord("s"):
    cv.imwrite("path/to/save/image", img)
    print("Saved image successfully!")