import random
from PIL import Image, ImageEnhance
import os


def resize_image(img, min_scale_factor, max_scale_factor):
    # Randomly resize an image
    random_scale_factor = random.uniform(min_scale_factor, max_scale_factor)  # Random scale factor between 1 and 2
    new_width = int(img.width * random_scale_factor)
    new_height = int(img.height * random_scale_factor)
    img = img.resize((new_width, new_height))

    return img


def merge_images(image1_path, image2_path): # (neg_path, can_path)
    # Open the images
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)
    img2 = apply_random_lighting_filter(img2)

    # Get the width and height of the second image
    width, height = img1.size

    # Randomly resize image2
    img2 = resize_image(img2, 0.9, 2.8)

    

    # Generate random coordinates within the second image
    x = random.randint(0, width - img2.width)
    y = random.randint(0, height - img2.height)

    # Create a new image by pasting image1 onto image2 at the random coordinates
    merged_img = img1.copy()
    merged_img.paste(img2, (x, y))

    # Show the merged image
    return merged_img, x, y, img2.width, img2.height


def match_images(folder1_path, folder2_path):
    folder1 = os.listdir(folder1_path)
    folder2 = os.listdir(folder2_path)

    matches = []

    # Iterate over the images and match them sequentially
    counter = 0
    for image in folder1:
        image1 = os.path.join(folder1_path, image)
        image2 = os.path.join(folder2_path, folder2[counter])
        match = (image1, image2)
        matches.append(match)
        counter += 1

        if counter == len(folder2):
            counter = 0

    return matches


def save_image(image, output_folder, image_filename):
    # Save the image in the output folder
    output_path = os.path.join(output_folder, image_filename)
    image.save(output_path)


def neg_file_generation(neg_path, negatives_path_folder):
    # Open the output file for writing, will overwrite all existing data in there
    with open(neg_path, 'w') as f:
        # Loop over all the filenames
        for filename in os.listdir(negatives_path_folder):
            f.write(negatives_path_folder + '/' + filename + '\n')


def pos_file_generation(pos_path, positives_path_folder, images_info):
    # info is a list s.t. [image_filename, x, y, w, h]
    with open(pos_path, 'w') as f:
        # Loop over all the filenames
        for image_filename, x, y, w, h in images_info:
            f.write(positives_path_folder + '/' + image_filename + f' 1 {x} {y} {w} {h}' + '\n')


def apply_random_lighting_filter(image):
    # Set the range of filter values
    min_value = 0.8
    max_value = 1.6

    # Generate a random filter value
    filter_value = random.uniform(min_value, max_value)

    # Apply the filter to the image
    enhancer = ImageEnhance.Brightness(image)
    filtered_image = enhancer.enhance(filter_value)
    enhancer = ImageEnhance.Contrast(filtered_image)
    filtered_image = enhancer.enhance(filter_value)

    return filtered_image

# # Example usage
# image_path = "cans/c1.jpg"
# image = Image.open(image_path)
# image = resize_image(image, 3, 4)

# filtered_image = apply_random_lighting_filter(image)
# image.show()
# filtered_image.show()



if __name__ == '__main__':
    negatives_path_folder = 'negatives'
    cans_path_folder = 'cans'
    positives_path_folder = 'positives' # craete a folder where you want the created positive images to be saved
    neg_path = 'neg.txt'
    pos_path = 'pos.txt'

    neg_file_generation(neg_path, negatives_path_folder)

    matches = match_images(negatives_path_folder, cans_path_folder)

    counter = 1
    images_info = []
    for match in matches: # (negative_image_path, can_image_path)
        # Apply distorsion to can

        merged_img, x, y, w, h = merge_images(match[0], match[1])
        image_filename = f'{counter}_pos.jpg'
        images_info.append([image_filename, x, y, w, h])
        save_image(merged_img, positives_path_folder, image_filename)
        counter += 1
    
    pos_file_generation(pos_path, positives_path_folder, images_info)