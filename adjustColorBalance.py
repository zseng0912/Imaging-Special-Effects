import numpy as np

#Read an image using OpenCV
img = cv2.imread('input_image.jpg')

#Adjust color balance by changing channel intensities
blue, green, red = cv2.split(img)

# Example: Increase red color
red_adjusted = cv2.addWeighted(red, 1.5, 0, 0, 0)

#Merge the channels back together
adjusted_img = cv2.merge((blue, green, red_adjusted)）

cv2.imshow('Color Balance Adjusted', adjusted_img)
