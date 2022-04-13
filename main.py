import numpy as np
import cv2

static0 = cv2.imread("fruits00.jpg")
static0_grey = cv2.cvtColor(static0, cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(static0_grey, 100, 255, 0)
cv2.imshow("fruits", thresh)
cv2.waitKey(0)