from PIL import Image, ImageEnhance

# Load an image
image_path = "b2.png"
image = Image.open(image_path)

# Create an ImageEnhance object for contrast
enhancer = ImageEnhance.Contrast(image)

# Adjust the contrast
factor = 2.0  # Change this value to increase or decrease contrast
enhanced_image = enhancer.enhance(factor)

# Save the enhanced image
enhanced_image.save("Contrast_b2.png")
