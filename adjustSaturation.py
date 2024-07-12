from PIL import Image, ImageEnhance

# Open an image
img = Image.open('input_image.jpg')

# Increase saturation 
enhancer = ImageEnhance.Color(img)
sat_img = enhancer.enhance(1.5) # Increase saturation by 50%
sat_img.show() 
