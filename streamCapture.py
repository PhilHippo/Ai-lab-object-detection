import cv2

# se lo stream non parte forse è perchè è già attivo sul browser
# o browser o openCV, entrambi contemporaneamente non va

# http://192.168.178.146 wifi
# http://192.168.132.152 Mi A3

URL = "http://192.168.178.146"

cap = cv2.VideoCapture(URL + ":81/stream")

# We need to check if camera is opened or not
if (cap.isOpened() == False): 
    print("Error reading video file")

#save video resolution
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)

#VideoWriter object will create a frame. The output is stored in 'filename.avi' file.
result = cv2.VideoWriter('videoshooting.avi', cv2.VideoWriter_fourcc(*'MJPG'), 24, size)

while True:
    frame = cap.read()[1]

    result.write(frame)

    cv2.imshow('stream', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

print('Video saved.')

