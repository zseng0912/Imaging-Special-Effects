from PIL import Image, ImageEnhance

# Load an image
image_path = "hiking.png"
image = Image.open(image_path)

# Create an ImageEnhance object for sharpness
enhancer = ImageEnhance.Sharpness(image)

# Adjust the sharpness
factor = 1.5  # Change this value to increase or decrease sharpness
enhanced_image = enhancer.enhance(factor)

# Save the enhanced image
enhanced_image.save("sharpen_hiking.png")
