import cv2 as cv 
img = cv.imread('Layer 1.png')
cv.imshow("lady",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
# 
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('gray',hsv)
# 
# lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow('LAB',lab)


cv.waitKey(0)