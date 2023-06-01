import os
import cv2


#example: sequential_jpg("positive", "_pos.jpg")
def sequential_jpg(path: str, suffix: str) -> None:
    """Opens a folder and renames sequentially the images contained in it
    """

    counter = 1

    for filename in os.listdir(path):
        new_filename = str(counter) + suffix
        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
        counter += 1


#example: sequentialAnnotation("info.lst", "_pos.txt")
def sequentialAnnotation(path: str, suffix: str) -> None:
    """opens a file and renames sequentially the image filenames
    """

    counter = 1
    newfile = []

    # Open the .lst file for reading and writing
    with open(path, "r") as lst_file:
        for line in lst_file:
            # Split the line into its components
            components = line.strip().split(" ")

            # Generate the new filename
            new_filename = "info/" + str(counter) + "_pos.jpg"

            # Update the line and append it to the new file list
            components[0] = new_filename
            new_line = " ".join(components) + "\n"
            newfile.append(new_line)

            counter += 1

    # update the annotation file
    with open(path, "w") as lst_file:
        lst_file.writelines(newfile)


def resize(directory: str, resize_factor: float) -> None:
    """Resizes all the images of a folder
    """

    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Open the image using Pillow (PIL)
            image = image.open(os.path.join(directory, filename))

            # Get the original size of the image
            width, height = image.size
        
            # Calculate the new size of the image
            new_width = int(width * resize_factor)
            new_height = int(height * resize_factor)

            # Resize the image using Pillow (PIL)
            resized_image = image.resize((new_width, new_height))

            # Save the resized image
            resized_image.save(os.path.join(directory, f"{filename}"))


#example: sequentialjpg("old_negative", "new_negative")
def applyFilters(folder_path: str, new_folder_path: str) -> None:
    """Applies a pipeline of filters to all the images in a given folder and puts them in a new folder
    """

    files = os.listdir(folder_path)
    image_files = [file for file in files if file.endswith(('.jpg'))]

    for i, file_name in enumerate(image_files):
        image_path = os.path.join(folder_path, file_name)
        image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)
        image = cv2.equalizeHist(image)
        clahe = cv2.createCLAHE(clipLimit=5, tileGridSize=(8,8))
        image = clahe.apply(image)

        #image = cv2.Canny(image, threshold1=30, threshold2=100)
        #image = cv2.GaussianBlur(image, (5, 5), 0)
        #image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 2)

        cv2.imwrite(new_folder_path+file_name, image)
        print(f"processing: {file_name}")
    print("Done")


def createCanAnnotations():
    """Automatically creates the annotations for the cans
    """

    for img in os.listdir("cans"):
        line = "positive" + '/' + img + ' 1 0 0 24 65\n'
        with open('info.dat','a') as f:
            f.write(line)