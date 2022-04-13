import numpy as np
import cv2

static0 = cv2.imread("fruits00.jpg")
static0_grey = cv2.cvtColor(static0, cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(static0_grey, 100, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

result = cv2.drawContours(static0, contours, -1, (0,255,0), 3)
cv2.imshow("result", result)
cv2.waitKey(0)
