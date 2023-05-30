import cv2 as cv
from playsound import playsound
from utility import *


def speak():
    can = get_biggest_rectangle(rectangles) # the can chosen as a target is the biggest one

    #if it detects at least 1 rectangle, play sound
    if can is not None:
        can_x = can[0]
        can_y = can[1]
        can_width = can[2]
        can_height = can[3]

        if below_of_can(can_height, can_y, frame_center[1]): audiopath = audio_paths["up"]
        elif above_of_can(can_y, frame_center[1]): audiopath = audio_paths["down"]
        elif right_of_can(can_width, can_x, frame_center[0]): audiopath = audio_paths["left"]
        elif left_of_can(can_x, frame_center[0]): audiopath = audio_paths["right"]
        else: audiopath = audio_paths["shoot"]

        playsound(audiopath, False)


if __name__ == '__main__':
    # load the trained model
    cascade_model = cv.CascadeClassifier('/Users/simonerussolillo/Desktop/Uni/Second Year/Second Semester/Computer Vision/Ai-lab-object-detection/cascade/haarcascade_eye_tree_eyeglasses.xml')
    cap = cv.VideoCapture(0)

    #list of audio paths
    #Windows traditionally uses the backslash (\) to separate directories in file paths
    #other operationg systems (including Mac OS X and Linux) use forward slash (/)
    audio_paths = {"up": 'audio\\up.mp3', "down": 'audio\\down.mp3', "left": 'audio\\left.mp3', "right": 'audio\\right.mp3', "shoot": 'audio\\shoot.mp3'}
    audio_paths = {"up": 'audio/up.mp3', "down": 'audio/down.mp3', "left": 'audio/left.mp3', "right": 'audio/right.mp3', "shoot": 'audio/shoot.mp3'}

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

        # do object detection
        rectangles = cascade_model.detectMultiScale(adjusted_frame, scaleFactor=1.1, minNeighbors=4)

        # draw the detection results onto the original image
        detection_image = draw_rectangle(rectangles, frame)
        detection_image = draw_cross(detection_image, frame_center[0], frame_center[1])
        
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