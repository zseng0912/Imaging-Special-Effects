import matplotlib.pyplot as plt
import numpy as np

# Create a simple scene
scene = np.zeros((100, 100, 3), dtype=np.uint8)
scene[40:60, 40:60] = [255, 255, 255] # White square representing an object

# Apply perspective transformation
def perspective_transform(image):
  rows, cols, _ = image.shape
  perspective_matrix = np.float32([[1, 0, 0], [0, 1, 0], [0.001, 0.001, 1]])
  perspective_image = cv2.warpPerspective(image, perspective_matrix, (cols, rows))
  return perspective_image
  
result = perspective_transform(scene)

#  Display original and transformed images
plt.subplot(1, 2, 1), plt.imshow(scene), 
plt.title('Original')
plt.subplot(1, 2, 2), plt.imshow(result), 
plt.title('Perspective Distortion')
plt.show()
