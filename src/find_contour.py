import cv2
import numpy as np

img = cv2.imread('data\\20220411-144903.jpg', cv2.IMREAD_UNCHANGED)

img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh = 100
ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('Number of contours: ', len(contours))

img_contours = np.zeros(img.shape)
cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow('img', img_contours)
cv2.waitKey(0)