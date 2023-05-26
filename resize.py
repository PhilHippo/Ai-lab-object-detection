from PIL import Image
import os

#directory containing the images
directory = "new_positive/"
resize_factor = 0.15

# Loop through the images in the directory
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        # Open the image using Pillow (PIL)
        image = Image.open(os.path.join(directory, filename))

        # Get the original size of the image
        width, height = image.size
       
        # Calculate the new size of the image
        new_width = int(width * resize_factor)
        new_height = int(height * resize_factor)

        # Resize the image using Pillow (PIL)
        resized_image = image.resize((new_width, new_height))

        # Save the resized image
        resized_image.save(os.path.join(directory, f"{filename}"))