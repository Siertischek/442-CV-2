import cv2 as cv
import numpy as np

def colorclick(evt, x, y, flags, pic):
    #print ("mouse Worked")
    if evt == cv.EVENT_LBUTTONDOWN:
            print (img[y,x,0])
            print (img[y,x,1])
            print (img[y,x,2])

def change_minH(value):
    min[0] = value

def change_minS(value):
    min[1] = value

def change_minV(value):
    min[2] = value

def change_maxH(value):
    max[0] = value

def change_maxS(value):
    max[1] = value

def change_maxV(value):
    max[2] = value


# My computer/camera worked with 0 instead of 1 like on the example code so it may need to be switched back 
cap = cv.VideoCapture(0)
cv.namedWindow("Video")
cv.namedWindow("hsv")
cv.namedWindow("GreyScale")

global min 
min = np.array([0,0,0])
global max
max = np.array([255,255,255])

cv.createTrackbar("minH", "hsv", 0, 255,  change_minH)
cv.createTrackbar("minS", "hsv", 0, 255, change_minS)
cv.createTrackbar("minV", "hsv", 0, 255,  change_minV)
cv.createTrackbar("maxH", "hsv", 0, 255, change_maxH)
cv.createTrackbar("maxS", "hsv", 0, 255,  change_maxS)
cv.createTrackbar("maxV", "hsv", 0, 255, change_maxV)

kernel = np.ones((5,5), np.uint8)

print("start")    
while True:
    status, img = cap.read()
    cv.imshow("Video", img)
    hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)
    cv.imshow("hsv", hsv)
    cv.setMouseCallback("hsv", colorclick, hsv)
    grey = cv.inRange(hsv, min, max)
    grey = cv.erode(grey, kernel, iterations=1)
    grey = cv.dilate(grey, kernel, iterations=1)
    cv.imshow("GreyScale", grey)

    k = cv.waitKey(1)
    if k == 27:
        break

print(img)   
cv.destroyAllWindows()
