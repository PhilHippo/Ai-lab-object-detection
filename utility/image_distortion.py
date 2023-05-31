import cv2
import numpy as np
import random
from PIL import Image

def apply_random_transform(image, rotation_extremes, transform_extremes):
    # Convert the image to a numpy array
    img = np.array(image)

    # Generate a random rotation angle within the given extremes
    rotation_angle = random.uniform(rotation_extremes[0], rotation_extremes[1])

    # Generate random projective transformation points within the given extremes
    height, width, _ = img.shape
    pts1 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    pts2 = np.float32([[random.uniform(transform_extremes[0], transform_extremes[1]), random.uniform(transform_extremes[0], transform_extremes[1])],
                       [width - random.uniform(transform_extremes[0], transform_extremes[1]), random.uniform(transform_extremes[0], transform_extremes[1])],
                       [random.uniform(transform_extremes[0], transform_extremes[1]), height - random.uniform(transform_extremes[0], transform_extremes[1])],
                       [width - random.uniform(transform_extremes[0], transform_extremes[1]), height - random.uniform(transform_extremes[0], transform_extremes[1])]])
    M = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply the random rotation and projective transformation
    img_rotated = cv2.warpPerspective(img, M, (width, height))
    img_transformed = cv2.rotate(img_rotated, cv2.rotate())

    # Convert the transformed image back to PIL Image format
    transformed_image = Image.fromarray(img_transformed)

    return transformed_image
