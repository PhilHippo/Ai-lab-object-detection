from PIL import Image
import cv2

def convert_to_grayscale(image_path):
    with Image.open(image_path) as img:
        # Convert the image to grayscale
        grayscale_img = cv2.GaussianBlur(img, (5, 5), 0)
    
    return grayscale_img

# Open the image file and convert it to grayscale
image_path = 'positive/559_pos.jpg'
grayscale_img = convert_to_grayscale(image_path)

# Display the grayscale image on the screen
grayscale_img.show()