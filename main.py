import numpy as np
import cv2

static0 = cv2.imread("fruits00.jpg")
result = static0
static0_grey = cv2.cvtColor(static0, cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(static0_grey, 90, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
crops = []

for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if area >= 300:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(result, (x,y), (x+w,y+h), (0,255,255), 2)     # Building ROI rectangles
        crops.append(cv2.imread("fruits00.jpg")[y:y+h, x:x+w])      # Cropped image for each ROI

for img in crops:
    cv2.imshow(" ", img)
    cv2.waitKey()
cv2.imshow("ROIs", result)
cv2.waitKey(0)