import numpy as np
import cv2 as cv

# draw rectangles around the detected faces in the original frame
def draw_rectangle(rectangles,frame):
    updated_frame = frame
    for (x, y, w, h) in rectangles:
        updated_frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return updated_frame

def draw_crosshair(frame, x, y, size=5, thickness=1, color=(0, 0, 255)):
    """
    Draws a crosshair centered at the (x, y) coordinate on the given frame.
    
    Parameters:
    - frame: a NumPy array representing the image or video frame to draw on
    - x: the x-coordinate of the center of the crosshair
    - y: the y-coordinate of the center of the crosshair
    - size: the size of the crosshair (default: 10)
    - thickness: the thickness of the crosshair (default: 1)
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

def getRectangleCenter(rectangle):
    if rectangle is not None:
        x, y, w, h = rectangle
        center_x = x + (w // 2)  # calculate the x-coordinate of the center
        center_y = y + (h // 2)  # calculate the y-coordinate of the center
        return (center_x, center_y)  # return the center as a tuple
    return None


#given a videocapture object, return the frame size (w, h)
def getFrameSize(cap):
    ret, frame = cap.read()
    return (frame.shape[1], frame.shape[0])


#go up!
def belowOfCan(canHeight, can_y, center_y):
    return center_y > can_y + canHeight

#go down!
def aboveOfCan(can_y, center_y):
    return center_y < can_y

#go right!
def leftOfCan(can_x, center_x):
    return center_x < can_x

#go left!
def rightOfCan(canWidth, can_x, center_x):
    return center_x > can_x + canWidth 

def getBiggestRectangle(rectangles):   
    if len(rectangles) > 0:
        # convert the list of rectangles to a numpy array
        rectangles_array = np.array(rectangles)

        # calculate the areas of all rectangles by multiplying the width and height element wise
        areas = rectangles_array[:, 2] * rectangles_array[:, 3]

        # get the index of the rectangle with the largest area and
        # return the biggest rectangle

        return rectangles[np.argmax(areas)]
    
    return None

