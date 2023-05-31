import cv2

'''
This function allows to:

1. save / simply display images
2. apply / not apply black and white filter
3. resize / not resize frame
4. apply / not apply contrast filter

By default:

1. doesn't save
2. applyes balck and white filter
3. doesn't resize
4. doesn't apply contrast filter

To save images output folder must be created and given as input

There two ways to save images:

1. press 's' on keyboard
2. insert each_th_frame integer variable: saves image automatically each tot frames

SCROLL DOWN TO INSERT ALL PARAMETERS
Than simply run algorithm
'''

def save_frames(output_folder=None, black_and_white=True, resize_width=None, resize_height=None, contrast_factor=None, each_th_frame=None):
    # Open the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error opening webcam")
        return
    
    frame_number = 0
    filename_counter = 1
    while True:
        # Read the next frame from the webcam
        frame = cap.read()[1]
        frame_number += 1

        # Convert the frame to grayscale if black_and_white=True
        if black_and_white:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply contrast to the grayscale frame if contrast is provided
        if contrast_factor:
            frame = cv2.convertScaleAbs(frame, alpha=contrast_factor, beta=0)

        # Resize the frame if width and height are provided
        if resize_width and resize_height:
            frame = cv2.resize(frame, (resize_width, resize_height))

        # If output_folder is provided becasue you want images to be saved
        # If each_th_frame is provided save a frame at intervals of specified number
        if output_folder and each_th_frame and frame_number % each_th_frame == 0:
            # Define the output file path
            output_path = f"{output_folder}/{filename_counter}.jpg"
            filename_counter += 1

            # Save the frame
            cv2.imwrite(output_path, frame)

        # Display the video stream
        cv2.imshow("Webcam", frame)
        k = cv2.waitKey(1)

        # Save frame manually if 's' is pressed
        if k == ord('s'):
            output_path = f"{output_folder}/{filename_counter}.jpg"
            filename_counter += 1

            # Save the frame
            cv2.imwrite(output_path, frame)

        # Exit if 'q' is pressed
        if k == ord('q'):
            break

    # Release the webcam and close any open windows
    cap.release()
    cv2.destroyAllWindows()


# Example usage
# output_folder = None if you don't want to save images
output_folder = "saved_frames" # Remeber to change path name otherwise images get overriden
black_and_white = True
resize_width = 640
resize_height = 360
contrast_factor = None
each_th_frame = 30
save_frames(output_folder, black_and_white, resize_width, resize_height, contrast_factor, each_th_frame)