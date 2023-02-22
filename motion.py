import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
cv.namedWindow("Video")
cv.namedWindow("absDiff")
cv.namedWindow("GreyScale")
cv.namedWindow("imageClone")

print("start")    
while True:
    status, img = cap.read()
    img = cv.convertScaleAbs(img, alpha=1, beta = 50)
    img = cv.blur(img, (5,5))
    cv.imshow("Video", img)
    accum = img
    cv.accumulateWeighted(img, accum, 0.5)
    grey = cv.convertScaleAbs()
    grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    cv.imshow("GreyScale", grey)

    k = cv.waitKey(1)
    if k == 27:
        break

print(img)   
cv.destroyAllWindows()