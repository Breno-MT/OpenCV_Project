import cv2 as cv
img = cv.imread("/home/scr0ll/Pictures/artworks-bxRk7aOfocMK2hVS-s5ITNA-t500x500.jpg")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window
