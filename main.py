import cv2 as cv
from utility import *

# load the trained model
cascade_model = cv.CascadeClassifier('cascade\haarcascade_eye_tree_eyeglasses.xml')
cap = cv.VideoCapture(0)

#list of audio paths
audio_paths = {"up": r'audio/up.mp3', "down": r'audio/down.mp3', "left": r'audio/left.mp3', "right": r'audio/right.mp3', "shoot": r'audio/shoot.mp3'}

# get the frame size and center
frame_size = get_frame_size(cap)
frame_center = get_rectangle_center((0, 0, frame_size[0], frame_size[1]))

frame_counter= 0

while(True):
    # get an updated image of the webcam
    ret, frame = cap.read()

    #pipeline filters
    adjusted_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)   
    adjusted_frame = cv.equalizeHist(adjusted_frame)
    adjusted_frame = cv.GaussianBlur(adjusted_frame, (3, 3), 0)

    # do object detection
    rectangles = cascade_model.detectMultiScale(adjusted_frame, scaleFactor=1.2, minNeighbors=10)

    # draw the detection results onto the original image
    detection_image = draw_rectangle(rectangles, frame)
    detection_image = draw_cross(detection_image, frame_center[0], frame_center[1])
    
    if frame_counter == 12:
        speak(rectangles, frame_center, audio_paths)
        frame_counter = 0

    cv.imshow('Matches', detection_image)

    frame_counter += 1

    # press 'q' with the output window focused to exit.
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    
print('Done.')