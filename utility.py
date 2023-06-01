import numpy as np
import cv2 as cv
from playsound import playsound


def draw_rectangle(rectangles: list, frame):
    """
    Draws a rectangle on the given frame for each tuple (x, y, w, h) in the rectangles list.
    """

    updated_frame = frame

    for (x, y, w, h) in rectangles:
        updated_frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return updated_frame



def draw_cross(frame, x, y, size=5, thickness=1, color=(0, 0, 255)):
    """
    Draws a cross centered at the (x, y) coordinate on the given frame.
    
    Parameters:
    - frame: a NumPy array representing the image or video frame to draw on
    - x: the x-coordinate of the center of the cross
    - y: the y-coordinate of the center of the cross
    - size: the size of the cross (default: 5)
    - thickness: the thickness of the cross (default: 1)
    - color: the color of the crosshair as a tuple of (B, G, R) values (default: red)
    """

    # Calculate the starting and ending points of the horizontal line
    x1 = x - size
    x2 = x + size

    # Draw the horizontal line
    cv.line(frame, (x1, y), (x2, y), color, thickness)

    # Calculate the starting and ending points of the vertical line
    y1 = y - size
    y2 = y + size

    # Draw the vertical line
    cv.line(frame, (x, y1), (x, y2), color, thickness)
    
    return frame



def get_rectangle_center(rectangle):
    """
    Returns the coordinates (x, y) of the center of a rectangle if rectangle is valid, otherwise returns None.
    """

    if rectangle is not None:
        x, y, w, h = rectangle
        center_x = x + (w // 2)  # calculate the x-coordinate of the center
        center_y = y + (h // 2)  # calculate the y-coordinate of the center
        return (center_x, center_y)  # return the center as a tuple
    
    else:
        return None



def get_frame_size(cap):
    """
    Returns the frame size (w, h) of the given videocapture object.
    """

    ret, frame = cap.read()

    return (frame.shape[1], frame.shape[0])



#go up!
def below_of_can(can_height, can_y, center_y):
    return center_y > can_y + can_height

#go down!
def above_of_can(can_y, center_y):
    return center_y < can_y

#go right!
def left_of_can(can_x, center_x):
    return center_x < can_x

#go left!
def right_of_can(can_width, can_x, center_x):
    return center_x > can_x + can_width



def get_biggest_rectangle(rectangles: list):
    """
    Returns the coordintes (x, y, w, h) of the biggest rectangle in the list rectangles if it is not empty, otherwise returns None.
    """

    if len(rectangles) > 0:
        # convert the list of rectangles to a numpy array
        rectangles_array = np.array(rectangles)

        # calculate the areas of all rectangles by multiplying the width and height element wise
        areas = rectangles_array[:, 2] * rectangles_array[:, 3]

        # get the index of the rectangle with the largest area and return the biggest rectangle
        return rectangles[np.argmax(areas)]
    
    return None



def speak(rectangles, frame_center, audio_paths):
    """
    Selects the correct audio signal to play given the the position of the target.
    """
    can = get_biggest_rectangle(rectangles)

    #if it detects at least 1 rectangle, play sound
    if can is not None:
        can_x = can[0]
        can_y = can[1]
        can_height = can[3]
        can_width = can[2]

        if below_of_can(can_height, can_y, frame_center[1]): audiopath = audio_paths["up"]
        elif above_of_can(can_y, frame_center[1]): audiopath = audio_paths["down"]
        elif right_of_can(can_width, can_x, frame_center[0]): audiopath = audio_paths["left"]
        elif left_of_can(can_x, frame_center[0]): audiopath = audio_paths["right"]
        else: audiopath = audio_paths["shoot"]

        playsound(audiopath, False)

def filterPipeline(frame):
    adjusted_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)   
    adjusted_frame = cv.equalizeHist(adjusted_frame)

    #clahe = cv.createCLAHE(clipLimit=5, tileGridSize=(8,8))
    #adjusted_image = clahe.apply(adjusted_frame)

    return adjusted_frame