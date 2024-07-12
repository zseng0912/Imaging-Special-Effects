from PIL import Image, ImageEnhance

# Load an image
image_path = "b2.png"
image = Image.open(image_path)

# Create an ImageEnhance object
enhancer = ImageEnhance.Brightness(image)

# Adjust the brightness
factor = 0.8  # Change this value to increase or decrease brightness
enhanced_image = enhancer.enhance(factor)

# Save the enhanced image
enhanced_image.save("dark_b2.png")
