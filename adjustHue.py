import cv2
import numpy as np

#Read an image using OpenCV
img = cv2.imread('input_image.jpg')

#Convert image from BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Shift hue by 50 units (value range is 0 - 179 in OpenCV)
hsv[ :, :, 0] = (hsv[ :, :, 0] + 50) % 180

#Convert back to BGR
hue_shifted_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imshow('Hue Shifted', hue_shifted_img)
cv2.waitKey(0)
