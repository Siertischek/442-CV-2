import cv2 as cv
import numpy as np

# My computer/camera worked with 0 instead of 1 like on the example code so it may need to be switched back 
cap = cv.VideoCapture(0)
cv.namedWindow("Video")
cv.namedWindow("absDiff")
cv.namedWindow("GreyScale")
cv.namedWindow("Contours")

first = True

print("start")    
while True:
    status, img = cap.read()
    #brighten and then blur
    img = cv.convertScaleAbs(img, alpha=1, beta = 50)
    img = cv.blur(img, (5,5))

    if(first == True):
       previous = img
       first = False

    #take running average and convert
    accum = np.float32(img)
    cv.accumulateWeighted(img, accum, 0.1)
    accum = cv.convertScaleAbs(accum)
    diff = cv.absdiff(previous, accum)
    diff = cv.cvtColor(diff, cv.COLOR_RGB2GRAY)
    cv.imshow("absDiff", diff)

    _,thresh = cv.threshold(diff, 40, 255, cv.THRESH_BINARY)
    thresh = cv.blur(thresh, (5,5))
    _,thresh = cv.threshold(thresh, 200, 255, cv.THRESH_BINARY)

    cv.imshow("GreyScale", thresh)

    contours, hier = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv.contourArea(contour) < 200:
            continue
        (x,y,w,h) = cv.boundingRect(contour)
        cv.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

    cv.imshow("Video", img)

    previous = img

    k = cv.waitKey(1)
    if k == 27:
        break

print(img)   
cv.destroyAllWindows()