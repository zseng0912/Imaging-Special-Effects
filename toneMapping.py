# Read the HDR image
hdr_image = cv2.imread('hdr_image.jpg')

# Apply tone mapping for display
tonemap = cv2.createTonemapReinhard()
tonemapped_image = tonemap.process(hdr_image)

# Save the tone-mapped image
cv2.imwrite('tonemapped_image.jpg', tonemapped_image)
