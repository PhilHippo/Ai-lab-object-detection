import cv2 as cv
import numpy as np
import os
from time import time

def filter_image(img):
    # convert the image to the HSV color space
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # define the lower and upper bounds of the color range in HSV
    lower_color = np.array([0, 100, 20])
    upper_color = np.array([40, 255, 255])

    # create a mask that isolates the color range in the image
    mask = cv.inRange(hsv, lower_color, upper_color)

    # apply the mask to the original image to obtain the filtered image
    filtered_img = cv.bitwise_and(img, img, mask=mask)

    # blend the filtered image with the original image to retain some other colors
    alpha = 0.5
    blended_img = cv.addWeighted(img, alpha, filtered_img, 1 - alpha, 0)

    return blended_img


# draw rectangles around the detected faces in the original frame
def draw_rectangle(rectangles,frame):
    updated_frame = frame
    for (x, y, w, h) in rectangles:
        updated_frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return updated_frame


# load the trained model
cascade_fanta = cv.CascadeClassifier('cascade/cascade.xml')

loop_time = time()
cap = cv.VideoCapture(0)

while(True):

    # get an updated image of the webcam
    ret, frame = cap.read()

    filtered_frame = filter_image(frame)

    # do object detection
    rectangles = cascade_fanta.detectMultiScale(filtered_frame, scaleFactor=1.5, minNeighbors=5)

    # draw the detection results onto the original image
    detection_image = draw_rectangle(rectangles, frame)

    # display the images
    cv.imshow('Matches', detection_image)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')