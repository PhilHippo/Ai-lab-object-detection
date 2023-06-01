import os

def rename_images(folder_path):
    """
    Renames all images inside a folder with an ascending numeric prefix
    """
    
    # Get a list of all images in the folder
    set_of_images = os.listdir(folder_path)
    
    # Rename the images sequentially
    counter = 1
    new_filenames_list = []
    for i in range(len(set_of_images)):
        # Generate the new filenames with a numeric prefix
        new_filename = f"{counter}.jpg"  # Modify the extension if needed
        new_filenames_list.append(new_filename)
        counter += 1

    index = 0
    for new_filename in new_filenames_list:
        # If there exists an image in set_of_images with the same name as new_filename
        if new_filename in set_of_images:
            image = set_of_images.index(new_filename)
            set_of_images.pop(image) # Do not rename the file

        else:
            # Get the full paths of the old and new filenames
            image = set_of_images[index]
            set_of_images.pop(index)
            old_path = os.path.join(folder_path, image)
            new_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(old_path, new_path)

# Example usage
folder_path = "negatives"
rename_images(folder_path)