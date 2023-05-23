#rename sequentially all images
import os

folder_path = "positive"  # Replace with the actual path to the folder containing images
counter = 1

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"): 
        # Replace with the actual file extensions of your images
        new_filename = str(counter) + " pos.jpg"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        counter += 1