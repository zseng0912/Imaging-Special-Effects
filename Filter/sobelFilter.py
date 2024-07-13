import cv2
import numpy as np

image = cv2.imread('input_image.jpg', 
cv2.IMREAD_GRAYSCALE)

# Apply Sobel filter for edge detection
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Combine x and y gradients to get the final edgedetected image
edges = np.sqrt(sobel_x**2 + sobel_y**2)

# Display original and edge-detected images
cv2.imshow('Original', image)
cv2.imshow('Edges (Sobel Filter)', edges)
cv2.waitKey(0)
cv2.destroyAllWindows(
