from PIL import Image
import os

directory = "positive"

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        # Open the image using Pillow (PIL)
        image = Image.open(os.path.join(directory, filename))

        width, height = image.size

        if width > height:

            print(filename)