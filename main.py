import cv2 as cv
from playsound import playsound
from utility import *

def speak():
    can = getBiggestRectangle(rectangles)

    #if it detects at least 1 rectangle, play sound
    if can is not None:
        can_xy = can[0:2]
        can_height = can[3]
        can_width = can[2]

        if belowOfCan(can_height, can_xy[1], frame_center[1]): audiopath = audio_paths["up"]
        elif aboveOfCan(can_xy[1], frame_center[1]): audiopath = audio_paths["down"]
        elif rightOfCan(can_width, can_xy[0] , frame_center[0]): audiopath = audio_paths["left"]
        elif leftOfCan(can_xy[0], frame_center[0]): audiopath = audio_paths["right"]
        else: audiopath = audio_paths["shoot"]

        playsound(audiopath, False)

# load the trained model
cascade_model = cv.CascadeClassifier('cascade\haarcascade_eye_tree_eyeglasses.xml')
cap = cv.VideoCapture(0)

#list of audio paths
audio_paths = {"up": r'audio\up.mp3', "down": r'audio\down.mp3', "left": r'audio\left.mp3', "right": r'audio\right.mp3', "shoot": r'audio\shoot.mp3'}

# get the frame size and center
frame_size = getFrameSize(cap)
frame_center = getRectangleCenter((0, 0, frame_size[0], frame_size[1]))

frame_counter= 0

while(True):
    # get an updated image of the webcam
    ret, frame = cap.read()

    #pipeline filters
    adjusted_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)   
    adjusted_frame = cv.equalizeHist(adjusted_frame)

    # do object detection
    rectangles = cascade_model.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=4)

    # draw the detection results onto the original image
    detection_image = draw_rectangle(rectangles, frame)
    detection_image = draw_crosshair(detection_image, frame_center[0], frame_center[1])
    
    if frame_counter == 12:
        speak()
        frame_counter = 0

    cv.imshow('Matches', detection_image)

    frame_counter += 1

    # press 'q' with the output window focused to exit.
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    
print('Done.')