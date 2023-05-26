#rename sequentially all images
import os

folder_path = "kaggle_negatives"  # Replace with the actual path to the folder containing images
counter = 1

for filename in os.listdir(folder_path):
    # Replace with the actual file extensions of your images
    new_filename = str(counter) + "_neg.jpg"
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
    counter += 1