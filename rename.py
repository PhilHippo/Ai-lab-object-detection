#rename sequentially all images
import os

folder_path = "positive"  # Replace with the actual path to the folder containing images
counter = 1

for filename in os.listdir(folder_path):
    # Replace with the actual file extensions of your images
    list_filename = filename.split("_")
    new_filename = list_filename[0] + "_pos.jpg"
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))